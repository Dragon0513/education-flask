import datetime
import json
import os
import pickle
from typing import Any, Mapping
from jose import jws, jwk
from jose.backends.base import Key
from cryptography.hazmat.primitives import serialization as crypto_serialization

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
    return json.loads(jws.verify(jwt_token, key, algorithms=["RS256"]).decode('UTF-8'))

def get_unverified_header(jwt_token : str):
    return jws.get_unverified_header(jwt_token)

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

def generate_state_jwt(nonce : str, state : str, audience : str, issuer : str):
    state_jwt = {
        'state': state,
        'nonce': nonce,
        'iat': datetime.datetime.utcnow().timestamp(),
        'exp': (datetime.datetime.utcnow() + datetime.timedelta(minutes=60)).timestamp(),
        'aud': audience,
        'kid': 'backendprivatekey',
        'iss': issuer
    }
    return sign_jwt(state_jwt)