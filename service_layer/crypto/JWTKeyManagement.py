import datetime
import json
import os
from typing import Any, Mapping

from cryptography.hazmat.primitives import serialization as crypto_serialization
from jose import JWSError, jwk, jws
from jose.backends.base import Key

import errors.errors as err
import service_layer.service.SessionServiceFlask as SessionServiceFlask
from config import get_project_root
from errors.errors import InvalidJWTError

public_key = None
private_key = None


def private_key_location():
    return os.path.abspath(
        os.environ.get(
            os.path.join("JWT_KEYS_LOCATION" + "private.pem"),
            os.path.join(get_project_root(), "keys/private.pem"),
        )
    )


def public_key_location():
    return os.path.abspath(
        os.environ.get(
            os.path.join("JWT_KEYS_LOCATION", "public.pem"),
            os.path.join(get_project_root(), "keys/public.pem"),
        )
    )


def load_public_key():
    if not os.path.exists(public_key_location()):
        raise err.KeyNotFoundError(
            message="Public key location:"
            + public_key_location()
            + " not found. Please generate a\
                key pair as described in the README.md."
        )
    with open(os.path.abspath(public_key_location()), "rb") as key_file:
        public_key = crypto_serialization.load_pem_public_key(key_file.read())
        return public_key.public_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PublicFormat.SubjectPublicKeyInfo,
        )


def construct_key(key: str | bytes | dict[str, Any] | Key):
    return jwk.construct(key)


def verify_jwt(
    jwt_token: str,
    key: str | bytes | Mapping[str, Any] | Key | None = None,
):
    """Returns the payload of the JWT token if it is valid,
    otherwise raises an exception"""
    if key is None:
        global public_key
        if public_key is None:
            public_key = load_public_key().decode()
        key = public_key
    try:
        return json.loads(
            jws.verify(jwt_token, key, algorithms=["RS256"]).decode("UTF-8")
        )
    except JWSError as e:
        raise InvalidJWTError(e)


def get_unverified_header(jwt_token: str):
    try:
        return jws.get_unverified_header(jwt_token)
    except JWSError as e:
        raise InvalidJWTError(e)


def sign_jwt(payload: dict):
    if not os.path.exists(private_key_location()):
        raise err.KeyNotFoundError(
            message="Private key location:"
            + private_key_location()
            + " not found. Please generate a key pair as\
                described in the README.md."
        )
    with open(os.path.abspath(private_key_location()), "rb") as key_file:
        private_key = crypto_serialization.load_pem_private_key(
            key_file.read(), password=None
        )

        key_private = private_key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption(),
        )
        return jws.sign(payload, key_private, algorithm="RS256")


def load_jwt(jwt_token: str):
    return json.loads(jws.get_unverified_claims(jwt_token))


def generate_nonce_jwt(nonce: str, audience: str, issuer: str):
    nonce_jwt = {
        "nonce": nonce,
        "iat": datetime.datetime.utcnow().timestamp(),
        "exp": (
            datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        ).timestamp(),
        "aud": audience,
        "kid": "backendprivatekey",
        "iss": issuer,
    }
    return sign_jwt(nonce_jwt)


def generate_state_jwt(
    nonce: str,
    state: str,
    audience: str,
    issuer: str,
    additional_claims: dict = {},
    expiration: int = 60,
):
    state_jwt = {
        "state": state,
        "nonce": nonce,
        **additional_claims,
        "iat": datetime.datetime.utcnow().timestamp(),
        "exp": (
            datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration)
        ).timestamp(),
        "aud": audience,
        "kid": "backendprivatekey",
        "iss": issuer,
    }
    return sign_jwt(state_jwt)


def verify_jwt_payload(jwt_payload, verify_nonce=True) -> bool:
    """Verifies the payload of a JWT token. Returns\
        True if the payload is valid, otherwise False."""
    if verify_nonce and not SessionServiceFlask.get(jwt_payload["nonce"], "state"):
        return False
    # verify issued at
    if jwt_payload["iat"] > datetime.datetime.utcnow().timestamp():
        return False
    # verify expiration
    if jwt_payload["exp"] < datetime.datetime.utcnow().timestamp():
        return False
    # verify issuer
    if jwt_payload["iss"] != os.environ.get("BACKEND_URL", "https://backend.haski.app"):
        return False
    # verify kid
    if jwt_payload["kid"] != "backendprivatekey":
        return False
    return True


def verify_state_jwt_payload(
    state_jwt_payload, verify_nonce=True, session=True
) -> bool:
    if not verify_jwt_payload(state_jwt_payload, verify_nonce):
        return False
    # verify state in storage
    if (
        session
        and SessionServiceFlask.get(state_jwt_payload["nonce"], "state")
        != state_jwt_payload["state"]
    ):
        return False
    return True
