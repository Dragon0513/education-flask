import datetime
import json
import os
import pickle
from typing import Any, Mapping
from jose import JWSError, jws, jwk
from jose.backends.base import Key
from cryptography.hazmat.primitives import serialization as crypto_serialization
from errors.errors import InvalidJWTError

from service_layer.crypto.cryptorandom import CryptoRandom
from service_layer.lti import LaunchDataStorage

private_key_location : str = "keys/private.pem"
public_key_location : str = "keys/public.pem"

def load_public_key():
    with open(os.path.abspath(public_key_location), "rb") as key_file:
        public_key = crypto_serialization.load_pem_public_key(key_file.read())
        return public_key.public_bytes(crypto_serialization.Encoding.PEM,
                            crypto_serialization.PublicFormat.SubjectPublicKeyInfo)

def construct_key(key : str | bytes | dict[str, Any] | Key):
    return jwk.construct(key)

def verify_jwt(jwt_token : str, key : str | bytes | Mapping[str, Any] | Key = load_public_key().decode()):
    ''' Returns the payload of the JWT token if it is valid, otherwise raises an exception'''
    try:
        return json.loads(jws.verify(jwt_token, key, algorithms=["RS256"]).decode('UTF-8'))
    except JWSError as e:
        raise InvalidJWTError(e)

def get_unverified_header(jwt_token : str):
    try:
        return jws.get_unverified_header(jwt_token)
    except JWSError as e:
        raise InvalidJWTError(e)

def sign_jwt(payload : dict):
    with open(os.path.abspath(private_key_location), "rb") as key_file:
            private_key = crypto_serialization.load_pem_private_key(key_file.read(), password=None)

            key_private = private_key.private_bytes(crypto_serialization.Encoding.PEM,
                            crypto_serialization.PrivateFormat.PKCS8,
                            crypto_serialization.NoEncryption())
            return jws.sign(payload, key_private, algorithm="RS256")

def load_jwt(jwt_token : str):
    return json.loads(jws.get_unverified_claims(jwt_token))

def generate_nonce_jwt(nonce : str, audience : str, issuer : str):
    nonce_jwt = {
        'nonce': nonce,
        'iat': datetime.datetime.utcnow().timestamp(),
        'exp': (datetime.datetime.utcnow() + datetime.timedelta(minutes=60)).timestamp(),
        'aud': audience,
        'kid': 'backendprivatekey',
        'iss': issuer
    }
    return sign_jwt(nonce_jwt)

def generate_state_jwt(nonce : str, state : str, audience : str, issuer : str, additional_claims : dict = {}, expiration : int = 60):
    state_jwt = {
        'state': state,
        'nonce': nonce,
        **additional_claims,
        'iat': datetime.datetime.utcnow().timestamp(),
        'exp': (datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration)).timestamp(),
        'aud': audience,
        'kid': 'backendprivatekey',
        'iss': issuer
    }
    return sign_jwt(state_jwt)

def verify_jwt_payload(jwt_payload, verify_nonce=True) -> bool:
    """Verifies the payload of a JWT token. Returns True if the payload is valid, otherwise False."""
    if verify_nonce and not LaunchDataStorage.get_value(jwt_payload['nonce']):
        return False
    # verify issued at
    if jwt_payload['iat'] > datetime.datetime.utcnow().timestamp():
        return False
    # verify expiration
    if jwt_payload['exp'] < datetime.datetime.utcnow().timestamp():
        return False
    # verify issuer
    if jwt_payload['iss'] != os.environ.get('BACKEND_URL', 'http://localhost:5000'):
        return False
    # verify kid
    if jwt_payload['kid'] != 'backendprivatekey':
        return False
    return True

def verify_state_jwt_payload(state_jwt_payload) -> bool:
    if verify_jwt_payload(state_jwt_payload) == False:
        return False
    # verify state in storage
    if LaunchDataStorage.get_value(state_jwt_payload['nonce']) != state_jwt_payload['state']:
        return False
    return True