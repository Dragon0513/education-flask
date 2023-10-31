from domain.tutoringModel.utils import check_learning_style, influence


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

    def calculate_graf_score(self, learning_element, learning_style):
        if(learning_element == "KÜ"):
            return 99
        elif(learning_element == "EK"):
            return 98
        elif(learning_element == "LZ"):
            return -99
        elif(learning_element == "ZF"):
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
        else:
            sum = 0
            print(influence[learning_element])
            if(learning_style["processing_dimension"] == "act"):
                sum = sum + influence[learning_element][0] * \
                    learning_style["processing_value"]
            else:
                sum = sum + influence[learning_element][1] * \
                    learning_style["processing_value"]
            if(learning_style["perception_dimension"] == "sns"):
                sum = sum + influence[learning_element][2] * \
                    learning_style["perception_value"]
            else:
                sum = sum + influence[learning_element][3] * \
                    learning_style["perception_value"]
            if(learning_style["input_dimension"] == "act"):
                sum = sum + influence[learning_element][4] * \
                    learning_style["input_value"]
            else:
                sum = sum + influence[learning_element][5] * \
                    learning_style["input_value"]
            if(learning_style["understanding_dimension"] == "act"):
                sum = sum + influence[learning_element][6] * \
                    learning_style["understanding_value"]
            else:
                sum = sum + influence[learning_element][7] * \
                    learning_style["understanding_value"]
            return sum

    def sort_learning_path(self, learning_path):
        sort_learning_path = []

        for _ in range(len(learning_path)):
            highest_item = max(learning_path, key=learning_path.get)
            sort_learning_path.append(highest_item)
            del learning_path[highest_item]
        return sort_learning_path

    def get_learning_path(
        self,
        input_learning_style={},
        list_of_les={}
    ):
        check_learning_style(input_learning_style)
        learning_path = {}
        for le in list_of_les:
            value = self.calculate_graf_score(
                le['classification'], input_learning_style)
            learning_path[le['classification']] = value
        return self.sort_learning_path(learning_path)
