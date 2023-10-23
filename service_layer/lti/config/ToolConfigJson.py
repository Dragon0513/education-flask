import os

from errors import errors as err
from service_layer.lti.lms.Platform import Platform

# Parses LTI Config file and returns a dictionary of the contents
_iss_conf_dict = {
    os.environ.get("LMS_URL", "http://fakedomain.com"): {
        "default": True,
        "client_id": os.environ.get("CLIENT_ID", "None"),
        "tool_url": os.environ.get("BACKEND_URL", "http://fakedomain.com:5000"),
        "frontend_login_url": os.environ.get(
            "FRONTEND_URL", "http://fakedomain.com:8080"
        )
        + "/login",
        "target_link_uri": os.environ.get("BACKEND_URL", "http://fakedomain.com:5000")
        + "/lti_launch",
        "auth_login_url": os.environ.get("LMS_URL", "http://fakedomain.com")
        + "/mod/lti/auth.php",
        "auth_token_url": os.environ.get("LMS_URL", "http://fakedomain.com")
        + "/mod/lti/token.php",
        "key_set_url": os.environ.get("LMS_URL", "http://fakedomain.com")
        + "/mod/lti/certs.php",
        "haski_lti_activity": os.environ.get("LMS_URL", "http://fakedomain.com")
        + "/mod/lti/view.php?id=2",
        "platform_name": os.environ.get("PLATFORM_NAME", "HASKI"),
        "key_set": {
            "keys": [
                {
                    "kty": "RSA",
                    "alg": "RS256",
                    "kid": os.environ.get("KEY_ID", "None"),
                    "e": "AQAB",
                    "n": os.environ.get(
                        "KEY_N_VALUE", "None"
                    ),  # noqa: Place your default n value here
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
