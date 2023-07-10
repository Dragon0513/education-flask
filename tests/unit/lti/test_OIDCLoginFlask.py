from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from flask import request


tool_config = ToolConfigJson()
oidc_login = OIDCLoginFlask(request, tool_config)


# pytest tests\unit\lti\test_OIDCLoginFlask.py --cov


def test_check_params():
    assert oidc_login.check_params


def test_auth_redirect():
    response = oidc_login.auth_redirect

    assert response
