class GenerateLearningPath:

    # Learning Element Types: (+) = 1 and (-) = 0
    # "KU" and "LK":0 Equally relevant for all learners
    learning_style_RQ = {"AKT": 0, "REF": 1, "INT": 1}
    learning_style_SE = {"AKT": 1, "REF": 0, "SNS": 1}
    learning_style_FO = {"AKT": 1, "REF": 0, "INT": 0, "VIS": 0, "VRB": 1}
    learning_style_ZL = {"AKT": 0, "REF": 1,
                         "SNS": 0, "INT": 1, "VIS": 0, "VRB": 1}
    learning_style_AN = {"AKT": 1, "REF": 0,
                         "SNS": 1, "INT": 0, "VIS": 1, "VRB": 0}
    learning_style_ÜB = {"AKT": 1, "REF": 0, "SNS": 1, "INT": 1}
    learning_style_BE = {"AKT": 0, "REF": 1, "SNS": 1, "INT": 0, "GLO": 1}
    learning_style_AB = {"SNS": 1, "INT": 0, "GLO": 1}
    learning_style_ZF = {"REF": 1, "GLO": 1}

    def __init__(self):
        pass

    # Checks if the input Learning Style is out the range [0-11]
    def check_learning_style(self, input_learning_style):
        # input_learning_style= {"AKT": 2, "INT": 7,"VIS": 7, "GLO": 7}
        is_correct = False

        for iterator, y in input_learning_style.items():
            if (input_learning_style.get(iterator)):

                dimension_number = input_learning_style.get(iterator)
                if (dimension_number < 0 or dimension_number > 11):
                    is_correct = True
                    break
        return is_correct

    # Validates the special case of ZF learning elements
    def special_case_ZF(self, input_learning_style):

        # input_learning_style= {"AKT": 2, "REF": 7,"SEQ": 7, "GLO": 7}
        result = 0
        reflective = input_learning_style.get("REF")
        sequential = input_learning_style.get("SEQ")
        condition1 = reflective and sequential

        if (condition1 and reflective > sequential):

            result = 99
        else:
            if (sequential or input_learning_style.get("GLO")):
                result = 99

        return result
    
    #  Calculates the sequence of the learning elements to constructs the learning path
    def calculate_sequence(self, learning_element_types, input_learning_style):

        # input_learning_style= {"AKT": 2, "REF": 7,"SEQ": 7, "GLO": 7}
        # learning_element_types = learning_style_RQ or learning_style_FO, etc
        sum = 0
        learning_style = 0

        # learning_element_types = positive 1 or negative 0

        for learning_style, value in learning_element_types.items():
            # print ("learning_style",learning_style)
            if (input_learning_style.get(learning_style)):
                learning_style = input_learning_style.get(learning_style)

                if (value == 0):
                    learning_style *= -1

                sum += learning_style

        return sum

     #sortes the sequence of the learning elements   
    def sorted_learning_path(self, learning_path):
        sorted_learning_path = {}
        sorted_keys = sorted(
            learning_path, key=learning_path.get, reverse=True)

        for w in sorted_keys:
            sorted_learning_path[w] = learning_path[w]
        print(sorted_learning_path)
        return sorted_learning_path

    #Calculates the sequence of the learning path and validates the input values of the learning styles
    def get_learning_path(self, input_learning_style={"AKT": 0, "INT": 0,
                                                      "VIS": 0, "GLO": 0}):
        if (len(input_learning_style) != 4):
            raise ValueError('The Size of Learning Style is not 4')

        if self.check_learning_style(input_learning_style):
            raise ValueError(
                'The Input Learning Style is out the range [0-11]')

        LPath = {}
        print("\n", input_learning_style)

        LPath["RQ"] = self.calculate_sequence(self.learning_style_RQ, input_learning_style)
        LPath["SE"] = self.calculate_sequence(self.learning_style_SE, input_learning_style)
        LPath["FO"] = self.calculate_sequence(self.learning_style_FO, input_learning_style)
        LPath["ZL"] = self.calculate_sequence(self.learning_style_ZL, input_learning_style)
        LPath["AN"] = self.calculate_sequence(self.learning_style_AN, input_learning_style)
        LPath["ÜB"] = self.calculate_sequence(self.learning_style_ÜB, input_learning_style)
        LPath["BE"] = self.calculate_sequence(self.learning_style_BE, input_learning_style)
        LPath["AB"] = self.calculate_sequence(self.learning_style_AB, input_learning_style)
        LPath["ZF"] = self.special_case_ZF(input_learning_style)

        return self.sorted_learning_path(LPath)
