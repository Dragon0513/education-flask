import os
import shutil
import unittest
from unittest.mock import patch

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import service_layer.crypto.JWTKeyManagement as jwt
from service_layer.crypto.cryptorandom import CryptoRandom
from service_layer.service import SessionServiceFlask

PRIVATE_KEY_LOCATION: str = "keys/private.pem"
PUBLIC_KEY_LOCATION: str = "keys/public.pem"

BACKEND_URL = "https://backend.haski.app"
LMS_URL = "https://moodle.haski.app"


# ignore E501
config_file = {
    "https://moodle.haski.app": {
        "default": True,
        "client_id": "VRCKkhKlZtHNHtD",
        "tool_url": "https://backend.haski.app",
        "frontend_login_url": "https://haski.app/login",
        "target_link_uri": "https://backend.haski.app/lti_launch",
        "auth_login_url": "https://moodle.haski.app/mod/lti/auth.php",
        "auth_token_url": "https://moodle.haski.app/mod/lti/token.php",
        "key_set_url": "https://moodle.haski.app/mod/lti/certs.php",
        "haski_lti_activity": "https://moodle.haski.app/mod/lti/view.php?id=138",
        "platform_name": "HASKI",
        "key_set": {
            "keys": [
                {
                    "kty": "RSA",
                    "alg": "RS256",
                    "kid": "5e58bef6fa8030be050b",
                    "e": "AQAB",
                    # pylint: disable=line-too-long
                    "n": "z8uwIpHep-dGbqqutVqQPsXdwJk8ESoXPw1UD-9PmlTm06Q6PmXl5jHT9J6hTuW-9OjiycuBs07DW1At6LEAEBOJbFw2H6aflmPyhq09Cwernuk6OzekRRmnPdmfYeOcjpHAGaZ3qwaU0E6zPt_Ki1ZqdtLnB53ytO1fuYTmK1FVSbnexK9i4OkLk6OHMCHkInQTndRMWOiKWwrAoc591LlNSzgvlW_S9s-Vj2N4sHAcikKobzMMD8ixsV84Lx3mZyb13qph9qXUMJB9It-5WXa-FfsbUQZ6MeC0ks9_XSyl7tI7Q2eHUqenPimZL15uQnWek-gaE61IAK7ihKSMew",  # noqa: E501
                    "use": "sig",
                }
            ]
        },
        "private_key_file": "private.key",
        "public_key_file": "public.key",
        "deployment_ids": ["1"],
    }
}


class TestJWTKeyManagement(unittest.TestCase):
    def setUp(self):
        """
        Generate mock keys/private.pem and public.pem for testing.
        """
        super().setUp()
        if not os.path.exists("test_keys"):
            print("Generating test_keys directory")
            os.makedirs("test_keys")
        if not os.path.exists("test_keys/private.pem"):
            print("Generating test_keys/private.pem")
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend(),
            )
            with open("test_keys/private.pem", "wb") as f:
                f.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
            print("Generating test_keys/public.pem")
            with open("test_keys/public.pem", "wb") as f:
                f.write(
                    private_key.public_key().public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )
        # set the environment variables for the keys/ path
        os.environ["JWT_KEYS_LOCATION"] = "test_keys"

        os.environ["BACKEND_URL"] = BACKEND_URL
        os.environ["LMS_URL"] = LMS_URL

    def tearDown(self) -> None:
        """
        Cleanup mock keys/private.pem and public.pem after testing.
        """
        super().tearDown()
        print("Cleaning up test_keys directory")
        if os.path.exists("test_keys"):
            shutil.rmtree("test_keys")
            print("Removed test_keys directory")

    def test_get_unverified_header(self):
        """Test if a unverified header contains the correct information."""
        # Arrange
        test_dictionary = {"a": "b"}

        # Act
        token = jwt.sign_jwt(test_dictionary)
        header = jwt.get_unverified_header(token)

        # Assert
        assert header["alg"] == "RS256" and header["typ"] == "JWT"

    def test_fail_get_unverified_header(self):
        """Test if a unverified header with a wrong token fails."""
        # Arrange
        test_dictionary = {"a": "b"}

        # Act
        token = jwt.sign_jwt(test_dictionary)

        # Assert
        with self.assertRaises(Exception):
            corrupt_string = bytearray(token, "utf-8").replace(b".", b"!")
            jwt.get_unverified_header(corrupt_string.decode("utf-8"))

    def test_load_jwt(self):
        """Test if the unverified claims contains the correct information."""
        # Arrange
        test_dictionary = {"a": "b"}

        # Act
        token = jwt.sign_jwt(test_dictionary)
        claims = jwt.load_jwt(token)

        # Assert
        assert claims == test_dictionary

    def test_sign_verify_jwt(self):
        """Test if a payload can be signed with a\
            private key and verified with the public key."""
        # Arrange
        test_dictionary = {"a": "b"}

        # Act
        token = jwt.sign_jwt(test_dictionary)
        key_public = jwt.load_public_key()

        # Assert
        assert test_dictionary == jwt.verify_jwt(token, key_public)

    def test_no_key_sign_verify_jwt(self):
        """Test if a payload can be signed with a\
            private key and verified with the public key."""
        # Arrange
        test_dictionary = {"a": "b"}

        # Act
        token = jwt.sign_jwt(test_dictionary)

        # Assert
        assert test_dictionary == jwt.verify_jwt(token)

    def test_fail_verify_jwt(self):
        """Test if a payload can be signed with a\
            private key and verified with the public key."""
        # Arrange
        test_dictionary = {"a": "b"}

        # Act
        token = jwt.sign_jwt(test_dictionary)
        key_public = jwt.load_public_key()

        # Assert exception
        #         str(
        #     "(JWSError('Signature verification failed.'), 'The passed JWT is invalid.', 400)"
        # ),
        with self.assertRaises(
            Exception,
        ):
            jwt.verify_jwt(token + "a", key_public)

    def test_construct_jwt(self):
        """Test if a payload can be signed with a\
            private key and verified with the public key."""
        # Arrange
        test_dictionary = {"a": "b"}

        # Act
        platform = config_file["https://moodle.haski.app"]
        hmac = next(
            (key for key in platform["key_set"]["keys"]),
            "",
        )

        # Assert
        assert jwt.construct_key(hmac)

    def test_no_public_key_location(self):
        with patch.object(
            jwt,
            "public_key_location",
            return_value="",
        ):
            with self.assertRaises(
                Exception,
            ):
                jwt.load_public_key()

    def test_no_private_key_location(self):
        with patch.object(
            jwt,
            "private_key_location",
            return_value="",
        ):
            with self.assertRaises(
                Exception,
            ):
                jwt.sign_jwt({"a": "b"})

    def test_nonce_jwt(self):
        """Test if a nonce-token can be generated and verified."""
        # Arrange
        nonce = CryptoRandom().getrandomstring(32)
        state = CryptoRandom().getrandomstring(32)
        issuer = BACKEND_URL
        audience = "http://localhost"

        # Act
        token = jwt.generate_nonce_jwt(nonce, audience, issuer)
        state = jwt.generate_state_jwt(nonce, state, audience, issuer)
        state_jwt = SessionServiceFlask.set_state_jwt(
            nonce,
            LMS_URL + "/mod/lti/auth.php",
            BACKEND_URL,
        )
        key_public = jwt.load_public_key()

        # Assert
        assert jwt.verify_jwt_payload(jwt.verify_jwt(token, key_public))
        assert SessionServiceFlask.get(nonce, "state_jwt") == state_jwt

    def test_state_jwt(self):
        """Test if a state-token can be generated and verified."""
        # Arrange
        state = CryptoRandom().getrandomstring(32)
        nonce = CryptoRandom().getrandomstring(32)
        issuer = BACKEND_URL
        audience = "http://localhost:2000"
        expiration = 60
        claims = {"a": "b"}

        # Act
        token = jwt.generate_state_jwt(
            nonce, state, audience, issuer, claims, expiration
        )
        # When verifying the state token,
        # we need to set the state in the session
        SessionServiceFlask.set_state_jwt(
            nonce,
            LMS_URL + "/mod/lti/auth.php",
            BACKEND_URL,
        )
        key_public = jwt.load_public_key()

        # Assert
        assert jwt.verify_state_jwt_payload(
            jwt.verify_jwt(token, key_public),
            verify_nonce=False,
            session=False,
        )
