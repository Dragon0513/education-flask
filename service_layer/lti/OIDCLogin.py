from abc import ABC, abstractmethod
from flask.wrappers import Request

from service_layer.lti.config.ToolConfigJson import ToolConfigJson

class OIDCLogin(ABC):
    ''' Base class for OIDC login. Derive from this class and implement the abstract methods '''
    _response = None
    def __init__(self, request : Request, tool_config : ToolConfigJson):
        self._request = request
        self._tool_config = tool_config
    @abstractmethod
    def check_auth(self):
        pass
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def lti_launch_from_id_token(self):
        pass

    @staticmethod
    def make_url_accept_param(url):
        if '?' in url:
            return url + '&'
        else:
            return url + '?'