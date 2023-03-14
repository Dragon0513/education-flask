from collections import namedtuple
import json
import os
from errors import errors as err
from service_layer.lti.lms.Platform import Platform


# Parses LTI Config file and returns a dictionary of the contents
class ToolConfigJson():
    _iss_conf_dict : dict = {} # stores all the platform configurations
    def __init__(self, config_file="../../../config/lti_config.json"):
        #if not os.path.isfile(config_file):
            #raise FileNotFoundError("LTI tool config file not found: " + config_file)

        #with open(config_file, 'r') as cfg:
            #self._iss_conf_dict = json.loads(cfg.read())
        self._iss_conf_dict = lti_config
        
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
    
#Test
lti_config = {
  "http://fakedomain.com": {
    "default": True,
    "client_id": "baxlYFroQGZBk7O",
    "tool_url": "http://fakedomain.com:5000",
    "target_link_uri": "http://fakedomain.com:5000/lti_launch",
    "auth_login_url": "http://fakedomain.com/mod/lti/auth.php",
    "auth_token_url": "http://fakedomain.com/mod/lti/token.php",
    "key_set_url": "http://fakedomain.com/mod/lti/certs.php",
    "platform_name": "moodle",
    "key_set": {
      "keys": [
        {
          "kty": "RSA",
          "alg": "RS256",
          "kid": "9ff4cd444a5c3535df3a",
          "e": "AQAB",
          "n": "qgtgjGKc86cwm6LIxdAHH1wiX30bLeDwqnr07MBGL6efDmUC2HbQYhURaMtCrAV7jQigSYXSB-KhVvnK19rPsOZEOYo3zvdh4NFAh-yxjIbAcvVopiPAPWvYJd4lCkvufoEch8KpJ_t5J_k4_usVZlxViDX99PszokM9396nk1oOfNWJn-T97tB9DOcHW-jYfmI1CcUENIwGjUUgs7ry0A8wZut5-Zo3nDaNh2aDma4R2hQyAvlL6gi_Cg4X-yji-hEhWOKbQJd1f1dJbVgY5FF4UxyFxxQCs1C1ePvuvOhOhZiMVttS1RH9-ggqRFliK5OHgafSMF85W8F5OO17ew",
          "use": "sig"
        }
      ]
    },
    "private_key_file": "private.key",
    "public_key_file": "public.key",
    "deployment_ids": ["1"]
  }
}
