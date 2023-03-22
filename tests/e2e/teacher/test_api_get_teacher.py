# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, teacher_id,\
                         keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['courses'],
        ['id', 'name', 'lms_id', 'user_nr', 'created_at'],
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
def test_api_get_courses_by_teacher_id(
    client,
    user_id,
    lms_user_id,
    teacher_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/teacher/" + str(teacher_id) + "/course"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'courses' in keys_expected_1:
        for key in response['courses'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, teacher_id, course_id,\
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['learning_style', 'performer', 'time_spend'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        ['error'],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        ['error'],
        404
    )
])
def test_api_get_dashboard_by_course_id_by_teacher_id(
    client,
    user_id,
    lms_user_id,
    teacher_id,
    course_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/teacher/" + str(teacher_id) + "dashboard/course/" + \
        str(course_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, teacher_id, course_id,\
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['clicks', 'knowledge', 'time'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        ['error'],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        ['error'],
        404
    )
])
def test_api_get_dashboard_topic_by_course_id_by_teacher_id(
    client,
    user_id,
    lms_user_id,
    teacher_id,
    course_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/teacher/" + str(teacher_id) + "dashboard/course/" + \
        str(course_id) + "/topic"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, teacher_id, course_id,\
                         topic_id, keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        ['feedback', 'clicks', 'knowledge', 'time'],
        ['error_analysis', 'learning_progress'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        ['error'],
        [],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        ['error'],
        [],
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        ['error'],
        [],
        404
    )
])
def test_api_get_dashboard_les_by_course_id_by_teacher_id(
    client,
    user_id,
    lms_user_id,
    teacher_id,
    course_id,
    topic_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/teacher/" + str(teacher_id) + "dashboard/course/" + \
        str(course_id) + "/topic/" + str(topic_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'knowledge' in keys_expected_1:
        for key in response['knowledge'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1
