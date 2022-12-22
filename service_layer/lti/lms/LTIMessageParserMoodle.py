from service_layer.lti.Messages import LTIIDToken
from service_layer.lti.lms.LTIMessageParser import LTIMessageParser


class LTIMessageParserMoodle(LTIMessageParser):
    @staticmethod
    def parse(token: str):        
        pass

    @staticmethod
    def parse_id_token(token: str) -> LTIIDToken:
        return None