class CookieService(object):
    def __init__(self, request):
        self._request = request

    def get_cookie(self, name):
        return 'cookie'

    def set_cookie(self, name, value, exp=3600):
        pass

    def update_response(self, response):
        pass