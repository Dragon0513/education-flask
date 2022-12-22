import datetime
import json
import os
from service_layer.crypto.cryptorandom import CryptoRandom
from service_layer.lti.Messages import LTIIDToken
from service_layer.lti.OIDCLogin import OIDCLogin
from service_layer.service.StateServiceFlask import StateServiceFlask
from service_layer.service.CookieServiceFlask import CookieServiceFlask
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from errors import errors as err
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement
import service_layer.lti.LaunchDataStorage as LaunchDataStorage
import urllib.parse
from flask import redirect,make_response
from flask.wrappers import Request
from werkzeug.wrappers.response import Response

class OIDCLoginFlask(OIDCLogin):
    ''' Flask implementation of OIDC login '''
    def __init__(self, request : Request, tool_config : ToolConfigJson, session_service=None, cookie_service=None, session=None):
        self._cookie_service = cookie_service if cookie_service else CookieServiceFlask(request)
        self._session_service = session_service if session_service else StateServiceFlask(session)
        super(OIDCLoginFlask, self).__init__(request, tool_config)

    def check_auth(self) -> OIDCLogin:
        # check issuer
        if not self._request.form.get('iss'):
            raise err.ErrorExcepion(message="No issuer found", status_code=400)
        # check client_id
        if not self._request.form.get('client_id'):
            self._response = "No client_id found", 400
            return self
        # check login hint
        if not self._request.form.get('login_hint'):
            self._response = "No login_hint found", 400
            return self
        # check target link uri
        if not self._request.form.get('target_link_uri'):
            self._response = "No target_link_uri found", 400
            return self
        # check lti deployment id
        if not self._request.form.get('lti_deployment_id'):
            self._response = "No lti_deployment_id found", 400
            return self

        # check cookie
        # if not self._cookie_service.get_cookie('MoodleSession'):
        #     self._response = "No cookie found", 400
        #     return self

        # Get the platform settings (same scheme as in the tool config json)
        self.platform = self._tool_config.decode_platform(self._tool_config.get_platform(self._request.form.get('iss')))
        if not self.platform:
            self._response = "No platform found", 400
            return self
        try:
            urllib.parse.urlparse(self._request.form.get('target_link_uri'))
        except ValueError:
            self._response = "target_link_uri is not URL", 400
            return self
        if os.environ.get('FLASK_ENV') == 'production':
            if urllib.parse.urlparse(self._request.form.get('target_link_uri')).scheme != 'https':
                self._response = "target_link_uri is not HTTPS", 400
                return self
        if urllib.parse.urlparse(self._request.form.get('target_link_uri')).netloc != self._request.host:
            self._response = "target_link_uri is not from the same host", 400
            return self
        # Verify if the target_link_uri is valid and does not redirect to other domain than our tool
        if self._request.form.get('target_link_uri') != self.platform.target_link_uri:
            self._response = "Invalid target_link_uri", 400

        return self

    def auth_redirect(self) -> Response:
        ''' Login to OIDC provider
            Crafts the redirect url by adding the necessary parameters
        '''
        # check auth
        if self._response:
            return make_response(self._response)

        # Create a unique nonce for this flow
        nonce = CryptoRandom().getrandomstring(32)

        # Consider using a state JWT as described in
        # https://tools.ietf.org/html/draft-bradley-oauth-jwt-encoded-state-09
        state = CryptoRandom().getrandomstring(32)

        assert self.platform is not None
        state_jwt = JWTKeyManagement.generate_state_jwt(nonce,state, self.platform.auth_login_url, "https://localhost:5000")


        # Store the nonce and state so they can be validated when the id_token
        # is posted back to the tool by the Authorization Server.
        LaunchDataStorage.set_value(key=nonce, value=state)
        
        platform = self._tool_config.get_platform(self._request.form.get('iss'))
        ru = self.make_url_accept_param(platform['auth_login_url'])
        params = {
            'client_id': platform['client_id'],
            'response_mode': 'form_post',
            'redirect_uri': self._request.form.get('target_link_uri'),
            'response_type': 'id_token',
            'scope': 'openid',
            'nonce': nonce,
            'state': state_jwt,
            'login_hint': self._request.form.get('login_hint'),
            'lti_message_hint': self._request.form.get('lti_message_hint'), # resource link id or deep link idc
            }
        print(ru + urllib.parse.urlencode(params))
        response = redirect(ru + urllib.parse.urlencode(params))        
        self._cookie_service.set_cookie(response,key='state',value=state_jwt, domain='127.0.0.1')
        return response



    def verify_state(self) -> OIDCLogin:
        ''' Verify the state parameter
            If the state parameter is not valid, the request is rejected with a 403 Forbidden response.
        '''
        # check auth
        if self._response:
            return self

        # Verify the state parameter
        if not self._request.form.get('state'):
            self._response = "No state found", 403
            return self
        
        # check cookie
        if not self._cookie_service.get_cookie('state'):
            self._response = "No cookie found", 403
            return self
        
        # verify state paramter signature
        state_form_jwt = self._request.form.get('state', type=str) or ''
        state_form = JWTKeyManagement.verify_jwt(state_form_jwt)
        assert(JWTKeyManagement.verify_state_jwt_payload(state_form))
        if not state_form:
            self._response = "Invalid state signature", 403
            return self

        # verify cookie signature
        state_cookie_jwt = self._cookie_service.get_cookie('state', type=str) or ''
        state_cookie = JWTKeyManagement.verify_jwt(state_cookie_jwt)
        assert(JWTKeyManagement.verify_state_jwt_payload(state_cookie))
        if not state_cookie:
            self._response = "Invalid state signature", 403
            return self

        # verify both state form and cookie are the same
        if state_form != state_cookie:
            self._response = "Invalid state", 403
            return self

        return self

    def verify_id_token(self) -> OIDCLogin:
        ''' Verify the id_token
            If the id_token is not valid, the request is rejected with a 403 Forbidden response.
        '''
        # check auth
        if self._response:
            return self
        
        # check if error in request
        if self._request.form.get('error'):
            self._response = self._request.form.get('error'), 400
        if not self._request.form.get('id_token'):
            self._response = "No id_token found", 400

        # Decode the id_token
        id_token_jwt = self._request.form.get('id_token', type=str) or ''
        id_token_header_unverified = JWTKeyManagement.get_unverified_header(id_token_jwt)
        id_token_unverified = JWTKeyManagement.load_jwt(id_token_jwt)

        platform = self._tool_config.get_platform(id_token_unverified['iss'])
        print(id_token_header_unverified)
        hmac_key : str = next((key for key in platform['key_set']['keys'] if key['kid'] == id_token_header_unverified['kid']), "")
        if not hmac_key: # TODO try to get new keys, if that fails return error
            self._response = "Invalid key", 400
            return self
        # hmac_key = filter(lambda key: key.kid == id_token_unverified['kid'], platform['key_set']['keys'])
        self.id_token = JWTKeyManagement.verify_jwt(id_token_jwt, JWTKeyManagement.construct_key(hmac_key))
        if not self.id_token:
            self._response = "Invalid id_token signature", 403
            return self
        # self.id_token = LTIIDToken(**id_token)
        # TODO parse token and write into structures
       

        return self

    def lti_launch_from_id_token(self) -> Response:
        # check if error in state
        if self._response:
            return make_response(self._response)

        # state from form
        state_form_jwt = self._request.form.get('state', type=str) or ''
        state_form = JWTKeyManagement.verify_jwt(state_form_jwt)
        assert(JWTKeyManagement.verify_state_jwt_payload(state_form))

        # generate nonce to obtain cookie
        nonce = CryptoRandom().getrandomstring(32)
        nonce_jwt = JWTKeyManagement.generate_nonce_jwt(nonce, self._request.referrer, "https://localhost:5000")
        LaunchDataStorage.set_value(key=nonce, value=nonce_jwt)
        LaunchDataStorage.set_value(key="key", value=self.id_token)

        # redirect to tool (login url in react)
        response = redirect('http://localhost:8080/login?' + urllib.parse.urlencode({'nonce': nonce_jwt}))
        return response

        # get issuer
        # based on issuer platform get corresponsing implementaiton and write id token data into structures
        platform = self._tool_config.decode_platform(
            self._tool_config.get_platform(
                self._request.form.get('iss')))
        if platform:
            return make_response(platform.launch())
        else:
            return make_response("No platform found", 400)

    def get_login(self) -> Response:
        # verify nonce jwt in request
        json_data = self._request.get_json() or {}
        if not json_data.get('nonce'):
            self._response = "No nonce found", 403
            return make_response(self._response)
        nonce_jwt = json_data['nonce'] or ''
        nonce_payload = JWTKeyManagement.verify_jwt(nonce_jwt)
        if not nonce_payload:
            self._response = "Invalid nonce signature", 403
            return make_response(self._response)

        if not JWTKeyManagement.verify_jwt_payload(nonce_payload):
            self._response = "Invalid nonce", 403
            return make_response(self._response)
        userinfo = LaunchDataStorage.get_value(key="key")
        # TODO this cookie holds authorization data
        state_jwt = JWTKeyManagement.generate_state_jwt(CryptoRandom.createuniqueid(32), CryptoRandom.createuniqueid(32), self._request.referrer, "https://localhost:5000")
        response = Response(
            response=json.dumps(userinfo),
            status=200,
            mimetype='application/json'
        )
        self._cookie_service.set_cookie(response,key='state',value=state_jwt, domain='127.0.0.1')
        return response