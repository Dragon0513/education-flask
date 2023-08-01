import unittest
from flask import request

from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask

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
                    "n": "z8uwIpHep-dGbqqutVqQPsXdwJk8ESoXPw1UD-9PmlTm06Q6PmXl5jHT9J6hTuW-9OjiycuBs07DW1At6LEAEBOJbFw2H6aflmPyhq09Cwernuk6OzekRRmnPdmfYeOcjpHAGaZ3qwaU0E6zPt_Ki1ZqdtLnB53ytO1fuYTmK1FVSbnexK9i4OkLk6OHMCHkInQTndRMWOiKWwrAoc591LlNSzgvlW_S9s-Vj2N4sHAcikKobzMMD8ixsV84Lx3mZyb13qph9qXUMJB9It-5WXa-FfsbUQZ6MeC0ks9_XSyl7tI7Q2eHUqenPimZL15uQnWek-gaE61IAK7ihKSMew",
                    "use": "sig",
                }
            ]
        },
        "private_key_file": "private.key",
        "public_key_file": "public.key",
        "deployment_ids": ["1"],
    }
}


# self._platform = self._tool_config.decode_platform(
#     self._tool_config.get_platform(
#         os.environ.get("LMS_URL", "https://moodle.haski.app")
#     )
# )


class ToolConfigJsonMock(ToolConfigJson):
    def __init__(self):
        self._iss_conf_dict = config_file


# pytest tests\unit\lti\test_OIDCLoginFlask.py --cov
class TestOIDCLoginFlask(unittest.TestCase):
    def setUp(self):
        self.tool_config = ToolConfigJsonMock()
        self.oidc_login = OIDCLoginFlask(request, self.tool_config)

    def test_tool_config(self):
        self.assertEqual(
            self.oidc_login._tool_config._iss_conf_dict,
            self.tool_config._iss_conf_dict,
        )

    def test_tool_config_get_platform(self):
        self.assertEqual(
            self.oidc_login._tool_config.get_platform("https://moodle.haski.app"),
            self.tool_config.get_platform("https://moodle.haski.app"),
        )

    def test_tool_config_decode_platform(self):
        # dont need to check every value, just one
        platform = self.oidc_login._tool_config.decode_platform(
            self.tool_config.get_platform("https://moodle.haski.app")
        )
        self.assertEqual(
            platform.platform_name,
            "HASKI",
        )
