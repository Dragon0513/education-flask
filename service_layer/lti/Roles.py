from utils.auth.permissions import Permissions


# This file contains the mapping of IMS roles to LTI / LMS roles
lti_roles = {
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor": "Instructor",
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner": "Learner",
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator": "Administrator",
}

lti_permissions = {
    "Instructor": [Permissions.READ, Permissions.WRITE],
    "Learner": [Permissions.READ],
    "Administrator": [Permissions.READ, Permissions.WRITE, Permissions.ADMIN],
}


class RoleMapper:
    """Maps IMS roles to a single LTI role
    Example:
    IMS roles: http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor,\
        http://purl.imsglobal.org/vocab/lis/v2/membership#Learner
    LTI role: Instructor
    return by get_role(): Instructor
    """

    # map IMS roles to LTI roles
    @staticmethod
    def map_role(role: str):
        if role in lti_roles:
            return lti_roles[role]
        return "Unknown"

    def __init__(self, roles_list: list[str]):
        self.role: str = "Unknown"
        for role in roles_list:
            if RoleMapper.map_role(role) != "Unknown":
                self.role = RoleMapper.map_role(role)
                break

    def get_role(self):
        return self.role

    def get_permissions(self) -> list[Permissions]:
        return lti_permissions[self.role]
