from abc import ABC, abstractmethod

from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from service_layer.lti.lms.Platform import Platform

class OIDCLogin(ABC):
    ''' Base class for OIDC login. Derive from this class and implement the abstract methods '''
    _response = None
    _platform : Platform
    def __init__(self, request, tool_config : ToolConfigJson):
        self._request = request
        self._tool_config = tool_config
        
    @abstractmethod
    def check_params(self):
        pass

    @abstractmethod
    def auth_redirect(self):
        pass

    @abstractmethod
    def lti_launch_from_id_token(self):
        pass

    @abstractmethod
    def verify_id_token(self) -> 'OIDCLogin':
        pass

    @abstractmethod
    def get_login(self):
        pass

    @staticmethod
    def make_url_accept_param(url):
        if '?' in url:
            return url + '&'
        else:
            return url + '?'