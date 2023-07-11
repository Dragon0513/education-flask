import json
import os
import time
import urllib.parse
from service_layer import services, unit_of_work
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement
from errors import errors as err
from flask import redirect
from flask.wrappers import Request
from werkzeug.wrappers.response import Response
from service_layer.crypto.cryptorandom import CryptoRandom
from service_layer.lti.Messages import LTIIDToken
from service_layer.lti.OIDCLogin import OIDCLogin
from service_layer.lti.Roles import RoleMapper
from service_layer.service.CookieServiceFlask import CookieServiceFlask
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
import service_layer.service.SessionServiceFlask as SessionServiceFlask


class OIDCLoginFlask(OIDCLogin):
    """Flask implementation of OIDC login"""

    def __init__(
        self,
        request: Request,
        tool_config: ToolConfigJson,
        cookie_service=None,
    ):
        self._request = request
        self._cookie_service = (
            cookie_service if cookie_service else CookieServiceFlask(request)
        )
        self.oidc_login_params = {
            "iss",
            "client_id",
            "login_hint",
            "lti_message_hint",
            "target_link_uri",
            "lti_deployment_id",
        }
        super(OIDCLoginFlask, self).__init__(request, tool_config)

    def check_params(self) -> "OIDCLoginFlask":
        # Check if all parameters are present
        try:
            if not self.oidc_login_params.issubset(self._request.form.keys()):
                raise err.MissingParameterError(status_code=400)
            # store subset with values from request form in object
            else:
                self._oidc_login_params_dict = {
                    key: self._request.form.get(key)
                    for key in self.oidc_login_params
                }
        except Exception as e:
            raise err.ErrorException(
                e, message="Error in checking parameters", status_code=400
            )

        # Get the platform settings (same scheme as in the tool config json)
        # HTTP_ORIGIN is a safe way to get the origin of the request
        # and a way to avoid CSRF attacks
        # when redirected from http it doesnt work anymore
        try:
            self._platform = self._tool_config.decode_platform(
                self._tool_config.get_platform(
                    os.environ.get("LMS_URL", "https://moodle.haski.app")
                )
            )
            if not self._platform:
                raise err.ErrorException(
                    message="No platform found", status_code=400
                )
        except Exception as e:
            raise err.ErrorException(
                e, message="Error in check_auth", status_code=400
            )
        try:
            parsed_target_link_url = (
                urllib.parse.urlparse(
                    self._oidc_login_params_dict.get("target_link_uri")
                )
                or None
            )
        except ValueError as e:
            raise err.ErrorException(
                e, message="target_link_uri is not URL", status_code=400
            )

        # Verify if the target_link_uri is valid
        # and does not redirect to other domain than our tool
        # Verify HTTPS if in production
        try:
            if os.environ.get("FLASK_ENV") == "production":
                if parsed_target_link_url.scheme != "https":
                    raise err.ErrorException(
                        message="target_link_uri is not HTTPS", status_code=400
                    )
            if parsed_target_link_url.netloc != self._request.host:
                raise err.ErrorException(
                    message="target_link_uri is not from the same host",
                    status_code=400,
                )
        except Exception as e:
            raise err.ErrorException(
                e, message="target_link_uri invalid", status_code=400
            )

        # Verify if the target_link_uri is valid and
        # does not redirect to other domain than our tool
        if (
            self._oidc_login_params_dict.get("target_link_uri")
            != self._platform.target_link_uri
        ):
            raise err.ErrorException(
                message="target_link_uri may be malicious", status_code=400
            )

        return self

    def auth_redirect(self) -> Response:
        """Login to OIDC provider from LMS.
        Crafts the redirect url by adding the necessary parameters
        """

        # Create a unique nonce in session for this
        # flow to prevent replay attacks
        nonce = CryptoRandom().getrandomstring(32)
        # Create a unique state and state jwt for this flow
        # to ensure integrity of the response
        # Store nonce and state pair in server
        # side storage for later verification
        state_jwt = SessionServiceFlask.set_state_jwt(
            nonce,
            self._platform.auth_login_url,
            self._tool_config.get_tool_url(
                self._request.environ.get("HTTP_ORIGIN", "")
            ),
        )

        platform = self._tool_config.get_platform(
            os.environ.get("LMS_URL", "https://moodle.haski.app")
        )
        ru = self.make_url_accept_param(platform["auth_login_url"])
        params = {
            "client_id": platform["client_id"],
            "response_mode": "form_post",
            "redirect_uri": self._oidc_login_params_dict.get(
                "target_link_uri"
            ),
            "response_type": "id_token",
            "scope": "openid",
            "nonce": nonce,
            "state": state_jwt,
            "login_hint": self._oidc_login_params_dict.get("login_hint"),
            # resource link id or deep link idc
            "lti_message_hint": self._oidc_login_params_dict.get(
                "lti_message_hint"
            ),
        }
        print(ru + urllib.parse.urlencode(params))
        response = redirect(ru + urllib.parse.urlencode(params))
        return response

    def verify_state(self) -> "OIDCLoginFlask":
        """Verify the state parameter
        If the state parameter is not valid, the request
         is rejected with a 403 Forbidden response.
        """
        # 🔑 check auth

        # Verify the state parameter
        if not self._request.form.get("state"):
            raise err.ErrorException(message="No state found", status_code=403)

        # verify state paramter signature
        state_form_jwt = self._request.form.get("state", type=str) or ""
        state_form = JWTKeyManagement.verify_jwt(state_form_jwt)
        if not state_form:
            raise err.ErrorException(
                message="Invalid state signature", status_code=403
            )
        if not JWTKeyManagement.verify_state_jwt_payload(state_form):
            raise err.ErrorException(
                message="Invalid state payload", status_code=403
            )

        return self

    def verify_id_token(self) -> "OIDCLoginFlask":
        """Verify the id_token
        If the id_token is not valid,
         the request is rejected with a 403 Forbidden response.
        """

        # check if error in request
        if self._request.form.get("error"):
            raise err.ErrorException(
                message=self._request.form.get("error") or "Unknown error",
                status_code=400,
            )
        if not self._request.form.get("id_token"):
            raise err.ErrorException(
                message="No id_token found", status_code=400
            )

        # Decode the id_token
        id_token_jwt = self._request.form.get("id_token", type=str) or ""
        if not id_token_jwt:
            raise err.ErrorException(
                message="Invalid id_token, crypto key\
                    signature or lti config data of LMS may have changed",
                status_code=400,)

        id_token_header_unverified = JWTKeyManagement.get_unverified_header(
            id_token_jwt
        )
        id_token_unverified = JWTKeyManagement.load_jwt(id_token_jwt)

        platform = self._tool_config.get_platform(id_token_unverified["iss"])
        hmac_key: str = next(
            (
                key
                for key in platform["key_set"]["keys"]
                if key["kid"] == id_token_header_unverified["kid"]
            ),
            "",
        )
        if not hmac_key:
            raise err.ErrorException(
                message="Invalid decryption key", status_code=400
            )
        self.id_token = JWTKeyManagement.verify_jwt(
            id_token_jwt, JWTKeyManagement.construct_key(hmac_key)
        )
        if not self.id_token:
            raise err.ErrorException(
                message="Invalid id_token signature", status_code=403
            )
        try:
            self.id_token = LTIIDToken(**self.id_token)
            SessionServiceFlask.set(
                self.id_token.nonce, "id_token", self.id_token
            )
        except Exception as e:
            raise err.ErrorException(
                e, message="Invalid id_token", status_code=403
            )

        return self

    def lti_launch_from_id_token(self) -> Response:
        """Launch LTI from id_token. Redirects\
            to Frontend with nonce jwt in URL."""
        # state from form
        state_form_jwt = self._request.form.get("state", type=str) or ""
        state_form = JWTKeyManagement.verify_jwt(state_form_jwt)
        if not JWTKeyManagement.verify_state_jwt_payload(state_form):
            raise err.ErrorException(
                message="Invalid state payload", status_code=403
            )

        # generate nonce to obtain cookie in next request
        nonce_jwt = JWTKeyManagement.generate_nonce_jwt(
            self.id_token.nonce,
            self._request.referrer,
            os.environ.get("BACKEND_URL", "https://backend.haski.app"),
        )
        SessionServiceFlask.set(self.id_token.nonce, "nonce_jwt", nonce_jwt)
        # get platform from origin
        try:
            self._platform = self._tool_config.decode_platform(
                self._tool_config.get_platform(
                    self._request.environ.get("HTTP_ORIGIN", "")
                )
            )
            if not self._platform:
                raise err.ErrorException(
                    message="No platform found", status_code=400
                )
        except Exception as e:
            raise err.ErrorException(
                e, message="Error\
                    in check_auth", status_code=400
            )
        # redirect to tool (login url in frontend)
        # e.g. https://haski.app/login?nonce=...
        response = redirect(
            self._platform.frontend_login_url
            + "?"
            + urllib.parse.urlencode({"nonce": nonce_jwt})
        )

        try:
            user = services.get_user_by_lms_id(
                unit_of_work.SqlAlchemyUnitOfWork(), self.id_token.sub
            )
            if not user:
                user = services.create_user(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    name=self.id_token.name, university=self.id_token
                    ["https://purl.imsglobal.org/spec/lti/claim/tool_platform"]
                    ["name"],
                    lms_user_id=self.id_token.sub,
                    role=RoleMapper(
                        self.id_token
                        ["https://purl.imsglobal.org/spec/lti/claim/roles"]).
                    get_role(),)
            if user["role"] == "student":
                # Type student, has to work cause of Substitution Principle
                user = services.get_student_by_user_id(
                    unit_of_work.SqlAlchemyUnitOfWork(), user["id"]
                )
            SessionServiceFlask.set(self.id_token.nonce, "user", user)
        except Exception as e:
            raise err.ErrorException(
                e, message="User could not be created", status_code=400
            )

        return response

    def get_cookie_expiration(self) -> Response:
        # verify nonce jwt in request
        json_data = self._request.get_json() or {}
        if not json_data.get("nonce"):
            raise err.ErrorException(message="No nonce found", status_code=403)
        nonce_jwt = json_data["nonce"] or ""
        nonce_payload = JWTKeyManagement.verify_jwt(nonce_jwt)
        if not nonce_payload:
            raise err.ErrorException(
                message="Invalid nonce signature", status_code=403
            )

        if not JWTKeyManagement.verify_jwt_payload(nonce_payload):
            raise err.ErrorException(
                message="Invalid nonce payload", status_code=403
            )

        # get user based on id_token
        token = SessionServiceFlask.get(nonce_payload["nonce"], "id_token")
        if not token:
            raise err.ErrorException(message="Invalid nonce", status_code=403)

        user = SessionServiceFlask.get(nonce_payload["nonce"], "user")
        if not user:
            raise err.ErrorException(message="Invalid state", status_code=403)

        role_mapper = RoleMapper(
            token["https://purl.imsglobal.org/spec/lti/claim/roles"]
        )
        role = role_mapper.get_role().lower()
        permissions = role_mapper.get_permissions()
        cookie_expiration = 43200
        state_jwt = JWTKeyManagement.generate_state_jwt(
            nonce=CryptoRandom.createuniqueid(32),
            state=CryptoRandom.createuniqueid(32),
            audience=self._request.referrer,
            issuer=os.environ.get("BACKEND_URL", "https://backend.haski.app"),
            expiration=cookie_expiration,
            additional_claims={
                "id": user.get("id"),
                "user_id": user.get("user_id"),
                "lms_user_id": user["lms_user_id"],
                "university": user["university"],
                "role": role,
                "role_id": user["role_id"],
                "session_nonce": nonce_payload["nonce"],
                "permissions": [
                    permission.value for permission in permissions
                ],
            },
        )
        # response object to attach a cookie
        response = Response(
            response=json.dumps(
                {
                    # UNIX time
                    "expiration": int(time.time())
                    + cookie_expiration * 60,
                }
            ),
            status=200,
            mimetype="application/json",
        )
        # set 🔑 auth 🍪 cookie
        domain = urllib.parse.urlparse(self._request.referrer).hostname
        secure = True if self._request.referrer.startswith("https") else False
        self._cookie_service.set_cookie(
            response=response,
            key="haski_state",
            value=state_jwt,
            secure=secure,
            httponly=True,
            samesite="Lax",
            max_age=cookie_expiration,
            domain=domain,
        )
        return response

    def get_logout(self) -> Response:
        response = Response(status=204)
        domain = urllib.parse.urlparse(self._request.referrer).hostname
        self._cookie_service.set_cookie(
            response,
            key="haski_state",
            value="",
            secure=False,
            httponly=True,
            samesite="Lax",
            max_age=0,
            domain=domain,
        )

        return response
