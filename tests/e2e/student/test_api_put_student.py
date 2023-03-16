# Tests for put methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, student_id, request_body, \
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
            ],
            "knowledge": [
                {}
            ],
            "learning_analytics": [
                {}
            ]
        },
        {
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
            ],
            "knowledge": [
                {}
            ],
            "learning_analytics": [
                {}
            ]
        },
        201
    ),
    # User not found
    (
        2,
        1,
        1,
        {
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
            ],
            "knowledge": [
                {}
            ],
            "learning_analytics": [
                {}
            ]
        },
        {
            "error": "The User was not found"
        },
        404
    ),
    # Empty Request body
    (
        2,
        1,
        1,
        {},
        {
            "error": "The Request Body is missing."
        },
        404
    ),
    # Wrong numbers in request body
    (
        1,
        1,
        1,
        {
            "learning_style": [
                {
                    "perception_dimension": "SNS",
                    "perception_value": 12,
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
            ],
            "knowledge": [
                {}
            ],
            "learning_analytics": [
                {}
            ]
        },
        {
            "error": "The Input Learning Style is out the range [0-11]."
        },
        404
    ),
    # Wrong number of dimensions in request body
    (
        1,
        1,
        1,
        {
            "learning_style": [
                {
                    "perception_dimension": "SNS",
                    "perception_value": 7,
                    "input_dimension": "VIS",
                    "input_value": 7,
                    "processing_dimension": "ACT",
                    "processing_value": 7
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
        {
            "error": "There need to be 4 dimensions for the Learning Style."
        },
        404
    ),
    # Missing data in Request body
    (
        1,
        1,
        1,
        {
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
            "knowledge": [
                {}
            ],
            "learning_analytics": [
                {}
            ]
        },
        {
            "error": "The request body is incomplete."
        },
        404
    )
])
def test_api_put_learning_characteristics_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    request_body,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningCharacteristics"
    r = client.put(url, json=request_body)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, request_body, \
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
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
    # User not found
    (
        2,
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
        {
            "error": "The User was not found"
        },
        404
    ),
    # Empty Request body
    (
        2,
        1,
        1,
        {},
        {
            "error": "The Request Body is missing."
        },
        404
    ),
    # Wrong numbers in request body
    (
        1,
        1,
        1,
        {
            "perception_dimension": "SNS",
            "perception_value": 12,
            "input_dimension": "VIS",
            "input_value": 7,
            "processing_dimension": "ACT",
            "processing_value": 7,
            "understanding_dimension": "GLO",
            "understanding_value": 7
        },
        {
            "error": "The Input Learning Style is out the range [0-11]."
        },
        404
    ),
    # Wrong number of dimensions in request body
    (
        1,
        1,
        1,
        {
            "perception_dimension": "SNS",
            "perception_value": 7,
            "input_dimension": "VIS",
            "input_value": 7,
            "processing_dimension": "ACT",
            "processing_value": 7
        },
        {
            "error": "There need to be 4 dimensions for the Learning Style."
        },
        404
    )
])
def test_api_put_learning_style_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    request_body,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningStyle"
    r = client.put(url, json=request_body)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
