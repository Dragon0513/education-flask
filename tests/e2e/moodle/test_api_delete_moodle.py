# Tests for delete methods
import pytest
import json


@pytest.mark.parametrize("user_id, moodle_user_id, output_expected,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        {
            "message": "Deletion was successful"
        },
        200
    ),
    # User not found
    (
        1,
        1,
        {
            "error": "The user was not found."
        },
        404
    )
])
def test_api_delete_user_from_moodle(
    client,
    user_id,
    moodle_user_id,
    output_expected,
    status_code_expected
):
    url = "/moodle/user/" + str(user_id) + "/" + str(moodle_user_id)
    r = client.delete(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("course_id, moodle_course_id, output_expected,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        {
            "message": "Deletion was successful"
        },
        200
    ),
    # Course not found
    (
        1,
        1,
        {
            "error": "The course was not found."
        },
        404
    )
])
def test_api_delete_course_from_moodle(
    client,
    course_id,
    moodle_course_id,
    output_expected,
    status_code_expected
):
    url = "/moodle/course/" + str(course_id) + "/" + str(moodle_course_id)
    r = client.delete(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("course_id, moodle_course_id, topic_id,\
                         moodle_topic_id, output_expected,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        {
            "message": "Deletion was successful"
        },
        200
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        {
            "error": "The topic was not found."
        },
        404
    )
])
def test_api_delete_topic_from_moodle(
    client,
    course_id,
    moodle_course_id,
    topic_id,
    moodle_topic_id,
    output_expected,
    status_code_expected
):
    url = "/moodle/course/" + str(course_id) + \
        "/" + str(moodle_course_id) + "/topic/" + \
        str(topic_id) + "/" + str(moodle_topic_id)
    r = client.post(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("course_id, moodle_course_id, topic_id,\
                         moodle_topic_id, learning_element_id,\
                         moodle_learning_element_id, output_expected,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        1,
        {
            "message": "Deletion was successful"
        },
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
        {
            "error": "The learning element was not found."
        },
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
    output_expected,
    status_code_expected
):
    url = "/moodle/course/" + str(course_id) + "/" + str(moodle_course_id) + \
        "/topic/" + str(topic_id) + "/" + str(moodle_topic_id) + \
        "/learningElement/" + str(learning_element_id) + "/" + \
        str(moodle_learning_element_id)
    r = client.post(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
