from cryptography.hazmat.primitives import serialization as crypto_serialization
from service_layer.crypto.cryptorandom import CryptoRandom
from service_layer.lti import LaunchDataStorage
import service_layer.crypto.JWTKeyManagement as jwt


private_key_location : str = "keys/private.pem"
public_key_location : str = "keys/public.pem"


def test_get_unverified_header():
    """Test if a unverified header contains the correct information."""
    # Arrange
    test_dictionary = {'a': 'b'}

    # Act
    token = jwt.sign_jwt(test_dictionary)
    header = jwt.get_unverified_header(token)

    #Assert
    assert header['alg'] == "RS256" and header['typ'] == "JWT"

def test_load_jwt():
    """Test if the unverified claims contains the correct information."""
    # Arrange
    test_dictionary = {'a': 'b'}

    # Act
    token = jwt.sign_jwt(test_dictionary)
    claims = jwt.load_jwt(token)

    #Assert
    assert claims == test_dictionary


def test_sign_verify_jwt():
    """Test if a payload can be signed with a private key and verified with the public key."""
    # Arrange
    test_dictionary = {'a': 'b'}

    # Act
    token = jwt.sign_jwt(test_dictionary)
    key_public = jwt.load_public_key()

    # Assert
    assert test_dictionary == jwt.verify_jwt(token, key_public)

def test_nonce_jwt():
    """Test if a nonce-token can be generated and verified."""
    # Arrange
    nonce = CryptoRandom().getrandomstring(32)
    LaunchDataStorage.set_value(nonce, nonce)
    issuer = 'http://fakedomain.com:5000'
    audience = 'http://fakedomain.com:2000'

    # Act
    token = jwt.generate_nonce_jwt(nonce, audience, issuer)
    key_public = jwt.load_public_key()

    # Assert
    assert jwt.verify_jwt_payload(jwt.verify_jwt(token, key_public))

def test_state_jwt():
    """Test if a state-token can be generated and verified."""
    # Arrange
    state = CryptoRandom().getrandomstring(32)
    nonce = CryptoRandom().getrandomstring(32)
    LaunchDataStorage.set_value(nonce, state)
    issuer = 'http://fakedomain.com:5000'
    audience = 'http://fakedomain.com:2000'
    expiration = 60
    claims = {'a' : 'b'}

    # Act
    token = jwt.generate_state_jwt(nonce, state, audience, issuer, claims, expiration)
    key_public = jwt.load_public_key()

    # Assert
    assert jwt.verify_state_jwt_payload(jwt.verify_jwt(token, key_public))