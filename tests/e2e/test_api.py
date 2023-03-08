import pytest
import errors as err
import json


def test_api_post_course(client):
    data = {"name": "Test Course"}
    r = client.post("/course", json=data)

    assert r.status_code == 201


def test_api_get_frontend_logs(client):
    r = client.get('/logs/frontend')

    assert r.status_code == 200

    logs_expected = {"logs": [{
        "name": "FID",
        "value": 1.900000000372529,
        "rating": "good",
        "delta": 1.900000000372529,
        "entries": [
            {
                "name": "pointerdown",
                "entryType": "first-input",
                "startTime": 1611.5,
                "duration": 8,
                "processingStart": 1613.4000000003725,
                "processingEnd": 1613.4000000003725,
                "cancelable": True
            }
        ],
        "id": "v3-1665130071366-6352791670096",
        "navigationType": "reload"
    }]}
    assert json.loads(r.data.decode("utf-8").strip('\n')) == logs_expected


def test_api_post_frontend_logs(client):
    data = {
        "name": "FID",
        "value": 1.900000000372529,
        "rating": "good",
        "delta": 1.900000000372529,
        "entries": [
            {
                "name": "pointerdown",
                "entryType": "first-input",
                "startTime": 1611.5,
                "duration": 8,
                "processingStart": 1613.4000000003725,
                "processingEnd": 1613.4000000003725,
                "cancelable": True
            }
        ],
        "id": "v3-1665130071366-6352791670096",
        "navigationType": "reload"
    }
    r = client.post("/logs/frontend", json=data)

    assert r.status_code == 201


def test_api_post_frontend_logs_missing_value(client):
    data = {
        "value": 1.900000000372529,
        "rating": "good",
        "delta": 1.900000000372529,
        "entries": [
            {
                "name": "pointerdown",
                "entryType": "first-input",
                "startTime": 1611.5,
                "duration": 8,
                "processingStart": 1613.4000000003725,
                "processingEnd": 1613.4000000003725,
                "cancelable": True
            }
        ],
        "id": "v3-1665130071366-6352791670096",
        "navigationType": "reload"
    }
    r = client.post("/logs/frontend", json=data)

    assert r.status_code == err.MissingParameterError().code
    assert json.loads(r.data.decode("utf-8").strip('\n')) == {
        "error": err.MissingParameterError().description}


def test_api_post_frontend_logs_without_data(client):
    data = {}
    r = client.post("/logs/frontend", json=data)

    assert r.status_code == 400


def test_api_post_frontend_logs_with_wrong_values(client):
    data = {
        "name": "Test",
        "value": 1.900000000372529,
        "rating": "good",
        "delta": 1.900000000372529,
        "entries": [
            {
                "name": "pointerdown",
                "entryType": "first-input",
                "startTime": 1611.5,
                "duration": 8,
                "processingStart": 1613.4000000003725,
                "processingEnd": 1613.4000000003725,
                "cancelable": True
            }
        ],
        "id": "v3-1665130071366-6352791670096",
        "navigationType": "reload"
    }
    r = client.post("/logs/frontend", json=data)

    assert r.status_code == 404
