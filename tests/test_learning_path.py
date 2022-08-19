import domain.tutoringModel.learning_path as LP
import pytest


def test_get_learning_path_correct_result():
    input_learning_style = {"AKT": 5, "INT": 9, "VIS": 9, "GLO": 9}
    LearningPath = LP.LearningPath()
    learning_path = {
        'ZF': 99, 'UB': 14, 'SE': 5, 'AN': 5,
        'RQ': 4, 'AB': 0, 'ZL': -5, 'BE': -5, 'FO': -13}
    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_2():
    input_learning_style = {"REF": 1, "SNS": 7, "VIS": 5, "SEQ": 5}
    LearningPath = LP.LearningPath()
    learning_path = {
        'AN': 11,  'BE': 8, 'AB': 7, 'SE': 6, 'UB': 6,
        'RQ': 1, 'ZF': 0, 'FO': -6, 'ZL': -11}

    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_3():

    input_learning_style = {"AKT": 3, "SNS": 7, "VIS": 3, "GLO": 3}
    LearningPath = LP.LearningPath()
    learning_path = {'ZF': 99, 'AN': 13, 'SE': 10, 'UB': 10,
                     'AB': 10, 'BE': 7, 'FO': 0, 'RQ': -3, 'ZL': -13}
    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_4():

    input_learning_style = {"AKT": 5, "SNS": 7, "VIS": 7, "GLO": 3}
    LearningPath = LP.LearningPath()
    learning_path = {'ZF': 99, 'AN': 19, 'SE': 12, 'UB': 12,
                     'AB': 10, 'BE': 5, 'FO': -2, 'RQ': -5, 'ZL': -19}
    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_with_empty_learning_style():
    LearningPath = LP.LearningPath()
    learning_path = {'ZF': 0, 'AN': 0, 'SE': 0, 'UB': 0,
                     'AB': 0, 'BE': 0, 'FO': 0, 'RQ': 0, 'ZL': 0}
    assert LearningPath.get_learning_path() == learning_path


def test_get_learning_path_with_different_size_of_input_learning_style():
    LearningPath = LP.LearningPath()
    input_learning_style = {"INT": 9, "VIS": 9, "GLO": 9}
    with pytest.raises(ValueError):
        LearningPath.get_learning_path(input_learning_style)


def test_get_learning_path_with_out_of_Range_input_learning_style_dimension():
    LearningPath = LP.LearningPath()
    input_learning_style = {"AKT": 12, "INT": 2, "VIS": 11, "GLO": 9}
    with pytest.raises(ValueError):
        LearningPath.get_learning_path(input_learning_style)
