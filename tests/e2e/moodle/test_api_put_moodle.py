# Tests for put methods
import pytest
import json


@pytest.mark.parametrize("input, user_id, moodle_user_id, keys_expected,\
                         status_code_expected", [
    # Working Example
    (
        {
            "name": "Max Mustermann",
            "role": "Student",
            "university": "TH-AB",
            "settings": [
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
                }
            ]
        },
        1,
        1,
        ['id', 'name', 'university', 'lms_user_id', 'role', 'settings'],
        201
    ),
    # Missing Parameter
    (
        {
            "role": "Student",
            "university": "TH-AB",
            "settings": [
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
                }
            ]
        },
        1,
        1,
        ['error'],
        400
    )
])
def test_api_update_user_from_moodle(
    client,
    input,
    user_id,
    moodle_user_id,
    keys_expected,
    status_code_expected
):
    url = "/moodle/user/" + str(user_id) + "/" + str(moodle_user_id)
    r = client.put(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("input, course_id, moodle_course_id, keys_expected,\
                         status_code_expected", [
    # Working Example
    (
        {
            "name": "Test Course Updated",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "last_updated": "2018-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        ['id', 'name', 'lms_id', 'created_at', 'created_by', 'university'],
        201
    ),
    # Missing Parameter
    (
        {
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "last_updated": "2018-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        ['error'],
        400
    ),
    # Parameter with wrong data type
    (
        {
            "name": "Test Course Updated",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "last_updated": "01.01.2023",
            "university": "TH-AB"
        },
        1,
        1,
        ['error'],
        400
    )
])
def test_api_update_course_from_moodle(
    client,
    input,
    course_id,
    moodle_course_id,
    keys_expected,
    status_code_expected
):
    url = "/moodle/course/" + str(course_id) + "/" + str(moodle_course_id)
    r = client.put(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("input, course_id, moodle_course_id, topic_id,\
                         moodle_topic_id, keys_expected,\
                         status_code_expected", [
    # Working Example for Topic
    (
        {
            "name": "Test Topic Updated",
            "is_topic": True,
            "parent_id": 1,
            "contains_le": False,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "updated_at": "2018-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        ['id', 'name', 'lms_id', 'is_topic', 'parent_id', 'contains_le',\
         'created_by', 'created_at', 'university'],
        201
    ),
    # Working Example for Sub-Topic
    (
        {
            "name": "Test Sub-Topic Updated",
            "is_topic": False,
            "parent_id": 1,
            "contains_le": True,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "updated_at": "2018-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        ['id', 'name', 'lms_id', 'is_topic', 'parent_id', 'contains_le',\
         'created_by', 'created_at', 'university'],
        201
    ),
    # Missing Parameter
    (
        {
            "is_topic": True,
            "parent_id": 1,
            "contains_le": False,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "updated_at": "2018-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        ['error'],
        400
    ),
    # Parameter with wrong data type
    (
        {
            "name": "Test Topic Updated",
            "is_topic": True,
            "parent_id": "1",
            "contains_le": False,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "updated_at": "2018-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        ['error'],
        400
    )
])
def test_api_update_topic_from_moodle(
    client,
    input,
    course_id,
    moodle_course_id,
    topic_id,
    moodle_topic_id,
    keys_expected,
    status_code_expected
):
    url = "/moodle/course/" + str(course_id) + \
        "/" + str(moodle_course_id) + "/topic/" + \
        str(topic_id) + "/" + str(moodle_topic_id)
    r = client.put(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("input, course_id, moodle_course_id, topic_id,\
                         moodle_topic_id, learning_element_id,\
                         moodle_learning_element_id, keys_expected,\
                         status_code_expected", [
    # Working Example for LE
    (
        {
            "activity_type": "Quiz",
            "classification": "RQ",
            "name": "Test Learning Element Updated",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "last_updated": "2018-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        1,
        1,
        ['id', 'lms_id', 'activity_type', 'classification', 'name',\
         'created_by', 'created_at', 'university'],
        201
    ),
    # Missing Parameter
    (
        {
            "classification": "RQ",
            "name": "Test Learning Element Updated",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "last_updated": "2018-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        1,
        1,
        ['error'],
        400
    ),
    # Parameter with wrong data type
    (
        {
            "activity_type": "Quiz",
            "classification": "RQ",
            "name": "Test Learning Element Updated",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "last_updated": "01.01.2023",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        1,
        1,
        ['error'],
        400
    )
])
def test_api_update_le_from_moodle(
    client,
    input,
    course_id,
    moodle_course_id,
    topic_id,
    moodle_topic_id,
    learning_element_id,
    moodle_learning_element_id,
    keys_expected,
    status_code_expected
):
    url = "/moodle/course/" + str(course_id) + "/" + str(moodle_course_id) + \
        "/topic/" + str(topic_id) + "/" + str(moodle_topic_id) + \
        "/learningElement/" + str(learning_element_id) + "/" + \
        str(moodle_learning_element_id)
    r = client.put(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
