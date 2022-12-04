from abc import abstractmethod
from flask.wrappers import Request

class OIDCLogin:
    ''' Base class for OIDC login. Derive from this class and implement the abstract methods '''
    _response = None
    def __init__(self, request : Request, tool_config):
        self._request = request
        self._tool_config = tool_config
    @abstractmethod
    def check_auth(self):
        pass
    @abstractmethod
    def login(self):
        pass

    @staticmethod
    def make_url_accept_param(url):
        if '?' in url:
            return url + '&'
        else:
            return url + '?'