# Tests for put methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, request_body, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        {
            "theme": [
                {
                    "color": "dark",
                    "style": "dark",
                    "typography": "Comic Sans",
                    "language": "EN"
                }
            ],
            "password": "password"
        },
        ['theme', 'password'],
        201
    ),
    # User not found
    (
        2,
        1,
        {
            "theme": [
                {
                    "color": "dark",
                    "style": "dark",
                    "typography": "Comic Sans",
                    "language": "EN"
                }
            ],
            "password": "password"
        },
        ['error'],
        404
    )
])
def test_api_update_user_settings_by_id(
    client,
    user_id,
    lms_user_id,
    request_body,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + "/settings"
    r = client.put(url, json=request_body)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
