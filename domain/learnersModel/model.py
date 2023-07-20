class LearningCharacteristic:
    def __init__(
        self,
        student_id,
        knowledge=None,
        learning_analytics=None,
        learning_strategy=None,
        learning_style=None,
    ) -> None:
        self.student_id = student_id
        self.knowledge = knowledge
        self.learning_analytics = learning_analytics
        self.learning_strategy = learning_strategy
        self.learning_style = learning_style

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "knowledge": self.knowledge,
            "learning_analytics": self.learning_analytics,
            "learning_strategy": self.learning_strategy,
            "learning_style": self.learning_style,
        }


class LearningStyle:
    def __init__(
        self,
        characteristic_id=None,
        perception_dimension="sns",
        perception_value=0,
        input_dimension="vrb",
        input_value=0,
        processing_dimension="act",
        processing_value=0,
        understanding_dimension="seq",
        understanding_value=0,
    ) -> None:
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
            "id": self.id,
            "characteristic_id": self.characteristic_id,
            "perception_dimension": self.perception_dimension,
            "perception_value": self.perception_value,
            "input_dimension": self.input_dimension,
            "input_value": self.input_value,
            "processing_dimension": self.processing_dimension,
            "processing_value": self.processing_value,
            "understanding_dimension": self.understanding_dimension,
            "understanding_value": self.understanding_value,
        }


class LearningStrategy:
    def __init__(self, characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {"id": self.id, "characteristic_id": self.characteristic_id}


class Knowledge:
    def __init__(self, characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {"id": self.id, "characteristic_id": self.characteristic_id}


class LearningAnalytics:
    def __init__(self, characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {"id": self.id, "characteristic_id": self.characteristic_id}


class Questionnaire:
    def __init__(self, student_id, learning_style=None, learning_strategy=None) -> None:
        self.student_id = student_id
        self.learning_style = learning_style
        self.learning_strategy = learning_strategy

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "learning_style": self.learning_style,
            "learning_strategy": self.learning_strategy,
        }


class IlsInputAnswers:
    def __init__(
        self,
        questionnaire_id,
        vv_2_f7,
        vv_5_f19,
        vv_7_f27,
        vv_10_f39,
        vv_11_f43,
        vv_1_f3=None,
        vv_3_f11=None,
        vv_4_f15=None,
        vv_6_f23=None,
        vv_8_f31=None,
        vv_9_f35=None,
    ) -> None:
        self.questionnaire_id = questionnaire_id
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
            "id": self.id,
            "questionnaire_id": self.questionnaire_id,
            "vv_1_f3": self.vv_1_f3,
            "vv_2_f7": self.vv_2_f7,
            "vv_3_f11": self.vv_3_f11,
            "vv_4_f15": self.vv_4_f15,
            "vv_5_f19": self.vv_5_f19,
            "vv_6_f23": self.vv_6_f23,
            "vv_7_f27": self.vv_7_f27,
            "vv_8_f31": self.vv_8_f31,
            "vv_9_f35": self.vv_9_f35,
            "vv_10_f39": self.vv_10_f39,
            "vv_11_f43": self.vv_11_f43,
        }


class IlsPerceptionAnswers:
    def __init__(
        self,
        questionnaire_id,
        si_1_f2,
        si_4_f14,
        si_7_f26,
        si_10_f38,
        si_11_f42,
        si_2_f6=None,
        si_3_f10=None,
        si_5_f18=None,
        si_6_f22=None,
        si_8_f30=None,
        si_9_f34=None,
    ) -> None:
        self.questionnaire_id = questionnaire_id
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
            "id": self.id,
            "questionnaire_id": self.questionnaire_id,
            "si_1_f2": self.si_1_f2,
            "si_2_f6": self.si_2_f6,
            "si_3_f10": self.si_3_f10,
            "si_4_f14": self.si_4_f14,
            "si_5_f18": self.si_5_f18,
            "si_6_f22": self.si_6_f22,
            "si_7_f26": self.si_7_f26,
            "si_8_f30": self.si_8_f30,
            "si_9_f34": self.si_9_f34,
            "si_10_f38": self.si_10_f38,
            "si_11_f42": self.si_11_f42,
        }


class IlsProcessingAnswers:
    def __init__(
        self,
        questionnaire_id,
        ar_3_f9,
        ar_4_f13,
        ar_6_f21,
        ar_7_f25,
        ar_8_f29,
        ar_1_f1=None,
        ar_2_f5=None,
        ar_5_f17=None,
        ar_9_f33=None,
        ar_10_f37=None,
        ar_11_f41=None,
    ) -> None:
        self.questionnaire_id = questionnaire_id
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
            "id": self.id,
            "questionnaire_id": self.questionnaire_id,
            "ar_1_f1": self.ar_1_f1,
            "ar_2_f5": self.ar_2_f5,
            "ar_3_f9": self.ar_3_f9,
            "ar_4_f13": self.ar_4_f13,
            "ar_5_f17": self.ar_5_f17,
            "ar_6_f21": self.ar_6_f21,
            "ar_7_f25": self.ar_7_f25,
            "ar_8_f29": self.ar_8_f29,
            "ar_9_f33": self.ar_9_f33,
            "ar_10_f37": self.ar_10_f37,
            "ar_11_f41": self.ar_11_f41,
        }


class IlsUnderstandingAnswers:
    def __init__(
        self,
        questionnaire_id,
        sg_1_f4,
        sg_2_f8,
        sg_4_f16,
        sg_10_f40,
        sg_11_f44,
        sg_3_f12=None,
        sg_5_f20=None,
        sg_6_f24=None,
        sg_7_f28=None,
        sg_8_f32=None,
        sg_9_f36=None,
    ) -> None:
        self.questionnaire_id = questionnaire_id
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
            "id": self.id,
            "questionnaire_id": self.questionnaire_id,
            "sg_1_f4": self.sg_1_f4,
            "sg_2_f8": self.sg_2_f8,
            "sg_3_f12": self.sg_3_f12,
            "sg_4_f16": self.sg_4_f16,
            "sg_5_f20": self.sg_5_f20,
            "sg_6_f24": self.sg_6_f24,
            "sg_7_f28": self.sg_7_f28,
            "sg_8_f32": self.sg_8_f32,
            "sg_9_f36": self.sg_9_f36,
            "sg_10_f40": self.sg_10_f40,
            "sg_11_f44": self.sg_11_f44,
        }


class ListK:
    def __init__(
        self,
        questionnaire_id,
        org1_f1,
        org2_f2,
        org3_f3,
        ela1_f4,
        ela2_f5,
        ela3_f6,
        krp1_f7,
        krp2_f8,
        krp3_f9,
        wie1_f10,
        wie2_f11,
        wie3_f12,
        zp1_f13,
        zp2_f14,
        zp3_f15,
        kon1_f16,
        kon2_f17,
        kon3_f18,
        reg1_f19,
        reg2_f20,
        reg3_f21,
        auf1_f22,
        auf2_f23,
        auf3_f24,
        ans1_f25,
        ans2_f26,
        ans3_f27,
        zei1_f28,
        zei2_f29,
        zei3_f30,
        lms1_f31,
        lms2_f32,
        lms3_f33,
        lit1_f34,
        lit2_f35,
        lit3_f36,
        lu1_f37,
        lu2_f38,
        lu3_f39,
    ) -> None:
        self.questionnaire_id = questionnaire_id
        self.org1_f1 = org1_f1
        self.org2_f2 = org2_f2
        self.org3_f3 = org3_f3
        self.ela1_f4 = ela1_f4
        self.ela2_f5 = ela2_f5
        self.ela3_f6 = ela3_f6
        self.krp1_f7 = krp1_f7
        self.krp2_f8 = krp2_f8
        self.krp3_f9 = krp3_f9
        self.wie1_f10 = wie1_f10
        self.wie2_f11 = wie2_f11
        self.wie3_f12 = wie3_f12
        self.zp1_f13 = zp1_f13
        self.zp2_f14 = zp2_f14
        self.zp3_f15 = zp3_f15
        self.kon1_f16 = kon1_f16
        self.kon2_f17 = kon2_f17
        self.kon3_f18 = kon3_f18
        self.reg1_f19 = reg1_f19
        self.reg2_f20 = reg2_f20
        self.reg3_f21 = reg3_f21
        self.auf1_f22 = auf1_f22
        self.auf2_f23 = auf2_f23
        self.auf3_f24 = auf3_f24
        self.ans1_f25 = ans1_f25
        self.ans2_f26 = ans2_f26
        self.ans3_f27 = ans3_f27
        self.zei1_f28 = zei1_f28
        self.zei2_f29 = zei2_f29
        self.zei3_f30 = zei3_f30
        self.lms1_f31 = lms1_f31
        self.lms2_f32 = lms2_f32
        self.lms3_f33 = lms3_f33
        self.lit1_f34 = lit1_f34
        self.lit2_f35 = lit2_f35
        self.lit3_f36 = lit3_f36
        self.lu1_f37 = lu1_f37
        self.lu2_f38 = lu2_f38
        self.lu3_f39 = lu3_f39

    def serialize(self):
        return {
            "id": self.id,
            "questionnaire_id": self.questionnaire_id,
            "org1_f1": self.org1_f1,
            "org2_f2": self.org2_f2,
            "org3_f3": self.org3_f3,
            "ela1_f4": self.ela1_f4,
            "ela2_f5": self.ela2_f5,
            "ela3_f6": self.ela3_f6,
            "krp1_f7": self.krp1_f7,
            "krp2_f8": self.krp2_f8,
            "krp3_f9": self.krp3_f9,
            "wie1_f10": self.wie1_f10,
            "wie2_f11": self.wie2_f11,
            "wie3_f12": self.wie3_f12,
            "zp1_f13": self.zp1_f13,
            "zp2_f14": self.zp2_f14,
            "zp3_f15": self.zp3_f15,
            "kon1_f16": self.kon1_f16,
            "kon2_f17": self.kon2_f17,
            "kon3_f18": self.kon3_f18,
            "reg1_f19": self.reg1_f19,
            "reg2_f20": self.reg2_f20,
            "reg3_f21": self.reg3_f21,
            "auf1_f22": self.auf1_f22,
            "auf2_f23": self.auf2_f23,
            "auf3_f24": self.auf3_f24,
            "ans1_f25": self.ans1_f25,
            "ans2_f26": self.ans2_f26,
            "ans3_f27": self.ans3_f27,
            "zei1_f28": self.zei1_f28,
            "zei2_f29": self.zei2_f29,
            "zei3_f30": self.zei3_f30,
            "lms1_f31": self.lms1_f31,
            "lms2_f32": self.lms2_f32,
            "lms3_f33": self.lms3_f33,
            "lit1_f34": self.lit1_f34,
            "lit2_f35": self.lit2_f35,
            "lit3_f36": self.lit3_f36,
            "lu1_f37": self.lu1_f37,
            "lu2_f38": self.lu2_f38,
            "lu3_f39": self.lu3_f39,
        }
