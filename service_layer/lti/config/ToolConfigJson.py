import json
import os

from config import get_project_root
from errors import errors as err
from service_layer.lti.lms.Platform import Platform


# Parses LTI Config file and returns a dictionary of the contents
_iss_conf_dict = {
    "http://fakedomain.com": {
        "default": True,
        "client_id": "L27dePw8pAl34ST",
        "tool_url": os.environ.get("BACKEND_URL", "http://fakedomain.com:5000"),
        "frontend_login_url": os.environ.get(
            "FRONTEND_URL", "http://fakedomain.com:8080"
        )
        + "/login",
        "target_link_uri": os.environ.get("BACKEND_URL", "http://fakedomain.com:5000")
        + "/lti_launch",
        "auth_login_url": os.environ.get("MOODLE_URL", "http://fakedomain.com")
        + "/mod/lti/auth.php",
        "auth_token_url": os.environ.get("MOODLE_URL", "http://fakedomain.com")
        + "/mod/lti/token.php",
        "key_set_url": os.environ.get("MOODLE_URL", "http://fakedomain.com")
        + "/mod/lti/certs.php",
        "haski_lti_activity": os.environ.get("MOODLE_URL", "http://fakedomain.com")
        + "/mod/lti/view.php?id=2",
        "platform_name": "HASKI",
        "key_set": {
            "keys": [
                {
                    "kty": "RSA",
                    "alg": "RS256",
                    "kid": "77ce2052ed246a4259da",
                    "e": "AQAB",
                    "n": "poaM0tABqlxYEEzlqZaD1UsicOunF3WxYBeWHRFZE8s2yTzae3EXJJay6df0FevpE67d0URspbG-U0cVVZnOR7r4Q-4BqJd_KDuQ6e9ZTYCvjCbWWxEu74gutZuZ9phMPWEGB8VJYWmfr0xi0YSGAwKqkNsyqbwJuO2sIXMCjJ7TleUz4QwCGoKAzDhXG6AROKMFa85blKz3Qz7PK6AWSGsQv5I-3kYWbZmQ8dlHhUe_Fgrul9by8qcYW3as5R9R00gheR5oAcminqiZTyjEWMLurCibaAuo-DrwNLeRkh1Z5dxi0JS3EqBWeTexXt8Yoh8cIGzifvNgHkwxSVwaYQ",
                    "use": "sig",
                }
            ]
        },
        "private_key_file": "private.key",
        "public_key_file": "public.key",
        "deployment_ids": ["1"],
    }
}


def get_platform(iss: str):
    return _iss_conf_dict[iss]


def decode_platform(platformdict: dict) -> Platform:
    """Decodes a platform dictionary into a Platform object"""
    try:
        return Platform(**platformdict)
    except TypeError as e:
        raise err.TypeException(
            e,
            message="Error decoding platform dictionary: " + str(e),
            status_code=500,
        )


def get_tool_url(iss: str) -> str:
    """Returns the tool url from the config file"""
    return _iss_conf_dict[iss]["tool_url"]


def get_frontend_login_url(iss: str) -> str:
    """Returns the frontend login url from the config file"""
    return _iss_conf_dict[iss]["frontend_login_url"]


def get_haski_activity_url(iss: str) -> str:
    """Returns the haski activity url from the config file"""
    return _iss_conf_dict[iss]["haski_lti_activity"]
