import os
import pickle
from jose import jws
from cryptography.hazmat.primitives import serialization as crypto_serialization

private_key_location : str = "keys/private.pem"
public_key_location : str = "keys/public.pem"

def load_public_key():
    with open(os.path.abspath(public_key_location), "rb") as key_file:
        public_key = crypto_serialization.load_pem_public_key(key_file.read())
        return public_key.public_bytes(crypto_serialization.Encoding.PEM,
                            crypto_serialization.PublicFormat.SubjectPublicKeyInfo)

def verify_own_jwt(jwt_token : str):
    return jws.verify(jwt_token, load_public_key().decode(), algorithms=["RS256"])

def sign_jwt(payload : dict):
    with open(os.path.abspath(private_key_location), "rb") as key_file:
            private_key = crypto_serialization.load_pem_private_key(key_file.read(), password=None)

            key_private = private_key.private_bytes(crypto_serialization.Encoding.PEM,
                            crypto_serialization.PrivateFormat.PKCS8,
                            crypto_serialization.NoEncryption())
            return jws.sign(payload, key_private, algorithm="RS256")

def load_jwt(jwt_token : str):
    return jws.get_unverified_claims(jwt_token)