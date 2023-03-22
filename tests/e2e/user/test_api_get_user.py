# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        ['id', 'name', 'university', 'lms_user_id', 'role', 'settings'],
        200
    ),
    # User not found
    (
        2,
        1,
        ['error'],
        404
    )
])
def test_api_get_user_by_id(
    client,
    user_id,
    lms_user_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        ['theme', 'passworrd'],
        200
    ),
    # User not found
    (
        2,
        1,
        ['error'],
        404
    )
])
def test_api_get_user_settings_by_id(
    client,
    user_id,
    lms_user_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + "/settings"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
