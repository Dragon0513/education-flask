from abc import ABC, abstractmethod
class CookieService(ABC):
    @abstractmethod
    def get_cookie(self, name):
        pass
    @abstractmethod
    def set_cookie(self, name, value, max_age=None, expires=None, samesite=None, path=None, domain=None, secure=None, httponly=None):
        pass
    @abstractmethod
    def delete_cookie(self, name, path=None, domain=None):
        pass