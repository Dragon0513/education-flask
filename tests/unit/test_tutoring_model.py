import pytest

import errors.errors as err
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.tutoringModel import tyche, utils
from domain.tutoringModel.graf import GrafAlgorithm as Graf


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
    # Test Tyche with success:
    list_of_les = []
    list_of_keys = [
        "ZF",
        "KÜ",
        "SE",
        "LZ",
        "ZL",
        "AN",
        "ÜB",
        "EK",
        "FO",
        "AB",
        "BE",
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
    result = lp.path
    erg = False
    if all(le in result for le in list_of_keys):
        erg = True
    assert erg

    tyche_alg = tyche.TycheAlgorithm()
    last_element = "RQ"
    tyche_path_success2 = tyche_alg.get_learning_path(
        learning_style, list_of_les, last_element
    )
    print(tyche_path_success2)
    erg11 = False
    if all(le in tyche_path_success2 for le in list_of_keys):
        erg11 = True
    assert erg11

    list_of_les2 = []
    list_of_keys2 = [
        "KÜ",
        "LZ",
        "ZL",
        "ÜB",
        "FO",
        "AB",
        "BE",
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
    erg2 = False
    if all(le in result2 for le in list_of_keys2):
        erg2 = True
    assert erg2

    list_of_les3 = []
    list_of_keys3 = [
        "ZF",
        "RQ",
        "AN",
        "EK",
        "BE",
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
    erg3 = False
    if all(le in result3 for le in list_of_keys3):
        erg3 = True
    assert erg3

    list_of_les4 = []
    list_of_keys4 = [
        "ZF",
        "RQ",
        "AN",
        "EK",
        "BE",
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
    erg4 = False
    if all(le in result4 for le in list_of_keys4):
        erg4 = True
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
        "ZF",
        "KÜ",
        "SE",
        "LZ",
        "ZL",
        "AN",
        "ÜB",
        "EK",
        "RQ",
        "FO",
        "AB",
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
