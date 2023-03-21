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
                 vv_1_f3,
                 vv_2_f7,
                 vv_3_f11,
                 vv_4_f15,
                 vv_5_f19,
                 vv_6_f23,
                 vv_7_f27,
                 vv_8_f31,
                 vv_9_f35,
                 vv_10_f39,
                 vv_11_f43) -> None:
        self.vv_1_f3 = vv_1_f3
        self.vv_2_f7 = vv_2_f7
        self.vv_3_f11 = vv_3_f11
        self.vv_4_f15 = vv_4_f15
        self.vv_5_f19 = vv_5_f19
        self.vv_6_f23 = vv_6_f23
        self.vv_7_f27 = vv_7_f27
        self.vv_8_f31 = vv_8_f31
        self.vv_9_f35 = vv_9_f35
        self.vv_10_f39 = vv_10_f39
        self.vv_11_f43 = vv_11_f43

    def serialize(self):
        return {
            'id': self.id,
            'vv_1_f3': self.vv_1_f3,
            'vv_2_f7': self.vv_2_f7,
            'vv_3_f11': self.vv_3_f11,
            'vv_4_f15': self.vv_4_f15,
            'vv_5_f19': self.vv_5_f19,
            'vv_6_f23': self.vv_6_f23,
            'vv_7_f27': self.vv_7_f27,
            'vv_8_f31': self.vv_8_f31,
            'vv_9_f35': self.vv_9_f35,
            'vv_10_f39': self.vv_10_f39,
            'vv_11_f43': self.vv_11_f43
        }


class IlsPerceptionAnswers:
    def __init__(self,
                 si_1_f2,
                 si_2_f6,
                 si_3_f10,
                 si_4_f14,
                 si_5_f18,
                 si_6_f22,
                 si_7_f26,
                 si_8_f30,
                 si_9_f34,
                 si_10_f38,
                 si_11_f42) -> None:
        self.si_1_f2 = si_1_f2
        self.si_2_f6 = si_2_f6
        self.si_3_f10 = si_3_f10
        self.si_4_f14 = si_4_f14
        self.si_5_f18 = si_5_f18
        self.si_6_f22 = si_6_f22
        self.si_7_f26 = si_7_f26
        self.si_8_f30 = si_8_f30
        self.si_9_f34 = si_9_f34
        self.si_10_f38 = si_10_f38
        self.si_11_f42 = si_11_f42

    def serialize(self):
        return {
            'id': self.id,
            'si_1_f2': self.si_1_f2,
            'si_2_f6': self.si_2_f6,
            'si_3_f10': self.si_3_f10,
            'si_4_f14': self.si_4_f14,
            'si_5_f18': self.si_5_f18,
            'si_6_f22': self.si_6_f22,
            'si_7_f26': self.si_7_f26,
            'si_8_f30': self.si_8_f30,
            'si_9_f34': self.si_9_f34,
            'si_10_f38': self.si_10_f38,
            'si_11_f42': self.si_11_f42
        }


class IlsProcessingAnswers:
    def __init__(self,
                 ar_1_f1,
                 ar_2_f5,
                 ar_3_f9,
                 ar_4_f13,
                 ar_5_f17,
                 ar_6_f21,
                 ar_7_f25,
                 ar_8_f29,
                 ar_9_f33,
                 ar_10_f37,
                 ar_11_f41) -> None:
        self.ar_1_f1 = ar_1_f1
        self.ar_2_f5 = ar_2_f5
        self.ar_3_f9 = ar_3_f9
        self.ar_4_f13 = ar_4_f13
        self.ar_5_f17 = ar_5_f17
        self.ar_6_f21 = ar_6_f21
        self.ar_7_f25 = ar_7_f25
        self.ar_8_f29 = ar_8_f29
        self.ar_9_f33 = ar_9_f33
        self.ar_10_f37 = ar_10_f37
        self.ar_11_f41 = ar_11_f41

    def serialize(self):
        return {
            'id': self.id,
            'ar_1_f1': self.ar_1_f1,
            'ar_2_f5': self.ar_2_f5,
            'ar_3_f9': self.ar_3_f9,
            'ar_4_f13': self.ar_4_f13,
            'ar_5_f17': self.ar_5_f17,
            'ar_6_f21': self.ar_6_f21,
            'ar_7_f25': self.ar_7_f25,
            'ar_8_f29': self.ar_8_f29,
            'ar_9_f33': self.ar_9_f33,
            'ar_10_f37': self.ar_10_f37,
            'ar_11_f41': self.ar_11_f41
        }


class IlsUnderstandingAnswers:
    def __init__(self,
                 sg_1_f4,
                 sg_2_f8,
                 sg_3_f12,
                 sg_4_f16,
                 sg_5_f20,
                 sg_6_f24,
                 sg_7_f28,
                 sg_8_f32,
                 sg_9_f36,
                 sg_10_f40,
                 sg_11_f44) -> None:
        self.sg_1_f4 = sg_1_f4
        self.sg_2_f8 = sg_2_f8
        self.sg_3_f12 = sg_3_f12
        self.sg_4_f16 = sg_4_f16
        self.sg_5_f20 = sg_5_f20
        self.sg_6_f24 = sg_6_f24
        self.sg_7_f28 = sg_7_f28
        self.sg_8_f32 = sg_8_f32
        self.sg_9_f36 = sg_9_f36
        self.sg_10_f40 = sg_10_f40
        self.sg_11_f44 = sg_11_f44

    def serialize(self):
        return {
            'id': self.id,
            'sg_1_f4': self.sg_1_f4,
            'sg_2_f8': self.sg_2_f8,
            'sg_3_f12': self.sg_3_f12,
            'sg_4_f16': self.sg_4_f16,
            'sg_5_f20': self.sg_5_f20,
            'sg_6_f24': self.sg_6_f24,
            'sg_7_f28': self.sg_7_f28,
            'sg_8_f32': self.sg_8_f32,
            'sg_9_f36': self.sg_9_f36,
            'sg_10_f40': self.sg_10_f40,
            'sg_11_f44': self.sg_11_f44
        }
