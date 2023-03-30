# Tests for delete methods
import pytest
import json


@pytest.mark.parametrize("user_id, moodle_user_id, keys_expected,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        ['message'],
        200
    ),
    # User not found
    (
        1,
        1,
        ['error'],
        404
    )
])
def test_api_delete_user_from_moodle(
    client,
    user_id,
    moodle_user_id,
    keys_expected,
    status_code_expected
):
    url = "/lms/user/" + str(user_id) + "/" + str(moodle_user_id)
    r = client.delete(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("course_id, moodle_course_id, keys_expected,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        ['message'],
        200
    ),
    # Course not found
    (
        1,
        1,
        ['error'],
        404
    )
])
def test_api_delete_course_from_moodle(
    client,
    course_id,
    moodle_course_id,
    keys_expected,
    status_code_expected
):
    url = "/lms/course/" + str(course_id) + "/" + str(moodle_course_id)
    r = client.delete(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("course_id, moodle_course_id, topic_id,\
                         moodle_topic_id, keys_expected,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['message'],
        200
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_delete_topic_from_moodle(
    client,
    course_id,
    moodle_course_id,
    topic_id,
    moodle_topic_id,
    keys_expected,
    status_code_expected
):
    url = "/lms/course/" + str(course_id) + \
        "/" + str(moodle_course_id) + "/topic/" + \
        str(topic_id) + "/" + str(moodle_topic_id)
    r = client.post(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("course_id, moodle_course_id, topic_id,\
                         moodle_topic_id, learning_element_id,\
                         moodle_learning_element_id, keys_expected,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        1,
        ['message'],
        200
    ),
    # Learning Element not found
    (
        1,
        1,
        1,
        1,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_delete_le_from_moodle(
    client,
    course_id,
    moodle_course_id,
    topic_id,
    moodle_topic_id,
    learning_element_id,
    moodle_learning_element_id,
    keys_expected,
    status_code_expected
):
    url = "/lms/course/" + str(course_id) + "/" + str(moodle_course_id) + \
        "/topic/" + str(topic_id) + "/" + str(moodle_topic_id) + \
        "/learningElement/" + str(learning_element_id) + "/" + \
        str(moodle_learning_element_id)
    r = client.post(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
