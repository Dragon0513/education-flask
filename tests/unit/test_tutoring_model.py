import numpy as np
import pytest

import errors.errors as err
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.tutoringModel import tyche, utils
from domain.tutoringModel.graf import GrafAlgorithm as Graf
from utils import constants as cons

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
                "characteristic_id": 2,
                "perception_dimension": "int",
                "perception_value": 5,
                "input_dimension": "vrb",
                "input_value": 0,
                "processing_dimension": "ref",
                "processing_value": 9,
                "understanding_dimension": "seq",
                "understanding_value": 11,
            }
        ),
        (
            {
                "id": 3,
                "characteristic_id": 4,
                "perception_dimension": "sns",
                "perception_value": 1,
                "input_dimension": "vis",
                "input_value": 11,
                "processing_dimension": "act",
                "processing_value": 1,
                "understanding_dimension": "glo",
                "understanding_value": 3,
            }
        ),
    ],
)
def test_prepare_les_for_tyche(learning_style):
    """Test function for Tyche algorithm with successfull and
    error outcomes.
    """

    # Test Tyche with success:
    list_of_les = []
    list_of_keys = [
        cons.abbreviation_cc,
        cons.abbreviation_ct,
        cons.abbreviation_se,
        cons.abbreviation_as,
        cons.abbreviation_rm,
        cons.abbreviation_an,
        cons.abbreviation_ec,
        cons.abbreviation_co,
        cons.abbreviation_fo,
        cons.abbreviation_ra,
        cons.abbreviation_ex,
    ]
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
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="tyche")

    lp.get_learning_path(
        student_id=1,
        learning_style=learning_style,
        _algorithm="tyche",
        list_of_les=list_of_les,
    )
    erg = False
    result = lp.path
    if not result:
        assert result
    if all(le in result for le in list_of_keys):
        erg = True
    else:
        erg = False
    assert erg

    tyche_alg = tyche.TycheAlgorithm()
    last_element = cons.abbreviation_rq
    tyche_path_success2 = tyche_alg.get_learning_path(
        learning_style, list_of_les, last_element
    )
    print(tyche_path_success2)
    if not tyche_path_success2:
        assert tyche_path_success2
    erg11 = False
    if all(le in tyche_path_success2 for le in list_of_keys):
        erg11 = True
    else:
        erg11 = False
    assert erg11

    list_of_les2 = []
    list_of_keys2 = [
        cons.abbreviation_ct,
        cons.abbreviation_as,
        cons.abbreviation_rm,
        cons.abbreviation_ec,
        cons.abbreviation_fo,
        cons.abbreviation_ra,
        cons.abbreviation_ex,
    ]
    for i, ele_name in enumerate(list_of_keys2):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les2.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="tyche")

    lp.get_learning_path(
        student_id=1,
        learning_style=learning_style,
        _algorithm="tyche",
        list_of_les=list_of_les2,
    )
    result2 = lp.path
    if not result2:
        assert result2
    erg2 = False
    if all(le in result2 for le in list_of_keys2):
        erg2 = True
    else:
        erg2 = False
    assert erg2

    list_of_les3 = []
    list_of_keys3 = [
        cons.abbreviation_cc,
        cons.abbreviation_rq,
        cons.abbreviation_an,
        cons.abbreviation_co,
        cons.abbreviation_ex,
    ]
    for i, ele_name in enumerate(list_of_keys3):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les3.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="tyche")

    lp.get_learning_path(
        student_id=1,
        learning_style=learning_style,
        _algorithm="tyche",
        list_of_les=list_of_les3,
    )
    result3 = lp.path
    if not result3:
        assert result3
    erg3 = False
    if all(le in result3 for le in list_of_keys3):
        erg3 = True
    else:
        erg3 = False
    assert erg3

    list_of_les4 = []
    list_of_keys4 = [
        cons.abbreviation_cc,
        cons.abbreviation_rq,
        cons.abbreviation_an,
        cons.abbreviation_co,
        cons.abbreviation_ex,
    ]
    for i, ele_name in enumerate(list_of_keys4):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les4.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="tyche")

    lp.get_learning_path(
        student_id=1,
        learning_style=learning_style,
        _algorithm="tyche",
        list_of_les=list_of_les4,
    )
    result4 = lp.path
    if not result4:
        assert result4
    erg4 = False
    if all(le in result4 for le in list_of_keys4):
        erg4 = True
    else:
        erg4 = False
    assert erg4

    # Test invalid error parameter for lp algorithm:
    with pytest.raises(err.NoValidAlgorithmError):
        lp.get_learning_path(
            student_id=1,
            learning_style=learning_style,
            _algorithm="foo",
            list_of_les=list_of_les,
        )

    # Test Tyche with errors:
    list_of_les5 = []
    list_of_keys5 = [
        cons.abbreviation_cc,
        cons.abbreviation_ct,
        cons.abbreviation_se,
        cons.abbreviation_as,
        cons.abbreviation_rm,
        cons.abbreviation_an,
        cons.abbreviation_ec,
        cons.abbreviation_co,
        cons.abbreviation_rq,
        cons.abbreviation_fo,
        cons.abbreviation_ra,
        "XX",
    ]
    for i, ele_name in enumerate(list_of_keys5):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les5.append(le.serialize())
    with pytest.raises(err.WrongParameterValueError):
        lp.get_learning_path(
            student_id=1,
            learning_style=learning_style,
            _algorithm="tyche",
            list_of_les=list_of_les5,
        )
    with pytest.raises(err.MissingParameterError):
        tyche_alg.get_learning_path({}, list_of_les, last_element)
    with pytest.raises(err.NoValidParameterValueError):
        tyche_alg.get_learning_path(learning_style, [], last_element)


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
        result = utils.check_learning_style(learning_style)
        assert result


@pytest.mark.parametrize(
    "learning_element, learning_style, expected_result",
    [
        (
            "SE",
            {
                "id": 35,
                "characteristic_id": 35,
                "perception_dimension": "int",
                "perception_value": 7,
                "input_dimension": "vis",
                "input_value": 11,
                "processing_dimension": "act",
                "processing_value": 9,
                "understanding_dimension": "glo",
                "understanding_value": 1,
            },
            9,
        ),
        (
            "ÜB",
            {
                "id": 35,
                "characteristic_id": 35,
                "perception_dimension": "sns",
                "perception_value": 7,
                "input_dimension": "vrb",
                "input_value": 11,
                "processing_dimension": "ref",
                "processing_value": 9,
                "understanding_dimension": "seq",
                "understanding_value": 1,
            },
            -2,
        ),
    ],
)
def test_calculate_variable_score_graf(
    learning_element, learning_style, expected_result
):
    algorithmus = Graf(student_id=1)
    score = algorithmus.calculate_variable_score(learning_element, learning_style)
    assert score == expected_result


def get_learning_path_ga(learning_style, list_of_elements):
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

        result = get_learning_path_ga(learning_style, list_of_elements)
        assert isinstance(result, str)
        assert ", " in result
        result = result.split(", ")
        assert isinstance(result, list)
        print("OUTPUT:", result, "\n")
        if "KÜ" in list_of_elements:
            assert result[0] == "KÜ"
        if "EK" in list_of_elements:
            assert result[0] == "EK" or result[1] == "EK"
        if "LZ" in list_of_elements:
            assert result[-1] == "LZ"


@pytest.mark.parametrize(
    "learning_style, list_of_keys",
    [
        # only 1 Learning element is in the list
        (None, ["BE"]),
        # only 2 Learning elements are in the list
        (None, ["RQ", "EK"]),
        # Test 2
        (None, ["ÜB", "FO", "LZ", "SE", "AN", "KÜ", "EK"]),
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
        ),
    ],
)
def test_prepare_les_for_ga(learning_style, list_of_keys):
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
    result = get_learning_path_ga(learning_style, list_of_keys)

    assert isinstance(result, str)
    if len(result) > 2:
        assert ", " in result
    result = result.split(", ")
    print("Input", list_of_keys)
    print("result", result, "GA")
    assert isinstance(result, list)

    if "KÜ" in list_of_keys:
        assert result[0] == "KÜ"
    if "EK" in list_of_keys:
        assert result[0] == "EK" or result[1] == "EK"
    if "LZ" in list_of_keys:
        assert result[-1] == "LZ"
