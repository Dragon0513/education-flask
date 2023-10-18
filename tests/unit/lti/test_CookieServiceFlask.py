from unittest.mock import Mock

from werkzeug.wrappers import Response

from service_layer.service.CookieServiceFlask import CookieServiceFlask


def test_set_cookie():
    # Create a mock response object
    response = Mock(spec=Response)

    # Create a CookieServiceFlask instance
    cookie_service = CookieServiceFlask()

    # Call the set_cookie method with some test values
    cookie_service.set_cookie(response, "test_key", "test_value")

    # Assert that the response.set_cookie method was called with the correct arguments
    response.set_cookie.assert_called_once_with(
        key="test_key",
        value="test_value",
        max_age=None,
        expires=None,
        path="/",
        domain=None,
        secure=True,
        httponly=True,
        samesite="none",
    )


def test_delete_cookie():
    # Create a mock response object
    response = Mock(spec=Response)

    # Create a CookieServiceFlask instance
    cookie_service = CookieServiceFlask()

    # Set the cookie to be deleted

    # Call the delete_cookie method with some test values
    cookie_service.delete_cookie(response, "test_key")

    # Assert that the response.set_cookie method was called with the correct arguments
    response.set_cookie.assert_called_once_with("test_key", "", expires=0)
