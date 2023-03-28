# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['courses'],
        ['id', 'name', 'lms_id', 'created_by', 'created_at', 'university'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        [],
        404
    )
])
def test_api_get_courses_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/course"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'courses' in keys_expected_1:
        for key in response['courses'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['users'],
        ['name', 'role', 'university'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        [],
        404
    )
])
def test_api_get_users_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/user"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'users' in keys_expected_1:
        for key in response['users'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['access_logs', 'frontend_logs', 'main_logs',\
         'error_logs', 'system_logs'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/logs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['time', 'user', 'session_id', 'message'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_access_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/accessLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'error' in keys_expected:
        for key in response.keys():
            assert key in keys_expected
    else:
        for i in range(len(response)):
            for key in response[i].keys():
                assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['name', 'value', 'rating', 'delta', 'entries',\
         'id', 'navigationType'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_frontend_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/frontendLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'error' in keys_expected:
        for key in response.keys():
            assert key in keys_expected
    else:
        for i in range(len(response)):
            for key in response[i].keys():
                assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['time', 'session_id', 'message'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_main_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/mainLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'error' in keys_expected:
        for key in response.keys():
            assert key in keys_expected
    else:
        for i in range(len(response)):
            for key in response[i].keys():
                assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['time', 'session_id', 'message'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_error_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/errorLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'error' in keys_expected:
        for key in response.keys():
            assert key in keys_expected
    else:
        for i in range(len(response)):
            for key in response[i].keys():
                assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['time', 'message'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_system_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/systemLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'error' in keys_expected:
        for key in response.keys():
            assert key in keys_expected
    else:
        for i in range(len(response)):
            for key in response[i].keys():
                assert key in keys_expected
