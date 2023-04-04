# Tests for put methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, student_id, request_body, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        147,
        1,
        103,
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
        147,
        1,
        103,
        {},
        ['error'],
        400
    ),
    # Wrong numbers in request body
    (
        147,
        1,
        103,
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
        400
    ),
    # Wrong number of dimensions in request body
    (
        147,
        1,
        103,
        {
            "perception_dimension": "SNS",
            "perception_value": 7,
            "input_dimension": "VIS",
            "input_value": 7,
            "processing_dimension": "ACT",
            "processing_value": 7
        },
        ['error'],
        400
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
    for key in keys_expected:
        assert key in response.keys()
