# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, course_creator_id,\
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
                    "created_at": "2017-07-21T17:32:28Z",
                    "last_updated": "2017-07-21T17:32:28Z",
                    "nr_teachers": 3,
                    "teachers": [
                        {
                            "name": "Maria Musterfrau"
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
        {
            "error": "The User was not found"
        },
        404
    )
])
def test_api_get_courses_by_course_creator_id(
    client,
    user_id,
    lms_user_id,
    course_creator_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/courseCreator/" + str(course_creator_id) + "/course"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
