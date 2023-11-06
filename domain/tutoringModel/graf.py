from domain.tutoringModel.utils import check_learning_style, influence
from utils import constants as cons


class GrafAlgorithm:
    def __init__(
        self,
        student_id,
        learning_path=None,
        id=None,
    ):
        self.id = id
        self.student_id = student_id
        self.learning_path = learning_path

    def get_standard_values_for_graf(self, learning_element):
        if learning_element == cons.abbreviation_ct:
            return 99
        elif learning_element == cons.abbreviation_co:
            return 98
        elif learning_element == cons.abbreviation_as:
            return -99

    def get_cc_score(self, learning_style):
        if (
            learning_style["processing_dimension"] == "ref"
            and learning_style["understanding_dimension"] == "seq"
        ):
            if (
                learning_style["processing_value"]
                > learning_style["understanding_value"]
            ):
                return 97
            else:
                return 0
        elif (
            learning_style["processing_dimension"] == "ref"
            or learning_style["understanding_dimension"] == "glo"
        ):
            return 97
        else:
            return 0

    def calculate_variable_score(self, learning_element, learning_style):
        score = 0
        if learning_style["processing_dimension"] == "act":
            score = (
                score
                + influence[learning_element][0] * learning_style["processing_value"]
            )
        else:
            score = (
                score
                + influence[learning_element][1] * learning_style["processing_value"]
            )
        if learning_style["perception_dimension"] == "sns":
            score = (
                score
                + influence[learning_element][2] * learning_style["perception_value"]
            )
        else:
            score = (
                score
                + influence[learning_element][3] * learning_style["perception_value"]
            )
        if learning_style["input_dimension"] == "act":
            score = (
                score + influence[learning_element][4] * learning_style["input_value"]
            )
        else:
            score = (
                score + influence[learning_element][5] * learning_style["input_value"]
            )
        if learning_style["understanding_dimension"] == "act":
            score = (
                score
                + influence[learning_element][6] * learning_style["understanding_value"]
            )
        else:
            score = (
                score
                + influence[learning_element][7] * learning_style["understanding_value"]
            )
        return score

    def calculate_graf_score(self, learning_element, learning_style):
        if (
            learning_element == cons.abbreviation_ct
            or learning_element == cons.abbreviation_co
            or learning_element == cons.abbreviation_as
        ):
            return self.get_standard_values_for_graf(learning_element)
        elif learning_element == cons.abbreviation_cc:
            return self.get_cc_score(learning_style)
        else:
            return self.calculate_variable_score(learning_element, learning_style)

    def sort_learning_path(self, learning_path):
        sort_learning_path = []

        for _ in range(len(learning_path)):
            highest_item = max(learning_path, key=learning_path.get)
            sort_learning_path.append(highest_item)
            del learning_path[highest_item]
        return sort_learning_path

    def get_learning_path(self, input_learning_style={}, list_of_les={}):
        check_learning_style(input_learning_style)
        learning_path = {}
        for le in list_of_les:
            value = self.calculate_graf_score(
                le["classification"], input_learning_style
            )
            learning_path[le["classification"]] = value
        return self.sort_learning_path(learning_path)
