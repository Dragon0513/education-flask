from abc import ABC, abstractmethod

from service_layer.lti.Messages import LTIIDToken


class LTIMessageParser(ABC):
    @staticmethod
    @abstractmethod
    def parse(token: str) -> LTIIDToken:
        pass

    @staticmethod
    @abstractmethod
    def parse_id_token(token: str) -> LTIIDToken:
        pass