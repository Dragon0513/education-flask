# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['learning_style', 'learning_strategy',\
         'knowledge', 'learning_analytics'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_learning_characteristics_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningCharacteristics"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_learning_analytics_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningAnalytics"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['perception_dimension', 'perception_value', 'input_dimension',\
         'input_value', 'processing_dimension', 'processing_value',\
         'understanding_dimension', 'understanding_value'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_learning_style_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningStyle"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_learning_strategy_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/learningStrategy"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_knowledge_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/knowledge"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['courses'],
        ['id', 'name', 'lms_id', 'time_spend'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        [],
        404
    )
])
def test_api_get_courses_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'courses' in keys_expected_1:
        for key in response['courses'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['id', 'name', 'lms_id', 'time_spend'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        ['error'],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        ['error'],
        404
    )
])
def test_api_get_course_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['id', 'name', 'lms_id', 'is_topic', 'parent_id', 'contains_le',\
         'done', 'done_percantage', 'last_visit', 'time_spend',\
         'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        ['error'],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        ['error'],
        404
    )
])
def test_api_get_topic_recommendation_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/recommendation"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['position', 'topic'],
        ['id', 'name', 'lms_id', 'is_topic', 'parent_id', 'contains_le',\
         'done', 'done_percentage', 'last_visit', 'time_spend',\
         'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        ['error'],
        [],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        ['error'],
        [],
        404
    )
])
def test_api_get_topic_learningPath_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/learningPath"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'topic' in keys_expected_1:
        for key in response['courses'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['topics'],
        ['id', 'name', 'lms_id', 'parent_id', 'contains_le', 'done'\
         'done_percantage', 'last_visit', 'time_spend', 'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        ['error'],
        [],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        ['error'],
        [],
        404
    )
])
def test_api_get_topics_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'topics' in keys_expected_1:
        for key in response['topics'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['learning_elements'],
        ['id', 'lms_id', 'activity_type', 'classification', 'name', 'done',\
         'done_at', 'nr_of_visits', 'last_visit', 'time_spend',\
         'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        ['error'],
        [],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        ['error'],
        [],
        404
    )
])
def test_api_get_learning_elements_for_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/learningElement"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'learning_elements' in keys_expected_1:
        for key in response['learning_elements'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        ['id', 'name', 'lms_id', 'is_topic', 'parent_id',\
         'contains_le', 'done', 'done_percantage', 'last_visit',\
         'time_spend', 'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        ['error'],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        ['error'],
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        ['error'],
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
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        ['id', 'name', 'lms_id', 'is_topic', 'parent_id',\
         'contains_le', 'done', 'done_percantage', 'last_visit',\
         'time_spend', 'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        ['error'],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        ['error'],
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        ['error'],
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
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/recommendation"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        ['position', 'learning_element'],
        ['id', 'lms_id', 'activity_type', 'classification', 'name', 'done',\
         'done_at', 'nr_of_visits', 'last_visit', 'time_spend',\
         'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        ['error'],
        [],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        ['error'],
        [],
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        ['error'],
        [],
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
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/learningPath"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'learning_element' in keys_expected_1:
        for key in response['learning_element'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        ['topics'],
        ['id', 'name', 'lms_id', 'parent_id', 'contains_le', 'done'\
         'done_percantage', 'last_visit', 'time_spend', 'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        ['error'],
        [],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        ['error'],
        [],
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        ['error'],
        [],
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
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/subtopic"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'topics' in keys_expected_1:
        for key in response['topics'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        ['learning_elements'],
        ['id', 'lms_id', 'activity_type', 'classification', 'name', 'done',\
         'done_at', 'nr_of_visits', 'last_visit', 'time_spend',\
         'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        ['error'],
        [],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        ['error'],
        [],
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        ['error'],
        [],
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
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/learningElement"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'learning_elements' in keys_expected_1:
        for key in response['learning_elements'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, learning_element_id, keys_expected, \
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        1,
        ['id', 'lms_id', 'activity_type', 'classification', 'name', 'done',\
         'done_at', 'nr_of_visits', 'last_visit', 'time_spend',\
         'is_recommended'],
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
        ['error'],
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
        ['error'],
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
        ['error'],
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
        ['error'],
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
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/course/" + str(course_id) +\
        "/topic/" + str(topic_id) + "/learningElement/" +\
        str(learning_element_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['courses', 'learning_style', 'learning_strategy'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        404
    )
])
def test_api_get_dashboard_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/dashboard/overview"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        ['topics', 'learning_style', 'learning_style_course'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        ['error'],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        ['error'],
        404
    )
])
def test_api_get_dashboard_course_by_student_id(
    client,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    keys_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/dashboard/course/" + \
        str(course_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("user_id, lms_user_id, student_id, course_id, \
                         topic_id, keys_expected_1, keys_expected_2,\
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        ['topics'],
        ['id', 'name', 'lms_id', 'parent_id', 'contains_le', 'done'\
         'done_percantage', 'last_visit', 'time_spend', 'is_recommended'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        1,
        1,
        ['error'],
        [],
        404
    ),
    # Course not found
    (
        1,
        1,
        1,
        2,
        1,
        ['error'],
        [],
        404
    ),
    # Topic not found
    (
        1,
        1,
        1,
        1,
        2,
        ['error'],
        [],
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
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/student/" + str(student_id) + "/dashboard/course/" + \
        str(course_id) + "/topic/" + str(topic_id)
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'topics' in keys_expected_1:
        for key in response['topics'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1
