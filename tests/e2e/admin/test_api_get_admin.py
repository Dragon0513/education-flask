# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
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
                    "created_by": "Maria Musterfrau",
                    "created_at": "2017-07-21T17:32:28Z",
                    "last_updated": "2017-07-21T17:32:28Z",
                    "university": "TH-AB"
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
def test_api_get_courses_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/course"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [
            {
                "name": "Maria Musterfrau",
                "role": "Student",
                "university": "TH-AB"
            }
        ],
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
def test_api_get_users_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/user"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        {
            "access_logs": [
                {
                    "time": "2017-07-21T17:32:28Z",
                    "user": "Max Mustermann",
                    "session_id": "1a2b3c4d",
                    "message": "Accessed was Endpoint xyz."
                }
            ],
            "frontend_logs": [
                {
                    "name": "FCP",
                    "value": 3957.6999999284744,
                    "rating": "poor",
                    "delta": 3957.6999999284744,
                    "entries": [
                        {
                            "name": "first-contentful-paint",
                            "entryType": "paint",
                            "startTime": 3957.6999999284744,
                            "duration": 0
                        },
                        {
                            "name": "http://localhost:8080/",
                            "entryType": "navigation",
                            "startTime": 0,
                            "duration": 4003.0999999046326,
                            "initiatorType": "navigation",
                            "nextHopProtocol": "http/1.1",
                            "workerStart": 0,
                            "redirectStart": 0,
                            "redirectEnd": 0,
                            "fetchStart": 7.699999928474426,
                            "domainLookupStart": 99.19999992847443,
                            "domainLookupEnd": 99.29999995231628,
                            "connectStart": 99.29999995231628,
                            "connectEnd": 99.89999997615814,
                            "secureConnectionStart": "0,",
                            "requestStart": 100,
                            "responseStart": 3638.7999999523163,
                            "responseEnd": 3640,
                            "transferSize": 810,
                            "encodedBodySize": 510,
                            "decodedBodySize": 510,
                            "serverTiming": [
                                ""
                            ],
                            "workerTiming": [
                                ""
                            ],
                            "unloadEventStart": 0,
                            "unloadEventEnd": 0,
                            "domInteractive": 3717.5,
                            "domContentLoadedEventStart": 3937.5999999046326,
                            "domContentLoadedEventEnd": 3938.899999976158,
                            "domComplete": 4003.0999999046326,
                            "loadEventStart": 4003.0999999046326,
                            "loadEventEnd": 4003.0999999046326,
                            "type": "navigate",
                            "redirectCount": 0
                        },
                        {},
                        {
                            "name": "",
                            "entryType": "largest-contentful-paint",
                            "startTime": 3957.699,
                            "duration": 0,
                            "size": 867,
                            "renderTime": 3957.699,
                            "loadTime": 0,
                            "firstAnimatedFrameTime": 0,
                            "id": "",
                            "url": ""
                        },
                        {},
                        {}
                    ],
                    "id": "v3-1665068191217-4248786867866",
                    "navigationType": "navigate"
                }
            ],
            "main_logs": [
                {
                    "time": "2017-07-21T17:32:28Z",
                    "session_id": "1a2b3c4d",
                    "message": "Calculation of new learning Path"
                }
            ],
            "error_logs": [
                {
                    "time": "2017-07-21T17:32:28Z",
                    "session_id": "1a2b3c4d",
                    "message": "Error on updating the learner model."
                }
            ],
            "system_logs": [
                {
                    "time": "2017-07-21T17:32:28Z",
                    "message": "System is up and running."
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
def test_api_get_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/logs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [
            {
                "time": "2017-07-21T17:32:28Z",
                "user": "Max Mustermann",
                "session_id": "1a2b3c4d",
                "message": "Accessed was Endpoint xyz."
            }
        ],
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
def test_api_get_access_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/accessLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [
            {
                "name": "FCP",
                "value": 3957.6999999284744,
                "rating": "poor",
                "delta": 3957.6999999284744,
                "entries": [
                    {
                        "name": "first-contentful-paint",
                        "entryType": "paint",
                        "startTime": 3957.6999999284744,
                        "duration": 0
                    },
                    {
                        "name": "http://localhost:8080/",
                        "entryType": "navigation",
                        "startTime": 0,
                        "duration": 4003.0999999046326,
                        "initiatorType": "navigation",
                        "nextHopProtocol": "http/1.1",
                        "workerStart": 0,
                        "redirectStart": 0,
                        "redirectEnd": 0,
                        "fetchStart": 7.699999928474426,
                        "domainLookupStart": 99.19999992847443,
                        "domainLookupEnd": 99.29999995231628,
                        "connectStart": 99.29999995231628,
                        "connectEnd": 99.89999997615814,
                        "secureConnectionStart": "0,",
                        "requestStart": 100,
                        "responseStart": 3638.7999999523163,
                        "responseEnd": 3640,
                        "transferSize": 810,
                        "encodedBodySize": 510,
                        "decodedBodySize": 510,
                        "serverTiming": [
                            ""
                        ],
                        "workerTiming": [
                            ""
                        ],
                        "unloadEventStart": 0,
                        "unloadEventEnd": 0,
                        "domInteractive": 3717.5,
                        "domContentLoadedEventStart": 3937.5999999046326,
                        "domContentLoadedEventEnd": 3938.899999976158,
                        "domComplete": 4003.0999999046326,
                        "loadEventStart": 4003.0999999046326,
                        "loadEventEnd": 4003.0999999046326,
                        "type": "navigate",
                        "redirectCount": 0
                    },
                    {},
                    {
                        "name": "",
                        "entryType": "largest-contentful-paint",
                        "startTime": 3957.699,
                        "duration": 0,
                        "size": 867,
                        "renderTime": 3957.699,
                        "loadTime": 0,
                        "firstAnimatedFrameTime": 0,
                        "id": "",
                        "url": ""
                    },
                    {},
                    {}
                ],
                "id": "v3-1665068191217-4248786867866",
                "navigationType": "navigate"
            }
        ],
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
def test_api_get_frontend_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/frontendLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [
            {
                "time": "2017-07-21T17:32:28Z",
                "session_id": "1a2b3c4d",
                "message": "Calculation of new learning Path"
            }
        ],
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
def test_api_get_main_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/mainLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [
            {
                "time": "2017-07-21T17:32:28Z",
                "session_id": "1a2b3c4d",
                "message": "Error on updating the learner model."
            }
        ],
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
def test_api_get_error_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/errorLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected


@pytest.mark.parametrize("user_id, lms_user_id, admin_id,\
                         output_expected, status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        [
            {
                "time": "2017-07-21T17:32:28Z",
                "message": "System is up and running."
            }
        ],
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
def test_api_get_system_logs_by_admin_id(
    client,
    user_id,
    lms_user_id,
    admin_id,
    output_expected,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/admin/" + str(admin_id) + "/systemLogs"
    r = client.get(url)
    assert r.status_code == status_code_expected
    assert json.loads(r.data.decode("utf-8").strip('\n')) == output_expected
