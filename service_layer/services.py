from service_layer import unit_of_work
from domain.userAdministartion import model as UA
from domain.learnersModel import model as LM
from domain.domainModel import model as DM


def add_course_creator_to_course(
        uow: unit_of_work.AbstractUnitOfWork,
        created_by,
        course_id,
        created_at
) -> dict:
    with uow:
        course_creator = uow.course_creator.get_course_creator_by_id(
            created_by
        )
        course_creator_course = DM.CourseCreatorCourse(
            course_creator[0].id,
            course_id,
            created_at
        )
        uow.course_creator_course.add_course_creator_to_course(
            course_creator_course
        )
        uow.commit()
        result = course_creator_course.serialize()
        return result


def add_student_to_course(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        course_id
) -> dict:
    with uow:
        characteristics = get_learning_characteristics(uow, student_id)
        learning_style = get_learning_style(uow, characteristics['id'])
        student_course = DM.StudentCourse(
            student_id,
            course_id,
            learning_style['perception_dimension'],
            learning_style['perception_value'],
            learning_style['input_dimension'],
            learning_style['input_value'],
            learning_style['processing_dimension'],
            learning_style['processing_value'],
            learning_style['understanding_dimension'],
            learning_style['understanding_value']
        )
        uow.student_course.add_student_to_course(
            student_course
        )
        uow.commit()
        result = student_course.serialize()
        add_student_to_topics(uow,
                              student_id,
                              course_id)
        return result


def add_student_to_learning_element(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        topic_id
):
    with uow:
        learning_elements = get_learning_elements_for_topic_id(
            uow,
            topic_id
        )
        for le in learning_elements:
            student_learning_element =\
                DM.StudentLearningElement(
                    student_id, le['learning_element_id'])
            uow.student_learning_element.add_student_to_learning_element(
                student_learning_element)
            uow.commit()


def add_student_to_topics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        course_id
):
    with uow:
        topics = get_topics_for_course_id(
            uow,
            course_id
        )
        for topic in topics:
            student_topic = DM.StudentTopic(student_id, topic['topic_id'])
            uow.student_topic.add_student_to_topic(student_topic)
            uow.commit()
            add_student_to_learning_element(uow, student_id, topic['topic_id'])


def add_student_learning_element_visit(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        learning_element_id,
        visit_start,
        previous_learning_element_id
) -> dict:
    with uow:
        update_previous_learning_element_visit(
            uow,
            student_id,
            visit_start
        )
        update_student_learning_element(
            uow,
            student_id,
            learning_element_id,
            visit_start
        )
        student_learning_element_visit = DM.StudentLearningElementVisit(
            student_id,
            learning_element_id,
            visit_start
        )
        uow.student_learning_element_visit.add_student_learning_element_visit(
            student_learning_element_visit
        )
        uow.commit()
        result = student_learning_element_visit.serialize()
        return result


def add_student_topic_visit(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        topic_id,
        visit_start,
        previous_topic_id
) -> dict:
    with uow:
        update_previous_topic_visit(
            uow,
            student_id,
            visit_start
        )
        student_topic_visit = DM.StudentTopicVisit(
            student_id,
            topic_id,
            visit_start
        )
        uow.student_topic_visit.add_student_topic_visit(
            student_topic_visit
        )
        uow.commit()
        result = student_topic_visit.serialize()
        return result


def add_teacher_to_course(
        uow: unit_of_work.AbstractUnitOfWork,
        teacher_id,
        course_id
) -> dict:
    with uow:
        teacher_course = DM.TeacherCourse(
            teacher_id,
            course_id
        )
        uow.teacher_course.add_teacher_to_course(
            teacher_course
        )
        uow.commit()
        result = teacher_course.serialize()
        return result


def create_admin(
        uow: unit_of_work.AbstractUnitOfWork,
        user
) -> dict:
    with uow:
        admin = UA.Admin(user)
        uow.admin.create_admin(admin)
        uow.commit()
        result = admin.serialize()
        return result


def create_course(
        uow: unit_of_work.AbstractUnitOfWork,
        lms_id,
        name,
        university,
        created_by,
        created_at
) -> dict:
    with uow:
        course = DM.Course(lms_id, name, university)
        uow.course.create_course(course)
        uow.commit()
        result = course.serialize()
        add_course_creator_to_course(
            uow,
            created_by,
            result['id'],
            created_at
        )
        return result


def create_course_creator(
        uow: unit_of_work.AbstractUnitOfWork,
        user
) -> dict:
    with uow:
        course_creator = UA.CourseCreator(user)
        uow.course_creator.create_course_creator(course_creator)
        uow.commit()
        result = course_creator.serialize()
        return result


def create_course_topic(
        uow: unit_of_work.AbstractUnitOfWork,
        course_id,
        topic_id
) -> dict:
    with uow:
        course_topic = DM.CourseTopic(course_id, topic_id)
        uow.course_topic.create_course_topic(course_topic)
        uow.commit()
        result = course_topic.serialize()
        return result


def create_ils_input_answers(
        uow: unit_of_work.AbstractUnitOfWork,
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
        vv_9_f35=None
) -> dict:
    with uow:
        ils_input_answers = LM.IlsInputAnswers(
            questionnaire_id,
            vv_2_f7,
            vv_5_f19,
            vv_7_f27,
            vv_10_f39,
            vv_11_f43,
            vv_1_f3,
            vv_3_f11,
            vv_4_f15,
            vv_6_f23,
            vv_8_f31,
            vv_9_f35
        )
        uow.ils_input_answers.create_ils_input_answers(ils_input_answers)
        uow.commit()
        result = ils_input_answers.serialize()
        return result


def create_ils_perception_answers(
        uow: unit_of_work.AbstractUnitOfWork,
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
        si_9_f34=None
) -> dict:
    with uow:
        ils_perception_answers = LM.IlsPerceptionAnswers(
            questionnaire_id,
            si_1_f2,
            si_4_f14,
            si_7_f26,
            si_10_f38,
            si_11_f42,
            si_2_f6,
            si_3_f10,
            si_5_f18,
            si_6_f22,
            si_8_f30,
            si_9_f34
        )
        uow.ils_perception_answers\
            .create_ils_perception_answers(ils_perception_answers)
        uow.commit()
        result = ils_perception_answers.serialize()
        return result


def create_ils_processing_answers(
        uow: unit_of_work.AbstractUnitOfWork,
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
        ar_11_f41=None
) -> dict:
    with uow:
        ils_processing_answers = LM.IlsProcessingAnswers(
            questionnaire_id,
            ar_3_f9,
            ar_4_f13,
            ar_6_f21,
            ar_7_f25,
            ar_8_f29,
            ar_1_f1,
            ar_2_f5,
            ar_5_f17,
            ar_9_f33,
            ar_10_f37,
            ar_11_f41
        )
        uow.ils_processing_answers\
            .create_ils_processing_answers(ils_processing_answers)
        uow.commit()
        result = ils_processing_answers.serialize()
        return result


def create_ils_understanding_answers(
        uow: unit_of_work.AbstractUnitOfWork,
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
        sg_9_f36=None
) -> dict:
    with uow:
        ils_understanding_answers = LM.IlsUnderstandingAnswers(
            questionnaire_id,
            sg_1_f4,
            sg_2_f8,
            sg_4_f16,
            sg_10_f40,
            sg_11_f44,
            sg_3_f12,
            sg_5_f20,
            sg_6_f24,
            sg_7_f28,
            sg_8_f32,
            sg_9_f36
        )
        uow.ils_understanding_answers\
            .create_ils_understanding_answers(ils_understanding_answers)
        uow.commit()
        result = ils_understanding_answers.serialize()
        return result


def create_knowledge(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        knowledge = LM.Knowledge(characteristic_id)
        uow.knowledge.create_knowledge(knowledge)
        uow.commit()
        result = knowledge.serialize()
        return result


def create_learning_analytics(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        learning_analytics = LM.LearningAnalytics(characteristic_id)
        uow.learning_analytics.create_learning_analytics(learning_analytics)
        uow.commit()
        result = learning_analytics.serialize()
        return result


def create_learning_characteristics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = LM.LearningCharacteristic(student_id)
        uow.learning_characteristics.create_learning_characteristics(
            characteristic)
        uow.commit()
        create_knowledge(uow, characteristic.id)
        create_learning_analytics(uow, characteristic.id)
        create_learning_strategy(uow, characteristic.id)
        create_learning_style(uow, characteristic.id)
        result = characteristic.serialize()
        return result


def create_learning_element(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id,
        lms_id,
        activity_type,
        classification,
        name,
        created_by,
        created_at,
        university
) -> dict:
    with uow:
        learning_element = DM.LearningElement(lms_id,
                                              activity_type,
                                              classification,
                                              name,
                                              university,
                                              created_by,
                                              created_at)
        uow.learning_element.create_learning_element(learning_element)
        uow.commit()
        result = learning_element.serialize()
        create_topic_learning_element(uow, topic_id, result['id'])
        return result


def create_learning_strategy(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        learning_strategy = LM.LearningStrategy(characteristic_id)
        uow.learning_strategy.create_learning_strategy(learning_strategy)
        uow.commit()
        result = learning_strategy.serialize()
        return result


def create_learning_style(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        learning_style = LM.LearningStyle(characteristic_id)
        uow.learning_style.create_learning_style(learning_style)
        uow.commit()
        result = learning_style.serialize()
        return result


def create_list_k(
        uow: unit_of_work.AbstractUnitOfWork,
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
        lu3_f39
) -> dict:
    with uow:
        list_k = LM.ListK(
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
            lu3_f39
        )
        uow.list_k.create_list_k(list_k)
        uow.commit()
        result = list_k.serialize()
        return result


def create_questionnaire(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        vv_2_f7,
        vv_5_f19,
        vv_7_f27,
        vv_10_f39,
        vv_11_f43,
        si_1_f2,
        si_4_f14,
        si_7_f26,
        si_10_f38,
        si_11_f42,
        ar_3_f9,
        ar_4_f13,
        ar_6_f21,
        ar_7_f25,
        ar_8_f29,
        sg_1_f4,
        sg_2_f8,
        sg_4_f16,
        sg_10_f40,
        sg_11_f44,
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
        **kwargs
) -> dict:
    with uow:
        questionnaire = LM.Questionnaire(student_id)
        uow.questionnaire.create_questionnaire(questionnaire)
        uow.commit()
        create_ils_input_answers(uow,
                                 questionnaire.id,
                                 vv_2_f7,
                                 vv_5_f19,
                                 vv_7_f27,
                                 vv_10_f39,
                                 vv_11_f43,
                                 kwargs['vv_1_f3']
                                 if 'vv_1_f3' in kwargs else None,
                                 kwargs['vv_3_f11']
                                 if 'vv_3_f11' in kwargs else None,
                                 kwargs['vv_4_f15']
                                 if 'vv_4_f15' in kwargs else None,
                                 kwargs['vv_6_f23']
                                 if 'vv_6_f23' in kwargs else None,
                                 kwargs['vv_8_f31']
                                 if 'vv_8_f31' in kwargs else None,
                                 kwargs['vv_9_f35']
                                 if 'vv_9_f35' in kwargs else None
                                 )
        create_ils_perception_answers(uow,
                                      questionnaire.id,
                                      si_1_f2,
                                      si_4_f14,
                                      si_7_f26,
                                      si_10_f38,
                                      si_11_f42
                                      )
        create_ils_processing_answers(uow,
                                      questionnaire.id,
                                      ar_3_f9,
                                      ar_4_f13,
                                      ar_6_f21,
                                      ar_7_f25,
                                      ar_8_f29
                                      )
        create_ils_understanding_answers(uow,
                                         questionnaire.id,
                                         sg_1_f4,
                                         sg_2_f8,
                                         sg_4_f16,
                                         sg_10_f40,
                                         sg_11_f44
                                         )
        create_list_k(uow,
                      questionnaire.id,
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
                      lu3_f39)
        result = questionnaire.serialize()
        return result


def create_settings(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
) -> dict:
    with uow:
        setting = UA.Settings(user_id)
        uow.settings.create_settings(setting)
        uow.commit()
        result = setting.serialize()
        return result


def create_student(
        uow: unit_of_work.AbstractUnitOfWork,
        user
) -> dict:
    with uow:
        student = UA.Student(user)
        uow.student.create_student(student)
        uow.commit()
        create_learning_characteristics(uow, student.id)
        result = student.serialize()
        return result


def create_teacher(
        uow: unit_of_work.AbstractUnitOfWork,
        user
) -> dict:
    with uow:
        teacher = UA.Teacher(user)
        uow.teacher.create_teacher(teacher)
        uow.commit()
        result = teacher.serialize()
        return result


def create_topic(
    uow: unit_of_work.AbstractUnitOfWork,
    course_id,
    lms_id,
    is_topic,
    parent_id,
    contains_le,
    name,
    university,
    created_by,
    created_at,

) -> dict:
    with uow:
        topic = DM.Topic(lms_id, is_topic, parent_id, contains_le,
                         name, university, created_by, created_at)
        uow.topic.create_topic(topic)
        uow.commit()
        result = topic.serialize()
        create_course_topic(uow, course_id, result['id'])
        return result


def create_topic_learning_element(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id,
        learning_element_id
) -> dict:
    with uow:
        topic_learning_element = DM.TopicLearningElement(
            topic_id,
            learning_element_id
        )
        uow.topic_learning_element.create_topic_learning_element(
            topic_learning_element
        )
        uow.commit()
        result = topic_learning_element.serialize()
        return result


def create_user(
        uow: unit_of_work.AbstractUnitOfWork,
        name,
        university,
        lms_user_id,
        role
) -> dict:
    with uow:
        user = UA.User(name, university, lms_user_id, role)
        uow.user.create_user(user)
        uow.commit()
        user.settings = create_settings(
            uow, user.id)
        match role.lower():
            case "admin":
                create_admin(uow, user)
            case "course creator":
                create_course_creator(uow, user)
            case "student":
                create_student(uow, user)
            case "teacher":
                create_teacher(uow, user)
        result = user.serialize()
    return result


def delete_admin(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        uow.admin.delete_admin(user_id)
        uow.commit()
        return {}


def delete_course(
        uow: unit_of_work.AbstractUnitOfWork,
        course_id
):
    with uow:
        uow.course.delete_course(course_id)
        uow.commit()
        return {}


def delete_course_creator(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        uow.course_creator.delete_course_creator(user_id)
        uow.commit()
        return {}


def delete_course_topic_by_course(
        uow: unit_of_work.AbstractUnitOfWork,
        course_id
) -> dict:
    with uow:
        uow.course_topic.delete_course_topic_by_course(
            course_id
        )
        uow.commit()
        return {}


def delete_course_topic_by_topic(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id
) -> dict:
    with uow:
        uow.course_topic.delete_course_topic_by_topic(
            topic_id
        )
        uow.commit()
        return {}


def delete_ils_input_answers(
        uow: unit_of_work.AbstractUnitOfWork,
        questionnaire_id
):
    with uow:
        uow.ils_input_answers\
            .delete_ils_input_answers(questionnaire_id)
        uow.commit()
        return{}


def delete_ils_perception_answers(
        uow: unit_of_work.AbstractUnitOfWork,
        questionnaire_id
):
    with uow:
        uow.ils_perception_answers\
            .delete_ils_perception_answers(questionnaire_id)
        uow.commit()
        return{}


def delete_ils_processing_answers(
        uow: unit_of_work.AbstractUnitOfWork,
        questionnaire_id
):
    with uow:
        uow.ils_processing_answers\
            .delete_ils_processing_answers(questionnaire_id)
        uow.commit()
        return{}


def delete_ils_understanding_answers(
        uow: unit_of_work.AbstractUnitOfWork,
        questionnaire_id
):
    with uow:
        uow.ils_understanding_answers\
            .delete_ils_understanding_answers(questionnaire_id)
        uow.commit()
        return{}


def delete_learning_element(
        uow: unit_of_work.AbstractUnitOfWork,
        learning_element_id
):
    with uow:
        uow.learning_element\
            .delete_learning_element(learning_element_id)
        uow.commit()
        return {}


def delete_list_k(
        uow: unit_of_work.AbstractUnitOfWork,
        questionnaire_id
):
    with uow:
        uow.list_k\
            .delete_list_k(questionnaire_id)
        uow.commit()
        return{}


def delete_questionnaire(
        uow: unit_of_work.AbstractUnitOfWork,
        questionnaire_id
):
    with uow:
        uow.questionnaire\
            .delete_questionnaire(questionnaire_id)
        uow.commit()
        return{}


def delete_settings(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        uow.settings.delete_settings(user_id)
        uow.commit()
        return {}


def delete_student(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        student = uow.student.get_student_by_id(user_id)
        delete_learning_characteristics(uow, student[0].id)
        uow.student.delete_student(user_id)
        uow.commit()
        return {}


def delete_teacher(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        uow.teacher.delete_teacher(user_id)
        uow.commit()
        return {}


def delete_user(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id,
        lms_user_id
):
    with uow:
        user = get_user_by_id(uow, user_id, lms_user_id)
        match user['role']:
            case "admin":
                delete_admin(uow, user['id'])
            case "course_creator":
                delete_course_creator(uow, user['id'])
            case "student":
                delete_student(uow, user['id'])
            case "teacher":
                delete_teacher(uow, user['id'])
        delete_settings(uow, user_id)
        uow.user.delete_user(user_id, lms_user_id)
        uow.commit()
        return {}


def delete_knowledge(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
):
    with uow:
        uow.knowledge.delete_knowledge(characteristic_id)
        uow.commit()
        return {}


def delete_learning_analytics(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
):
    with uow:
        uow.learning_analytics.delete_learning_analytics(characteristic_id)
        uow.commit()
        return {}


def delete_learning_characteristics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
):
    with uow:
        characteristic = get_learning_characteristics(uow, student_id)
        delete_knowledge(uow, characteristic['id'])
        delete_learning_analytics(uow, characteristic['id'])
        delete_learning_strategy(uow, characteristic['id'])
        delete_learning_style(uow, characteristic['id'])
        uow.learning_characteristics.delete_learning_characteristics(
            student_id)
        uow.commit()
        return {}


def delete_learning_strategy(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
):
    with uow:
        uow.learning_strategy.delete_learning_strategy(characteristic_id)
        uow.commit()
        return {}


def delete_learning_style(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
):
    with uow:
        uow.learning_style.delete_learning_style(characteristic_id)
        uow.commit()
        return {}


def delete_topic(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id
):
    with uow:
        uow.topic.delete_course_topic_by_topic(topic_id)
        uow.commit()
        uow.topic.delete_topic(topic_id)
        uow.commit()
        return {}


def delete_topic_learning_element_by_topic(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id
):
    with uow:
        uow.topic_learning_element.delete_topic_learning_element_by_topic(
            topic_id
        )
        uow.commit()
        return {}


def delete_topic_learning_element_by_learning_element(
        uow: unit_of_work.AbstractUnitOfWork,
        learning_element_id
):
    with uow:
        uow.topic_learning_element\
            .delete_topic_learning_element_by_learning_element(
                learning_element_id
            )
        uow.commit()
        return {}


def get_course_by_id(
        uow: unit_of_work.AbstractUnitOfWork,
        course_id
) -> dict:
    with uow:
        course = uow.course.get_course_by_id(course_id)
        if course == []:
            result = {}
        else:
            result = course[0].serialize()
        return result


def get_courses_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        courses = uow.course.get_courses_by_student_id(
            student_id
        )
        result_courses = []
        for course in courses:
            course_by_id = get_course_by_id(uow, course.course_id)
            result_courses.append(course_by_id)
        result = {}
        result['courses'] = result_courses
        return result


def get_course_topic_by_course(
        uow: unit_of_work.AbstractUnitOfWork,
        course_id
) -> dict:
    with uow:
        course_topic = uow.course_topic.get_course_topic_by_course(
            course_id
        )
        if course_topic == []:
            result = {}
        else:
            result = course_topic[0].serialize()
        return result


def get_course_topic_by_topic(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id
) -> dict:
    with uow:
        course_topic = uow.course_topic.get_course_topic_by_topic(
            topic_id
        )
        if course_topic == []:
            result = {}
        else:
            result = course_topic[0].serialize()
        return result


def get_knowledge(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        knowledge = uow.knowledge.get_knowledge(characteristic_id)
        if knowledge == []:
            result = {}
        else:
            result = knowledge[0].serialize()
        return result


def get_knowledge_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = get_learning_characteristics(
            uow,
            student_id
        )
        learning_style = uow.learning_style.get_knowledge(
            characteristic['id']
        )
        result = learning_style[0].serialize()
        return result


def get_learning_analytics(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        analytics = uow.learning_analytics\
            .get_learning_analytics(
                characteristic_id)
        if analytics == []:
            result = {}
        else:
            result = analytics[0].serialize()
        return result


def get_learning_analytics_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = get_learning_characteristics(
            uow,
            student_id
        )
        learning_style = uow.learning_style.get_learning_analytics(
            characteristic['id']
        )
        result = learning_style[0].serialize()
        return result


def get_learning_characteristics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristics = uow.learning_characteristics\
            .get_learning_characteristics(
                student_id)
        if characteristics == []:
            result = {}
        else:
            characteristics = characteristics[0]
            characteristics.knowledge = get_knowledge(
                uow,
                characteristics.id
            )
            characteristics.learning_analytics = get_learning_analytics(
                uow,
                characteristics.id
            )
            characteristics.learning_strategy = get_learning_strategy(
                uow,
                characteristics.id
            )
            characteristics.learning_style = get_learning_style(
                uow,
                characteristics.id
            )
            result = characteristics.serialize()
        return result


def get_learning_element_by_id(
        uow: unit_of_work.AbstractUnitOfWork,
        learning_element_id
) -> dict:
    with uow:
        learning_element = uow.learning_element\
            .get_learning_element_by_id(learning_element_id)
        if learning_element == []:
            result = {}
        else:
            result = learning_element[0].serialize()
        return result


def get_learning_elements_for_course_and_topic_id(
        uow: unit_of_work.AbstractUnitOfWork,
        course_id,
        topic_id
) -> dict:
    with uow:
        learning_elements = get_learning_elements_for_topic_id(
            uow,
            topic_id
        )
        result = {}
        result['learning_elements'] = learning_elements
        return result


def get_learning_elements_for_topic_id(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id
) -> list:
    with uow:
        try:
            learning_elements = uow.topic_learning_element\
                .get_topic_learning_element_by_topic(topic_id)
            results = []
            for le in learning_elements:
                results.append(le.serialize())
            return results
        except Exception:
            return []


def get_learning_strategy(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        strategy = uow.learning_strategy.get_learning_strategy(
            characteristic_id)
        if strategy == []:
            result = {}
        else:
            result = strategy[0].serialize()
        return result


def get_learning_strategy_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = get_learning_characteristics(
            uow,
            student_id
        )
        learning_style = uow.learning_style.get_learning_strategy(
            characteristic['id']
        )
        result = learning_style[0].serialize()
        return result


def get_learning_style(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        style = uow.learning_style.get_learning_style(characteristic_id)
        if style == []:
            result = {}
        else:
            result = style[0].serialize()
        return result


def get_learning_style_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = get_learning_characteristics(
            uow,
            student_id
        )
        learning_style = uow.learning_style.get_learning_style(
            characteristic['id']
        )
        result = learning_style[0].serialize()
        return result


def get_sub_topic_by_topic_id(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id
) -> dict:
    with uow:
        subtopics = uow.topic.get_sub_topics_for_topic_id(
            topic_id
        )
        result_subtopics = []
        for subtopic in subtopics:
            result_subtopics.append(subtopic.serialize())
        result = {}
        result['topics'] = result_subtopics
        return result


def get_topic_by_id(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id
) -> dict:
    with uow:
        topic = uow.topic.get_topic_by_id(topic_id)
        if topic == []:
            result = {}
        else:
            result = topic[0].serialize()
        return result


def get_topics_by_student_and_course_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        course_id
) -> dict:
    with uow:
        topics = get_topics_for_course_id(
            uow,
            course_id
        )
        result_topics = []
        for topic in topics:
            topic_by_id = get_topic_by_id(uow, topic['topic_id'])
            result_topics.append(topic_by_id)
        result = {}
        result['topics'] = result_topics
        return result


def get_topics_for_course_id(
        uow: unit_of_work.AbstractUnitOfWork,
        course_id
) -> list:
    with uow:
        try:
            topics = uow.course_topic.get_course_topic_by_course(course_id)
            results = []
            for topic in topics:
                results.append(topic.serialize())
            return results
        except Exception:
            return[]


def get_topic_learning_element_by_topic(
        uow: unit_of_work.AbstractUnitOfWork,
        topic_id
) -> dict:
    with uow:
        topic_learning_element = uow.topic_learning_element\
            .get_topic_learning_element_by_topic(
                topic_id
            )
        if topic_learning_element == []:
            result = {}
        else:
            result = topic_learning_element[0].serialize()
        return result


def get_topic_learning_element_by_learning_element(
        uow: unit_of_work.AbstractUnitOfWork,
        learning_element_id
) -> dict:
    with uow:
        topic_learning_element = uow.topic_learning_element\
            .get_topic_learning_element_by_learning_element(
                learning_element_id
            )
        if topic_learning_element == []:
            result = {}
        else:
            result = topic_learning_element[0].serialize()
        return result


def reset_knowledge(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        knowledge = LM.Knowledge(characteristic_id)
        uow.knowledge.update_knowledge(characteristic_id, knowledge)
        uow.commit()
        return knowledge.serialize()


def reset_knowledge_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = get_knowledge(
            uow,
            student_id
        )
        result = reset_knowledge(
            uow,
            characteristic['id']
        )
        return result


def reset_learning_analytics(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        analytics = LM.LearningAnalytics(characteristic_id)
        uow.learning_analytics.update_learning_analytics(
            characteristic_id, analytics)
        uow.commit()
        return analytics.serialize()


def reset_learning_analytics_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = get_learning_analytics(
            uow,
            student_id
        )
        result = reset_learning_analytics(
            uow,
            characteristic['id']
        )
        return result


def reset_learning_characteristics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristics = uow.learning_characteristics\
            .get_learning_characteristics(
                student_id)
        characteristics[0].knowledge = reset_knowledge(
            uow, characteristics[0].id)
        characteristics[0].learning_analytics = reset_learning_analytics(
            uow, characteristics[0].id)
        characteristics[0].learning_strategy = reset_learning_strategy(
            uow, characteristics[0].id)
        characteristics[0].learning_style = reset_learning_style(
            uow, characteristics[0].id)
        return characteristics[0].serialize()


def reset_learning_strategy(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        strategy = LM.LearningStrategy(characteristic_id)
        uow.learning_strategy.update_learning_strategy(
            characteristic_id, strategy)
        uow.commit()
        return strategy.serialize()


def reset_learning_strategy_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = get_learning_characteristics(
            uow,
            student_id
        )
        result = reset_learning_strategy(
            uow,
            characteristic['id']
        )
        return result


def reset_learning_style(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        style = LM.LearningStyle(characteristic_id)
        uow.learning_style.update_learning_style(characteristic_id, style)
        uow.commit()
        return style.serialize()


def reset_learning_style_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = get_learning_characteristics(
            uow,
            student_id
        )
        result = reset_learning_style(
            uow,
            characteristic['id']
        )
        return result


def reset_settings(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        settings = UA.Settings(user_id)
        uow.settings.update_settings(user_id, settings)
        uow.commit()
        return settings.serialize()


def get_settings_for_user(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
) -> dict:
    with uow:
        settings = uow.settings.get_settings(user_id)
        if settings == []:
            result = {}
        else:
            result = settings[0].serialize()
        return result


def get_user_by_id(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id,
        lms_user_id
) -> dict:
    with uow:
        user = uow.user.get_user_by_id(user_id, lms_user_id)
        settings = uow.settings.get_settings(user_id)
        if user == []:
            result = {}
        else:
            user[0].settings = settings[0].serialize()
            result = user[0].serialize()
        return result


def update_course(
        uow: unit_of_work.AbstractUnitOfWork,
        course_id,
        lms_id,
        name,
        university
) -> dict:
    with uow:
        course = DM.Course(lms_id, name, university)
        uow.course.update_course(course_id, course)
        uow.commit()
        return course.serialize()


def update_learning_element(
        uow: unit_of_work.AbstractUnitOfWork,
        learning_element_id,
        lms_id,
        activity_type,
        classification,
        name,
        created_by,
        created_at,
        last_updated,
        university
) -> dict:
    with uow:
        learning_element = DM.LearningElement(
            lms_id,
            activity_type,
            classification,
            name,
            university,
            created_by,
            created_at,
            last_updated
        )
        uow.learning_element.update_learning_element(
            learning_element_id,
            learning_element
        )
        uow.commit()
        result = learning_element.serialize()
        return result


def update_learning_style_by_student_id(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        perception_dimension,
        perception_value,
        input_dimension,
        input_value,
        processing_dimension,
        processing_value,
        understanding_dimension,
        understanding_value
) -> dict:
    with uow:
        characteristic = get_learning_characteristics(
            uow,
            student_id
        )
        learning_style = LM.LearningStyle(
            characteristic['id'],
            perception_dimension,
            perception_value,
            input_dimension,
            input_value,
            processing_dimension,
            processing_value,
            understanding_dimension,
            understanding_value
        )
        uow.learning_style.update_learning_style(
            characteristic['id'],
            learning_style
        )
        uow.commit()
        result = learning_style.serialize()
        return result


def update_previous_learning_element_visit(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        visit_time
) -> dict:
    with uow:
        uow.student_learning_element_visit\
            .update_previous_learning_element_visit(
                student_id,
                visit_time
            )
        uow.commit()


def update_previous_topic_visit(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        visit_time
) -> dict:
    with uow:
        uow.student_topic_visit.update_previous_topic_visit(
            student_id,
            visit_time
        )
        uow.commit()


def update_settings_for_user(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id,
        theme,
        pswd=None
) -> dict:
    with uow:
        settings = UA.Settings(user_id, theme, pswd)
        uow.settings.update_settings(user_id, settings)
        uow.commit()
        return settings.serialize()


def update_student_learning_element(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id,
        learning_element_id,
        visit_time
):
    with uow:
        uow.student_learning_element.update_student_learning_element(
            student_id,
            learning_element_id,
            visit_time
        )
        uow.commit()


def update_topic(
    uow: unit_of_work.AbstractUnitOfWork,
    topic_id,
    lms_id,
    is_topic,
    parent_id,
    contains_le,
    name,
    university,
    created_by,
    created_at,
    last_updated
) -> dict:
    with uow:
        topic = DM.Topic(lms_id, is_topic, parent_id, contains_le, name,
                         university, created_at, created_by, last_updated)
        uow.topic.update_topic(topic_id, topic)
        uow.commit()
        return topic.serialize()


def update_user(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id,
        lms_user_id,
        name,
        university
) -> dict:
    with uow:
        user = UA.User(name, university, lms_user_id)
        uow.user.update_user(user_id, lms_user_id, user)
        uow.commit()
        settings = uow.settings.get_settings(user_id)
        user.settings = settings[0].serialize()
        return user.serialize()
