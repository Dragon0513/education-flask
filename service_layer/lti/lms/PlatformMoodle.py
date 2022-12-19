from service_layer.lti.lms.Platform import Platform


class PlatformMoodle(Platform):
    def __init__(self, 
                default : bool, 
                client_id : str,
                auth_login_url : str, 
                auth_token_url : str,
                target_link_uri : str,
                key_set_url : str,
                platform_name : str,
                key_set : object,
                private_key_file : str,
                public_key_file : str,
                deployment_ids : list):
        super(PlatformMoodle, self).__init__(default, 
                client_id,
                auth_login_url, 
                auth_token_url,
                target_link_uri,
                key_set_url,
                platform_name,
                key_set,
                private_key_file,
                public_key_file,
                deployment_ids)