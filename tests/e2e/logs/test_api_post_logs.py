# Tests for post methods
import pytest
import json


@pytest.mark.parametrize("input, keys_expected, status_code_expected", [
    # Working Example
    (
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
        },
        ['name', 'value', 'rating', 'delta', 'entries',\
         'id', 'navigationType'],
        201
    )
])
def test_api_post_frontend_logs(
    client,
    input,
    keys_expected,
    status_code_expected
):
    url = "/logs/frontend"
    r = client.get(url, json=input)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    for key in response.keys():
        assert key in keys_expected
