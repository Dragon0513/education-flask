from flask import redirect
import urllib.parse
from service_layer.lti.CookieService import CookieService
from service_layer.lti.LaunchDataStorage import LaunchDataStorage

from service_layer.lti.SessionService import SessionService

class OIDCLogin:
    _response = None
    def __init__(self, request, tool_config, session_service=None, cookie_service=None, launch_data_storage=None):
        self._request = request
        self._tool_config = tool_config
        self._session_service = session_service if session_service else SessionService(request)
        self._cookie_service = cookie_service if cookie_service else CookieService(request)
        self._launch_data_storage = launch_data_storage if launch_data_storage else LaunchDataStorage()

    def check_auth(self):
        # check issuer
        if not self._request.form.get('iss'):
            _response = "No issuer found", 400
        # check client_id
        if not self._request.form.get('client_id'):
            _response = "No client_id found", 400
        # check login hint
        if not self._request.form.get('login_hint'):
            _response = "No login_hint found", 400
        # check target link uri
        if not self._request.form.get('target_link_uri'):
            _response = "No target_link_uri found", 400
        # check lti deployment id
        if not self._request.form.get('lti_deployment_id'):
            _response = "No lti_deployment_id found", 400
        return self

    def login(self):
        ''' Login to OIDC provider
            Crafts the redirect url by adding the necessary parameters
        '''
        # check auth
        self.check_auth()
        if self._response: # TODO: check if this is the right way to check if the request is valid
            return self._response

        # Get the platform settings (same scheme as in the tool config json)
        platform = self._tool_config.get_platform(self._request.form.get('iss'))
        if not platform:
            _response = "No platform found", 400

        # Verify if the target_link_uri is valid and does not redirect to other domain than our tool
        if self._request.form.get('target_link_uri') not in platform['target_link_uri']:
            _response = "Invalid target_link_uri", 400

        # Create a unique nonce for this flow
        nonce = self._session_service.get_nonce() # TODO: implement

        # Consider using a state JWT as described in
        # https://tools.ietf.org/html/draft-bradley-oauth-jwt-encoded-state-09
        state = self._session_service.get_state() # TODO: implement

        # Store the nonce and state so they can be validated when the id_token
        # is posted back to the tool by the Authorization Server.
        self._launch_data_storage.set_value('nonce', nonce)
        self._launch_data_storage.set_value('state', state)

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

    def make_url_accept_param(self, url):
        if '?' in url:
            return url + '&'
        else:
            return url + '?'