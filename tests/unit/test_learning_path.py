import domain.tutoringModel.learning_path as LP
import pytest


def test_get_learning_path_correct_result():
    input_learning_style = {"AKT": 5, "INT": 9, "VIS": 9, "GLO": 9}
    LearningPath = LP.LearningPath()
    learning_path = ['ZF', 'UB', 'SE', 'AN',
                     'RQ', 'AB', 'ZL', 'BE', 'FO']
    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_2():
    input_learning_style = {"REF": 1, "SNS": 7, "VIS": 5, "SEQ": 5}
    LearningPath = LP.LearningPath()
    learning_path = ['AN',  'BE', 'AB', 'SE', 'UB',
                     'RQ', 'ZF', 'FO', 'ZL']
    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_3():

    input_learning_style = {"AKT": 3, "SNS": 7, "VIS": 3, "GLO": 3}
    LearningPath = LP.LearningPath()
    learning_path = ['ZF', 'AN', 'SE', 'UB',
                     'AB', 'BE', 'FO', 'RQ', 'ZL']
    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_correct_result_4():

    input_learning_style = {"AKT": 5, "SNS": 7, "VIS": 7, "GLO": 3}
    LearningPath = LP.LearningPath()
    learning_path = ['ZF', 'AN', 'SE', 'UB',
                     'AB', 'BE', 'FO', 'RQ', 'ZL']
    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_with_empty_learning_style():
    LearningPath = LP.LearningPath()
    learning_path = ['RQ', 'SE', 'FO', 'ZL',
                     'AN', 'UB', 'BE', 'AB', 'ZF']
    assert LearningPath.get_learning_path() == learning_path


def test_get_learning_path_with_different_size_of_input_learning_style():
    LearningPath = LP.LearningPath()
    input_learning_style = {"INT": 9, "VIS": 9, "GLO": 9}
    assert type(LearningPath.get_learning_path(
        input_learning_style)) == ValueError


def test_get_learning_path_with_out_of_Range_input_learning_style_dimension():
    LearningPath = LP.LearningPath()
    input_learning_style = {"AKT": 12, "INT": 2, "VIS": 11, "GLO": 9}
    assert type(LearningPath.get_learning_path(
        input_learning_style)) == ValueError
