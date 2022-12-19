import os
from service_layer.lti.OIDCLogin import OIDCLogin
from service_layer.service.SessionServiceFlask import SessionServiceFlask
from service_layer.service.CookieServiceFlask import CookieServiceFlask
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
import service_layer.lti.LaunchDataStorage as LaunchDataStorage
import urllib.parse
from flask import redirect,make_response
from flask.wrappers import Request, Response

class OIDCLoginFlask(OIDCLogin):
    ''' Flask implementation of OIDC login '''
    def __init__(self, request : Request, tool_config : ToolConfigJson, session_service=None, cookie_service=None, session=None):
        self._cookie_service = cookie_service if cookie_service else CookieServiceFlask(request)
        self._session_service = session_service if session_service else SessionServiceFlask(session)
        super(OIDCLoginFlask, self).__init__(request, tool_config)

    def check_auth(self):
        # check issuer
        if not self._request.form.get('iss'):
            self._response = "No issuer found", 400
            return self
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
        if not self._cookie_service.get_cookie('MoodleSession'):
            self._response = "No cookie found", 400
            return self

        # Get the platform settings (same scheme as in the tool config json)
        platform = self._tool_config.decode_platform(self._tool_config.get_platform(self._request.form.get('iss')))
        if not platform:
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
        if self._request.form.get('target_link_uri') != platform.target_link_uri:
            self._response = "Invalid target_link_uri", 400

        return self

    def login(self):
        ''' Login to OIDC provider
            Crafts the redirect url by adding the necessary parameters
        '''
        # check auth
        if self._response:
            return make_response(self._response)

        # Create a unique nonce for this flow
        nonce = self._session_service.get_oidc_nonce()

        # Consider using a state JWT as described in
        # https://tools.ietf.org/html/draft-bradley-oauth-jwt-encoded-state-09
        state = self._session_service.get_oidc_state()

        # Store the nonce and state so they can be validated when the id_token
        # is posted back to the tool by the Authorization Server.
        # LaunchDataStorage.set_value(key=nonce, value=state)
        
        platform = self._tool_config.get_platform(self._request.form.get('iss'))
        ru = self.make_url_accept_param(platform['auth_login_url'])
        params = {
            'client_id': platform['client_id'],
            'response_mode': 'form_post',
            'redirect_uri': self._request.form.get('target_link_uri'),
            'response_type': 'id_token',
            'scope': 'openid',
            'nonce': nonce,
            'state': state,
            'login_hint': self._request.form.get('login_hint'),
            'lti_message_hint': self._request.form.get('lti_message_hint'), # resource link id or deep link idc
            }
        print(ru + urllib.parse.urlencode(params))
        return redirect(ru + urllib.parse.urlencode(params))

    def verify_state(self):
        ''' Verify the state parameter
            If the state parameter is not valid, the request is rejected with a 403 Forbidden response.
        '''
        # check auth
        if self._response:
            return self

        # Verify the state parameter
        if self._request.form.get('state') != self._session_service.get_oidc_state():
            self._response = "Invalid state", 403
            return self

        return self


    def lti_launch_from_id_token(self) -> Response:
        # get issuer
        # based on issuer platform get corresponsing implementaiton and write id token data into structures
        platform = self._tool_config.decode_platform(self._tool_config.get_platform(self._request.form.get('iss')))
        if platform:
            return make_response(platform.launch())
        else:
            return make_response("No platform found", 400)