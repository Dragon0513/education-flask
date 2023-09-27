from flask.wrappers import Request
from werkzeug import Response

from service_layer.service.CookieService import CookieService


class CookieServiceFlask(CookieService):
    def set_cookie(
        self,
        response: Response,
        key,
        value,
        max_age=None,
        expires=None,
        samesite="none",
        path="/",
        domain=None,
        secure=True,
        httponly=True,
    ):
        response.set_cookie(
            key=key,
            value=value,
            max_age=max_age,
            expires=expires,
            path=path,
            domain=domain,
            secure=secure,
            httponly=httponly,
            samesite=samesite,
        )

    def delete_cookie(self, response, key, path=None, domain=None):
        response.set_cookie(key, "", expires=0)
