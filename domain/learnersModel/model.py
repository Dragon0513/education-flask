class LearningCharacteristic:
    def __init__(
        self,
        student_id,
        knowledge=None,
        learning_analytics=None,
        learning_strategy=None,
        learning_style=None,
    ) -> None:
        self.id = None
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
        self.id = None
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
    def __init__(
        self,
        characteristic_id,
        cogn_str=0.00,
        org=0.00,
        elab=0.00,
        crit_rev=0.00,
        rep=0.00,
        metacogn_str=0.00,
        goal_plan=0.00,
        con=0.00,
        reg=0.00,
        int_res_mng_str=0.00,
        att=0.00,
        eff=0.00,
        time=0.00,
        ext_res_mng_str=0.00,
        lrn_w_cls=0.00,
        lit_res=0.00,
        lrn_env=0.00,
    ) -> None:
        self.id = None
        self.characteristic_id = characteristic_id
        self.cogn_str = cogn_str
        self.org = org
        self.elab = elab
        self.crit_rev = crit_rev
        self.rep = rep
        self.metacogn_str = metacogn_str
        self.goal_plan = goal_plan
        self.con = con
        self.reg = reg
        self.int_res_mng_str = int_res_mng_str
        self.att = att
        self.eff = eff
        self.time = time
        self.ext_res_mng_str = ext_res_mng_str
        self.lrn_w_cls = lrn_w_cls
        self.lit_res = lit_res
        self.lrn_env = lrn_env

    def serialize(self):
        return {
            "id": self.id,
            "characteristic_id": self.characteristic_id,
            "cogn_str": self.cogn_str,
            "org": self.org,
            "elab": self.elab,
            "crit_rev": self.crit_rev,
            "rep": self.rep,
            "metacogn_str": self.metacogn_str,
            "goal_plan": self.goal_plan,
            "con": self.con,
            "reg": self.reg,
            "int_res_mng_str": self.int_res_mng_str,
            "att": self.att,
            "eff": self.eff,
            "time": self.time,
            "ext_res_mng_str": self.ext_res_mng_str,
            "lrn_w_cls": self.lrn_w_cls,
            "lit_res": self.lit_res,
            "lrn_env": self.lrn_env,
        }


class Knowledge:
    def __init__(self, characteristic_id) -> None:
        self.id = None
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {"id": self.id, "characteristic_id": self.characteristic_id}


class LearningAnalytics:
    def __init__(self, characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {"id": self.id, "characteristic_id": self.characteristic_id}


class QuestionnaireIls:
    def __init__(self, student_id, learning_style=None, learning_strategy=None) -> None:
        self.id = None
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
        questionnaire_ils_id,
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
        self.id = None
        self.questionnaire_ils_id = questionnaire_ils_id
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
            "questionnaire_ils_id": self.questionnaire_ils_id,
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
        questionnaire_ils_id,
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
        self.id = None
        self.questionnaire_ils_id = questionnaire_ils_id
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
            "questionnaire_ils_id": self.questionnaire_ils_id,
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
        questionnaire_ils_id,
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
        self.id = None
        self.questionnaire_ils_id = questionnaire_ils_id
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
            "questionnaire_ils_id": self.questionnaire_ils_id,
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
        questionnaire_ils_id,
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
        self.id = None
        self.questionnaire_ils_id = questionnaire_ils_id
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
            "questionnaire_ils_id": self.questionnaire_ils_id,
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


class QuestionnaireListK:
    def __init__(
        self,
        student_id,
        org1_f1,
        org2_f2,
        org3_f3,
        elab1_f4,
        elab2_f5,
        elab3_f6,
        crit_rev1_f7,
        crit_rev2_f8,
        crit_rev3_f9,
        rep1_f10,
        rep2_f11,
        rep3_f12,
        goal_plan1_f13,
        goal_plan2_f14,
        goal_plan3_f15,
        con1_f16,
        con2_f17,
        con3_f18,
        reg1_f19,
        reg2_f20,
        reg3_f21,
        att1_f22,
        att2_f23,
        att3_f24,
        eff1_f25,
        eff2_f26,
        eff3_f27,
        time1_f28,
        time2_f29,
        time3_f30,
        lrn_w_cls1_f31,
        lrn_w_cls2_f32,
        lrn_w_cls3_f33,
        lit_res1_f34,
        lit_res2_f35,
        lit_res3_f36,
        lrn_env1_f37,
        lrn_env2_f38,
        lrn_env3_f39,
    ) -> None:
        self.id = None
        self.student_id = student_id
        self.org1_f1 = org1_f1
        self.org2_f2 = org2_f2
        self.org3_f3 = org3_f3
        self.elab1_f4 = elab1_f4
        self.elab2_f5 = elab2_f5
        self.elab3_f6 = elab3_f6
        self.crit_rev1_f7 = crit_rev1_f7
        self.crit_rev2_f8 = crit_rev2_f8
        self.crit_rev3_f9 = crit_rev3_f9
        self.rep1_f10 = rep1_f10
        self.rep2_f11 = rep2_f11
        self.rep3_f12 = rep3_f12
        self.goal_plan1_f13 = goal_plan1_f13
        self.goal_plan2_f14 = goal_plan2_f14
        self.goal_plan3_f15 = goal_plan3_f15
        self.con1_f16 = con1_f16
        self.con2_f17 = con2_f17
        self.con3_f18 = con3_f18
        self.reg1_f19 = reg1_f19
        self.reg2_f20 = reg2_f20
        self.reg3_f21 = reg3_f21
        self.att1_f22 = att1_f22
        self.att2_f23 = att2_f23
        self.att3_f24 = att3_f24
        self.eff1_f25 = eff1_f25
        self.eff2_f26 = eff2_f26
        self.eff3_f27 = eff3_f27
        self.time1_f28 = time1_f28
        self.time2_f29 = time2_f29
        self.time3_f30 = time3_f30
        self.lrn_w_cls1_f31 = lrn_w_cls1_f31
        self.lrn_w_cls2_f32 = lrn_w_cls2_f32
        self.lrn_w_cls3_f33 = lrn_w_cls3_f33
        self.lit_res1_f34 = lit_res1_f34
        self.lit_res2_f35 = lit_res2_f35
        self.lit_res3_f36 = lit_res3_f36
        self.lrn_env1_f37 = lrn_env1_f37
        self.lrn_env2_f38 = lrn_env2_f38
        self.lrn_env3_f39 = lrn_env3_f39

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "org1_f1": self.org1_f1,
            "org2_f2": self.org2_f2,
            "org3_f3": self.org3_f3,
            "elab1_f4": self.elab1_f4,
            "elab2_f5": self.elab2_f5,
            "elab3_f6": self.elab3_f6,
            "crit_rev1_f7": self.crit_rev1_f7,
            "crit_rev2_f8": self.crit_rev2_f8,
            "crit_rev3_f9": self.crit_rev3_f9,
            "rep1_f10": self.rep1_f10,
            "rep2_f11": self.rep2_f11,
            "rep3_f12": self.rep3_f12,
            "goal_plan1_f13": self.goal_plan1_f13,
            "goal_plan2_f14": self.goal_plan2_f14,
            "goal_plan3_f15": self.goal_plan3_f15,
            "con1_f16": self.con1_f16,
            "con2_f17": self.con2_f17,
            "con3_f18": self.con3_f18,
            "reg1_f19": self.reg1_f19,
            "reg2_f20": self.reg2_f20,
            "reg3_f21": self.reg3_f21,
            "att1_f22": self.att1_f22,
            "att2_f23": self.att2_f23,
            "att3_f24": self.att3_f24,
            "eff1_f25": self.eff1_f25,
            "eff2_f26": self.eff2_f26,
            "eff3_f27": self.eff3_f27,
            "time1_f28": self.time1_f28,
            "time2_f29": self.time2_f29,
            "time3_f30": self.time3_f30,
            "lrn_w_cls1_f31": self.lrn_w_cls1_f31,
            "lrn_w_cls2_f32": self.lrn_w_cls2_f32,
            "lrn_w_cls3_f33": self.lrn_w_cls3_f33,
            "lit_res1_f34": self.lit_res1_f34,
            "lit_res2_f35": self.lit_res2_f35,
            "lit_res3_f36": self.lit_res3_f36,
            "lrn_env1_f37": self.lrn_env1_f37,
            "lrn_env2_f38": self.lrn_env2_f38,
            "lrn_env3_f39": self.lrn_env3_f39,
        }
