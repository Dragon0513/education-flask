import pytest
import config
import requests


def test_api_get_learning_path_for_learning_style():
    # input_learning_style = {"AKT": 5, "INT": 9, "VIS": 9, "GLO": 9}
    data = {"studentId": 123, "learningStyle": {
        "AKT": 5,
        "INT": 9,
        "VIS": 9,
        "GLO": 9
    }}
    url = config.get_api_url()
    r = requests.get(f"{url}/learningPath", json=data)

    assert r.status_code == 200
    learning_path_expected = {
        'ZF': 99, 'UB': 14, 'SE': 5, 'AN': 5,
        'RQ': 4, 'AB': 0, 'ZL': -5, 'BE': -5, 'FO': -13}
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
    learning_path_expected = {'ZF': 0, 'AN': 0, 'SE': 0, 'UB': 0,
                              'AB': 0, 'BE': 0, 'FO': 0, 'RQ': 0, 'ZL': 0}
    assert r.json()['learningPath'] == learning_path_expected
