import pytest
import config
import requests
import errors as err


def test_api_get_learning_path_for_learning_style():
    data = {"studentId": 123, "learningStyle": {
        "AKT": 5, "INT": 9, "VIS": 9, "GLO": 9
    }}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == 200
    learning_path_expected = ['ZF', 'UB', 'SE', 'AN',
                              'RQ', 'AB', 'ZL', 'BE', 'FO']
    assert r.json()['learningPath'] == ', '.join(learning_path_expected)


def test_api_get_learning_path_for_learning_style_without_studentId():
    data = {}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == err.MissingParameterError().code
    assert r.json() == {
        "error": err.MissingParameterError().description}


def test_api_get_learning_path_for_learning_style_without_learningStyle():
    data = {"studentId": 123}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == 200
    learning_path_expected = ['RQ', 'SE', 'FO', 'ZL',
                              'AN', 'UB', 'BE', 'AB', 'ZF']
    assert r.json()['learningPath'] == ', '.join(learning_path_expected)


def test_api_get_learning_path_for_ls_with_wrong_number_of_dimensions():
    data = {"studentId": 123, "learningStyle": {
        "AKT": 5, "INT": 9, "VIS": 9
    }}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == err.WrongLearningStyleNumberError().code
    assert r.json() == {
        "error": err.WrongLearningStyleNumberError().description}


def test_api_get_learning_path_for_ls_with_wrong_number_in_dimension():
    data = {"studentId": 123, "learningStyle": {
        "AKT": 5, "INT": 9, "VIS": 9, "GLO": 12
    }}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == err.WrongLearningStyleDimensionError().code
    assert r.json() == {
        "error": err.WrongLearningStyleDimensionError().description}


def test_api_get_frontend_logs():
    url = config.get_api_url()
    r = requests.get(f"{url}/logs/frontend")

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
    assert r.json() == logs_expected


def test_api_post_frontend_logs():
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
    url = config.get_api_url()
    r = requests.post(f"{url}/logs/frontend", json=data)

    assert r.status_code == 201


def test_api_post_frontend_logs_missing_value():
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
    url = config.get_api_url()
    r = requests.post(f"{url}/logs/frontend", json=data)

    assert r.status_code == err.MissingParameterError().code
    assert r.json() == {
        "error": err.MissingParameterError().description}


def test_api_post_frontend_logs_without_data():
    data = {}
    url = config.get_api_url()
    r = requests.post(f"{url}/logs/frontend", json=data)

    assert r.status_code == 404


def test_api_post_frontend_logs_with_wrong_values():
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
    url = config.get_api_url()
    r = requests.post(f"{url}/logs/frontend", json=data)

    assert r.status_code == 404
