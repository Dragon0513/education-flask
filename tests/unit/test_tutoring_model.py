import numpy as np
import pytest

import errors.errors as err
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.tutoringModel import utils

rng = np.random.default_rng(20)


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
    list_of_les = ["BE", "FO", "KÜ", "SE", "LZ", "EK", "ÜB", "ZF", "ÜB"]
    result = utils.get_coordinates(
        learning_style=ls.serialize(), list_of_les=list_of_les
    )
    assert type(result) == dict
    assert result is not None
    assert result["KÜ"] == (13, 13, 13, 13)
    assert result["EK"] == (12, 12, 12, 12)
    assert result["LZ"] == (-12, -12, -12, -12)


@pytest.mark.parametrize(
    "learning_style,error",
    [
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 15,
                "input_dimension": "vrb",
                "input_value": -20,
                "processing_dimension": "act",
                "processing_value": -50,
                "understanding_dimension": "seq",
                "understanding_value": -13,
            },
            "dimension",
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "input_dimension": "vrb",
                "input_value": 15,
                "processing_dimension": "act",
                "processing_value": -50,
                "understanding_dimension": "seq",
                "understanding_value": -13,
            },
            "number",
        ),
    ],
)
def test_with_out_of_range_learning_style_for_ga(learning_style, error):
    list_of_elements = ["ZF", "KÜ", "SE", "LZ", "ZL", "ÜB", "AB", "EK"]
    if error == "dimension":
        with pytest.raises(err.WrongLearningStyleDimensionError):
            get_learning_pad_ga(learning_style, list_of_elements)
    elif error == "number":
        with pytest.raises(err.WrongLearningStyleNumberError):
            utils.check_learning_style(learning_style)


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
        result = utils.check_learning_style(learning_style)
        assert result


@pytest.mark.parametrize(
    "learning_style, list_of_elements",
    [
        (
            {
                "id": 1,
                "characteristic_id": 11,
                "perception_dimension": "int",
                "perception_value": 5,
                "input_dimension": "vis",
                "input_value": 9,
                "processing_dimension": "ref",
                "processing_value": 5,
                "understanding_dimension": "glo",
                "understanding_value": 9,
            },
            ["FOO", "%$&", "=?&%"],
        ),
    ],
)
def test_learning_element_check(learning_style, list_of_elements):
    with pytest.raises(err.NoValidParameterValueError):
        get_learning_pad_ga(learning_style, list_of_elements)


def get_learning_pad_ga(learning_style, list_of_elements):
    list_of_les = []
    for i, ele_name in enumerate(list_of_elements):
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
    return lp.path


@pytest.mark.parametrize(
    "learning_style, list_of_keys",
    [
        (
            {
                "id": 1,
                "characteristic_id": 11,
                "perception_dimension": "int",
                "perception_value": 5,
                "input_dimension": "vis",
                "input_value": 9,
                "processing_dimension": "ref",
                "processing_value": 5,
                "understanding_dimension": "glo",
                "understanding_value": 9,
            },
            np.array(
                [
                    "ZF",
                    "LZ",
                    "ÜB",
                    "ÜB",
                    "ÜB",
                    "SE",
                    "BE",
                    "AN",
                    "EK",
                    "EK",
                    "EK",
                    "ZL",
                    "AB",
                    "KÜ",
                    "FO",
                    "RQ",
                    "LZ",
                    "FOO",
                    "FOO",
                    "",
                    "None",
                    "$%/==+",
                ],
            ),
        ),
    ],
)
def test_prepare_les_for_ga_2(learning_style, list_of_keys):
    num_of_test = 10
    list_of_le_size = rng.integers(2, 50, size=num_of_test)

    for i in range(num_of_test):
        le_position = rng.integers(2, len(list_of_keys), size=list_of_le_size[i])
        list_of_elements = list_of_keys[le_position]
        list_of_elements = rng.permutation(list_of_elements)

        result = get_learning_pad_ga(learning_style, list_of_elements)
        assert isinstance(result, str)
        assert ", " in result
        result = result.split(", ")
        assert isinstance(result, list)
        print("OUTPUT:", result, "\n")
        if "KÜ" in list_of_elements:
            assert result[0] == "KÜ" or result[1] == "KÜ"
        if "EK" in list_of_elements:
            assert result[0] == "EK" or result[1] == "EK"
        if "LZ" in list_of_elements:
            assert result[-1] == "LZ"


@pytest.mark.parametrize(
    "learning_style, list_of_keys, expected_keys",
    [
        (None, ["BE"], None),
        # only 1 Learning element is in the list
        (None, ["BE"], None),
        # only 2 Learning elements are in the list
        (None, ["RQ", "EK"], ["EK", "RQ"]),
        # Test 2
        (
            None,
            ["ÜB", "FO", "LZ", "SE", "AN", "KÜ", "EK"],
            ["KÜ", "EK", "ÜB", "SE", "AN", "FO", "LZ"],
        ),
        # all learning elements are only once in the list
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 7,
                "input_dimension": "vis",
                "input_value": 9,
                "processing_dimension": "ref",
                "processing_value": 5,
                "understanding_dimension": "glo",
                "understanding_value": 9,
            },
            ["ZF", "LZ", "ÜB", "SE", "BE", "AN", "EK", "ZL", "AB", "KÜ", "FO", "RQ"],
            ["KÜ", "EK", "ZF", "RQ", "ZL", "BE", "AB", "FO", "AN", "SE", "ÜB", "LZ"],
        ),
        #  all learning elements are only once, except 1 is multiple times in the list
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 9,
                "input_dimension": "vrb",
                "input_value": 11,
                "processing_dimension": "act",
                "processing_value": 5,
                "understanding_dimension": "seq",
                "understanding_value": 11,
            },
            [
                "ÜB",
                "ÜB",
                "ÜB",
                "ÜB",
                "ÜB",
                "ÜB",
                "ÜB",
                "ÜB",
                "SE",
                "LZ",
                "ZL",
                "KÜ",
                "AN",
                "EK",
                "RQ",
                "FO",
            ],
            ["KÜ", "EK", "FO", "AN", "SE", "ÜB", "RQ", "ZL", "LZ"],
        ),
        #  all learning elements are multiple times in a list
        (
            {
                "id": 1,
                "characteristic_id": 7,
                "perception_dimension": "int",
                "perception_value": 9,
                "input_dimension": "vis",
                "input_value": 11,
                "processing_dimension": "ref",
                "processing_value": 1,
                "understanding_dimension": "glo",
                "understanding_value": 5,
            },
            [
                "ÜB",
                "ÜB",
                "LZ",
                "LZ",
                "ZF",
                "ZF",
                "SE",
                "SE",
                "ZL",
                "ZL",
                "EK",
                "EK",
                "AN",
                "AN",
                "KÜ",
                "KÜ",
                "FO",
                "FO",
                "RQ",
                "RQ",
                "AB",
                "AB",
                "BE",
                "BE",
            ],
            ["EK", "ZF", "KÜ", "AN", "BE", "AB", "RQ", "ÜB", "ZL", "SE", "FO", "LZ"],
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 3,
                "input_dimension": "vis",
                "input_value": 5,
                "processing_dimension": "ref",
                "processing_value": 7,
                "understanding_dimension": "glo",
                "understanding_value": 1,
            },
            [
                "ÜB",
                "ÜB",
                "ÜB",
                "AB",
                "AB",
                "ÜB",
                "ÜB",
                "ÜB",
                "LZ",
                "LZ",
                "SE",
                "BE",
                "AN",
                "EK",
                "KÜ",
                "ZL",
                "AB",
                "ZF",
            ],
            ["KÜ", "EK", "ZF", "ZL", "BE", "AB", "AN", "SE", "ÜB", "LZ"],
        ),
        # all learning element are in the list, except
        # there is one with an unknown abreviation for example "ZZ"
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 5,
                "input_dimension": "vis",
                "input_value": 9,
                "processing_dimension": "act",
                "processing_value": 3,
                "understanding_dimension": "seq",
                "understanding_value": 5,
            },
            [
                "ZT",
                "WW",
                "ÜB",
                "se",
                "BE",
                "AN",
                "SE",
                "EK",
                "SE",
                "ZZ",
                "AB",
                "KÜ",
                "FO",
                "RQ",
                "SE",
            ],
            ["KÜ", "EK", "AN", "SE", "ÜB", "AB", "BE", "RQ", "FO"],
        ),
    ],
)
def test_prepare_les_for_ga(learning_style, list_of_keys, expected_keys):
    if learning_style is None:
        learning_style = {
            "id": 1,
            "characteristic_id": 1,
            "perception_dimension": "int",
            "perception_value": 11,
            "input_dimension": "vis",
            "input_value": 3,
            "processing_dimension": "ref",
            "processing_value": 7,
            "understanding_dimension": "glo",
            "understanding_value": 9,
        }
    result = get_learning_pad_ga(learning_style, list_of_keys)

    assert isinstance(result, str)
    if len(result) > 2:
        assert ", " in result
    result = result.split(", ")
    print("Input", list_of_keys)
    print("result", result, "GA")
    assert isinstance(result, list)

    if "KÜ" in list_of_keys:
        assert result[0] == "KÜ" or result[1] == "KÜ"
    if "EK" in list_of_keys:
        assert result[0] == "EK" or result[1] == "EK"
    if "LZ" in list_of_keys:
        assert result[-1] == "LZ" or result[-2] == "LZ"
