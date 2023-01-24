import json
import os
from service_layer.crypto.cryptorandom import CryptoRandom
from service_layer.lti.OIDCLogin import OIDCLogin
from service_layer.service.StateServiceFlask import StateServiceFlask
from service_layer.service.CookieServiceFlask import CookieServiceFlask
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from errors import errors as err
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement
import urllib.parse
from flask import redirect,make_response
from flask.wrappers import Request
from werkzeug.wrappers.response import Response

class OIDCLoginFlask(OIDCLogin):
    ''' Flask implementation of OIDC login '''
    def __init__(self, request : Request, tool_config : ToolConfigJson, session_service=None, cookie_service=None, session=None):
        self._request = request
        self._cookie_service = cookie_service if cookie_service else CookieServiceFlask(request)
        self._session_service = session_service if session_service else StateServiceFlask(session)
        self.oidc_login_params = {'iss', 'client_id', 'login_hint', 'lti_message_hint',  'target_link_uri', 'lti_deployment_id'}
        super(OIDCLoginFlask, self).__init__(request, tool_config)

    def check_params(self) -> OIDCLogin:
        # Check if all parameters are present
        try:
            if not self.oidc_login_params.issubset(self._request.form.keys()):
                raise err.MissingParameterError(status_code=400)
            # store subset with values from request form in object
            else:
                self._oidc_login_params_dict = {key: self._request.form.get(key) for key in self.oidc_login_params}
        except Exception as e:
            raise err.ErrorExcepion(e,message="Error in checking parameters", status_code=400)


        # Get the platform settings (same scheme as in the tool config json)
        # HTTP_ORIGIN is a safe way to get the origin of the request and a way to avoid CSRF attacks
        try:
            self._platform = self._tool_config.decode_platform(self._tool_config.get_platform(self._request.environ.get('HTTP_ORIGIN', '')))
            if not self._platform:
                raise err.ErrorExcepion(message="No platform found", status_code=400)
        except Exception as e:
            raise err.ErrorExcepion(e,message="Error in check_auth", status_code=400)
        try:
            parsed_target_link_url = urllib.parse.urlparse(self._oidc_login_params_dict.get('target_link_uri')) or None
        except ValueError as e:
            raise err.ErrorExcepion(e,message="target_link_uri is not URL", status_code=400)

        # Verify if the target_link_uri is valid and does not redirect to other domain than our tool
        # Verify HTTPS if in production
        try:
            if os.environ.get('FLASK_ENV') == 'production':
                if parsed_target_link_url.scheme != 'https':
                    raise err.ErrorExcepion(message="target_link_uri is not HTTPS", status_code=400)
            if parsed_target_link_url.netloc != self._request.host:
                raise err.ErrorExcepion(message="target_link_uri is not from the same host", status_code=400)
        except Exception as e:
            raise err.ErrorExcepion(e,message="target_link_uri invalid", status_code=400)

        # Verify if the target_link_uri is valid and does not redirect to other domain than our tool
        if self._oidc_login_params_dict.get('target_link_uri') != self._platform.target_link_uri:
            raise err.ErrorExcepion(message="target_link_uri may be malicious", status_code=400)

        return self

    def auth_redirect(self) -> Response:
        ''' Login to OIDC provider from LMS.
            Crafts the redirect url by adding the necessary parameters
        '''

        # Create a unique nonce for this flow to prevent replay attacks
        nonce = CryptoRandom().getrandomstring(32)

        # Create a unique state for this flow to ensure integrity of the response
        state = CryptoRandom().getrandomstring(32)

        state_jwt = JWTKeyManagement.generate_state_jwt(nonce,
                                                        state, 
                                                        self._platform.auth_login_url, 
                                                        self._tool_config.get_tool_url(self._request.environ.get('HTTP_ORIGIN', '')))
        
        platform = self._tool_config.get_platform(self._request.environ.get('HTTP_ORIGIN', ''))
        ru = self.make_url_accept_param(platform['auth_login_url'])
        params = {
            'client_id': platform['client_id'],
            'response_mode': 'form_post',
            'redirect_uri': self._oidc_login_params_dict.get('target_link_uri'),
            'response_type': 'id_token',
            'scope': 'openid',
            'nonce': nonce,
            'state': state_jwt,
            'login_hint': self._oidc_login_params_dict.get('login_hint'),
            'lti_message_hint': self._oidc_login_params_dict.get('lti_message_hint'), # resource link id or deep link idc
            }
        print(ru + urllib.parse.urlencode(params))
        response = redirect(ru + urllib.parse.urlencode(params))        
        return response



    def verify_state(self) -> OIDCLogin:
        ''' Verify the state parameter
            If the state parameter is not valid, the request is rejected with a 403 Forbidden response.
        '''
        # 🔑 check auth
        if self._response:
            return self

        # Verify the state parameter
        if not self._request.form.get('state'):
            self._response = "No state found", 403
            return self
        
        # verify state paramter signature
        state_form_jwt = self._request.form.get('state', type=str) or ''
        state_form = JWTKeyManagement.verify_jwt(state_form_jwt)
        assert(JWTKeyManagement.verify_state_jwt_payload(state_form))
        if not state_form:
            self._response = "Invalid state signature", 403
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
            self._response = "Invalid decryption key", 400
            return self
        
        self.id_token = JWTKeyManagement.verify_jwt(id_token_jwt, JWTKeyManagement.construct_key(hmac_key))
        if not self.id_token:
            self._response = "Invalid id_token signature", 403
            return self
        # self.id_token = LTIIDToken(**id_token)
        # TODO🧾 parse token and write into structures       

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
        nonce_jwt = JWTKeyManagement.generate_nonce_jwt(nonce, self._request.referrer, os.environ.get('BACKEND_URL', 'http://localhost:5000'))

        # get platform
        try:
            self._platform = self._tool_config.decode_platform(self._tool_config.get_platform(self._request.environ.get('HTTP_ORIGIN', '')))
            if not self._platform:
                raise err.ErrorExcepion(message="No platform found", status_code=400)
        except Exception as e:
            raise err.ErrorExcepion(e,message="Error in check_auth", status_code=400)
        # redirect to tool (login url in react)
        response = redirect(self._platform.frontend_login_url + '?' + urllib.parse.urlencode({'nonce': nonce_jwt}))
        return response

        # get issuer
        # TODO🧾 based on issuer platform get corresponsing implementaiton and write id token data into structures

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
        # TODO🧾 this cookie holds authorization data. implement right and role management
        cookie_expiration = 2 # 1 Minutes
        state_jwt = JWTKeyManagement.generate_state_jwt(nonce=CryptoRandom.createuniqueid(32), 
                                                        state=CryptoRandom.createuniqueid(32), 
                                                        audience=self._request.referrer, 
                                                        issuer=os.environ.get('BACKEND_URL', 'http://localhost:5000'),
                                                        expiration=cookie_expiration,
                                                        additional_claims={'user_id': 2, 'permissions': ['read:user_info']}
                                                        )
        response = Response(
            response=json.dumps(state_jwt),
            status=200,
            mimetype='application/json'
        )
        # set 🔑 auth 🍪 cookie
        self._cookie_service.set_cookie(response=response,key='haski_state',value=state_jwt, secure=False, httponly=True, samesite='Lax', max_age=cookie_expiration*60)
        return response

    def get_loginstatus(self) -> Response:
        # verify state jwt in request cookie
        state_jwt = self._request.cookies.get('haski_state')
        if not state_jwt:
            self._response = "No state found", 403
            # TODO 🧾 redirect to login
            return make_response(self._response)
        state_payload = JWTKeyManagement.verify_jwt(state_jwt)
        if not state_payload:
            self._response = "Invalid state signature", 403
            # TODO 🧾 redirect to login
            return make_response(self._response)
        # return OK
        return make_response("OK", 200)