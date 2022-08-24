from datetime import datetime
import errors as err


class LearningPath:

    # Learning Element Types: (+) = 1 and (-) = 0
    learning_style_RQ = {"AKT": 0, "REF": 1, "INT": 1}
    learning_style_SE = {"AKT": 1, "REF": 0, "SNS": 1}
    learning_style_FO = {"AKT": 1, "REF": 0, "INT": 0, "VIS": 0, "VRB": 1}
    learning_style_ZL = {"AKT": 0, "REF": 1,
                         "SNS": 0, "INT": 1, "VIS": 0, "VRB": 1}
    learning_style_AN = {"AKT": 1, "REF": 0,
                         "SNS": 1, "INT": 0, "VIS": 1, "VRB": 0}
    learning_style_UB = {"AKT": 1, "REF": 0, "SNS": 1, "INT": 1}
    learning_style_BE = {"AKT": 0, "REF": 1, "SNS": 1, "INT": 0, "GLO": 1}
    learning_style_AB = {"SNS": 1, "INT": 0, "GLO": 1}
    learning_style_ZF = {"REF": 1, "GLO": 1}

    def __init__(self,
                 student_id,
                 learning_path=None,
                 learning_style={"AKT": 0, "INT": 0, "VIS": 0, "GLO": 0},
                 id=None):
        if id is None:
            self.id = datetime.timestamp(datetime.now())
        else:
            self.id = id
        self.student_id = student_id
        if learning_path is None:
            self.learning_path = self.get_learning_path(learning_style)
        else:
            self.learning_path = learning_path

    def check_learning_style(self, input_learning_style):
        is_correct = False

        for iterator in input_learning_style:
            if (input_learning_style.get(iterator)):

                dimension_number = input_learning_style.get(iterator)
                if (dimension_number < 0 or dimension_number > 11):
                    is_correct = True
                    break
        return is_correct

    def special_case_ZF(self, input_learning_style):
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

        sum = 0
        learning_style = 0

        for learning_style, value in learning_element_types.items():
            if (input_learning_style.get(learning_style)):
                learning_style = input_learning_style.get(learning_style)

                if (value == 0):
                    learning_style *= -1

                sum += learning_style

        return sum

    def sort_learning_path(self, learning_path):
        sort_learning_path = []

        for _ in range(len(learning_path)):
            highest_item = max(learning_path, key=learning_path.get)
            sort_learning_path.append(highest_item)
            del learning_path[highest_item]
        return sort_learning_path

    def get_learning_path(self, input_learning_style={"AKT": 0, "INT": 0,
                                                      "VIS": 0, "GLO": 0}):
        if (len(input_learning_style) != 4):
            raise err.WrongLearningStyleNumberError()

        if self.check_learning_style(input_learning_style):
            raise err.WrongLearningStyleDimensionError()

        LPath = {}

        LPath["RQ"] = self.calculate_sequence(
            self.learning_style_RQ, input_learning_style)
        LPath["SE"] = self.calculate_sequence(
            self.learning_style_SE, input_learning_style)
        LPath["FO"] = self.calculate_sequence(
            self.learning_style_FO, input_learning_style)
        LPath["ZL"] = self.calculate_sequence(
            self.learning_style_ZL, input_learning_style)
        LPath["AN"] = self.calculate_sequence(
            self.learning_style_AN, input_learning_style)
        LPath["UB"] = self.calculate_sequence(
            self.learning_style_UB, input_learning_style)
        LPath["BE"] = self.calculate_sequence(
            self.learning_style_BE, input_learning_style)
        LPath["AB"] = self.calculate_sequence(
            self.learning_style_AB, input_learning_style)
        LPath["ZF"] = self.special_case_ZF(input_learning_style)

        return self.sort_learning_path(LPath)
