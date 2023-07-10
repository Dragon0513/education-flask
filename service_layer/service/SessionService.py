from abc import ABC, abstractmethod


class SessionService(ABC):
    @abstractmethod
    def get_oidc_nonce(self):
        pass

    @abstractmethod
    def get_oidc_state_jwt(self):
        pass
