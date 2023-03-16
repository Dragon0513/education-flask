# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        {
            "learning_style": [
                {
                    "perception_dimension": "SNS",
                    "perception_value": 0,
                    "input_dimension": "VIS",
                    "input_value": 0,
                    "processing_dimension": "ACT",
                    "processing_value": 0,
                    "understanding_dimension": "GLO",
                    "understanding_value": 0
                }
            ],
            "learning_strategy": [
                {}
            ],
            "knowledge": [
                {}
            ],
            "learning_analytics": [
                {}
            ]
        },
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_get_learning_characteristics_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningCharacteristics"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        {},
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_get_learning_analytics_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningAnalytics"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        {
            "perception_dimension": "SNS",
            "perception_value": 0,
            "input_dimension": "VIS",
            "input_value": 0,
            "processing_dimension": "ACT",
            "processing_value": 0,
            "understanding_dimension": "GLO",
            "understanding_value": 0
        },
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_get_learning_style_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningStyle"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        {},
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_get_learning_strategy_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningStrategy"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        {},
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_get_knowledge_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/knowledge"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        {
            "courses": [
                {
                    "id": 1,
                    "name": "Test Course",
                    "lms_id": 1,
                    "time_spend": 234.56
                }
            ]
        },
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_get_courses_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        {
            "id": 1,
            "name": "Test Course",
            "lms_id": 1,
            "time_spend": 234.56
        },
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        {
            "error": "The Course was not found"
        },
        404
    )
])
def test_api_get_course_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        {
            "id": 1,
            "name": "Test Topic",
            "lms_id": 1,
            "is_topic": True,
            "parent_id": 1,
            "contains_le": False,
            "done": False,
            "done_percantage": 75.25,
            "last_visit": "2017-07-21T17:32:28Z",
            "time_spend": 123.45,
            "is_recommended": True
        },
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        {
            "error": "The Course was not found"
        },
        404
    )
])
def test_api_get_topic_recommendation_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/recommendation"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        [
            [
                {
                    "position": 1,
                    "topic": {
                        "id": 1,
                        "name": "Test Topic",
                        "lms_id": 1,
                        "is_topic": True,
                        "parent_id": 1,
                        "contains_le": False,
                        "done": False,
                        "done_percantage": 75.25,
                        "last_visit": "2017-07-21T17:32:28Z",
                        "time_spend": 123.45,
                        "is_recommended": True
                    }
                }
            ]
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        {
            "error": "The Course was not found"
        },
        404
    )
])
def test_api_get_topic_learningPath_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/learningPath"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        [
            {
                "topics": [
                    {
                        "id": 1,
                        "name": "Test Topic",
                        "lms_id": 1,
                        "is_topic": True,
                        "parent_id": 1,
                        "contains_le": False,
                        "done": False,
                        "done_percantage": 75.25,
                        "last_visit": "2017-07-21T17:32:28Z",
                        "time_spend": 123.45,
                        "is_recommended": True
                    }
                ]
            }
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        {
            "error": "The Course was not found"
        },
        404
    )
])
def test_api_get_topics_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        [
            {
                "learning_elements": [
                    {
                        "id": 1,
                        "lms_id": 1,
                        "activity_type": "Quiz",
                        "classification": "RQ",
                        "name": "Test Learning Element",
                        "done": False,
                        "done_at": "2017-07-21T17:32:28Z",
                        "nr_of_visits": 3,
                        "last_visit": "2017-07-21T17:32:28Z",
                        "time_spend": 123.45,
                        "is_recommended": True
                    }
                ]
            }
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        {
            "error": "The Course was not found"
        },
        404
    )
])
def test_api_get_learning_elements_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/learningElement"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        [
            {
                "id": 1,
                "name": "Test Topic",
                "lms_id": 1,
                "is_topic": True,
                "parent_id": 1,
                "contains_le": False,
                "done": False,
                "done_percantage": 75.25,
                "last_visit": "2017-07-21T17:32:28Z",
                "time_spend": 123.45,
                "is_recommended": True
            }
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        {
            "error": "The Course was not found"
        },
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        {
            "error": "The Topic was not found"
        },
        404
    )
])
def test_api_get_topic_for_topic_id_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        [
            {
                "id": 1,
                "name": "Test Topic",
                "lms_id": 1,
                "is_topic": True,
                "parent_id": 1,
                "contains_le": False,
                "done": False,
                "done_percantage": 75.25,
                "last_visit": "2017-07-21T17:32:28Z",
                "time_spend": 123.45,
                "is_recommended": True
            }
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        {
            "error": "The Course was not found"
        },
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        {
            "error": "The Topic was not found"
        },
        404
    )
])
def test_api_get_topic_recommendation_for_topic_id_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/recommendation"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        [
            [
                {
                    "position": 1,
                    "learning_element": {
                        "id": 1,
                        "lms_id": 1,
                        "activity_type": "Quiz",
                        "classification": "RQ",
                        "name": "Test Learning Element",
                        "done": False,
                        "done_at": "2017-07-21T17:32:28Z",
                        "nr_of_visits": 3,
                        "last_visit": "2017-07-21T17:32:28Z",
                        "time_spend": 123.45,
                        "is_recommended": True
                    }
                }
            ]
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        {
            "error": "The Course was not found"
        },
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        {
            "error": "The Topic was not found"
        },
        404
    )
])
def test_api_get_topic_learning_path_for_topic_id_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/learningPath"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        [
            {
                "topics": [
                    {
                        "id": 1,
                        "name": "Test Topic",
                        "lms_id": 1,
                        "is_topic": True,
                        "parent_id": 1,
                        "contains_le": False,
                        "done": False,
                        "done_percantage": 75.25,
                        "last_visit": "2017-07-21T17:32:28Z",
                        "time_spend": 123.45,
                        "is_recommended": True
                    }
                ]
            }
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        {
            "error": "The Course was not found"
        },
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        {
            "error": "The Topic was not found"
        },
        404
    )
])
def test_api_get_subtopics_for_topic_id_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/subtopic"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        [
            {
                "learning_elements": [
                    {
                        "id": 1,
                        "lms_id": 1,
                        "activity_type": "Quiz",
                        "classification": "RQ",
                        "name": "Test Learning Element",
                        "done": False,
                        "done_at": "2017-07-21T17:32:28Z",
                        "nr_of_visits": 3,
                        "last_visit": "2017-07-21T17:32:28Z",
                        "time_spend": 123.45,
                        "is_recommended": True
                    }
                ]
            }
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        {
            "error": "The Course was not found"
        },
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        {
            "error": "The Topic was not found"
        },
        404
    )
])
def test_api_get_learning_elements_for_topic_id_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/learningElement"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, learning_element_id, output_expected, \
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        1,
        [
            {
                "id": 1,
                "lms_id": 1,
                "activity_type": "Quiz",
                "classification": "RQ",
                "name": "Test Learning Element",
                "done": False,
                "done_at": "2017-07-21T17:32:28Z",
                "nr_of_visits": 3,
                "last_visit": "2017-07-21T17:32:28Z",
                "time_spend": 123.45,
                "is_recommended": True
            }
        ],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        1,
        {
            "error": "The Course was not found"
        },
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        1,
        {
            "error": "The Topic was not found"
        },
        404
    ),
    # Learning Element not found
    (
        1,
        1,
        1,
        1,
        1,
        2,
        {
            "error": "The Learning Element was not found"
        },
        404
    )
])
def test_api_get_learning_element_for_le_id_for_topic_id_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    learning_element_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/learningElement/" +\
        str(learning_element_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        {
            "courses": [
                {
                    "id": 1,
                    "name": "Test Course",
                    "lms_id": 1,
                    "time_spend": 234.56
                }
            ],
            "learning_style": [
                {
                    "perception_dimension": "SNS",
                    "perception_value": 7,
                    "input_dimension": "VIS",
                    "input_value": 7,
                    "processing_dimension": "ACT",
                    "processing_value": 7,
                    "understanding_dimension": "GLO",
                    "understanding_value": 7
                }
            ],
            "learning_strategy": [
                {}
            ]
        },
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_get_dashboard_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/dashboard/overview"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        {
            "topics": [
                {
                    "id": 1,
                    "name": "Test Topic",
                    "lms_id": 1,
                    "is_topic": True,
                    "parent_id": 1,
                    "contains_le": False,
                    "done": False,
                    "done_percantage": 75.25,
                    "last_visit": "2017-07-21T17:32:28Z",
                    "time_spend": 123.45,
                    "is_recommended": True
                }
            ],
            "learning_style": [
                {
                    "perception_dimension": "SNS",
                    "perception_value": 7,
                    "input_dimension": "VIS",
                    "input_value": 7,
                    "processing_dimension": "ACT",
                    "processing_value": 7,
                    "understanding_dimension": "GLO",
                    "understanding_value": 7
                }
            ],
            "learning_style_course": [
                {
                    "perception_dimension": "SNS",
                    "perception_value": 7,
                    "input_dimension": "VIS",
                    "input_value": 7,
                    "processing_dimension": "ACT",
                    "processing_value": 7,
                    "understanding_dimension": "GLO",
                    "understanding_value": 7
                }
            ]
        },
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        {
            "error": "The Course was not found"
        },
        404
    )
])
def test_api_get_dashboard_course_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/dashboard/course/" + \
        str(course_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        {
            "topics": [
                {
                    "id": 1,
                    "name": "Test Topic",
                    "lms_id": 1,
                    "is_topic": True,
                    "parent_id": 1,
                    "contains_le": False,
                    "done": False,
                    "done_percantage": 75.25,
                    "last_visit": "2017-07-21T17:32:28Z",
                    "time_spend": 123.45,
                    "is_recommended": True
                }
            ]
        },
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        {
            "error": "The User was not found"
        },
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        {
            "error": "The Course was not found"
        },
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        {
            "error": "The Topic was not found"
        },
        404
    )
])
def test_api_get_dashboard_topic_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/dashboard/course/" + \
        str(course_id) + "/topic/" + str(topic_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
