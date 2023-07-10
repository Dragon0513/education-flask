from service_layer.crypto.cryptorandom import CryptoRandom
import service_layer.crypto.JWTKeyManagement as jwt
from service_layer.service import SessionServiceFlask


private_key_location: str = "keys/private.pem"
public_key_location: str = "keys/public.pem"

# pytest tests\unit\lti\test_JWTKeyManagement.py --cov


def test_get_unverified_header():
    """Test if a unverified header contains the correct information."""
    # Arrange
    test_dictionary = {"a": "b"}

    # Act
    token = jwt.sign_jwt(test_dictionary)
    header = jwt.get_unverified_header(token)

    # Assert
    assert header["alg"] == "RS256" and header["typ"] == "JWT"


def test_load_jwt():
    """Test if the unverified claims contains the correct information."""
    # Arrange
    test_dictionary = {"a": "b"}

    # Act
    token = jwt.sign_jwt(test_dictionary)
    claims = jwt.load_jwt(token)

    # Assert
    assert claims == test_dictionary


def test_sign_verify_jwt():
    """Test if a payload can be signed with a private key and verified with the public key."""
    # Arrange
    test_dictionary = {"a": "b"}

    # Act
    token = jwt.sign_jwt(test_dictionary)
    key_public = jwt.load_public_key()

    # Assert
    assert test_dictionary == jwt.verify_jwt(token, key_public)


def test_nonce_jwt():
    """Test if a nonce-token can be generated and verified."""
    # Arrange
    nonce = CryptoRandom().getrandomstring(32)
    state = CryptoRandom().getrandomstring(32)
    issuer = "https://backend.haski.app"
    audience = "http://localhost"

    # Act
    token = jwt.generate_nonce_jwt(nonce, audience, issuer)
    state = jwt.generate_state_jwt(nonce, state, audience, issuer)
    state_jwt = SessionServiceFlask.set_state_jwt(
        nonce,
        "https://moodle.haski.app/mod/lti/auth.php",
        "https://backend.haski.app",
    )
    key_public = jwt.load_public_key()

    # Assert
    assert jwt.verify_jwt_payload(jwt.verify_jwt(token, key_public))
    assert SessionServiceFlask.get(
        nonce, "state_jwt") == state_jwt


def test_state_jwt():
    """Test if a state-token can be generated and verified."""
    # Arrange
    state = CryptoRandom().getrandomstring(32)
    nonce = CryptoRandom().getrandomstring(32)
    issuer = "https://backend.haski.app"
    audience = "http://localhost:2000"
    expiration = 60
    claims = {"a": "b"}

    # Act
    token = jwt.generate_state_jwt(
        nonce, state, audience, issuer, claims, expiration
    )
    # When verifying the state token, we need to set the state in the session
    SessionServiceFlask.set_state_jwt(
        nonce,
        "https://moodle.haski.app/mod/lti/auth.php",
        "https://backend.haski.app",
    )
    key_public = jwt.load_public_key()

    # Assert
    assert jwt.verify_state_jwt_payload(
        jwt.verify_jwt(token, key_public), verify_nonce=False, session=False
    )
