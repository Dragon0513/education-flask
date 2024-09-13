import unittest
from datetime import datetime

from domain.learnersModel import basic_ils_algorithm as BILSA
from domain.learnersModel import basic_listk_algorithm as BLKA
from domain.learnersModel import model as LM


class TestBasicQuestionnaireAlgorithms(unittest.TestCase):
    def test_basic_ils_algorithm(self):
        ils_input = {"vv_1_f3": "a", "vv_2_f7": "a", "vv_3_f12": "b", "vv_4_f13": "a"}
        ils_perception = {
            "si_1_f2": "a",
            "si_2_f6": "a",
            "si_3_f11": "b",
            "si_4_f15": "a",
        }
        ils_procession = {
            "ar_1_f1": "a",
            "ar_2_f5": "a",
            "ar_3_f10": "b",
            "ar_4_f14": "a",
        }
        ils_understanding = {
            "sg_1_f4": "a",
            "sg_2_f8": "a",
            "sg_3_f9": "b",
            "sg_4_f16": "a",
        }

        value = BILSA.calculate_basic_learning_style(
            ils_input, ils_perception, ils_procession, ils_understanding
        )
        assert value == (("vis", 2), ("sns", 2), ("act", 2), ("seq", 2))

    def test_basic_listk_algorithm(self):
        list_k_answers = {
            "org1_f1": 1,
            "org2_f2": 2,
            "org3_f3": 3,
            "elab1_f4": 4,
            "elab2_f5": 5,
            "elab3_f6": 1,
            "crit_rev1_f7": 2,
            "crit_rev2_f8": 3,
            "crit_rev3_f9": 4,
            "rep1_f10": 5,
            "rep2_f11": 1,
            "rep3_f12": 2,
            "goal_plan1_f13": 3,
            "goal_plan2_f14": 4,
            "goal_plan3_f15": 5,
            "con1_f16": 1,
            "con2_f17": 2,
            "con3_f18": 3,
            "reg1_f19": 4,
            "reg2_f20": 5,
            "reg3_f21": 1,
            "att1_f22": 5,
            "att2_f23": 3,
            "att3_f24": 5,
            "eff1_f25": 5,
            "eff2_f26": 1,
            "eff3_f27": 2,
            "time1_f28": 3,
            "time2_f29": 4,
            "time3_f30": 5,
            "lrn_w_cls1_f31": 1,
            "lrn_w_cls2_f32": 2,
            "lrn_w_cls3_f33": 3,
            "lit_res1_f34": 4,
            "lit_res2_f35": 5,
            "lit_res3_f36": 1,
            "lrn_env1_f37": 2,
            "lrn_env2_f38": 3,
            "lrn_env3_f39": 4,
        }

        value = BLKA.calculate_basic_learning_strategy(list_k_answers)
        assert value == (
            (2.0, 3.33, 3.0, 2.67, 2.75),
            (2.67, 2.0, 3.33, 2.67),
            (1.67, 2.67, 4.0, 2.78),
            (2.0, 3.33, 3.0, 2.78),
        )


def test_calculate_student_rating():
    student_rating = LM.StudentRating(
        1, 1, datetime.fromisoformat("2023-01-01 16:00"), None, None
    )
    serialized_student_rating = student_rating.serialize()
    assert serialized_student_rating["rating_value"] == 1500
    assert serialized_student_rating["rating_deviation"] == 350

    student_rating_2 = LM.StudentRating(
        2, 1, datetime.fromisoformat("2023-01-01 16:00"), 1500, 350
    )
    result = student_rating_2.calculate_updated_rating(
        attempt_timestamp=datetime.fromisoformat("2023-01-01 16:00"),
        attempt_result=True,
        learning_element_id=1,
        learning_element_rating_value=1500,
        learning_element_rating_deviation=350,
        learning_element_rating_timestamp=datetime.fromisoformat("2023-01-01 16:00"),
    )

    assert result == {
        "value": 1629.7696020846117,
        "deviation": 290.2305060910912,
        "timestamp": datetime.fromisoformat("2023-01-01 16:00"),
    }
