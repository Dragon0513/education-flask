import json
import os


# Parses LTI Config file and returns a dictionary of the contents
class ToolConfigJson():
    _iss_conf_dict : dict = {}
    def __init__(self, config_file="../../../config/lti_config.json"):
        if not os.path.isfile(config_file):
            raise FileNotFoundError("LTI tool config file not found: " + config_file)

        with open(config_file, 'r') as cfg:
            self._iss_conf_dict = json.loads(cfg.read())
        
    def get_platform(self, iss, client_id=None):
        return self._iss_conf_dict[iss]
