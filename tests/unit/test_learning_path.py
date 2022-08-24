import domain.tutoringModel.learning_path as LP
import pytest
import errors as err


def test_get_learning_path_correct_result():
    input_learning_style = {"AKT": 5, "INT": 9, "VIS": 9, "GLO": 9}
    LearningPath = LP.LearningPath(student_id=123)
    learning_path = ['ZF', 'UB', 'SE', 'AN',
                     'RQ', 'AB', 'ZL', 'BE', 'FO']
    assert LearningPath.get_learning_path(
        input_learning_style) == learning_path


def test_get_learning_path_with_empty_learning_style():
    LearningPath = LP.LearningPath(student_id=123)
    learning_path = ['RQ', 'SE', 'FO', 'ZL',
                     'AN', 'UB', 'BE', 'AB', 'ZF']
    assert LearningPath.get_learning_path() == learning_path


def test_get_learning_path_with_different_size_of_input_learning_style():
    LearningPath = LP.LearningPath(student_id=123)
    input_learning_style = {"INT": 9, "VIS": 9, "GLO": 9}
    with pytest.raises(err.WrongLearningStyleNumberError):
        LearningPath.get_learning_path(input_learning_style)


def test_get_learning_path_with_out_of_Range_input_learning_style_dimension():
    LearningPath = LP.LearningPath(student_id=123)
    input_learning_style = {"AKT": 12, "INT": 2, "VIS": 11, "GLO": 9}
    with pytest.raises(err.WrongLearningStyleDimensionError):
        LearningPath.get_learning_path(input_learning_style)
