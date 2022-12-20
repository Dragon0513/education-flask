from abc import ABC, abstractmethod
class StateService(ABC):
    @abstractmethod
    def get_oidc_nonce(self):
        pass
    @abstractmethod
    def get_oidc_state(self):
        pass