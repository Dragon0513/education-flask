# Tests for delete methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        {
            "message": "Deletion successful."
        },
        200
    ),
    # User not found
    (
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_delete_user_by_id(
    client,
    user_id,
    lms_user_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id)
    r = client.delete(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        {
            "theme": [
                {
                    "color": "dark",
                    "style": "dark",
                    "typography": "Arial Black",
                    "language": "DE"
                }
            ],
            "password": "password"
        },
        200
    ),
    # User not found
    (
        2,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_delete_user_settings_by_id(
    client,
    user_id,
    lms_user_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + "/settings"
    r = client.delete(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
