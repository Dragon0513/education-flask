import service_layer.crypto.JWTKeyManagement as JWT
from jose.backends.base import Key
import os
from cryptography.hazmat.primitives import serialization as crypto_serialization
from service_layer.crypto.cryptorandom import CryptoRandom


private_key_location : str = "keys/private.pem"
public_key_location : str = "keys/public.pem"


def test_get_unverified_header():
    """Test if a unverified header contains the correct information."""
    # Arrange
    test_dictionary = {'a': 'b'}

    # Act
    token = JWT.sign_jwt(test_dictionary)
    header = JWT.get_unverified_header(token)

    #Assert
    assert header['alg'] == "RS256" and header['typ'] == "JWT"

def test_load_jwt():
    """Test if the unverified claims contains the correct information."""
    # Arrange
    test_dictionary = {'a': 'b'}

    # Act
    token = JWT.sign_jwt(test_dictionary)
    claims = JWT.load_jwt(token)

    #Assert
    #assert claims == ?????


def test_sign_verify_jwt():
    """Test if a payload can be signed with a private key and verified with the public key."""
    # Arrange
    test_dictionary = {'a': 'b'}

    # Act
    token = JWT.sign_jwt(test_dictionary)
    key_public = JWT.load_public_key()

    # Assert
    assert test_dictionary == JWT.verify_jwt(token, key_public)

def test_nonce_jwt():
    """Test if a nonce-token can be generated and verified."""
    # Arrange
    nonce = CryptoRandom().getrandomstring(32)
    issuer = 'http://fakedomain.com:5000'
    audience = 'http://fakedomain.com:2000'

    # Act
    token = JWT.generate_nonce_jwt(nonce, audience, issuer)
    key_public = JWT.load_public_key()

    # Assert
    assert JWT.verify_jwt_payload(JWT.verify_jwt(token, key_public))

def test_state_jwt():
    """Test if a state-token can be generated and verified."""
    # Arrange
    state = CryptoRandom().getrandomstring(32)
    nonce = CryptoRandom().getrandomstring(32)
    issuer = 'http://fakedomain.com:5000'
    audience = 'http://fakedomain.com:2000'
    expiration = 60
    claims = {'a' : 'b'}

    # Act
    token = JWT.generate_state_jwt(nonce, state, audience, issuer, claims, expiration)
    key_public = JWT.load_public_key()

    # Assert
    assert JWT.verify_state_jwt_payload(JWT.verify_jwt(token, key_public))