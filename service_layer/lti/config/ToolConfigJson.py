from collections import namedtuple
import json
import os
from errors import errors as err
from service_layer.lti.lms.Platform import Platform


# Parses LTI Config file and returns a dictionary of the contents
class ToolConfigJson():
    _iss_conf_dict : dict = {} # stores all the platform configurations
    def __init__(self, config_file="../../../config/lti_config.json"):
        if not os.path.isfile(config_file):
            raise FileNotFoundError("LTI tool config file not found: " + config_file)

        with open(config_file, 'r') as cfg:
            self._iss_conf_dict = json.loads(cfg.read())
        
    def get_platform(self, iss : str):
        return self._iss_conf_dict[iss]

    def decode_platform(self, platformdict : dict):
        """ Decodes a platform dictionary into a Platform object """
        try:
            return Platform(**platformdict)
        except TypeError as e:
            raise err.TypeException(e,message="Error decoding platform dictionary: " + str(e), status_code=500)

    def get_tool_url(self, iss : str):
        """ Returns the tool url from the config file"""
        return self._iss_conf_dict[iss]['tool_url']

    def get_frontend_login_url(self, iss : str):
        """ Returns the frontend login url from the config file"""
        return self._iss_conf_dict[iss]['frontend_login_url']  