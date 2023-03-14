from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask
from service_layer.lti.OIDCLogin import OIDCLogin
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from flask import Flask, abort, jsonify, request, session
from werkzeug.wrappers.response import Response

import html

tool_config = ToolConfigJson()
oidc_login = OIDCLoginFlask(request, tool_config)


#pytest tests\unit\lti\test_OIDCLoginFlask.py --cov

def test_check_params():

    assert oidc_login.check_params


def test_auth_redirect():
    
    response = oidc_login.auth_redirect

    assert response