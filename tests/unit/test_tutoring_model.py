import pytest

import errors.errors as err
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.tutoringModel import utils


def test_prepare_les_for_aco():
    list_of_les = []
    list_of_keys = ["BE", "FO", "KÜ", "SE", "LZ", "EK", "ÜB"]
    for i, key in enumerate(list_of_keys):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=key,
            name="Test",
            university="TH-AB",
            created_by=i,
            created_at="2023-01-01",
        )
        list_of_les.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="aco")
    result = lp.prepare_le_for_aco(list_of_les=list_of_les)
    assert type(result) == list
    assert len(result) != 0
    assert result[0] == "KÜ"
    assert result[-1] == "LZ"


def test_distance():
    result = utils.distance((1, 1, 1, 1), (2, 2, 2, 2))
    assert type(result) == float
    assert result == 2


@pytest.mark.parametrize(
    "input_dimension, perception_dimension,\
                         processing_dimension, understanding_dimension",
    [("vis", "sns", "act", "glo"), ("vrb", "int", "ref", "seq")],
)
def test_get_coordinates(
    input_dimension, perception_dimension, processing_dimension, understanding_dimension
):
    ls = LM.LearningStyle(
        input_dimension=input_dimension,
        input_value=7,
        perception_dimension=perception_dimension,
        perception_value=7,
        processing_dimension=processing_dimension,
        processing_value=7,
        understanding_dimension=understanding_dimension,
        understanding_value=7,
    )
    list_of_les = ["BE", "FO", "KÜ", "SE", "LZ", "EK", "ÜB", "ZF"]
    result = utils.get_coordinates(
        learning_style=ls.serialize(), list_of_les=list_of_les
    )
    assert type(result) == dict
    assert result is not None
    assert result["KÜ"] == (13, 13, 13, 13)
    assert result["EK"] == (12, 12, 12, 12)
    assert result["LZ"] == (-12, -12, -12, -12)


@pytest.mark.parametrize(
    "learning_style",
    [
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 5,
                "input_dimension": "vrb",
                "input_value": 0,
                "processing_dimension": "act",
                "processing_value": 9,
                "understanding_dimension": "seq",
                "understanding_value": 11,
            }
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 1,
                "input_dimension": "vis",
                "input_value": 11,
                "processing_dimension": "ref",
                "processing_value": 1,
                "understanding_dimension": "glo",
                "understanding_value": 3,
            }
        ),
    ],
)
def test_prepare_les_for_ga(learning_style):
    list_of_les = []
    list_of_keys = ["ZF", "KÜ", "SE", "LZ", "ZL", "AN", "ÜB", "EK"]
    for i, ele_name in enumerate(list_of_keys):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="ga")
    lp.get_learning_path(
        student_id=1,
        learning_style=learning_style,
        _algorithm="ga",
        list_of_les=list_of_les,
    )
    result = lp.path
    assert isinstance(result, str)
    assert ", " in result
    result = result.split(", ")
    assert isinstance(result, list)
    assert result[0] == "KÜ"
    assert result[1] == "EK"
    assert result[-1] == "LZ"


@pytest.mark.parametrize(
    "learning_style",
    [
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 15,
                "input_dimension": "vrb",
                "input_value": 20,
                "processing_dimension": "act",
                "processing_value": 5,
                "understanding_dimension": "seq",
                "understanding_value": 13,
            }
        )
    ],
)
def test_with_out_of_range_learning_style_for_ga(learning_style):
    list_of_les = []
    list_of_keys = ["ZF", "KÜ", "SE", "LZ", "ZL", "ÜB", "AB", "EK"]
    for i, ele_name in enumerate(list_of_keys):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="ga")
    with pytest.raises(err.WrongLearningStyleDimensionError):
        lp.get_learning_path(
            student_id=1,
            learning_style=learning_style,
            _algorithm="ga",
            list_of_les=list_of_les,
        )


@pytest.mark.parametrize(
    "learning_style, error",
    [
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 7,
                "input_dimension": "vrb",
                "input_value": 11,
                "processing_dimension": "act",
                "processing_value": 5,
                "understanding_dimension": "seq",
                "understanding_value": 7,
            },
            None,
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 7,
                "input_dimension": "vis",
                "input_value": 11,
                "processing_dimension": "ref",
                "processing_value": 5,
                "understanding_dimension": "glo",
                "understanding_value": 7,
            },
            None,
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 15,
                "input_dimension": "vis",
                "input_value": 20,
                "processing_dimension": "ref",
                "processing_value": 5,
                "understanding_dimension": "glo",
                "understanding_value": 13,
            },
            "dimension",
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 15,
                "input_dimension": "vis",
                "input_value": 20,
                "processing_dimension": "ref",
                "processing_value": 5,
            },
            "number",
        ),
    ],
)
def test_learning_style_check(learning_style, error):
    if error == "dimension":
        with pytest.raises(err.WrongLearningStyleDimensionError):
            utils.check_learning_style(learning_style)
    elif error == "number":
        with pytest.raises(err.WrongLearningStyleNumberError):
            utils.check_learning_style(learning_style)
    else:
        assert True
