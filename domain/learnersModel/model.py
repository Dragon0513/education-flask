class LearningCharacteristic:
    def __init__(self,
                 user_id) -> None:
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class LearningStyle:
    def __init__(self,
                 characteristic_id,
                 perception_dimension,
                 perception_value,
                 input_dimension,
                 input_value,
                 processing_dimension,
                 processing_value,
                 understanding_dimension,
                 understanding_value) -> None:
        self.characteristic_id = characteristic_id
        self.perception_dimension = perception_dimension
        self.perception_value = perception_value
        self.input_dimension = input_dimension
        self.input_value = input_value
        self.processing_dimension = processing_dimension
        self.processing_value = processing_value
        self.understanding_dimension = understanding_dimension
        self.understanding_value = understanding_value

    def serialize(self):
        return {
            'id': self.id,
            'characteristic_id': self.characteristic_id,
            'perception_dimension': self.perception_dimension,
            'perception_value': self.perception_value,
            'input_dimension': self.input_dimension,
            'input_value': self.input_value,
            'processing_dimension': self.processing_dimension,
            'processing_value': self.processing_value,
            'understanding_dimension': self.understanding_dimension,
            'understanding_value': self.understanding_value
        }


class LearningStrategy:
    def __init__(self,
                 characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {
            'id': self.id,
            'characteristic_id': self.characteristic_id
        }


class Knowledge:
    def __init__(self,
                 characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {
            'id': self.id,
            'characteristic_id': self.characteristic_id
        }


class LearningAnalytics:
    def __init__(self,
                 characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {
            'id': self.id,
            'characteristic_id': self.characteristic_id
        }


class Questionnaire:
    def __init__(self,
                student_id) -> None:
        self.student_id = student_id

    def serialize(self):
        return {
            'id': self.id,
            'student_id': self.student_id
        }


class IlsInputAnswers:
    def __init__(self,
                vv_1,
                vv_2,
                vv_3,
                vv_4,
                vv_5,
                vv_6,
                vv_7,
                vv_8,
                vv_9,
                vv_10,
                vv_11) -> None:
        self.vv_1 = vv_1
        self.vv_2 = vv_2
        self.vv_3 = vv_3
        self.vv_4 = vv_4
        self.vv_5 = vv_5
        self.vv_6 = vv_6
        self.vv_7 = vv_7
        self.vv_8 = vv_8
        self.vv_9 = vv_9
        self.vv_10 = vv_10
        self.vv_11 = vv_11

    def serialize(self):
        return {
            'id': self.id,
            'vv_1': self.vv_1,
            'vv_2': self.vv_2,
            'vv_3': self.vv_3,
            'vv_4': self.vv_4,
            'vv_5': self.vv_5,
            'vv_6': self.vv_6,
            'vv_7': self.vv_7,
            'vv_8': self.vv_8,
            'vv_9': self.vv_9,
            'vv_10': self.vv_10,
            'vv_11': self.vv_11
        }


class IlsPerceptionAnswers:
    def __init__(self,
                si_1,
                si_2,
                si_3,
                si_4,
                si_5,
                si_6,
                si_7,
                si_8,
                si_9,
                si_10,
                si_11) -> None:
        self.si_1 = si_1
        self.si_2 = si_2
        self.si_3 = si_3
        self.si_4 = si_4
        self.si_5 = si_5
        self.si_6 = si_6
        self.si_7 = si_7
        self.si_8 = si_8
        self.si_9 = si_9
        self.si_10 = si_10
        self.si_11 = si_11

    def serialize(self):
        return {
            'id': self.id,
            'si_1': self.si_1,
            'si_2': self.si_2,
            'si_3': self.si_3,
            'si_4': self.si_4,
            'si_5': self.si_5,
            'si_6': self.si_6,
            'si_7': self.si_7,
            'si_8': self.si_8,
            'si_9': self.si_9,
            'si_10': self.si_10,
            'si_11': self.si_11
        }


class IlsProcessingAnswers:
    def __init__(self,
                ar_1,
                ar_2,
                ar_3,
                ar_4,
                ar_5,
                ar_6,
                ar_7,
                ar_8,
                ar_9,
                ar_10,
                ar_11) -> None:
        self.ar_1 = ar_1
        self.ar_2 = ar_2
        self.ar_3 = ar_3
        self.ar_4 = ar_4
        self.ar_5 = ar_5
        self.ar_6 = ar_6
        self.ar_7 = ar_7
        self.ar_8 = ar_8
        self.ar_9 = ar_9
        self.ar_10 = ar_10
        self.ar_11 = ar_11

    def serialize(self):
        return {
            'id': self.id,
            'ar_1': self.ar_1,
            'ar_2': self.ar_2,
            'ar_3': self.ar_3,
            'ar_4': self.ar_4,
            'ar_5': self.ar_5,
            'ar_6': self.ar_6,
            'ar_7': self.ar_7,
            'ar_8': self.ar_8,
            'ar_9': self.ar_9,
            'ar_10': self.ar_10,
            'ar_11': self.ar_11
        }


class IlsUnderstandingAnswers:
    def __init__(self,
                sg_1,
                sg_2,
                sg_3,
                sg_4,
                sg_5,
                sg_6,
                sg_7,
                sg_8,
                sg_9,
                sg_10,
                sg_11) -> None:
        self.sg_1 = sg_1
        self.sg_2 = sg_2
        self.sg_3 = sg_3
        self.sg_4 = sg_4
        self.sg_5 = sg_5
        self.sg_6 = sg_6
        self.sg_7 = sg_7
        self.sg_8 = sg_8
        self.sg_9 = sg_9
        self.sg_10 = sg_10
        self.sg_11 = sg_11

    def serialize(self):
        return {
            'id': self.id,
            'sg_1': self.sg_1,
            'sg_2': self.sg_2,
            'sg_3': self.sg_3,
            'sg_4': self.sg_4,
            'sg_5': self.sg_5,
            'sg_6': self.sg_6,
            'sg_7': self.sg_7,
            'sg_8': self.sg_8,
            'sg_9': self.sg_9,
            'sg_10': self.sg_10,
            'sg_11': self.sg_11
        }

