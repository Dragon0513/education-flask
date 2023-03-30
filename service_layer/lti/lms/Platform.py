class Platform():
    def __init__(self, 
                default : bool, 
                client_id : str,
                tool_url : str,
                frontend_login_url : str,
                auth_login_url : str, 
                auth_token_url : str,
                target_link_uri : str,
                key_set_url : str,
                platform_name : str,
                key_set : object,
                private_key_file : str,
                public_key_file : str,
                haski_lti_activity: str,
                deployment_ids : list) -> None:
        self.default = default
        self.client_id = client_id
        self.tool_url = tool_url
        self.frontend_login_url = frontend_login_url
        self.auth_login_url = auth_login_url
        self.auth_token_url = auth_token_url
        self.target_link_uri = target_link_uri
        self.key_set_url = key_set_url
        self.platform_name = platform_name
        self.key_set = key_set
        self.private_key_file = private_key_file
        self.public_key_file = public_key_file
        self.haski_lti_activity = haski_lti_activity
        self.deployment_ids = deployment_ids

    def instance(self):
        if self.platform_name in globals():
            return globals()[self.platform_name]().lti_launch_from_id_token() # this is secure, because platform_name comes from own config file
        return self

    def launch(self):
        return "Launch from Platform", 200