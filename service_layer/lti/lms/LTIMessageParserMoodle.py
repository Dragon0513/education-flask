from service_layer.lti.Messages import LTIMessage
from service_layer.lti.lms.LTIMessageParser import LTIMessageParser


class LTIMessageParserMoodle(LTIMessageParser):
    def parse(self, token: str):        
        pass