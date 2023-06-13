import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from werkzeug.exceptions import Unauthorized
from utils.auth.permissions import Permissions
from utils.auth.auth import authorize
from service_layer.crypto.JWTKeyManagement import JWTKeyManagement


class TestAuthorizeDecorator(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def test_authorized_user(self):
        state = {'permissions': [Permissions.READ.value]}
        # Mock the request object
        with self.app.test_request_context():
            with patch.multiple(JWTKeyManagement,
                                verify_jwt=MagicMock(return_value=state),
                                verify_jwt_payload=MagicMock(
                                    return_value=True)):
                # Define a test route that requires READ permission
                @self.app.route('/test')
                @authorize([Permissions.READ])
                def test_route(state):
                    return 'Success'

                # Make a request with a valid JWT
                c = self.app.test_client()
                c.set_cookie('haski_state', 'haski_state')  # '' is not None
                response = c.get('/test')
                # Assert that the response is successful
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data, b'Success')

    def test_unauthorized_user(self):
        state = {'permissions': []}
        # Mock the request object
        with self.app.test_request_context():
            with patch.multiple(JWTKeyManagement,
                                verify_jwt=MagicMock(return_value=state),
                                verify_jwt_payload=MagicMock(
                                    return_value=True)):
                # Define a test route that requires READ permission
                @self.app.route('/test')
                @authorize([Permissions.READ])
                def test_route(state):
                    return 'Success'

                # Make a request with an invalid JWT
                c = self.app.test_client()
                c.set_cookie('haski_state', 'haski_state')
                response = c.get('/test')

                self.assertEqual(response.status_code, 401)
