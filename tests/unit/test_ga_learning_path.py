import domain.tutoringModel.ga as LP
import pytest
import errors as err

learning_elements = ['KÜ', 'LK', 'ZF', 'ÜB', 'AN', 'SE',
                     'RQ', 'AB', 'ZL', 'BE', 'FO', 'LZ']


def test_get_learning_path_correct_result():

    input_learning_style = {'ACT': 1, 'SNS': 3, 'VIS': 7, 'SEQ': 1}
    learning_path_calculated = LP.GA_Algorithmus(student_id=12)

    learning_path1 = ['KÜ', 'LK', 'ZF', 'AN', 'SE', 'ÜB',
                      'AB', 'BE', 'RQ', 'FO', 'ZL', 'LZ']
    learning_path2 = ['KÜ', 'LK', 'ZF', 'AN', 'ÜB', 'SE',
                      'AB', 'BE', 'RQ', 'FO', 'ZL', 'LZ']

    ga_learning_path, List_LPLE = learning_path_calculated.get_learning_path(
        input_learning_style)
    
    condition1 = ga_learning_path == learning_path1
    condition2 = ga_learning_path == learning_path2

    assert (condition2 or condition1)


def test_get_learning_path_with_empty_learning_style():

    learning_path_calculated = LP.GA_Algorithmus(student_id=123)

    learning_path1 = ['KÜ', 'LK', 'ZF', 'AN', 'SE',
                      'ÜB', 'AB', 'BE', 'RQ', 'FO', 'ZL', 'LZ']
    learning_path2 = ['KÜ', 'LK', 'ZF', 'AN', 'ÜB',
                      'SE', 'AB', 'BE', 'RQ', 'FO', 'ZL', 'LZ']

    ga_learning_path, List_LPLE = learning_path_calculated.get_learning_path()
    
    condition1 = ga_learning_path == learning_path1
    condition2 = ga_learning_path == learning_path2
    assert condition1 or condition2


def test_get_learning_path_with_different_size_of_input_learning_style():

    learning_path_calculated = LP.GA_Algorithmus(student_id=123)
    input_learning_style = {"INT": 1, "VIS": 2, "GLO": 3}
    with pytest.raises(err.WrongLearningStyleNumberError):
        learning_path_calculated.get_learning_path(input_learning_style)


def test_get_learning_path_with_out_of_range_input_learning_style_dimension():

    learning_path_calculated = LP.GA_Algorithmus(student_id=123)
    input_learning_style = {"ACT": 15, "INT": 2, "VIS": 11, "GLO": 9}
    with pytest.raises(err.WrongLearningStyleDimensionError):
        learning_path_calculated.get_learning_path(input_learning_style)


def test_get_learning_path_with_different_name_input_learning_style_dimension():

    learning_path_calculated = LP.GA_Algorithmus(student_id=123)
    input_learning_style = {"AKT": 5, "INT": 2, "VIS": 5, "GLOB": 9}
    with pytest.raises(err.WrongLearningStyleDimensionError):
        learning_path_calculated.get_learning_path(input_learning_style)
