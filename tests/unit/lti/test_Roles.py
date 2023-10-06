import unittest
from utils.auth.permissions import Permissions
from service_layer.lti.Roles import (
    RoleMapper,
    lti_roles,
    lti_permissions,
)  # Replace 'your_module' with the actual module where these are defined


class TestRoles(unittest.TestCase):
    def test_lti_roles(self):
        """Test if lti_roles has the expected mappings."""
        expected_roles = {
            "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor": "Instructor",
            "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner": "Learner",
            "http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator": "Administrator",
        }
        self.assertDictEqual(lti_roles, expected_roles)

    def test_lti_permissions(self):
        """Test if lti_permissions has the expected mappings."""
        expected_permissions = {
            "Instructor": [Permissions.READ, Permissions.WRITE],
            "Learner": [Permissions.READ],
            "Administrator": [Permissions.READ, Permissions.WRITE, Permissions.ADMIN],
        }
        self.assertDictEqual(lti_permissions, expected_permissions)


class TestRoleMapper(unittest.TestCase):
    def test_map_role(self):
        """Test the map_role method."""
        self.assertEqual(
            RoleMapper.map_role(
                "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"
            ),
            "Instructor",
        )
        self.assertEqual(RoleMapper.map_role("unknown_role"), "Unknown")

    def test_constructor(self):
        """Test the __init__ method."""
        role_mapper = RoleMapper(
            [
                "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner",
                "unknown_role",
            ]
        )
        self.assertEqual(role_mapper.get_role(), "Learner")
        role_mapper = RoleMapper(["unknown_role"])
        self.assertEqual(role_mapper.get_role(), "Unknown")

    def test_get_role(self):
        """Test the get_role method."""
        role_mapper = RoleMapper(
            ["http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator"]
        )
        self.assertEqual(role_mapper.get_role(), "Administrator")

    def test_get_permissions(self):
        """Test the get_permissions method."""
        role_mapper = RoleMapper(
            ["http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"]
        )
        self.assertEqual(
            role_mapper.get_permissions(), [Permissions.READ, Permissions.WRITE]
        )  # Replace with actual Permissions enum


if __name__ == "__main__":
    unittest.main()
