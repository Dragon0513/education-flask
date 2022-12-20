from service_layer.service.CookieService import CookieService
class CookieServiceFlask(CookieService):
    def __init__(self, request):
        self.request = request
    def get_cookie(self, name):
        return self.request.cookies.get(name)
    def set_cookie(self, name, value, max_age=None, expires=None, samesite="none", path="/", domain=None, secure=True, httponly=True):
        self.request.set_cookie(name=name, value=value, max_age=max_age, expires=expires, path=path, domain=domain, secure=secure, httponly=httponly, samesite=samesite)
    def delete_cookie(self, name, path=None, domain=None):
        self.request.delete_cookie(name, path, domain)