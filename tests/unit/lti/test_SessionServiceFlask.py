import datetime
import unittest
from unittest.mock import patch

from service_layer.service.SessionServiceFlask import (  # noqa: E501
    Session,
    check_expiration,
    get,
    sessions,
    set,
    set_state_jwt,
)


class TestSessionClass(unittest.TestCase):
    def test_constructor(self):
        """
        Test that the constructor initializes the object with the correct attributes.
        """
        session = Session()
        self.assertIsNone(session.expiration)
        self.assertFalse(session.modified)

    def test_setitem(self):
        """
        Test that the __setitem__ method modifies the 'modified' attribute to True.
        """
        session = Session()
        self.assertFalse(session.modified)  # Initial state
        session["key"] = "value"  # Using __setitem__
        self.assertTrue(session.modified)  # Should now be True

    def test_delitem(self):
        """
        Test that the __delitem__ method
        removes the item and sets the 'modified' attribute to True.
        """
        session = Session(key="value")
        self.assertFalse(session.modified)  # Initial state
        del session["key"]  # Using __delitem__
        self.assertTrue(session.modified)  # Should now be True
        with self.assertRaises(KeyError):
            _ = session["key"]  # Verify item was deleted

    def test_getitem(self):
        """
        Test that the __getitem__ method returns the correct item value.
        """
        session = Session(key="value")
        self.assertEqual(
            session["key"], "value"
        )  # Using __getitem__ to fetch the value


class TestSessionModule(unittest.TestCase):
    def setUp(self):
        sessions.clear()

    def tearDown(self):
        sessions.clear()

    @patch(
        "service_layer.crypto.JWTKeyManagement.generate_state_jwt",
        return_value="mocked_jwt",
    )
    @patch("service_layer.service.SessionServiceFlask.check_expiration")
    def test_set_state_jwt(self, mock_check_expiration, mock_generate_state_jwt):
        jwt = set_state_jwt("nonce1", "auth_url", "tool_url")
        self.assertEqual(jwt, "mocked_jwt")
        self.assertTrue("nonce1" in sessions)
        mock_check_expiration.assert_called()
        mock_generate_state_jwt.assert_called()

    def test_set(self):
        set("nonce2", "key2", "value2")
        self.assertTrue("nonce2" in sessions)
        self.assertEqual(sessions["nonce2"]["key2"], "value2")

    @patch("service_layer.service.SessionServiceFlask.check_expiration")
    def test_get(self, mock_check_expiration):
        set("nonce3", "key3", "value3")
        value = get("nonce3", "key3")
        self.assertEqual(value, "value3")
        mock_check_expiration.assert_called()
        self.assertIsNone(get("nonce3", "nonexistent_key"))
        self.assertIsNone(get("nonexistent_nonce", "key3"))

    @patch(
        "service_layer.crypto.JWTKeyManagement.generate_state_jwt",
        return_value="mocked_jwt",
    )
    def test_check_expiration(self, mock_generate_state_jwt):
        set_state_jwt("nonce4", "auth_url", "tool_url")
        self.assertTrue("nonce4" in sessions)
        self.assertFalse(sessions["nonce4"].is_expired())
        sessions["nonce4"].set_expiration(
            datetime.datetime.now() - datetime.timedelta(seconds=1)
        )
        self.assertTrue(sessions["nonce4"].is_expired())
        check_expiration()
        self.assertFalse("nonce4" in sessions)
        mock_generate_state_jwt.assert_called()


if __name__ == "__main__":
    unittest.main()
