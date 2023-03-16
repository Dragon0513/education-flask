# Tests for delete methods
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
            "message": "Deletion was successful."
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
def test_api_delete_learning_characteristics_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningCharacteristics"
    r = client.delete(url)
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
            "message": "Deletion was successful."
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
def test_api_delete_learning_analytics_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningAnalytics"
    r = client.delete(url)
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
            "message": "Deletion was successful."
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
def test_api_delete_learning_style_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningStyle"
    r = client.delete(url)
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
            "message": "Deletion was successful."
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
def test_api_delete_learning_strategy_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningStrategy"
    r = client.delete(url)
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
            "message": "Deletion was successful."
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
def test_api_delete_knowledge_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/knowledge"
    r = client.delete(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
