from service_layer.service.CookieService import CookieService
from flask.wrappers import Request
class CookieServiceFlask(CookieService):
    def __init__(self, request : Request):
        self.request = request
    def get_cookie(self, name, type=str):
        return self.request.cookies.get(name,type=type)
    def set_cookie(self, response, key, value, max_age=None, expires=None, samesite="none", path="/", domain=None, secure=True, httponly=True):
        response.set_cookie(key=key, value=value, max_age=max_age, expires=expires, path=path, domain=domain, secure=secure, httponly=httponly, samesite=samesite)
    def delete_cookie(self, response, key, path=None, domain=None):
        response.set_cookie(key, '', expires=0)