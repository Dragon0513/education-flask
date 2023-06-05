import json
import os
import urllib.parse
from service_layer import services, unit_of_work
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement
from errors import errors as err
from flask import jsonify, redirect,make_response
from flask.wrappers import Request
from werkzeug.wrappers.response import Response
from service_layer.crypto.cryptorandom import CryptoRandom
from service_layer.lti.Messages import LTIIDToken
from service_layer.lti.OIDCLogin import OIDCLogin
from service_layer.lti.Roles import RoleMapper
from service_layer.service.CookieServiceFlask import CookieServiceFlask
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
import service_layer.service.SessionServiceFlask as SessionServiceFlask
from domain.userAdministartion import model as UA


class OIDCLoginFlask(OIDCLogin):
    ''' Flask implementation of OIDC login '''
    def __init__(self, request : Request, tool_config : ToolConfigJson, session_service=None, cookie_service=None, session=None):
        self._request = request
        self._cookie_service = cookie_service if cookie_service else CookieServiceFlask(request)
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
            raise err.ErrorException(e,message="Error in checking parameters", status_code=400)


        # Get the platform settings (same scheme as in the tool config json)
        # HTTP_ORIGIN is a safe way to get the origin of the request and a way to avoid CSRF attacks
        # when redirected from http it doesnt work anymore
        try:
            self._platform = self._tool_config.decode_platform(self._tool_config.get_platform(os.environ.get('LMS_URL', 'https://moodle.haski.app')))
            if not self._platform:
                raise err.ErrorException(message="No platform found", status_code=400)
        except Exception as e:
            raise err.ErrorException(e,message="Error in check_auth", status_code=400)
        try:
            parsed_target_link_url = urllib.parse.urlparse(self._oidc_login_params_dict.get('target_link_uri')) or None
        except ValueError as e:
            raise err.ErrorException(e,message="target_link_uri is not URL", status_code=400)

        # Verify if the target_link_uri is valid and does not redirect to other domain than our tool
        # Verify HTTPS if in production
        try:
            if os.environ.get('FLASK_ENV') == 'production':
                if parsed_target_link_url.scheme != 'https':
                    raise err.ErrorException(message="target_link_uri is not HTTPS", status_code=400)
            if parsed_target_link_url.netloc != self._request.host:
                raise err.ErrorException(message="target_link_uri is not from the same host", status_code=400)
        except Exception as e:
            raise err.ErrorException(e,message="target_link_uri invalid", status_code=400)

        # Verify if the target_link_uri is valid and does not redirect to other domain than our tool
        if self._oidc_login_params_dict.get('target_link_uri') != self._platform.target_link_uri:
            raise err.ErrorException(message="target_link_uri may be malicious", status_code=400)

        return self

    def auth_redirect(self) -> Response:
        ''' Login to OIDC provider from LMS.
            Crafts the redirect url by adding the necessary parameters
        '''


        # Create a unique nonce in session for this flow to prevent replay attacks
        nonce = CryptoRandom().getrandomstring(32)
        # Create a unique state and state jwt for this flow to ensure integrity of the response
        # Store nonce and state pair in server side storage for later verification
        state_jwt = SessionServiceFlask.set_state_jwt(nonce,self._platform.auth_login_url, self._tool_config.get_tool_url(self._request.environ.get('HTTP_ORIGIN', '')))


        platform = self._tool_config.get_platform(os.environ.get('LMS_URL', 'https://moodle.haski.app'))
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



    def verify_state(self) -> 'OIDCLoginFlask':
        ''' Verify the state parameter
            If the state parameter is not valid, the request is rejected with a 403 Forbidden response.
        '''
        # 🔑 check auth
        if self._response:
            return self

        # Verify the state parameter
        if not self._request.form.get('state'):
            self._response = jsonify({'error': 'No state found'}), 403
            return self
        
        # verify state paramter signature
        state_form_jwt = self._request.form.get('state', type=str) or ''
        state_form = JWTKeyManagement.verify_jwt(state_form_jwt)
        assert(JWTKeyManagement.verify_state_jwt_payload(state_form))
        if not state_form:
            self._response = jsonify({'error': 'Invalid state signature'}), 403
            return self

        return self

    def verify_id_token(self) -> 'OIDCLoginFlask':
        ''' Verify the id_token
            If the id_token is not valid, the request is rejected with a 403 Forbidden response.
        '''
        # check auth
        if self._response:
            return self
        
        # check if error in request
        if self._request.form.get('error'):
            self._response = jsonify({'error': self._request.form.get('error')}), 400
        if not self._request.form.get('id_token'):
            self._response = jsonify({'error': 'No id_token found'}), 400

        # Decode the id_token
        id_token_jwt = self._request.form.get('id_token', type=str) or ''
        if not id_token_jwt:
            self._response = "Invalid id_token, crypto key signature or lti config data of LMS may have changed", 400
            return self
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
        try:
            # TODO🧾 parse token and write into structures       
            self.id_token = LTIIDToken(**self.id_token)
            SessionServiceFlask.set(self.id_token.nonce, 'id_token', self.id_token)
        except Exception as e:
            self._response = "Invalid id_token", 403
            return self

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
        nonce_jwt = JWTKeyManagement.generate_nonce_jwt(self.id_token.nonce, self._request.referrer, os.environ.get('BACKEND_URL', 'https://backend.haski.app'))
        SessionServiceFlask.set(self.id_token.nonce, 'nonce_jwt', nonce_jwt)
        # get platform
        try:
            self._platform = self._tool_config.decode_platform(self._tool_config.get_platform(self._request.environ.get('HTTP_ORIGIN', '')))
            if not self._platform:
                raise err.ErrorException(message="No platform found", status_code=400)
        except Exception as e:
            raise err.ErrorException(e,message="Error in check_auth", status_code=400)
        # redirect to tool (login url in react)
        response = redirect(self._platform.frontend_login_url + '?' + urllib.parse.urlencode({'nonce': nonce_jwt}))

        # get issuer
        # TODO🧾 based on issuer platform get corresponsing implementaiton and write id token data into structures

        # create user
        # TODO🧾 create student user if not exist
        try:
            user = services.get_user_by_lms_id(unit_of_work.SqlAlchemyUnitOfWork(), self.id_token.sub)
            if not user:
                user = services.create_user(unit_of_work.SqlAlchemyUnitOfWork(), name=self.id_token.name, university=self.id_token['https://purl.imsglobal.org/spec/lti/claim/tool_platform']['name'], lms_user_id=self.id_token.sub, role=RoleMapper(self.id_token['https://purl.imsglobal.org/spec/lti/claim/roles']).get_role())
            if user['role'] == 'student':
                # Type student, has to work cause of Substitution Principle
                user = services.get_student_by_user_id(unit_of_work.SqlAlchemyUnitOfWork(), user['id'])
            SessionServiceFlask.set(self.id_token.nonce, 'user', user)
        except Exception as e:
            raise err.ErrorException(e,message="User could not be created", status_code=400)

        return response

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
        # use session service id_token to get user data and write into cookie, create new user if not exist

        # get user based on id_token
        token = SessionServiceFlask.get(nonce_payload['nonce'], 'id_token')
        if not token:
            self._response = "Invalid nonce", 403
            return make_response(self._response)
        
        user = SessionServiceFlask.get(nonce_payload['nonce'], 'user')
        if not user:
            self._response = "Invalid state", 403
            # TODO 🧾 redirect to login
            return make_response(self._response)
        
        role = RoleMapper(token['https://purl.imsglobal.org/spec/lti/claim/roles']).get_role().lower()
        cookie_expiration = 43200 # 1 Minutes
        state_jwt = JWTKeyManagement.generate_state_jwt(nonce=CryptoRandom.createuniqueid(32), 
                                                        state=CryptoRandom.createuniqueid(32), 
                                                        audience=self._request.referrer, 
                                                        issuer=os.environ.get('BACKEND_URL', 'https://backend.haski.app'),
                                                        expiration=cookie_expiration,
                                                        additional_claims={'id': user.get('id'),
                                                                           'user_id': user.get('user_id'),
                                                                           'lms_user_id' : user['lms_user_id'], 
                                                                           'university': user['university'],                                                                           
                                                                           'role': role, 
                                                                           'role_id': user['role_id'],
                                                                           'session_nonce': nonce_payload['nonce']
                                                                           }
                                                        )
        response = Response(
            response=json.dumps(state_jwt),
            status=200,
            mimetype='application/json'
        )
        # set 🔑 auth 🍪 cookie
        domain = urllib.parse.urlparse(self._request.referrer).hostname
        self._cookie_service.set_cookie(response=response,key='haski_state',value=state_jwt, secure=False, httponly=True, samesite='Lax', max_age=cookie_expiration*60, domain=domain)
        return response

    def get_loginstatus(self) -> Response:
        # check if cookie exists
        if not self._request.cookies.get('haski_state'):
            self._response = jsonify({'message': 'No cookie found', 'status': 403})
            return make_response(self._response)
        
        # verify state jwt in request cookie        
        state_jwt = self._request.cookies.get('haski_state')
        if not state_jwt:
            self._response = jsonify({'message': 'No state found', 'status': 403})
            # TODO 🧾 redirect to login
            return make_response(self._response)
        state_payload = JWTKeyManagement.verify_jwt(state_jwt)
        if not state_payload:
            self._response = jsonify({'error': 'Invalid state signature'}), 403
            # TODO 🧾 redirect to login
            return make_response(self._response)
        return jsonify({'status': 200, 'message': 'User is logged in', 'data': state_payload})
    
    def get_logout(self) -> Response:
        self._response = jsonify({'status': 200})
        make_response(self._response)
        domain = urllib.parse.urlparse(self._request.referrer).hostname
        self._cookie_service.set_cookie(response=self._response,key='haski_state',value="", secure=False, httponly=True, samesite='Lax', max_age=0, domain=domain)
        
        return self._response