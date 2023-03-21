# Tests for post methods
import pytest
import json


@pytest.mark.parametrize("input, keys_expected, status_code_expected", [
    # Working Example
    (
        {
            "name": "Max Mustermann",
            "lms_user_id": 1,
            "role": "Student",
            "university": "TH-AB",
            "password": "password"
        },
        [
            'id',
            'name',
            'university',
            'lms_user_id',
            'role',
            'settings'
        ],
        201
    ),
    # Missing Parameter
    (
        {
            "lms_user_id": 1,
            "role": "Student",
            "university": "TH-AB",
            "password": "password"
        },
        ["error"],
        400
    ),
    # Parameter with wrong data type
    (
        {
            "name": "Max Mustermann",
            "lms_user_id": "1",
            "role": "Student",
            "university": "TH-AB",
            "password": "password"
        },
        ["error"],
        400
    ),
    # User already exists
    (
        {
            "name": "Max Mustermann",
            "lms_user_id": 1,
            "role": "Student",
            "university": "TH-AB",
            "password": "password"
        },
        ["error"],
        400
    ),
])
def test_api_create_user_from_moodle(
    client,
    input,
    keys_expected,
    status_code_expected
):
    r = client.post("/lms/user", json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("input, output_expected, status_code_expected", [
    # Working Example
    (
        {
            "name": "Test Course",
            "lms_id": 1,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        {
            "id": 1,
            "name": "Test Course",
            "lms_id": 1,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "last_updated": None,
            "university": "TH-AB"
        },
        201
    ),
    # Missing Parameter
    (
        {
            "name": "Test Course",
            "lms_id": 1,
            "created_by": "Maria Musterfrau",
            "university": "TH-AB"
        },
        {
            "error": "Paramaters are missing in the request body."
        },
        400
    ),
    # Parameter with wrong data type
    (
        {
            "name": "Test Course",
            "lms_id": "1",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        {
            "error": "Paramaters have the wrong data type."
        },
        400
    ),
    # Course already exists
    (
        {
            "name": "Test Course",
            "lms_id": 1,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        {
            "error": "This course already exists."
        },
        400
    ),

])
def test_api_create_course_from_moodle(
    client,
    input,
    output_expected,
    status_code_expected
):
    r = client.post("/moodle/course", json=input)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("input, course_id, moodle_course_id, \
                          output_expected, status_code_expected", [
    # Working Example for Topic
    (
        {
            "name": "Test Topic",
            "lms_id": 1,
            "is_topic": True,
            "contains_le": False,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        {
            "id": 1,
            "name": "Test Topic",
            "lms_id": 1,
            "is_topic": True,
            "parent_id": None,
            "contains_le": False,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "updated_at": None,
            "university": "TH-AB"
        },
        201
    ),
    # Working Example for Sub-Topic
    (
        {
            "name": "Test Sub-Topic",
            "lms_id": 2,
            "is_topic": False,
            "parent_id": 1,
            "contains_le": True,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        {
            "id": 2,
            "name": "Test Sub-Topic",
            "lms_id": 2,
            "is_topic": False,
            "parent_id": 1,
            "contains_le": True,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "updated_at": None,
            "university": "TH-AB"
        },
        201
    ),
    # Missing Parameter
    (
        {
            "name": "Test Topic",
            "is_topic": True,
            "contains_le": False,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        {
            "error": "Paramaters are missing in the request body."
        },
        400
    ),
    # Parameter with wrong data type
    (
        {
            "name": "Test Topic",
            "lms_id": "1",
            "is_topic": True,
            "contains_le": False,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        {
            "error": "Paramaters have the wrong data type."
        },
        400
    ),
    # Topic already exists
    (
        {
            "name": "Test Topic",
            "lms_id": 1,
            "is_topic": True,
            "contains_le": False,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        {
            "error": "This topic already exists."
        },
        400
    ),

])
def test_api_create_topic_from_moodle(
    client,
    input,
    course_id,
    moodle_course_id,
    output_expected,
    status_code_expected
):
    url = "/moodle/course/" + str(course_id) + \
        "/" + str(moodle_course_id) + "/topic"
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("input, course_id, moodle_course_id, topic_id, \
                         moodle_topic_id, output_expected, \
                         status_code_expected", [
    # Working Example for LE
    (
        {
            "lms_id": 1,
            "activity_type": "Quiz",
            "classification": "RQ",
            "name": "Test Learning Element",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        {
            "id": 1,
            "lms_id": 1,
            "activity_type": "Quiz",
            "classification": "RQ",
            "name": "Test Learning Element",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "last_updated": "2017-07-21T17:32:28Z"
        },
        201
    ),
    # Missing Parameter
    (
        {
            "lms_id": 1,
            "classification": "RQ",
            "name": "Test Learning Element",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        {
            "error": "Paramaters are missing in the request body."
        },
        400
    ),
    # Parameter with wrong data type
    (
        {
            "lms_id": "1",
            "activity_type": "Quiz",
            "classification": "RQ",
            "name": "Test Learning Element",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        {
            "error": "Paramaters have the wrong data type."
        },
        400
    ),
    # Topic already exists
    (
        {
            "lms_id": 1,
            "activity_type": "Quiz",
            "classification": "RQ",
            "name": "Test Learning Element",
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        1,
        1,
        1,
        1,
        {
            "error": "This topic already exists."
        },
        400
    )
])
def test_api_create_le_from_moodle(
    client,
    input,
    course_id,
    moodle_course_id,
    topic_id,
    moodle_topic_id,
    output_expected,
    status_code_expected
):
    url = "/moodle/course/" + str(course_id) + "/" + str(moodle_course_id) + \
        "/topic/" + str(topic_id) + "/" + \
        str(moodle_topic_id) + "/learningElement"
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("input, student_id, moodle_user_id, \
                         output_expected, status_code_expected", [
    # Working example
    (
        {
            "answers":
            [
                {
                    "question_id": "AR1",
                    "answer": "a"
                },
                {
                    "question_id": "AR2",
                    "answer": "a"
                },
                {
                    "question_id": "AR3",
                    "answer": "a"
                },
                {
                    "question_id": "AR4",
                    "answer": "a"
                },
                {
                    "question_id": "AR5",
                    "answer": "a"
                },
                {
                    "question_id": "AR6",
                    "answer": "a"
                },
                {
                    "question_id": "AR7",
                    "answer": "a"
                },
                {
                    "question_id": "AR8",
                    "answer": "a"
                },
                {
                    "question_id": "AR9",
                    "answer": "a"
                },
                {
                    "question_id": "AR10",
                    "answer": "a"
                },
                {
                    "question_id": "AR11",
                    "answer": "a"
                },

                {
                    "question_id": "VV1",
                    "answer": "a"
                },
                {
                    "question_id": "VV2",
                    "answer": "a"
                },
                {
                    "question_id": "VV3",
                    "answer": "a"
                },
                {
                    "question_id": "VV4",
                    "answer": "a"
                },
                {
                    "question_id": "VV5",
                    "answer": "a"
                },
                {
                    "question_id": "VV6",
                    "answer": "a"
                },
                {
                    "question_id": "VV7",
                    "answer": "a"
                },
                {
                    "question_id": "VV8",
                    "answer": "a"
                },
                {
                    "question_id": "VV9",
                    "answer": "a"
                },
                {
                    "question_id": "VV10",
                    "answer": "a"
                },
                {
                    "question_id": "VV11",
                    "answer": "a"
                },

                {
                    "question_id": "SI1",
                    "answer": "a"
                },
                {
                    "question_id": "SI2",
                    "answer": "a"
                },
                {
                    "question_id": "SI3",
                    "answer": "a"
                },
                {
                    "question_id": "SI4",
                    "answer": "a"
                },
                {
                    "question_id": "SI5",
                    "answer": "a"
                },
                {
                    "question_id": "SI6",
                    "answer": "a"
                },
                {
                    "question_id": "SI7",
                    "answer": "a"
                },
                {
                    "question_id": "SI8",
                    "answer": "a"
                },
                {
                    "question_id": "SI9",
                    "answer": "a"
                },
                {
                    "question_id": "SI10",
                    "answer": "a"
                },
                {
                    "question_id": "SI11",
                    "answer": "a"
                },

                {
                    "question_id": "GS1",
                    "answer": "a"
                },
                {
                    "question_id": "GS2",
                    "answer": "a"
                },
                {
                    "question_id": "GS3",
                    "answer": "a"
                },
                {
                    "question_id": "GS4",
                    "answer": "a"
                },
                {
                    "question_id": "GS5",
                    "answer": "a"
                },
                {
                    "question_id": "GS6",
                    "answer": "a"
                },
                {
                    "question_id": "GS7",
                    "answer": "a"
                },
                {
                    "question_id": "GS8",
                    "answer": "a"
                },
                {
                    "question_id": "GS9",
                    "answer": "a"
                },
                {
                    "question_id": "GS10",
                    "answer": "a"
                },
                {
                    "question_id": "GS11",
                    "answer": "a"
                }
            ],
        },
        1,
        1,
        {
            "perception_dimension": "SNS",
            "perception_value": 7,
            "input_dimension": "VIS",
            "input_value": 7,
            "processing_dimension": "ACT",
            "processing_value": 7,
            "understanding_dimension": "GLO",
            "understanding_value": 7
        },
        201
    ),
    # Working example short questionnaire
    (
        {
            "answers":
            [
                {
                    "question_id": "AR1",
                    "answer": "a"
                },
                {
                    "question_id": "AR2",
                    "answer": "a"
                },
                {
                    "question_id": "AR3",
                    "answer": "a"
                },
                {
                    "question_id": "AR4",
                    "answer": "a"
                },
                {
                    "question_id": "AR5",
                    "answer": "a"
                },

                {
                    "question_id": "VV1",
                    "answer": "a"
                },
                {
                    "question_id": "VV2",
                    "answer": "a"
                },
                {
                    "question_id": "VV3",
                    "answer": "a"
                },
                {
                    "question_id": "VV4",
                    "answer": "a"
                },
                {
                    "question_id": "VV5",
                    "answer": "a"
                },

                {
                    "question_id": "SI1",
                    "answer": "a"
                },
                {
                    "question_id": "SI2",
                    "answer": "a"
                },
                {
                    "question_id": "SI3",
                    "answer": "a"
                },
                {
                    "question_id": "SI4",
                    "answer": "a"
                },
                {
                    "question_id": "SI5",
                    "answer": "a"
                },

                {
                    "question_id": "GS1",
                    "answer": "a"
                },
                {
                    "question_id": "GS2",
                    "answer": "a"
                },
                {
                    "question_id": "GS3",
                    "answer": "a"
                },
                {
                    "question_id": "GS4",
                    "answer": "a"
                },
                {
                    "question_id": "GS5",
                    "answer": "a"
                }
            ],
        },
        1,
        1,
        {
            "perception_dimension": "SNS",
            "perception_value": 7,
            "input_dimension": "VIS",
            "input_value": 7,
            "processing_dimension": "ACT",
            "processing_value": 7,
            "understanding_dimension": "GLO",
            "understanding_value": 7
        },
        201
    ),
    # Wrong ID for question
    (
        {
            "answers":
            [
                {
                    "question_id": "ARF1",
                    "answer": "a"
                },
                {
                    "question_id": "ARF2",
                    "answer": "a"
                },
                {
                    "question_id": "ARF3",
                    "answer": "a"
                },
                {
                    "question_id": "ARF4",
                    "answer": "a"
                },
                {
                    "question_id": "ARF5",
                    "answer": "a"
                },
                {
                    "question_id": "ARF6",
                    "answer": "a"
                },
                {
                    "question_id": "ARF7",
                    "answer": "a"
                },
                {
                    "question_id": "ARF8",
                    "answer": "a"
                },
                {
                    "question_id": "ARF9",
                    "answer": "a"
                },
                {
                    "question_id": "ARF10",
                    "answer": "a"
                },
                {
                    "question_id": "ARF11",
                    "answer": "a"
                },

                {
                    "question_id": "VV1",
                    "answer": "a"
                },
                {
                    "question_id": "VV2",
                    "answer": "a"
                },
                {
                    "question_id": "VV3",
                    "answer": "a"
                },
                {
                    "question_id": "VV4",
                    "answer": "a"
                },
                {
                    "question_id": "VV5",
                    "answer": "a"
                },
                {
                    "question_id": "VV6",
                    "answer": "a"
                },
                {
                    "question_id": "VV7",
                    "answer": "a"
                },
                {
                    "question_id": "VV8",
                    "answer": "a"
                },
                {
                    "question_id": "VV9",
                    "answer": "a"
                },
                {
                    "question_id": "VV10",
                    "answer": "a"
                },
                {
                    "question_id": "VV11",
                    "answer": "a"
                },

                {
                    "question_id": "SI1",
                    "answer": "a"
                },
                {
                    "question_id": "SI2",
                    "answer": "a"
                },
                {
                    "question_id": "SI3",
                    "answer": "a"
                },
                {
                    "question_id": "SI4",
                    "answer": "a"
                },
                {
                    "question_id": "SI5",
                    "answer": "a"
                },
                {
                    "question_id": "SI6",
                    "answer": "a"
                },
                {
                    "question_id": "SI7",
                    "answer": "a"
                },
                {
                    "question_id": "SI8",
                    "answer": "a"
                },
                {
                    "question_id": "SI9",
                    "answer": "a"
                },
                {
                    "question_id": "SI10",
                    "answer": "a"
                },
                {
                    "question_id": "SI11",
                    "answer": "a"
                },

                {
                    "question_id": "GS1",
                    "answer": "a"
                },
                {
                    "question_id": "GS2",
                    "answer": "a"
                },
                {
                    "question_id": "GS3",
                    "answer": "a"
                },
                {
                    "question_id": "GS4",
                    "answer": "a"
                },
                {
                    "question_id": "GS5",
                    "answer": "a"
                },
                {
                    "question_id": "GS6",
                    "answer": "a"
                },
                {
                    "question_id": "GS7",
                    "answer": "a"
                },
                {
                    "question_id": "GS8",
                    "answer": "a"
                },
                {
                    "question_id": "GS9",
                    "answer": "a"
                },
                {
                    "question_id": "GS10",
                    "answer": "a"
                },
                {
                    "question_id": "GS11",
                    "answer": "a"
                }
            ],
        },
        1,
        1,
        {
            "error": "There is a non valid Question ID."
        },
        400
    )
])
def test_post_ils_questionnaire(
    client,
    input,
    student_id,
    moodle_user_id,
    output_expected,
    status_code_expected
):
    url = "/moodle/student/" + str(student_id) + \
        "/" + str(moodle_user_id) + "/questionnaire"
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("input, student_id, moodle_user_id, topic_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_topic_id": 1
        },
        1,
        1,
        1,
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_topic_id": 1
        },
        201
    ),
    # Working Example with no previous topic
    (
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_topic_id": None
        },
        1,
        1,
        1,
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_topic_id": None
        },
        201
    ),
    # Wrong data format
    (
        {
            "visit_start_time": "01.01.2023",
            "previous_topic_id": 1
        },
        1,
        1,
        1,
        {
            "error": "Paramaters have the wrong data type."
        },
        400
    ),
    # Missing Parameter
    (
        {
            "previous_topic_id": 1
        },
        1,
        1,
        1,
        {
            "error": "Paramaters are missing in the request body."
        },
        400
    )
])
def test_post_topic_visit(
    client,
    input,
    student_id,
    moodle_user_id,
    topic_id,
    output_expected,
    status_code_expected
):
    url = "/moodle/student/" + str(student_id) + \
        "/" + str(moodle_user_id) + "/topic/" + str(topic_id)
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("input, student_id, moodle_user_id, \
                         learning_element_id, output_expected, \
                         status_code_expected", [
    # Working Example
    (
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_learning_element_id": 1
        },
        1,
        1,
        1,
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_learning_element_id": 1
        },
        201
    ),
    # Working Example with no previous learning element
    (
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_learning_element_id": None
        },
        1,
        1,
        1,
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_learning_element_id": None
        },
        201
    ),
    # Wrong data format
    (
        {
            "visit_start_time": "01.01.2023",
            "previous_learning_element_id": 1
        },
        1,
        1,
        1,
        {
            "error": "Paramaters have the wrong data type."
        },
        400
    ),
    # Missing Parameter
    (
        {
            "previous_learning_element_id": 1
        },
        1,
        1,
        1,
        {
            "error": "Paramaters are missing in the request body."
        },
        400
    )
])
def test_post_learning_element_visit(
    client,
    input,
    student_id,
    moodle_user_id,
    learning_element_id,
    output_expected,
    status_code_expected
):
    url = "/moodle/student/" + str(student_id) + \
        "/" + str(moodle_user_id) + "/learning_element/" + \
        str(learning_element_id)
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
