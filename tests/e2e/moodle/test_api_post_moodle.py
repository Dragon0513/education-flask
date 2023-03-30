# Tests for post methods
import pytest
import json


# The IDs will be set during the post test to guarantee an available option
# for tests, that need a foreign key
user_id_test = 0
student_id_test = 0
course_id_test = 0
topic_id_test = 0


@pytest.mark.parametrize("input, keys_expected, status_code_expected,\
                         save_id", [
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
        201,
        True
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
        400,
        False
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
        400,
        False
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
        400,
        False
    ),
])
def test_api_create_user_from_moodle(
    client,
    input,
    keys_expected,
    status_code_expected,
    save_id
):
    r = client.post("/lms/user", json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
    if save_id:
        global user_id_test
        user_id_test = response['id']


@pytest.mark.parametrize("input, keys_expected, status_code_expected,\
                         save_id", [
    # Working Example
    (
        {
            "name": "Test Course",
            "lms_id": 1,
            "created_by": "Maria Musterfrau",
            "created_at": "2017-07-21T17:32:28Z",
            "university": "TH-AB"
        },
        ['id', 'name', 'lms_id', 'created_at', 'created_by', 'university'],
        201,
        True
    ),
    # Missing Parameter
    (
        {
            "name": "Test Course",
            "created_by": "Maria Musterfrau",
            "university": "TH-AB"
        },
        ['error'],
        400,
        False
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

        ['error'],
        400,
        False
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
        ['error'],
        400,
        False
    ),

])
def test_api_create_course_from_moodle(
    client,
    input,
    keys_expected,
    status_code_expected,
    save_id
):
    r = client.post("/lms/course", json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
    if save_id:
        global course_id_test
        course_id_test = response['id']


@pytest.mark.parametrize("input, moodle_course_id, \
                          keys_expected, status_code_expected, save_id", [
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
        ['id', 'name', 'lms_id', 'is_topic', 'parent_id',
            'contains_le', 'created_by', 'created_at', 'university'],
        201,
        True
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
        ['id', 'name', 'lms_id', 'is_topic', 'parent_id',
            'contains_le', 'created_by', 'created_at', 'university'],
        201,
        False
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
        ['error'],
        400,
        False
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
        ['error'],
        400,
        False
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
        ['error'],
        400,
        False
    ),

])
def test_api_create_topic_from_moodle(
    client,
    input,
    moodle_course_id,
    keys_expected,
    status_code_expected,
    save_id
):
    global course_id_test
    global topic_id_test
    url = "/lms/course/" + str(course_id_test) + \
        "/" + str(moodle_course_id) + "/topic"
    if topic_id_test != 0:
        input['parent_id'] = topic_id_test
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in keys_expected:
        assert key in response.keys()
    if save_id:
        topic_id_test = response['id']


@pytest.mark.parametrize("input, moodle_course_id,\
                         moodle_topic_id, keys_expected, \
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
        ['id', 'lms_id', 'activity_type', 'classification',
            'name', 'created_by', 'created_at', 'university'],
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
        ['error'],
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
        ['error'],
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
        ['error'],
        400
    )
])
def test_api_create_le_from_moodle(
    client,
    input,
    moodle_course_id,
    moodle_topic_id,
    keys_expected,
    status_code_expected
):
    global course_id_test
    global topic_id_test
    url = "/lms/course/" + str(course_id_test) + "/" + str(moodle_course_id) +\
        "/topic/" + str(topic_id_test) + "/" + \
        str(moodle_topic_id) + "/learningElement"
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in keys_expected:
        assert key in response.keys()


@pytest.mark.parametrize("input, student_id, moodle_user_id, \
                         keys_expected, status_code_expected", [
    # Working example
    (
        {
            "ils":
            [
                {
                    "question_id": "ar_1_f1",
                    "answer": "a"
                },
                {
                    "question_id": "ar_2_f5",
                    "answer": "a"
                },
                {
                    "question_id": "ar_3_f9",
                    "answer": "a"
                },
                {
                    "question_id": "ar_4_f13",
                    "answer": "a"
                },
                {
                    "question_id": "ar_5_f17",
                    "answer": "a"
                },
                {
                    "question_id": "ar_6_f21",
                    "answer": "a"
                },
                {
                    "question_id": "ar_7_f25",
                    "answer": "a"
                },
                {
                    "question_id": "ar_8_f29",
                    "answer": "a"
                },
                {
                    "question_id": "ar_9_f33",
                    "answer": "a"
                },
                {
                    "question_id": "ar_10_f37",
                    "answer": "a"
                },
                {
                    "question_id": "ar_11_f41",
                    "answer": "a"
                },

                {
                    "question_id": "vv_1_f3",
                    "answer": "a"
                },
                {
                    "question_id": "vv_2_f7",
                    "answer": "a"
                },
                {
                    "question_id": "vv_3_f11",
                    "answer": "a"
                },
                {
                    "question_id": "vv_4_f15",
                    "answer": "a"
                },
                {
                    "question_id": "vv_5_f19",
                    "answer": "a"
                },
                {
                    "question_id": "vv_6_f23",
                    "answer": "a"
                },
                {
                    "question_id": "vv_7_f27",
                    "answer": "a"
                },
                {
                    "question_id": "vv_8_f31",
                    "answer": "a"
                },
                {
                    "question_id": "vv_9_f35",
                    "answer": "a"
                },
                {
                    "question_id": "vv_10_f39",
                    "answer": "a"
                },
                {
                    "question_id": "vv_11_f43",
                    "answer": "a"
                },

                {
                    "question_id": "si_1_f2",
                    "answer": "a"
                },
                {
                    "question_id": "si_2_f6",
                    "answer": "a"
                },
                {
                    "question_id": "si_3_f10",
                    "answer": "a"
                },
                {
                    "question_id": "si_4_f14",
                    "answer": "a"
                },
                {
                    "question_id": "si_5_f18",
                    "answer": "a"
                },
                {
                    "question_id": "si_6_f22",
                    "answer": "a"
                },
                {
                    "question_id": "si_7_f26",
                    "answer": "a"
                },
                {
                    "question_id": "si_8_f30",
                    "answer": "a"
                },
                {
                    "question_id": "si_9_f34",
                    "answer": "a"
                },
                {
                    "question_id": "si_10_f38",
                    "answer": "a"
                },
                {
                    "question_id": "si_11_f42",
                    "answer": "a"
                },

                {
                    "question_id": "sg_1_f4",
                    "answer": "a"
                },
                {
                    "question_id": "sg_2_f8",
                    "answer": "a"
                },
                {
                    "question_id": "sg_3_f12",
                    "answer": "a"
                },
                {
                    "question_id": "sg_4_f16",
                    "answer": "a"
                },
                {
                    "question_id": "sg_5_f20",
                    "answer": "a"
                },
                {
                    "question_id": "sg_6_f24",
                    "answer": "a"
                },
                {
                    "question_id": "sg_7_f28",
                    "answer": "a"
                },
                {
                    "question_id": "sg_8_f32",
                    "answer": "a"
                },
                {
                    "question_id": "sg_9_f36",
                    "answer": "a"
                },
                {
                    "question_id": "sg_10_f40",
                    "answer": "a"
                },
                {
                    "question_id": "sg_11_f44",
                    "answer": "a"
                }
            ],
            "list_k":
            [
                {
                    "question_id": 'org1_f1',
                    "answer": 1
                },
                {
                    "question_id": 'org2_f2',
                    "answer": 1
                },
                {
                    "question_id": 'org3_f3',
                    "answer": 1
                },
                {
                    "question_id": 'ela1_f4',
                    "answer": 1
                },
                {
                    "question_id": 'ela2_f5',
                    "answer": 1
                },
                {
                    "question_id": 'ela3_f6',
                    "answer": 1
                },
                {
                    "question_id": 'krp1_f7',
                    "answer": 1
                },
                {
                    "question_id": 'krp2_f8',
                    "answer": 1
                },
                {
                    "question_id": 'krp3_f9',
                    "answer": 1
                },
                {
                    "question_id": 'wie1_f10',
                    "answer": 1
                },
                {
                    "question_id": 'wie2_f11',
                    "answer": 1
                },
                {
                    "question_id": 'wie3_f12',
                    "answer": 1
                },
                {
                    "question_id": 'zp1_f13',
                    "answer": 1
                },
                {
                    "question_id": 'zp2_f14',
                    "answer": 1
                },
                {
                    "question_id": 'zp3_f15',
                    "answer": 1
                },
                {
                    "question_id": 'kon1_f16',
                    "answer": 1
                },
                {
                    "question_id": 'kon2_f17',
                    "answer": 1
                },
                {
                    "question_id": 'kon3_f18',
                    "answer": 1
                },
                {
                    "question_id": 'reg1_f19',
                    "answer": 1
                },
                {
                    "question_id": 'reg2_f20',
                    "answer": 1
                },
                {
                    "question_id": 'reg3_f21',
                    "answer": 1
                },
                {
                    "question_id": 'auf1_f22',
                    "answer": 1
                },
                {
                    "question_id": 'auf2_f23',
                    "answer": 1
                },
                {
                    "question_id": 'auf3_f24',
                    "answer": 1
                },
                {
                    "question_id": 'ans1_f25',
                    "answer": 1
                },
                {
                    "question_id": 'ans2_f26',
                    "answer": 1
                },
                {
                    "question_id": 'ans3_f27',
                    "answer": 1
                },
                {
                    "question_id": 'zei1_f28',
                    "answer": 1
                },
                {
                    "question_id": 'zei2_f29',
                    "answer": 1
                },
                {
                    "question_id": 'zei3_f30',
                    "answer": 1
                },
                {
                    "question_id": 'lms1_f31',
                    "answer": 1
                },
                {
                    "question_id": 'lms2_f32',
                    "answer": 1
                },
                {
                    "question_id": 'lms3_f33',
                    "answer": 1
                },
                {
                    "question_id": 'lit1_f34',
                    "answer": 1
                },
                {
                    "question_id": 'lit2_f35',
                    "answer": 1
                },
                {
                    "question_id": 'lit3_f36',
                    "answer": 1
                },
                {
                    "question_id": 'lu1_f37',
                    "answer": 1
                },
                {
                    "question_id": 'lu2_f38',
                    "answer": 1
                },
                {
                    "question_id": 'lu3_f39',
                    "answer": 1
                }
            ]
        },
        52,
        1,
        ['perception_dimension', 'perception_value', 'input_dimension',\
         'input_value', 'processing_dimension', 'processing_value',\
         'understanding_dimension', 'understanding_value'],
        201
    ),
    # Working example short questionnaire
    (
        {
            "ils":
            [
                {
                    "question_id": "ar_3_f9",
                    "answer": "a"
                },
                {
                    "question_id": "ar_4_f13",
                    "answer": "a"
                },
                {
                    "question_id": "ar_6_f21",
                    "answer": "a"
                },
                {
                    "question_id": "ar_7_f25",
                    "answer": "a"
                },
                {
                    "question_id": "ar_8_f29",
                    "answer": "a"
                },

                {
                    "question_id": "vv_2_f7",
                    "answer": "a"
                },
                {
                    "question_id": "vv_5_f19",
                    "answer": "a"
                },
                {
                    "question_id": "vv_7_f27",
                    "answer": "a"
                },
                {
                    "question_id": "vv_10_f39",
                    "answer": "a"
                },
                {
                    "question_id": "vv_11_f43",
                    "answer": "a"
                },


                {
                    "question_id": "si_1_f2",
                    "answer": "a"
                },
                {
                    "question_id": "si_4_f14",
                    "answer": "a"
                },
                {
                    "question_id": "si_7_f26",
                    "answer": "a"
                },
                {
                    "question_id": "si_10_f38",
                    "answer": "a"
                },
                {
                    "question_id": "si_11_f42",
                    "answer": "a"
                },

                {
                    "question_id": "sg_1_f4",
                    "answer": "a"
                },
                {
                    "question_id": "sg_2_f8",
                    "answer": "a"
                },
                {
                    "question_id": "sg_4_f16",
                    "answer": "a"
                },
                {
                    "question_id": "sg_10_f40",
                    "answer": "a"
                },
                {
                    "question_id": "sg_11_f44",
                    "answer": "a"
                }
            ],
            "list_k":
            [
                {
                    "question_id": 'org1_f1',
                    "answer": 1
                },
                {
                    "question_id": 'org2_f2',
                    "answer": 1
                },
                {
                    "question_id": 'org3_f3',
                    "answer": 1
                },
                {
                    "question_id": 'ela1_f4',
                    "answer": 1
                },
                {
                    "question_id": 'ela2_f5',
                    "answer": 1
                },
                {
                    "question_id": 'ela3_f6',
                    "answer": 1
                },
                {
                    "question_id": 'krp1_f7',
                    "answer": 1
                },
                {
                    "question_id": 'krp2_f8',
                    "answer": 1
                },
                {
                    "question_id": 'krp3_f9',
                    "answer": 1
                },
                {
                    "question_id": 'wie1_f10',
                    "answer": 1
                },
                {
                    "question_id": 'wie2_f11',
                    "answer": 1
                },
                {
                    "question_id": 'wie3_f12',
                    "answer": 1
                },
                {
                    "question_id": 'zp1_f13',
                    "answer": 1
                },
                {
                    "question_id": 'zp2_f14',
                    "answer": 1
                },
                {
                    "question_id": 'zp3_f15',
                    "answer": 1
                },
                {
                    "question_id": 'kon1_f16',
                    "answer": 1
                },
                {
                    "question_id": 'kon2_f17',
                    "answer": 1
                },
                {
                    "question_id": 'kon3_f18',
                    "answer": 1
                },
                {
                    "question_id": 'reg1_f19',
                    "answer": 1
                },
                {
                    "question_id": 'reg2_f20',
                    "answer": 1
                },
                {
                    "question_id": 'reg3_f21',
                    "answer": 1
                },
                {
                    "question_id": 'auf1_f22',
                    "answer": 1
                },
                {
                    "question_id": 'auf2_f23',
                    "answer": 1
                },
                {
                    "question_id": 'auf3_f24',
                    "answer": 1
                },
                {
                    "question_id": 'ans1_f25',
                    "answer": 1
                },
                {
                    "question_id": 'ans2_f26',
                    "answer": 1
                },
                {
                    "question_id": 'ans3_f27',
                    "answer": 1
                },
                {
                    "question_id": 'zei1_f28',
                    "answer": 1
                },
                {
                    "question_id": 'zei2_f29',
                    "answer": 1
                },
                {
                    "question_id": 'zei3_f30',
                    "answer": 1
                },
                {
                    "question_id": 'lms1_f31',
                    "answer": 1
                },
                {
                    "question_id": 'lms2_f32',
                    "answer": 1
                },
                {
                    "question_id": 'lms3_f33',
                    "answer": 1
                },
                {
                    "question_id": 'lit1_f34',
                    "answer": 1
                },
                {
                    "question_id": 'lit2_f35',
                    "answer": 1
                },
                {
                    "question_id": 'lit3_f36',
                    "answer": 1
                },
                {
                    "question_id": 'lu1_f37',
                    "answer": 1
                },
                {
                    "question_id": 'lu2_f38',
                    "answer": 1
                },
                {
                    "question_id": 'lu3_f39',
                    "answer": 1
                }
            ]
        },
        1,
        1,
        ['perception_dimension', 'perception_value', 'input_dimension',\
         'input_value', 'processing_dimension', 'processing_value',\
         'understanding_dimension', 'understanding_value'],
        201
    ),
    # Missing mandatory answer
    (
        {
            "ils":
            [
                {
                    "question_id": "ar_3_f9",
                    "answer": "a"
                },
                {
                    "question_id": "ar_4_f13",
                    "answer": "a"
                },
                {
                    "question_id": "ar_6_f21",
                    "answer": "a"
                },
                {
                    "question_id": "ar_7_f25",
                    "answer": "a"
                },
                {
                    "question_id": "ar_8_f29",
                    "answer": "a"
                },

                {
                    "question_id": "vv_2_f7",
                    "answer": "a"
                },
                {
                    "question_id": "vv_5_f19",
                    "answer": "a"
                },
                {
                    "question_id": "vv_7_f27",
                    "answer": "a"
                },
                {
                    "question_id": "vv_10_f39",
                    "answer": "a"
                },
                {
                    "question_id": "vv_11_f43",
                    "answer": "a"
                },


                {
                    "question_id": "si_1_f2",
                    "answer": "a"
                },
                {
                    "question_id": "si_4_f14",
                    "answer": "a"
                },
                {
                    "question_id": "si_7_f26",
                    "answer": "a"
                },
                {
                    "question_id": "si_10_f38",
                    "answer": "a"
                },
                {
                    "question_id": "si_11_f42",
                    "answer": "a"
                },

                {
                    "question_id": "sg_1_f4",
                    "answer": "a"
                },
                {
                    "question_id": "sg_2_f8",
                    "answer": "a"
                },
                {
                    "question_id": "sg_4_f16",
                    "answer": "a"
                },
                {
                    "question_id": "sg_10_f40",
                    "answer": "a"
                }
            ],
            "list_k":
            [
                {
                    "question_id": 'org1_f1',
                    "answer": 1
                },
                {
                    "question_id": 'org2_f2',
                    "answer": 1
                },
                {
                    "question_id": 'org3_f3',
                    "answer": 1
                },
                {
                    "question_id": 'ela1_f4',
                    "answer": 1
                },
                {
                    "question_id": 'ela2_f5',
                    "answer": 1
                },
                {
                    "question_id": 'ela3_f6',
                    "answer": 1
                },
                {
                    "question_id": 'krp1_f7',
                    "answer": 1
                },
                {
                    "question_id": 'krp2_f8',
                    "answer": 1
                },
                {
                    "question_id": 'krp3_f9',
                    "answer": 1
                },
                {
                    "question_id": 'wie1_f10',
                    "answer": 1
                },
                {
                    "question_id": 'wie2_f11',
                    "answer": 1
                },
                {
                    "question_id": 'wie3_f12',
                    "answer": 1
                },
                {
                    "question_id": 'zp1_f13',
                    "answer": 1
                },
                {
                    "question_id": 'zp2_f14',
                    "answer": 1
                },
                {
                    "question_id": 'zp3_f15',
                    "answer": 1
                },
                {
                    "question_id": 'kon1_f16',
                    "answer": 1
                },
                {
                    "question_id": 'kon2_f17',
                    "answer": 1
                },
                {
                    "question_id": 'kon3_f18',
                    "answer": 1
                },
                {
                    "question_id": 'reg1_f19',
                    "answer": 1
                },
                {
                    "question_id": 'reg2_f20',
                    "answer": 1
                },
                {
                    "question_id": 'reg3_f21',
                    "answer": 1
                },
                {
                    "question_id": 'auf1_f22',
                    "answer": 1
                },
                {
                    "question_id": 'auf2_f23',
                    "answer": 1
                },
                {
                    "question_id": 'auf3_f24',
                    "answer": 1
                },
                {
                    "question_id": 'ans1_f25',
                    "answer": 1
                },
                {
                    "question_id": 'ans2_f26',
                    "answer": 1
                },
                {
                    "question_id": 'ans3_f27',
                    "answer": 1
                },
                {
                    "question_id": 'zei1_f28',
                    "answer": 1
                },
                {
                    "question_id": 'zei2_f29',
                    "answer": 1
                },
                {
                    "question_id": 'zei3_f30',
                    "answer": 1
                },
                {
                    "question_id": 'lms1_f31',
                    "answer": 1
                },
                {
                    "question_id": 'lms2_f32',
                    "answer": 1
                },
                {
                    "question_id": 'lms3_f33',
                    "answer": 1
                },
                {
                    "question_id": 'lit1_f34',
                    "answer": 1
                },
                {
                    "question_id": 'lit2_f35',
                    "answer": 1
                },
                {
                    "question_id": 'lit3_f36',
                    "answer": 1
                },
                {
                    "question_id": 'lu1_f37',
                    "answer": 1
                },
                {
                    "question_id": 'lu2_f38',
                    "answer": 1
                },
                {
                    "question_id": 'lu3_f39',
                    "answer": 1
                }
            ]
        },
        1,
        1,
        ['error'],
        400
    ),
    # Wrong ID for question
    (
        {
            "ils":
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
            "list_k":
            [
                {
                    "question_id": 'org1_f1',
                    "answer": 1
                },
                {
                    "question_id": 'org2_f2',
                    "answer": 1
                },
                {
                    "question_id": 'org3_f3',
                    "answer": 1
                },
                {
                    "question_id": 'ela1_f4',
                    "answer": 1
                },
                {
                    "question_id": 'ela2_f5',
                    "answer": 1
                },
                {
                    "question_id": 'ela3_f6',
                    "answer": 1
                },
                {
                    "question_id": 'krp1_f7',
                    "answer": 1
                },
                {
                    "question_id": 'krp2_f8',
                    "answer": 1
                },
                {
                    "question_id": 'krp3_f9',
                    "answer": 1
                },
                {
                    "question_id": 'wie1_f10',
                    "answer": 1
                },
                {
                    "question_id": 'wie2_f11',
                    "answer": 1
                },
                {
                    "question_id": 'wie3_f12',
                    "answer": 1
                },
                {
                    "question_id": 'zp1_f13',
                    "answer": 1
                },
                {
                    "question_id": 'zp2_f14',
                    "answer": 1
                },
                {
                    "question_id": 'zp3_f15',
                    "answer": 1
                },
                {
                    "question_id": 'kon1_f16',
                    "answer": 1
                },
                {
                    "question_id": 'kon2_f17',
                    "answer": 1
                },
                {
                    "question_id": 'kon3_f18',
                    "answer": 1
                },
                {
                    "question_id": 'reg1_f19',
                    "answer": 1
                },
                {
                    "question_id": 'reg2_f20',
                    "answer": 1
                },
                {
                    "question_id": 'reg3_f21',
                    "answer": 1
                },
                {
                    "question_id": 'auf1_f22',
                    "answer": 1
                },
                {
                    "question_id": 'auf2_f23',
                    "answer": 1
                },
                {
                    "question_id": 'auf3_f24',
                    "answer": 1
                },
                {
                    "question_id": 'ans1_f25',
                    "answer": 1
                },
                {
                    "question_id": 'ans2_f26',
                    "answer": 1
                },
                {
                    "question_id": 'ans3_f27',
                    "answer": 1
                },
                {
                    "question_id": 'zei1_f28',
                    "answer": 1
                },
                {
                    "question_id": 'zei2_f29',
                    "answer": 1
                },
                {
                    "question_id": 'zei3_f30',
                    "answer": 1
                },
                {
                    "question_id": 'lms1_f31',
                    "answer": 1
                },
                {
                    "question_id": 'lms2_f32',
                    "answer": 1
                },
                {
                    "question_id": 'lms3_f33',
                    "answer": 1
                },
                {
                    "question_id": 'lit1_f34',
                    "answer": 1
                },
                {
                    "question_id": 'lit2_f35',
                    "answer": 1
                },
                {
                    "question_id": 'lit3_f36',
                    "answer": 1
                },
                {
                    "question_id": 'lu1_f37',
                    "answer": 1
                },
                {
                    "question_id": 'lu2_f38',
                    "answer": 1
                },
                {
                    "question_id": 'lu3_f39',
                    "answer": 1
                }
            ]
        },
        1,
        1,
        ['error'],
        400
    ),
    # Wrong number as parameter
    (
        {
            "ils":
            [
                {
                    "question_id": "ar_1_f1",
                    "answer": "a"
                },
                {
                    "question_id": "ar_2_f5",
                    "answer": "a"
                },
                {
                    "question_id": "ar_3_f9",
                    "answer": "a"
                },
                {
                    "question_id": "ar_4_f13",
                    "answer": "a"
                },
                {
                    "question_id": "ar_5_f17",
                    "answer": "a"
                },
                {
                    "question_id": "ar_6_f21",
                    "answer": "a"
                },
                {
                    "question_id": "ar_7_f25",
                    "answer": "a"
                },
                {
                    "question_id": "ar_8_f29",
                    "answer": "a"
                },
                {
                    "question_id": "ar_9_f33",
                    "answer": "a"
                },
                {
                    "question_id": "ar_10_f37",
                    "answer": "a"
                },
                {
                    "question_id": "ar_11_f41",
                    "answer": "a"
                },

                {
                    "question_id": "vv_1_f3",
                    "answer": "a"
                },
                {
                    "question_id": "vv_2_f7",
                    "answer": "a"
                },
                {
                    "question_id": "vv_3_f11",
                    "answer": "a"
                },
                {
                    "question_id": "vv_4_f15",
                    "answer": "a"
                },
                {
                    "question_id": "vv_5_f19",
                    "answer": "a"
                },
                {
                    "question_id": "vv_6_f23",
                    "answer": "a"
                },
                {
                    "question_id": "vv_7_f27",
                    "answer": "a"
                },
                {
                    "question_id": "vv_8_f31",
                    "answer": "a"
                },
                {
                    "question_id": "vv_9_f35",
                    "answer": "a"
                },
                {
                    "question_id": "vv_10_f39",
                    "answer": "a"
                },
                {
                    "question_id": "vv_11_f43",
                    "answer": "a"
                },

                {
                    "question_id": "si_1_f2",
                    "answer": "a"
                },
                {
                    "question_id": "si_2_f6",
                    "answer": "a"
                },
                {
                    "question_id": "si_3_f10",
                    "answer": "a"
                },
                {
                    "question_id": "si_4_f14",
                    "answer": "a"
                },
                {
                    "question_id": "si_5_f18",
                    "answer": "a"
                },
                {
                    "question_id": "si_6_f22",
                    "answer": "a"
                },
                {
                    "question_id": "si_7_f26",
                    "answer": "a"
                },
                {
                    "question_id": "si_8_f30",
                    "answer": "a"
                },
                {
                    "question_id": "si_9_f34",
                    "answer": "a"
                },
                {
                    "question_id": "si_10_f38",
                    "answer": "a"
                },
                {
                    "question_id": "si_11_f42",
                    "answer": "a"
                },

                {
                    "question_id": "sg_1_f4",
                    "answer": "a"
                },
                {
                    "question_id": "sg_2_f8",
                    "answer": "a"
                },
                {
                    "question_id": "sg_3_f12",
                    "answer": "a"
                },
                {
                    "question_id": "sg_4_f16",
                    "answer": "a"
                },
                {
                    "question_id": "sg_5_f20",
                    "answer": "a"
                },
                {
                    "question_id": "sg_6_f24",
                    "answer": "a"
                },
                {
                    "question_id": "sg_7_f28",
                    "answer": "a"
                },
                {
                    "question_id": "sg_8_f32",
                    "answer": "a"
                },
                {
                    "question_id": "sg_9_f36",
                    "answer": "a"
                },
                {
                    "question_id": "sg_10_f40",
                    "answer": "a"
                },
                {
                    "question_id": "sg_11_f44",
                    "answer": "a"
                }
            ],
            "list_k":
            [
                {
                    "question_id": 'org1_f1',
                    "answer": 7
                },
                {
                    "question_id": 'org2_f2',
                    "answer": 1
                },
                {
                    "question_id": 'org3_f3',
                    "answer": 1
                },
                {
                    "question_id": 'ela1_f4',
                    "answer": 1
                },
                {
                    "question_id": 'ela2_f5',
                    "answer": 1
                },
                {
                    "question_id": 'ela3_f6',
                    "answer": 1
                },
                {
                    "question_id": 'krp1_f7',
                    "answer": 1
                },
                {
                    "question_id": 'krp2_f8',
                    "answer": 1
                },
                {
                    "question_id": 'krp3_f9',
                    "answer": 1
                },
                {
                    "question_id": 'wie1_f10',
                    "answer": 1
                },
                {
                    "question_id": 'wie2_f11',
                    "answer": 1
                },
                {
                    "question_id": 'wie3_f12',
                    "answer": 1
                },
                {
                    "question_id": 'zp1_f13',
                    "answer": 1
                },
                {
                    "question_id": 'zp2_f14',
                    "answer": 1
                },
                {
                    "question_id": 'zp3_f15',
                    "answer": 1
                },
                {
                    "question_id": 'kon1_f16',
                    "answer": 1
                },
                {
                    "question_id": 'kon2_f17',
                    "answer": 1
                },
                {
                    "question_id": 'kon3_f18',
                    "answer": 1
                },
                {
                    "question_id": 'reg1_f19',
                    "answer": 1
                },
                {
                    "question_id": 'reg2_f20',
                    "answer": 1
                },
                {
                    "question_id": 'reg3_f21',
                    "answer": 1
                },
                {
                    "question_id": 'auf1_f22',
                    "answer": 1
                },
                {
                    "question_id": 'auf2_f23',
                    "answer": 1
                },
                {
                    "question_id": 'auf3_f24',
                    "answer": 1
                },
                {
                    "question_id": 'ans1_f25',
                    "answer": 1
                },
                {
                    "question_id": 'ans2_f26',
                    "answer": 1
                },
                {
                    "question_id": 'ans3_f27',
                    "answer": 1
                },
                {
                    "question_id": 'zei1_f28',
                    "answer": 1
                },
                {
                    "question_id": 'zei2_f29',
                    "answer": 1
                },
                {
                    "question_id": 'zei3_f30',
                    "answer": 1
                },
                {
                    "question_id": 'lms1_f31',
                    "answer": 1
                },
                {
                    "question_id": 'lms2_f32',
                    "answer": 1
                },
                {
                    "question_id": 'lms3_f33',
                    "answer": 1
                },
                {
                    "question_id": 'lit1_f34',
                    "answer": 1
                },
                {
                    "question_id": 'lit2_f35',
                    "answer": 1
                },
                {
                    "question_id": 'lit3_f36',
                    "answer": 1
                },
                {
                    "question_id": 'lu1_f37',
                    "answer": 1
                },
                {
                    "question_id": 'lu2_f38',
                    "answer": 1
                },
                {
                    "question_id": 'lu3_f39',
                    "answer": 1
                }
            ]
        },
        1,
        1,
        ['error'],
        400
    )
])
def test_post_questionnaire(
    client,
    input,
    student_id,
    moodle_user_id,
    keys_expected,
    status_code_expected
):
    url = "/lms/student/" + str(student_id) + \
        "/" + str(moodle_user_id) + "/questionnaire"
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("input, student_id, moodle_user_id, topic_id, \
                         keys_expected, status_code_expected", [
    # Working Example
    (
        {
            "visit_start_time": "2017-07-21T17:32:28Z",
            "previous_topic_id": 1
        },
        1,
        1,
        1,
        ['visit_start', 'previous_topic_id'],
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
        ['visit_start', 'previous_topic_id'],
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
        ['error'],
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
        ['error'],
        400
    )
])
def test_post_topic_visit(
    client,
    input,
    student_id,
    moodle_user_id,
    topic_id,
    keys_expected,
    status_code_expected
):
    url = "/lms/student/" + str(student_id) + \
        "/" + str(moodle_user_id) + "/topic/" + str(topic_id)
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected


@pytest.mark.parametrize("input, student_id, moodle_user_id, \
                         learning_element_id, keys_expected, \
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
        ['visit_start', 'previous_topic_id'],
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
        ['visit_start', 'previous_topic_id'],
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
        ['error'],
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
        ['error'],
        400
    )
])
def test_post_learning_element_visit(
    client,
    input,
    student_id,
    moodle_user_id,
    learning_element_id,
    keys_expected,
    status_code_expected
):
    url = "/lms/student/" + str(student_id) + \
        "/" + str(moodle_user_id) + "/learning_element/" + \
        str(learning_element_id)
    r = client.post(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
