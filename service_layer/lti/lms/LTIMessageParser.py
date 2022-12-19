from abc import ABC, abstractmethod

from service_layer.lti.Messages import LTIMessage


class LTIMessageParser(ABC):
    @abstractmethod
    def parse(self, token: str) -> LTIMessage:
        pass