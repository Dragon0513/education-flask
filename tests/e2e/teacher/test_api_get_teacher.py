# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, teacher_id,\
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
                    "user_nr": 42,
                    "created_at": "2017-07-21T17:32:28Z",
                    "last_updated": "2017-07-21T17:32:28Z"
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
def test_api_get_courses_by_teacher_id(
    client,
    user_id,
    lms_user_id,
    teacher_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/teacher/" + str(teacher_id) + "/course"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, teacher_id, course_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        {
            "learning_style": [
                {
                    "perception_avg": 3.1,
                    "perception_min": -9.5,
                    "perception_max": 8.7,
                    "input_avg": 3.1,
                    "input_min": -9.5,
                    "input_max": 8.7,
                    "processing_avg": 3.1,
                    "processing_min": -9.5,
                    "processing_max": 8.7,
                    "understanding_avg": 3.1,
                    "understanding_min": -9.5,
                    "understanding_max": 8.7
                }
            ],
            "performer": [
                {
                    "poor_performer": 0.1,
                    "average_performer": 0.6,
                    "high_performer": 0.3
                }
            ],
            "time_spend": [
                {
                    "month": 1,
                    "min_time": 15.4,
                    "max_time": 52.7,
                    "avg_time": 52.7
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
def test_api_get_dashboard_by_course_id_by_teacher_id(
    client,
    user_id,
    lms_user_id,
    teacher_id,
    course_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/teacher/" + str(teacher_id) + "dashboard/course/" + \
        str(course_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, teacher_id, course_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        {
            "clicks": [
                {
                    "topic_name": "Test Topic 1",
                    "popularity": 7.8
                }
            ],
            "knowledge": [
                {
                    "score": 56.7
                }
            ],
            "time": [
                {
                    "month": 1,
                    "topics": [
                        {
                            "topic_name": "Test Topic 1",
                            "time_spend": 50.3
                        }
                    ]
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
def test_api_get_dashboard_topic_by_course_id_by_teacher_id(
    client,
    user_id,
    lms_user_id,
    teacher_id,
    course_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/teacher/" + str(teacher_id) + "dashboard/course/" + \
        str(course_id) + "/topic"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, teacher_id, course_id,\
                         topic_id, output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        {
            "feedback": [
                {
                    "learning_element_name": "Test Learning Element 1",
                    "score": 4.2
                }
            ],
            "clicks": [
                {
                    "topic_name": "Test Learning Element 1",
                    "visits": 42
                }
            ],
            "knowledge": [
                {
                    "error_analysis": [
                        {
                            "learning_element_name": "Test Learning Element 1",
                            "first_try": 10,
                            "second_try": 30,
                            "third_try": 8
                        }
                    ],
                    "learning_progress": [
                        {
                            "learning_element_name": "Test Learning Element 1",
                            "min_point": 0.15,
                            "avg_point": 0.6,
                            "max_point": 0.25
                        }
                    ]
                }
            ],
            "time": [
                {
                    "learning_element_name": "Test Learning Element 1",
                    "min_time": 3.5,
                    "avg_time": 7.2,
                    "max_time": 12.9
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
def test_api_get_dashboard_les_by_course_id_by_teacher_id(
    client,
    user_id,
    lms_user_id,
    teacher_id,
    course_id,
    topic_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/teacher/" + str(teacher_id) + "dashboard/course/" + \
        str(course_id) + "/topic/" + str(topic_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
