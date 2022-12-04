from CookieService import CookieService
class CookieServiceFlask(CookieService):
    def __init__(self, request):
        self.request = request
    def get_cookie(self, name):
        return self.request.cookies.get(name)
    def set_cookie(self, name, value, max_age=None, expires=None, path=None, domain=None, secure=None, httponly=None):
        self.request.set_cookie(name, value, max_age, expires, path, domain, secure, httponly)
    def delete_cookie(self, name, path=None, domain=None):
        self.request.delete_cookie(name, path, domain)