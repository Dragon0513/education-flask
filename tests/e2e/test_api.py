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
