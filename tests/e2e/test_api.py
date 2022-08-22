import pytest
import config
import requests


def test_api_get_learning_path_for_learning_style():
    data = {"studentId": 123, "learningStyle": {
        "AKT": 5, "INT": 9, "VIS": 9, "GLO": 9
    }}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == 200
    learning_path_expected = ['ZF', 'UB', 'SE', 'AN',
                              'RQ', 'AB', 'ZL', 'BE', 'FO']
    assert r.json()['learningPath'] == learning_path_expected


def test_api_get_learning_path_for_learning_style_without_studentId():
    data = {}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == 404
    assert r.json() == {}


def test_api_get_learning_path_for_learning_style_without_learningStyle():
    data = {"studentId": 123}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == 200
    learning_path_expected = ['RQ', 'SE', 'FO', 'ZL',
                              'AN', 'UB', 'BE', 'AB', 'ZF']
    assert r.json()['learningPath'] == learning_path_expected
