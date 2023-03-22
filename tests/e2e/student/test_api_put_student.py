# Tests for put methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, student_id, request_body, \
                         keys_expected, status_code_expected", [
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
        ['learning_style', 'learning_strategy', 'knowledge',\
         'learning_analytics'],
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
        ['error'],
        404
    ),
    # Empty Request body
    (
        2,
        1,
        1,
        {},
        ['error'],
        404
    ),
    # Wrong numbers in request body
    (
        1,
        1,
        1,
        [
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
            }
        ],
        ['error'],
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
        ['error'],
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
        ['error'],
        404
    )
])
def test_api_put_learning_characteristics_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    request_body,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningCharacteristics"
    r = client.put(url, json=request_body)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, request_body, \
                         keys_expected, status_code_expected", [
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
        ['perception_dimension', 'perception_value', 'input_dimension',\
         'input_value', 'processing_dimension', 'processing_value',\
         'understanding_dimension', 'understanding_value'],
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
        ['error'],
        404
    ),
    # Empty Request body
    (
        2,
        1,
        1,
        {},
        ['error'],
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
        ['error'],
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
        ['error'],
        404
    )
])
def test_api_put_learning_style_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    request_body,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningStyle"
    r = client.put(url, json=request_body)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
