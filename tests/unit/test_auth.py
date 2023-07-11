import json
import unittest
from unittest.mock import patch, MagicMock
import errors.errors as err
from utils.auth.permissions import Permissions
from utils.auth.auth import authorize
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement


class TestAuthorizeDecorator(unittest.TestCase):
    def setUp(self):
        from flask import Flask
        self.app = Flask(__name__)

    def test_authorized_user(self):
        state = {"permissions": [Permissions.READ.value]}
        # Mock the request object
        with self.app.test_request_context():
            with patch.multiple(
                JWTKeyManagement,
                verify_jwt=MagicMock(return_value=state),
                verify_jwt_payload=MagicMock(return_value=True),
                load_public_key=MagicMock(return_value="public_key"),
            ):
                # Define a test route that requires READ permission
                @self.app.route("/test")
                @authorize([Permissions.READ])
                def test_route(state):
                    return "Success"

                # Make a request with a valid JWT
                c = self.app.test_client()
                c.set_cookie("haski_state", "haski_state")  # '' is not None
                response = c.get("/test")
                # Assert that the response is successful
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data, b"Success")

    def test_unauthorized_user(self):
        state = {"permissions": []}
        # Mock the request object
        with self.app.test_request_context():
            with patch.multiple(
                JWTKeyManagement,
                verify_jwt=MagicMock(return_value=state),
                verify_jwt_payload=MagicMock(return_value=True),
                load_public_key=MagicMock(return_value="public_key"),
            ):
                # Define a test route that requires READ permission
                @self.app.route("/test")
                @authorize([Permissions.READ])
                def test_route(state):
                    return "Success"

                @self.app.errorhandler(err.AException)
                def handle_custom_exception(ex: err.AException):
                    response = json.dumps(
                        {"error": str(ex), "message": ex.message}
                    )
                    return response, ex.status_code

                # Make a request with an invalid JWT
                c = self.app.test_client()
                c.set_cookie("haski_state", "haski_state")
                response = c.get("/test")

                self.assertEqual(response.status_code, 401)
