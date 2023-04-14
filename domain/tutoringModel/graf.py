from domain.tutoringModel import model as tutoringModel
from domain.tutoringModel import util
from datetime import datetime
import errors as err


class GrafAlgorithm:

    # Learning Element Types: (+) = 1 and (-) = 0
    learning_style_rq = {"AKT": 0, "REF": 1, "INT": 1}
    learning_style_se = {"AKT": 1, "REF": 0, "SNS": 1}
    learning_style_fo = {"AKT": 1, "REF": 0, "INT": 0, "VIS": 0, "VRB": 1}
    learning_style_zl = {"AKT": 0, "REF": 1,
                         "SNS": 0, "INT": 1, "VIS": 0, "VRB": 1}
    learning_style_an = {"AKT": 1, "REF": 0,
                         "SNS": 1, "INT": 0, "VIS": 1, "VRB": 0}
    learning_style_ub = {"AKT": 1, "REF": 0, "SNS": 1, "INT": 1}
    learning_style_be = {"AKT": 0, "REF": 1, "SNS": 1, "INT": 0, "GLO": 1}
    learning_style_ab = {"SNS": 1, "INT": 0, "GLO": 1}
    learning_style_zf = {"REF": 1, "GLO": 1}

    def __init__(self,
                 student_id,
                 learning_path=None,
                 learning_style={"AKT": 0, "INT": 0, "VIS": 0, "GLO": 0},
                 dict_Learning_element=None,
                 id=None):
        if id is None:
            self.id = datetime.timestamp(datetime.now())
        else:
            self.id = id
        self.student_id = student_id

        if learning_path is None:
            self.learning_path = None#self.get_learning_path(learning_style)
        else:
            self.learning_path = learning_path

        if dict_Learning_element is None:
            self.dict_Learning_element = util.get_dict_Learning_element()
        else:
            self.dict_Learning_element = dict_Learning_element

    def check_learning_style(self, input_learning_style):
        is_correct = False

        for iterator in input_learning_style:
            if (input_learning_style.get(iterator)):

                dimension_number = input_learning_style.get(iterator)
                if (dimension_number < 0 or dimension_number > 11):
                    is_correct = True
                    break
        return is_correct

    def special_case_zf(self, input_learning_style):
        # Validates ZF learning elements
        result = 0
        reflective = input_learning_style.get("REF")
        sequential = input_learning_style.get("SEQ")
        style_global = input_learning_style.get("GLO")

        condition1 = reflective and sequential
        condition2 = condition1 and reflective > sequential
        condition3 = (reflective and not sequential) or style_global

        if (condition2 or condition3):
            result = 99

        return result

    def calculate_sequence(self, learning_element_types, input_learning_style):

        graf_value = 0
        learning_style = 0

        for learning_style, value in learning_element_types.items():
            if (input_learning_style.get(learning_style)):
                learning_style = input_learning_style.get(learning_style)

                if (value == 0):
                    learning_style *= -1

                graf_value += learning_style

        return graf_value

    def sort_learning_path(self, learning_path):
        sort_learning_path = []

        for _ in range(len(learning_path)):
            highest_item = max(learning_path, key=learning_path.get)
            sort_learning_path.append(highest_item)
            del learning_path[highest_item]
        return sort_learning_path

    def get_learning_path(self, input_learning_style={"AKT": 0, "INT": 0,
                                                      "VIS": 0, "GLO": 0},
                          dict_Learning_element=None,
                          unit_test=False):
        if (len(input_learning_style) != 4):
            raise err.WrongLearningStyleNumberError()

        if self.check_learning_style(input_learning_style):
            raise err.WrongLearningStyleDimensionError()

        learning_path = {}

        learning_path["RQ"] = self.calculate_sequence(
            self.learning_style_rq, input_learning_style)
        learning_path["SE"] = self.calculate_sequence(
            self.learning_style_se, input_learning_style)
        learning_path["FO"] = self.calculate_sequence(
            self.learning_style_fo, input_learning_style)
        learning_path["ZL"] = self.calculate_sequence(
            self.learning_style_zl, input_learning_style)
        learning_path["AN"] = self.calculate_sequence(
            self.learning_style_an, input_learning_style)
        learning_path["UB"] = self.calculate_sequence(
            self.learning_style_ub, input_learning_style)
        learning_path["BE"] = self.calculate_sequence(
            self.learning_style_be, input_learning_style)
        learning_path["AB"] = self.calculate_sequence(
            self.learning_style_ab, input_learning_style)
        learning_path["ZF"] = self.special_case_zf(input_learning_style)

        learning_path = self.sort_learning_path(learning_path)
        

        Learning_Path_id = self.id
        List_LPLE = util.get_list_LPLE(learning_path,
                                       dict_Learning_element,
                                       Learning_Path_id)

        #print(learning_path)
        return learning_path, List_LPLE
