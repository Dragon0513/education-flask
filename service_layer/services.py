from flask.wrappers import Request

import errors.errors as err
from domain.domainModel import model as DM
from domain.learnersModel import basic_ils_algorithm as BILSA
from domain.learnersModel import basic_listk_algorithm as BLKA
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.userAdministartion import model as UA
from service_layer import unit_of_work
from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask


def add_course_creator_to_course(
    uow: unit_of_work.AbstractUnitOfWork, created_by, course_id, created_at
) -> dict:
    with uow:
        course_creator = uow.course_creator.get_course_creator_by_id(created_by)
        course_creator_course = DM.CourseCreatorCourse(
            course_creator[0].id, course_id, created_at
        )
        uow.course_creator_course.add_course_creator_to_course(course_creator_course)
        uow.commit()
        result = course_creator_course.serialize()
        return result


def add_student_to_course(
    uow: unit_of_work.AbstractUnitOfWork, student_id, course_id
) -> dict:
    with uow:
        uow.student.get_student_by_student_id(student_id)
        get_course_by_id(uow, None, None, course_id)
        student_course = uow.student_course.get_student_course(student_id, course_id)
        if student_course != []:
            raise err.AlreadyExisting()
        characteristics = get_learning_characteristics(uow, student_id)
        learning_style = get_learning_style(uow, characteristics["id"])
        student_course = DM.StudentCourse(
            student_id,
            course_id,
            learning_style["perception_dimension"],
            learning_style["perception_value"],
            learning_style["input_dimension"],
            learning_style["input_value"],
            learning_style["processing_dimension"],
            learning_style["processing_value"],
            learning_style["understanding_dimension"],
            learning_style["understanding_value"],
        )
        uow.student_course.add_student_to_course(student_course)
        uow.commit()
        result = student_course.serialize()
        add_student_to_topics(uow, student_id, course_id)
        return result


def add_student_to_learning_element(
    uow: unit_of_work.AbstractUnitOfWork, student_id, topic_id
):
    with uow:
        learning_elements = get_learning_elements_for_topic_id(uow, topic_id)
        for le in learning_elements:
            student_learning_element = DM.StudentLearningElement(
                student_id, le["learning_element_id"]
            )
            uow.student_learning_element.add_student_to_learning_element(
                student_learning_element
            )
            uow.commit()


def add_student_to_topics(uow: unit_of_work.AbstractUnitOfWork, student_id, course_id):
    with uow:
        topics = get_topics_for_course_id(uow, course_id)
        for topic in topics:
            student_topic = DM.StudentTopic(student_id, topic["topic_id"])
            uow.student_topic.add_student_to_topic(student_topic)
            uow.commit()
            add_student_to_learning_element(uow, student_id, topic["topic_id"])


def add_student_learning_element_visit(
    uow: unit_of_work.AbstractUnitOfWork, student_id, learning_element_id, visit_start
) -> dict:
    with uow:
        update_previous_learning_element_visit(uow, student_id, visit_start)
        update_student_learning_element(
            uow, student_id, learning_element_id, visit_start
        )
        student_learning_element_visit = DM.StudentLearningElementVisit(
            student_id, learning_element_id, visit_start
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
    previous_topic_id,
) -> dict:
    with uow:
        if previous_topic_id is not None:
            update_previous_topic_visit(uow, student_id, visit_start)
        student_topic_visit = DM.StudentTopicVisit(student_id, topic_id, visit_start)
        uow.student_topic_visit.add_student_topic_visit(student_topic_visit)
        uow.commit()
        result = student_topic_visit.serialize()
        return result


def add_teacher_to_course(
    uow: unit_of_work.AbstractUnitOfWork, teacher_id, course_id
) -> dict:
    with uow:
        get_course_by_id(uow, None, None, course_id)
        user = uow.teacher.get_teacher_by_teacher_id(teacher_id)
        teacher_coures = get_courses_for_teacher(uow, user[0].user_id, teacher_id)
        for course in teacher_coures["courses"]:
            if int(course["id"]) == int(course_id):
                raise err.AlreadyExisting()
        teacher_course = DM.TeacherCourse(teacher_id, course_id)
        uow.teacher_course.add_teacher_to_course(teacher_course)
        uow.commit()
        result = teacher_course.serialize()
        return result


def create_admin(uow: unit_of_work.AbstractUnitOfWork, user) -> dict:
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
    created_at,
) -> dict:
    with uow:
        course = DM.Course(lms_id, name, university, None, None, None)
        uow.course.create_course(course)
        uow.commit()
        result = course.serialize()
        add_course_creator_to_course(uow, created_by, result["id"], created_at)
        return result


def create_course_creator(uow: unit_of_work.AbstractUnitOfWork, user) -> dict:
    with uow:
        course_creator = UA.CourseCreator(user)
        uow.course_creator.create_course_creator(course_creator)
        uow.commit()
        result = course_creator.serialize()
        return result


def create_course_topic(
    uow: unit_of_work.AbstractUnitOfWork, course_id, topic_id
) -> dict:
    with uow:
        course_topic = DM.CourseTopic(course_id, topic_id)
        uow.course_topic.create_course_topic(course_topic)
        uow.commit()
        result = course_topic.serialize()
        return result


def create_ils_input_answers(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id, answers
) -> dict:
    with uow:
        ils_input_answers = LM.IlsInputAnswers(
            questionnaire_ils_id,
            answers["vv_2_f7"],
            answers["vv_5_f19"],
            answers["vv_7_f27"],
            answers["vv_10_f39"],
            answers["vv_11_f43"],
            answers["vv_1_f3"] if "vv_1_f3" in answers.keys() else None,
            answers["vv_3_f11"] if "vv_3_f11" in answers.keys() else None,
            answers["vv_4_f15"] if "vv_4_f15" in answers.keys() else None,
            answers["vv_6_f23"] if "vv_6_f23" in answers.keys() else None,
            answers["vv_8_f31"] if "vv_8_f31" in answers.keys() else None,
            answers["vv_9_f35"] if "vv_9_f35" in answers.keys() else None,
        )
        uow.ils_input_answers.create_ils_input_answers(ils_input_answers)
        uow.commit()
        result = ils_input_answers.serialize()
        return result


def create_ils_perception_answers(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id, answers
) -> dict:
    with uow:
        ils_perception_answers = LM.IlsPerceptionAnswers(
            questionnaire_ils_id,
            answers["si_1_f2"],
            answers["si_4_f14"],
            answers["si_7_f26"],
            answers["si_10_f38"],
            answers["si_11_f42"],
            answers["si_2_f6"] if "si_2_f6" in answers.keys() else None,
            answers["si_3_f10"] if "si_3_f10" in answers.keys() else None,
            answers["si_5_f18"] if "si_5_f18" in answers.keys() else None,
            answers["si_6_f22"] if "si_6_f22" in answers.keys() else None,
            answers["si_8_f30"] if "si_8_f30" in answers.keys() else None,
            answers["si_9_f34"] if "si_9_f34" in answers.keys() else None,
        )
        uow.ils_perception_answers.create_ils_perception_answers(ils_perception_answers)
        uow.commit()
        result = ils_perception_answers.serialize()
        return result


def create_ils_processing_answers(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id, answers
) -> dict:
    with uow:
        ils_processing_answers = LM.IlsProcessingAnswers(
            questionnaire_ils_id,
            answers["ar_3_f9"],
            answers["ar_4_f13"],
            answers["ar_6_f21"],
            answers["ar_7_f25"],
            answers["ar_8_f29"],
            answers["ar_1_f1"] if "ar_1_f1" in answers.keys() else None,
            answers["ar_2_f5"] if "ar_2_f5" in answers.keys() else None,
            answers["ar_5_f17"] if "ar_5_f17" in answers.keys() else None,
            answers["ar_9_f33"] if "ar_9_f33" in answers.keys() else None,
            answers["ar_10_f37"] if "ar_10_f37" in answers.keys() else None,
            answers["ar_11_f41"] if "ar_11_f41" in answers.keys() else None,
        )
        uow.ils_processing_answers.create_ils_processing_answers(ils_processing_answers)
        uow.commit()
        result = ils_processing_answers.serialize()
        return result


def create_ils_understanding_answers(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id, answers
) -> dict:
    with uow:
        ils_understanding_answers = LM.IlsUnderstandingAnswers(
            questionnaire_ils_id,
            answers["sg_1_f4"],
            answers["sg_2_f8"],
            answers["sg_4_f16"],
            answers["sg_10_f40"],
            answers["sg_11_f44"],
            answers["sg_3_f12"] if "sg_3_f12" in answers.keys() else None,
            answers["sg_5_f20"] if "sg_5_f20" in answers.keys() else None,
            answers["sg_6_f24"] if "sg_6_f24" in answers.keys() else None,
            answers["sg_7_f28"] if "sg_7_f28" in answers.keys() else None,
            answers["sg_8_f32"] if "sg_8_f32" in answers.keys() else None,
            answers["sg_9_f36"] if "sg_9_f36" in answers.keys() else None,
        )
        uow.ils_understanding_answers.create_ils_understanding_answers(
            ils_understanding_answers
        )
        uow.commit()
        result = ils_understanding_answers.serialize()
        return result


def create_knowledge(uow: unit_of_work.AbstractUnitOfWork, characteristic_id) -> dict:
    with uow:
        knowledge = LM.Knowledge(characteristic_id)
        uow.knowledge.create_knowledge(knowledge)
        uow.commit()
        result = knowledge.serialize()
        return result


def create_learning_analytics(
    uow: unit_of_work.AbstractUnitOfWork, characteristic_id
) -> dict:
    with uow:
        learning_analytics = LM.LearningAnalytics(characteristic_id)
        uow.learning_analytics.create_learning_analytics(learning_analytics)
        uow.commit()
        result = learning_analytics.serialize()
        return result


def create_learning_characteristics(
    uow: unit_of_work.AbstractUnitOfWork, student_id
) -> dict:
    with uow:
        characteristic = LM.LearningCharacteristic(student_id)
        uow.learning_characteristics.create_learning_characteristics(characteristic)
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
    university,
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
        )
        uow.learning_element.create_learning_element(learning_element)
        uow.commit()
        result = learning_element.serialize()
        create_topic_learning_element(uow, topic_id, result["id"])
        return result


def create_learning_path(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    algorithm,
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        learning_elements = get_learning_elements_for_topic_id(uow, topic_id)
        if learning_elements == []:
            raise err.NoLearningElementsError()
        paths_exisiting = get_learning_paths(uow=uow, student_id=student_id)
        for path_exisiting in paths_exisiting:
            condition1 = int(path_exisiting["course_id"]) == int(course_id)
            condition2 = (
                int(path_exisiting["topic_id"]) == int(topic_id)
                if path_exisiting["topic_id"]
                else False
            )
            if condition1 and condition2:
                delete_learning_path_learning_element(
                    uow=uow, learning_path_id=int(path_exisiting["id"])
                )
                delete_learning_path_topic(
                    uow=uow, learning_path_id=int(path_exisiting["id"])
                )
                delete_learning_path(
                    uow=uow, learning_path_id=int(path_exisiting["id"])
                )
        learning_path = TM.LearningPath(student_id, course_id, algorithm, topic_id)
        uow.learning_path.create_learning_path(learning_path)
        uow.commit()
        result = learning_path.serialize()
        if len(learning_elements) == 1:
            le = get_learning_element_by_id(
                uow=uow,
                user_id=user_id,
                lms_user_id=lms_user_id,
                student_id=student_id,
                course_id=course_id,
                topic_id=topic_id,
                learning_element_id=learning_elements[0]["learning_element_id"],
            )
            path_element = TM.LearningPathLearningElement(
                learning_element_id=le["id"],
                learning_path_id=result["id"],
                recommended=True,
                position=1,
                learning_element=None,
            )
            uow.learning_path_learning_element.create_learning_path_learning_element(
                path_element
            )
            learning_path.path = le["classification"]
            result = learning_path.serialize()
        else:
            learning_style = get_learning_style_by_student_id(
                uow=uow, student_id=student_id
            )
            list_of_les = []
            for le in learning_elements:
                element = get_learning_element_by_id(
                    uow=uow,
                    user_id=user_id,
                    lms_user_id=lms_user_id,
                    student_id=student_id,
                    course_id=course_id,
                    topic_id=topic_id,
                    learning_element_id=le["learning_element_id"],
                )
                list_of_les.append(element)
            learning_path.get_learning_path(
                student_id=student_id,
                learning_style=learning_style,
                _algorithm=algorithm.lower(),
                list_of_les=list_of_les,
            )
            result = learning_path.serialize()
            for i, le in enumerate(result["path"].replace(",", "").split()):
                for temp in list_of_les:
                    if temp["classification"] == le:
                        path_element = TM.LearningPathLearningElement(
                            learning_element_id=temp["id"],
                            learning_path_id=result["id"],
                            recommended=True if i == 0 else False,
                            position=i + 1,
                            learning_element=None,
                        )
                        # fmt: off
                        uow.learning_path_learning_element.\
                            create_learning_path_learning_element(path_element)
        uow.commit()
        return result


def create_learning_strategy(
    uow: unit_of_work.AbstractUnitOfWork, characteristic_id
) -> dict:
    with uow:
        learning_strategy = LM.LearningStrategy(characteristic_id)
        uow.learning_strategy.create_learning_strategy(learning_strategy)
        uow.commit()
        result = learning_strategy.serialize()
        return result


def create_learning_style(
    uow: unit_of_work.AbstractUnitOfWork, characteristic_id
) -> dict:
    with uow:
        learning_style = LM.LearningStyle(characteristic_id)
        uow.learning_style.create_learning_style(learning_style)
        uow.commit()
        result = learning_style.serialize()
        return result


def create_questionnaire_list_k(
    uow: unit_of_work.AbstractUnitOfWork, student_id, list_k_answers
) -> dict:
    with uow:
        exist = uow.questionnaire_list_k.get_questionnaire_list_k_by_student_id(
            student_id
        )
        if exist != []:
            delete_questionnaire_list_k(uow, exist[0].id)
        questionnaire_list_k = LM.QuestionnaireListK(
            student_id,
            list_k_answers["org1_f1"],
            list_k_answers["org2_f2"],
            list_k_answers["org3_f3"],
            list_k_answers["elab1_f4"],
            list_k_answers["elab2_f5"],
            list_k_answers["elab3_f6"],
            list_k_answers["crit_rev1_f7"],
            list_k_answers["crit_rev2_f8"],
            list_k_answers["crit_rev3_f9"],
            list_k_answers["rep1_f10"],
            list_k_answers["rep2_f11"],
            list_k_answers["rep3_f12"],
            list_k_answers["goal_plan1_f13"],
            list_k_answers["goal_plan2_f14"],
            list_k_answers["goal_plan3_f15"],
            list_k_answers["con1_f16"],
            list_k_answers["con2_f17"],
            list_k_answers["con3_f18"],
            list_k_answers["reg1_f19"],
            list_k_answers["reg2_f20"],
            list_k_answers["reg3_f21"],
            list_k_answers["att1_f22"],
            list_k_answers["att2_f23"],
            list_k_answers["att3_f24"],
            list_k_answers["eff1_f25"],
            list_k_answers["eff2_f26"],
            list_k_answers["eff3_f27"],
            list_k_answers["time1_f28"],
            list_k_answers["time2_f29"],
            list_k_answers["time3_f30"],
            list_k_answers["lrn_w_cls1_f31"],
            list_k_answers["lrn_w_cls2_f32"],
            list_k_answers["lrn_w_cls3_f33"],
            list_k_answers["lit_res1_f34"],
            list_k_answers["lit_res2_f35"],
            list_k_answers["lit_res3_f36"],
            list_k_answers["lrn_env1_f37"],
            list_k_answers["lrn_env2_f38"],
            list_k_answers["lrn_env3_f39"],
        )
        uow.questionnaire_list_k.create_questionnaire_list_k(questionnaire_list_k)
        uow.commit()
        questionnaire_list_k.serialize()
        # Calculate basic learning strategy / implement other algorithm here
        basic_learning_strategy = BLKA.calculate_basic_learning_strategy(list_k_answers)
        # Get user_id with the student_id
        student = uow.student.get_student_by_student_id(student_id)
        user = get_user_by_id(uow, student[0].user_id, None)
        update_learning_strategy_by_student_id(
            uow,
            user["id"],
            user["lms_user_id"],
            student_id,
            basic_learning_strategy[0][4],
            basic_learning_strategy[0][0],
            basic_learning_strategy[0][1],
            basic_learning_strategy[0][2],
            basic_learning_strategy[0][3],
            basic_learning_strategy[1][3],
            basic_learning_strategy[1][0],
            basic_learning_strategy[1][1],
            basic_learning_strategy[1][2],
            basic_learning_strategy[2][3],
            basic_learning_strategy[2][0],
            basic_learning_strategy[2][1],
            basic_learning_strategy[2][2],
            basic_learning_strategy[3][3],
            basic_learning_strategy[3][0],
            basic_learning_strategy[3][1],
            basic_learning_strategy[3][2],
        )
        characteristics = get_learning_characteristics(uow, student_id)
        return get_learning_strategy(uow, characteristics["id"])


def create_questionnaire_ils(
    uow: unit_of_work.AbstractUnitOfWork, student_id, ils_answers
) -> dict:
    with uow:
        exist = uow.questionnaire_ils.get_questionnaire_ils_by_student_id(student_id)
        if exist != []:
            delete_questionnaire_ils(uow, exist[0].id)
        questionnaire_ils = LM.QuestionnaireIls(student_id)
        uow.questionnaire_ils.create_questionnaire_ils(questionnaire_ils)
        uow.commit()
        ils_input_answers = {}
        ils_perception_answers = {}
        ils_processing_answers = {}
        ils_understanding_answers = {}
        for id, answer in ils_answers.items():
            if id.startswith("vv"):
                ils_input_answers[id] = answer
            if id.startswith("si"):
                ils_perception_answers[id] = answer
            if id.startswith("ar"):
                ils_processing_answers[id] = answer
            if id.startswith("sg"):
                ils_understanding_answers[id] = answer
        questionnaire_ils.serialize()
        ils_input = create_ils_input_answers(
            uow, questionnaire_ils.id, ils_input_answers
        )
        ils_perception = create_ils_perception_answers(
            uow, questionnaire_ils.id, ils_perception_answers
        )
        ils_processing = create_ils_processing_answers(
            uow, questionnaire_ils.id, ils_processing_answers
        )
        ils_understading = create_ils_understanding_answers(
            uow, questionnaire_ils.id, ils_understanding_answers
        )
        ils_input_values = {
            key: value for key, value in ils_input.items() if key.startswith("vv")
        }
        ils_perception_values = {
            key: value for key, value in ils_perception.items() if key.startswith("si")
        }
        ils_processing_values = {
            key: value for key, value in ils_processing.items() if key.startswith("ar")
        }
        ils_understanding_values = {
            key: value
            for key, value in ils_understading.items()
            if key.startswith("sg")
        }
        # Calculate basic learning style / can be changed to other algorithms
        basic_learning_style = BILSA.calculate_basic_learning_style(
            ils_input_values,
            ils_perception_values,
            ils_processing_values,
            ils_understanding_values,
        )
        # Get user_id with the student_id
        student = uow.student.get_student_by_student_id(student_id)
        user = get_user_by_id(uow, student[0].user_id, None)
        update_learning_style_by_student_id(
            uow,
            user["id"],
            user["lms_user_id"],
            student_id,
            basic_learning_style[1][0],
            basic_learning_style[1][1],
            basic_learning_style[0][0],
            basic_learning_style[0][1],
            basic_learning_style[2][0],
            basic_learning_style[2][1],
            basic_learning_style[3][0],
            basic_learning_style[3][1],
        )
        characteristics = get_learning_characteristics(uow, student_id)
        return get_learning_style(uow, characteristics["id"])


def create_settings(uow: unit_of_work.AbstractUnitOfWork, user_id) -> dict:
    with uow:
        setting = UA.Settings(user_id)
        uow.settings.create_settings(setting)
        uow.commit()
        result = setting.serialize()
        return result


def create_student(uow: unit_of_work.AbstractUnitOfWork, user) -> dict:
    with uow:
        student = UA.Student(user)
        uow.student.create_student(student)
        uow.commit()
        create_learning_characteristics(uow, student.id)
        result = student.serialize()
        return result


def create_teacher(uow: unit_of_work.AbstractUnitOfWork, user) -> dict:
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
        topic = DM.Topic(
            lms_id,
            is_topic,
            parent_id,
            contains_le,
            name,
            university,
            created_by,
            created_at,
        )
        uow.topic.create_topic(topic)
        uow.commit()
        result = topic.serialize()
        create_course_topic(uow, course_id, result["id"])
        return result


def create_topic_learning_element(
    uow: unit_of_work.AbstractUnitOfWork, topic_id, learning_element_id
) -> dict:
    with uow:
        topic_learning_element = DM.TopicLearningElement(topic_id, learning_element_id)
        uow.topic_learning_element.create_topic_learning_element(topic_learning_element)
        uow.commit()
        result = topic_learning_element.serialize()
        return result


def create_user(
    uow: unit_of_work.AbstractUnitOfWork, name, university, lms_user_id, role
) -> dict:
    with uow:
        user = UA.User(name, university, lms_user_id, role)
        uow.user.create_user(user)
        uow.commit()
        user.settings = create_settings(uow, user.id)
        match role.lower():
            case "admin":
                role = create_admin(uow, user)
                user.role_id = role["id"]
            case "course creator":
                role = create_course_creator(uow, user)
                user.role_id = role["id"]
            case "student":
                role = create_student(uow, user)
                user.role_id = role["id"]
            case "teacher":
                role = create_teacher(uow, user)
                user.role_id = role["id"]
        result = user.serialize()
    return result


def delete_admin(uow: unit_of_work.AbstractUnitOfWork, user_id):
    with uow:
        uow.admin.delete_admin(user_id)
        uow.commit()
        return {}


def delete_contact_form(uow: unit_of_work.AbstractUnitOfWork, user_id):
    with uow:
        uow.contact_form.delete_contact_form(user_id)
        uow.commit()
        return {}


def delete_course(uow: unit_of_work.AbstractUnitOfWork, course_id):
    with uow:
        delete_course_topic_by_course(uow, course_id)
        delete_course_creator_course(uow, course_id)
        uow.course.delete_course(course_id)
        uow.commit()
        return {}


def delete_course_creator(uow: unit_of_work.AbstractUnitOfWork, user_id):
    with uow:
        uow.course_creator.delete_course_creator(user_id)
        uow.commit()
        return {}


def delete_course_creator_course(uow: unit_of_work.AbstractUnitOfWork, course_id):
    with uow:
        uow.course_creator_course.delete_course_creator_course(course_id)
        uow.commit()


def delete_course_topic_by_course(
    uow: unit_of_work.AbstractUnitOfWork, course_id
) -> dict:
    with uow:
        uow.course_topic.delete_course_topic_by_course(course_id)
        uow.commit()
        return {}


def delete_course_topic_by_topic(
    uow: unit_of_work.AbstractUnitOfWork, topic_id
) -> dict:
    with uow:
        uow.course_topic.delete_course_topic_by_topic(topic_id)
        uow.commit()
        return {}


def delete_ils_input_answers(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id
):
    with uow:
        uow.ils_input_answers.delete_ils_input_answers(questionnaire_ils_id)
        uow.commit()
        return {}


def delete_ils_perception_answers(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id
):
    with uow:
        uow.ils_perception_answers.delete_ils_perception_answers(questionnaire_ils_id)
        uow.commit()
        return {}


def delete_ils_processing_answers(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id
):
    with uow:
        uow.ils_processing_answers.delete_ils_processing_answers(questionnaire_ils_id)
        uow.commit()
        return {}


def delete_ils_understanding_answers(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id
):
    with uow:
        uow.ils_understanding_answers.delete_ils_understanding_answers(
            questionnaire_ils_id
        )
        uow.commit()
        return {}


def delete_learning_element(
    uow: unit_of_work.AbstractUnitOfWork, course_id, topic_id, learning_element_id
):
    with uow:
        get_course_by_id(uow, None, None, course_id)
        get_topic_by_id(uow, None, None, course_id, None, topic_id)
        delete_topic_learning_element_by_learning_element(uow, learning_element_id)
        uow.learning_element.delete_learning_element(learning_element_id)
        uow.commit()
        return {}


def delete_learning_path(uow: unit_of_work.AbstractUnitOfWork, learning_path_id):
    with uow:
        uow.learning_path.delete_learning_path(learning_path_id)
        uow.commit()


def delete_learning_paths(uow: unit_of_work.AbstractUnitOfWork, student_id):
    with uow:
        paths = get_learning_paths(uow, student_id)
        for path in paths:
            delete_learning_path_learning_element(uow, path["id"])
            delete_learning_path_topic(uow, path["id"])
            uow.learning_path.delete_learning_path(path["id"])
            uow.commit()


def delete_learning_path_learning_element(
    uow: unit_of_work.AbstractUnitOfWork, learning_path_id
):
    with uow:
        uow.learning_path_learning_element.delete_learning_path_learning_element(
            learning_path_id
        )
        uow.commit()


def delete_learning_path_topic(uow: unit_of_work.AbstractUnitOfWork, learning_path_id):
    with uow:
        uow.learning_path_topic.delete_learning_path_topic(learning_path_id)
        uow.commit()


def delete_questionnaire_list_k(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_list_k_id
):
    with uow:
        uow.questionnaire_list_k.delete_questionnaire_list_k(questionnaire_list_k_id)
        uow.commit()
        return {}


def delete_questionnaire_ils(
    uow: unit_of_work.AbstractUnitOfWork, questionnaire_ils_id
):
    with uow:
        delete_ils_input_answers(uow, questionnaire_ils_id)
        delete_ils_perception_answers(uow, questionnaire_ils_id)
        delete_ils_processing_answers(uow, questionnaire_ils_id)
        delete_ils_understanding_answers(uow, questionnaire_ils_id)
        uow.questionnaire_ils.delete_questionnaire_ils(questionnaire_ils_id)
        uow.commit()
        return {}


def delete_settings(uow: unit_of_work.AbstractUnitOfWork, user_id):
    with uow:
        uow.settings.delete_settings(user_id)
        uow.commit()
        return {}


def delete_student(uow: unit_of_work.AbstractUnitOfWork, user_id):
    with uow:
        student = uow.student.get_student_by_id(user_id)
        delete_learning_characteristics(uow, student[0].id)
        delete_student_learning_element(uow, student[0].id)
        delete_student_topic(uow, student[0].id)
        delete_student_course(uow, student[0].id)
        delete_learning_paths(uow, student[0].id)
        questionnaire_ils = uow.questionnaire_ils.get_questionnaire_ils_by_student_id(
            student[0].id
        )
        questionnaire_list_k = (
            uow.questionnaire_list_k.get_questionnaire_list_k_by_student_id(
                student[0].id
            )
        )
        if questionnaire_ils != []:
            delete_questionnaire_ils(uow, questionnaire_ils[0].id)
        if questionnaire_list_k != []:
            delete_questionnaire_list_k(uow, questionnaire_list_k[0].id)
        uow.student.delete_student(user_id)
        uow.commit()
        return {}


def delete_teacher(uow: unit_of_work.AbstractUnitOfWork, user_id):
    with uow:
        teacher = uow.teacher.get_teacher_by_id(user_id)
        delete_teacher_course(uow, teacher[0].id)
        uow.teacher.delete_teacher(user_id)
        uow.commit()
        return {}


def delete_teacher_course(uow: unit_of_work.AbstractUnitOfWork, teacher_id):
    with uow:
        uow.teacher_course.delete_teacher_course(teacher_id)
        uow.commit()


def delete_user(uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id):
    with uow:
        user = get_user_by_id(uow, user_id, lms_user_id)
        match user["role"]:
            case "admin":
                delete_admin(uow, user["id"])
            case "course_creator":
                delete_course_creator(uow, user["id"])
            case "student":
                delete_student(uow, user["id"])
            case "teacher":
                delete_teacher(uow, user["id"])
        delete_settings(uow, user_id)
        uow.user.delete_user(user_id, lms_user_id)
        uow.commit()
        return {}


def delete_knowledge(uow: unit_of_work.AbstractUnitOfWork, characteristic_id):
    with uow:
        uow.knowledge.delete_knowledge(characteristic_id)
        uow.commit()
        return {}


def delete_learning_analytics(uow: unit_of_work.AbstractUnitOfWork, characteristic_id):
    with uow:
        uow.learning_analytics.delete_learning_analytics(characteristic_id)
        uow.commit()
        return {}


def delete_learning_characteristics(uow: unit_of_work.AbstractUnitOfWork, student_id):
    with uow:
        characteristic = get_learning_characteristics(uow, student_id)
        if characteristic != {}:
            delete_knowledge(uow, characteristic["id"])
            delete_learning_analytics(uow, characteristic["id"])
            delete_learning_strategy(uow, characteristic["id"])
            delete_learning_style(uow, characteristic["id"])
            uow.learning_characteristics.delete_learning_characteristics(student_id)
            uow.commit()
        return {}


def delete_learning_strategy(uow: unit_of_work.AbstractUnitOfWork, characteristic_id):
    with uow:
        uow.learning_strategy.delete_learning_strategy(characteristic_id)
        uow.commit()
        return {}


def delete_learning_style(uow: unit_of_work.AbstractUnitOfWork, characteristic_id):
    with uow:
        uow.learning_style.delete_learning_style(characteristic_id)
        uow.commit()
        return {}


def delete_student_course(uow: unit_of_work.AbstractUnitOfWork, student_id):
    with uow:
        uow.student_course.delete_student_course(student_id)
        uow.commit()


def delete_student_learning_element(uow: unit_of_work.AbstractUnitOfWork, student_id):
    with uow:
        delete_student_learning_element_visit(uow, student_id)
        uow.student_learning_element.delete_student_learning_element(student_id)
        uow.commit()


def delete_student_learning_element_visit(
    uow: unit_of_work.AbstractUnitOfWork, student_id
):
    with uow:
        uow.student_learning_element_visit.delete_student_learning_element_visit(
            student_id
        )
        uow.commit()


def delete_student_topic(uow: unit_of_work.AbstractUnitOfWork, student_id):
    with uow:
        delete_student_topic_visit(uow, student_id)
        uow.student_topic.delete_student_topic(student_id)
        uow.commit()


def delete_student_topic_visit(uow: unit_of_work.AbstractUnitOfWork, student_id):
    with uow:
        uow.student_topic_visit.delete_student_topic_visit(student_id)
        uow.commit()


def delete_topic(uow: unit_of_work.AbstractUnitOfWork, topic_id):
    with uow:
        uow.course_topic.delete_course_topic_by_topic(topic_id)
        uow.commit()
        uow.topic.delete_topic(topic_id)
        uow.commit()
        return {}


def delete_topic_learning_element_by_topic(
    uow: unit_of_work.AbstractUnitOfWork, topic_id
):
    with uow:
        uow.topic_learning_element.delete_topic_learning_element_by_topic(topic_id)
        uow.commit()
        return {}


def delete_topic_learning_element_by_learning_element(
    uow: unit_of_work.AbstractUnitOfWork, learning_element_id
):
    with uow:
        uow.topic_learning_element.delete_topic_learning_element_by_learning_element(
            learning_element_id
        )
        uow.commit()
        return {}


def get_course_by_id(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, course_id
) -> dict:
    with uow:
        if user_id is not None and lms_user_id is not None:
            get_user_by_id(uow, user_id, lms_user_id)
        course = uow.course.get_course_by_id(course_id)
        if course == []:
            result = {}
        else:
            course[0].created_at = None
            course[0].created_by = None
            course[0].last_updated = None
            result = course[0].serialize()
        return result


def get_courses_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, student_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        uow.student.get_student_by_id(user_id)
        courses = uow.course.get_courses_by_student_id(student_id)
        result_courses = []
        for course in courses:
            course_by_id = get_course_by_id(uow, user_id, lms_user_id, course.course_id)
            result_courses.append(course_by_id)
        result = {}
        result["courses"] = result_courses
        return result


def get_courses_for_teacher(
    uow: unit_of_work.AbstractUnitOfWork, user_id, teacher_id
) -> dict:
    with uow:
        uow.teacher.get_teacher_by_id(user_id)
        courses = uow.teacher_course.get_courses_for_teacher(teacher_id)
        result = {}
        course_list = []
        for course in courses:
            course_temp = uow.course.get_course_by_id(course.course_id)
            course_temp[0].created_at = None
            course_temp[0].created_by = None
            course_temp[0].last_updated = None
            course_list.append(course_temp[0].serialize())
        result["courses"] = course_list
        return result


def get_course_topic_by_course(uow: unit_of_work.AbstractUnitOfWork, course_id) -> dict:
    with uow:
        course_topic = uow.course_topic.get_course_topic_by_course(course_id)
        if course_topic == []:
            result = {}
        else:
            result = course_topic[0].serialize()
        return result


def get_course_topic_by_topic(uow: unit_of_work.AbstractUnitOfWork, topic_id) -> dict:
    with uow:
        course_topic = uow.course_topic.get_course_topic_by_topic(topic_id)
        if course_topic == []:
            result = {}
        else:
            result = course_topic[0].serialize()
        return result


def get_knowledge(uow: unit_of_work.AbstractUnitOfWork, characteristic_id) -> dict:
    with uow:
        knowledge = uow.knowledge.get_knowledge(characteristic_id)
        if knowledge == []:
            result = {}
        else:
            result = knowledge[0].serialize()
        return result


def get_knowledge_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, student_id
) -> dict:
    with uow:
        uow.student.get_student_by_student_id(student_id)
        characteristic = get_learning_characteristics(uow, student_id)
        result = characteristic["knowledge"]
        return result


def get_learning_analytics(
    uow: unit_of_work.AbstractUnitOfWork, characteristic_id
) -> dict:
    with uow:
        analytics = uow.learning_analytics.get_learning_analytics(characteristic_id)
        if analytics == []:
            result = {}
        else:
            result = analytics[0].serialize()
        return result


def get_learning_analytics_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, student_id
) -> dict:
    with uow:
        uow.student.get_student_by_student_id(student_id)
        characteristic = get_learning_characteristics(uow, student_id)
        result = characteristic["learning_analytics"]
        return result


def get_learning_characteristics(
    uow: unit_of_work.AbstractUnitOfWork, student_id, user_id=None, lms_user_id=None
) -> dict:
    with uow:
        uow.student.get_student_by_student_id(student_id)
        if user_id is not None:
            get_user_by_id(uow, user_id, lms_user_id)
        characteristics = uow.learning_characteristics.get_learning_characteristics(
            student_id
        )
        if characteristics == []:
            result = {}
        else:
            characteristics = characteristics[0]
            characteristics.knowledge = get_knowledge(uow, characteristics.id)
            characteristics.learning_analytics = get_learning_analytics(
                uow, characteristics.id
            )
            characteristics.learning_strategy = get_learning_strategy(
                uow, characteristics.id
            )
            characteristics.learning_style = get_learning_style(uow, characteristics.id)
            result = characteristics.serialize()
        return result


def get_learning_element_by_id(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
    learning_element_id,
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        get_course_by_id(uow, user_id, lms_user_id, course_id)
        get_topic_by_id(uow, user_id, lms_user_id, course_id, student_id, topic_id)
        learning_element = uow.learning_element.get_learning_element_by_id(
            learning_element_id
        )
        if learning_element[0] is None:
            result = {}
        else:
            student_learning_element = (
                uow.student_learning_element.get_student_learning_element(
                    student_id, learning_element_id
                )
            )
            if student_learning_element == []:
                learning_element[0].student_learning_element = None
            else:
                learning_element[0].student_learning_element = student_learning_element[
                    0
                ].serialize()
            result = learning_element[0].serialize()
        return result


def get_learning_elements_for_course_id(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, student_id, course_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        get_course_by_id(uow, user_id, lms_user_id, course_id)
        topics = get_topics_for_course_id(uow, course_id)
        result = {}
        learning_elements = []
        for topic in topics:
            les = get_learning_elements_for_topic_id(uow, topic["topic_id"])
            for le in les:
                le_by_id = get_learning_element_by_id(
                    uow,
                    user_id,
                    lms_user_id,
                    student_id,
                    course_id,
                    le["topic_id"],
                    le["learning_element_id"],
                )
                student_le = uow.student_learning_element.get_student_learning_element(
                    student_id, le["learning_element_id"]
                )
                le_by_id["student_learning_element"] = student_le[0].serialize()
                learning_elements.append(le_by_id)
        result["learning_elements"] = learning_elements
        return result


def get_learning_elements_for_course_and_topic_id(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        get_course_by_id(uow, user_id, lms_user_id, course_id)
        get_topic_by_id(uow, user_id, lms_user_id, course_id, student_id, topic_id)
        learning_elements = get_learning_elements_for_topic_id(uow, topic_id)
        les = []
        for le in learning_elements:
            learning_element = get_learning_element_by_id(
                uow,
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id,
                le["learning_element_id"],
            )
            student_learning_element = (
                uow.student_learning_element.get_student_learning_element(
                    student_id, le["learning_element_id"]
                )
            )
            learning_element["student_learning_element"] = student_learning_element[
                0
            ].serialize()
            les.append(learning_element)
        result = {}
        result["learning_elements"] = les
        return result


def get_learning_elements_for_topic_id(
    uow: unit_of_work.AbstractUnitOfWork, topic_id
) -> list:
    with uow:
        try:
            learning_elements = (
                uow.topic_learning_element.get_topic_learning_element_by_topic(topic_id)
            )
            results = []
            for le in learning_elements:
                results.append(le.serialize())
            return results
        except Exception:
            return []


def get_learning_element_recommendation(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        get_course_by_id(uow, user_id, lms_user_id, course_id)
        get_topic_by_id(uow, user_id, lms_user_id, course_id, student_id, topic_id)
        path = get_learning_path(
            uow, user_id, lms_user_id, student_id, course_id, topic_id
        )
        result = uow.learning_path_learning_element.get_learning_element_recommendation(
            path["id"]
        )
        return get_learning_element_by_id(
            uow,
            user_id,
            lms_user_id,
            student_id,
            course_id,
            topic_id,
            result[0].learning_element_id,
        )


def get_learning_path(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        get_course_by_id(uow, user_id, lms_user_id, course_id)
        learning_path = uow.learning_path.get_learning_path(
            student_id, course_id, topic_id
        )
        if learning_path == []:
            result = {}
        else:
            les_for_path = (
                uow.learning_path_learning_element.get_learning_path_learning_element(
                    learning_path[0].id
                )
            )
            les = []
            for le in les_for_path:
                le_by_id = get_learning_element_by_id(
                    uow,
                    user_id,
                    lms_user_id,
                    student_id,
                    course_id,
                    topic_id,
                    le.learning_element_id,
                )
                le.learning_element = le_by_id
                les.append(le.serialize())
            learning_path[0].path = les
            result = learning_path[0].serialize()
        return result


def get_learning_paths(uow: unit_of_work.AbstractUnitOfWork, student_id) -> list:
    with uow:
        paths = uow.learning_path.get_learning_paths(student_id)
        result = []
        for path in paths:
            path.path = None
            result.append(path.serialize())
        return result


def get_learning_strategy(
    uow: unit_of_work.AbstractUnitOfWork, characteristic_id
) -> dict:
    with uow:
        strategy = uow.learning_strategy.get_learning_strategy(characteristic_id)
        if strategy == []:
            result = {}
        else:
            result = strategy[0].serialize()
        return result


def get_learning_strategy_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, student_id
) -> dict:
    with uow:
        uow.student.get_student_by_student_id(student_id)
        characteristic = get_learning_characteristics(uow, student_id)
        result = characteristic["learning_strategy"]
        return result


def get_learning_style(uow: unit_of_work.AbstractUnitOfWork, characteristic_id) -> dict:
    with uow:
        style = uow.learning_style.get_learning_style(characteristic_id)
        if style == []:
            result = {}
        else:
            result = style[0].serialize()
        return result


def get_learning_style_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, student_id
) -> dict:
    with uow:
        uow.student.get_student_by_student_id(student_id)
        characteristic = get_learning_characteristics(uow, student_id)
        result = characteristic["learning_style"]
        return result


def get_sub_topic_by_topic_id(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id,
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        get_course_by_id(uow, user_id, lms_user_id, course_id)
        subtopics = uow.topic.get_sub_topics_for_topic_id(topic_id)
        for st in subtopics:
            student_topic = uow.student_topic.get_student_topic(student_id, topic_id)
            if student_topic != []:
                student_topic[0].visits = None
                st.student_topic = student_topic[0].serialize()
            else:
                st.student_topic = None
        result_subtopics = []
        for subtopic in subtopics:
            result_subtopics.append(subtopic.serialize())
        result = {}
        result["topics"] = result_subtopics
        return result


def get_topic_by_id(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    course_id,
    student_id,
    topic_id,
) -> dict:
    with uow:
        if user_id is not None or lms_user_id is not None:
            get_user_by_id(uow, user_id, lms_user_id)
            get_course_by_id(uow, user_id, lms_user_id, course_id)
        topic = uow.topic.get_topic_by_id(topic_id)
        if topic == []:
            result = {}
        else:
            student_topic = uow.student_topic.get_student_topic(student_id, topic_id)
            if student_topic == []:
                topic[0].student_topic = None
            else:
                student_topic_visit = uow.student_topic_visit.get_student_topic_visit(
                    student_id, topic_id
                )
                if student_topic_visit == []:
                    student_topic[0].visits = None
                else:
                    student_topic[0].visits = student_topic_visit[0].serialize()
                topic[0].student_topic = student_topic[0].serialize()
            result = topic[0].serialize()
        return result


def get_topics_by_student_and_course_id(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, student_id, course_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        get_course_by_id(uow, user_id, lms_user_id, course_id)
        topics = get_topics_for_course_id(uow, course_id)
        result_topics = []
        for topic in topics:
            student_topic_visit = uow.student_topic_visit.get_student_topic_visit(
                student_id, topic["topic_id"]
            )
            visits = []
            for stv in student_topic_visit:
                visits.append(stv.serialize())
            student_topic = uow.student_topic.get_student_topic(
                student_id, topic["topic_id"]
            )
            student_topic[0].visits = visits
            topic_details = get_topic_by_id(
                uow, user_id, lms_user_id, course_id, student_id, topic["topic_id"]
            )
            topic_details["student_topic"] = student_topic[0].serialize()
            result_topics.append(topic_details)
        result = {}
        result["topics"] = result_topics
        return result


def get_topics_for_course_id(uow: unit_of_work.AbstractUnitOfWork, course_id) -> list:
    with uow:
        try:
            topics = uow.course_topic.get_course_topic_by_course(course_id)
            results = []
            for topic in topics:
                results.append(topic.serialize())
            return results
        except Exception:
            return []


def get_topic_learning_element_by_topic(
    uow: unit_of_work.AbstractUnitOfWork, topic_id
) -> dict:
    with uow:
        topic_learning_element = (
            uow.topic_learning_element.get_topic_learning_element_by_topic(topic_id)
        )
        if topic_learning_element == []:
            result = {}
        else:
            result = topic_learning_element[0].serialize()
        return result


def get_topic_learning_element_by_learning_element(
    uow: unit_of_work.AbstractUnitOfWork, learning_element_id
) -> dict:
    with uow:
        topic_learning_element = (
            uow.topic_learning_element.get_topic_learning_element_by_learning_element(
                learning_element_id
            )
        )
        if topic_learning_element == []:
            result = {}
        else:
            result = topic_learning_element[0].serialize()
        return result


def get_users_by_admin(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id
) -> dict:
    with uow:
        admin_user = uow.user.get_user_by_id(user_id, lms_user_id)
        admin_user[0].settings = None
        users = uow.user.get_users_by_uni(admin_user[0].university)
        result = {}
        user_list = []
        for user in users:
            user.settings = None
            user.role_id = None
            user_list.append(user.serialize())
        result["users"] = user_list
        return result


def reset_knowledge(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, characteristic_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        knowledge = LM.Knowledge(characteristic_id)
        uow.knowledge.update_knowledge(characteristic_id, knowledge)
        uow.commit()
        return knowledge.serialize()


def reset_knowledge_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, student_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        characteristic = get_learning_characteristics(uow, student_id)
        result = reset_knowledge(uow, user_id, lms_user_id, characteristic["id"])
        return result


def reset_learning_analytics(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, characteristic_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        analytics = LM.LearningAnalytics(characteristic_id)
        uow.learning_analytics.update_learning_analytics(characteristic_id, analytics)
        uow.commit()
        return analytics.serialize()


def reset_learning_analytics_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, student_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        characteristic = get_learning_characteristics(uow, student_id)
        result = reset_learning_analytics(
            uow, user_id, lms_user_id, characteristic["id"]
        )
        return result


def reset_learning_characteristics(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, student_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        characteristics = uow.learning_characteristics.get_learning_characteristics(
            student_id
        )
        characteristics[0].knowledge = reset_knowledge(
            uow, user_id, lms_user_id, characteristics[0].id
        )
        characteristics[0].learning_analytics = reset_learning_analytics(
            uow, user_id, lms_user_id, characteristics[0].id
        )
        characteristics[0].learning_strategy = reset_learning_strategy(
            uow, user_id, lms_user_id, characteristics[0].id
        )
        characteristics[0].learning_style = reset_learning_style(
            uow, user_id, lms_user_id, characteristics[0].id
        )
        return characteristics[0].serialize()


def reset_learning_strategy(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, characteristic_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        strategy = LM.LearningStrategy(characteristic_id)
        uow.learning_strategy.update_learning_strategy(characteristic_id, strategy)
        uow.commit()
        return strategy.serialize()


def reset_learning_strategy_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, student_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        characteristic = get_learning_characteristics(uow, student_id)
        result = reset_learning_strategy(
            uow, user_id, lms_user_id, characteristic["id"]
        )
        return result


def reset_learning_style(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, characteristic_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        style = LM.LearningStyle(characteristic_id)
        uow.learning_style.update_learning_style(characteristic_id, style)
        uow.commit()
        return style.serialize()


def reset_learning_style_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, student_id
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        characteristic = get_learning_characteristics(uow, student_id)
        result = reset_learning_style(uow, user_id, lms_user_id, characteristic["id"])
        return result


def reset_settings(uow: unit_of_work.AbstractUnitOfWork, user_id):
    with uow:
        settings = UA.Settings(user_id)
        uow.settings.update_settings(user_id, settings)
        uow.commit()
        return settings.serialize()


def get_settings_for_user(uow: unit_of_work.AbstractUnitOfWork, user_id) -> dict:
    with uow:
        settings = uow.settings.get_settings(user_id)
        if settings == []:
            result = {}
        else:
            result = settings[0].serialize()
        return result


def create_contact_form(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    report_topic,
    report_type,
    report_description,
    date,
) -> dict:
    with uow:
        user = get_user_by_id(uow, user_id, lms_user_id)
        if user == {}:
            raise err.MissingUserError()
        else:
            contact_form = UA.ContactForm(
                user_id, report_topic, report_type, report_description, date
            )
            uow.contact_form.create_contact_form(contact_form)
            uow.commit()
            result = contact_form.serialize()
        return result


def get_user_by_id(uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id) -> dict:
    with uow:
        user = uow.user.get_user_by_id(user_id, lms_user_id)
        settings = uow.settings.get_settings(user_id)
        if user == []:
            result = {}
        else:
            user[0].settings = settings[0].serialize()
            user[0].role_id = None
            result = user[0].serialize()
        return result


def get_user_by_lms_id(uow: unit_of_work.AbstractUnitOfWork, lms_user_id) -> dict:
    with uow:
        user = uow.user.get_user_by_lms_id(lms_user_id)
        settings = uow.settings.get_settings(user[0].id)
        if user == []:
            result = {}
        else:
            user[0].settings = settings[0].serialize()
            user[0].role_id = None
            result = user[0].serialize()
        return result


def get_student_by_user_id(uow: unit_of_work.AbstractUnitOfWork, user_id) -> dict:
    with uow:
        student = uow.student.get_student_by_id(user_id)
        user = uow.user.get_user_by_id(user_id, None)
        student[0].__init__(user[0])
        settings = uow.settings.get_settings(user_id)
        if student[0] == []:
            result = {}
        else:
            student[0].settings = settings[0].serialize()
            student[0].role_id = None
            result = student[0].serialize()
        return result


def update_course(
    uow: unit_of_work.AbstractUnitOfWork, course_id, lms_id, name, university
) -> dict:
    with uow:
        course = DM.Course(lms_id, name, university, None, None, None)
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
    university,
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
            last_updated,
        )
        uow.learning_element.update_learning_element(
            learning_element_id, learning_element
        )
        uow.commit()
        result = learning_element.serialize()
        return result


def update_learning_style_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    student_id,
    perception_dimension,
    perception_value,
    input_dimension,
    input_value,
    processing_dimension,
    processing_value,
    understanding_dimension,
    understanding_value,
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        characteristic = get_learning_characteristics(uow, student_id)
        learning_style = LM.LearningStyle(
            characteristic["id"],
            perception_dimension,
            perception_value,
            input_dimension,
            input_value,
            processing_dimension,
            processing_value,
            understanding_dimension,
            understanding_value,
        )
        uow.learning_style.update_learning_style(characteristic["id"], learning_style)
        uow.commit()
        result = learning_style.serialize()
        return result


def update_learning_strategy_by_student_id(
    uow: unit_of_work.AbstractUnitOfWork,
    user_id,
    lms_user_id,
    student_id,
    cogn_str,
    org,
    elab,
    crit_rev,
    rep,
    metacogn_str,
    goal_plan,
    con,
    reg,
    int_res_mng_str,
    att,
    eff,
    time,
    ext_res_mng_str,
    lrn_w_cls,
    lit_res,
    lrn_env,
) -> dict:
    with uow:
        get_user_by_id(uow, user_id, lms_user_id)
        characteristic = get_learning_characteristics(uow, student_id)
        learning_strategy = LM.LearningStrategy(
            characteristic["id"],
            cogn_str,
            org,
            elab,
            crit_rev,
            rep,
            metacogn_str,
            goal_plan,
            con,
            reg,
            int_res_mng_str,
            att,
            eff,
            time,
            ext_res_mng_str,
            lrn_w_cls,
            lit_res,
            lrn_env,
        )
        uow.learning_strategy.update_learning_strategy(
            characteristic["id"], learning_strategy
        )
        uow.commit()
        result = learning_strategy.serialize()
        return result


def update_previous_learning_element_visit(
    uow: unit_of_work.AbstractUnitOfWork, student_id, visit_time
) -> dict:
    with uow:
        uow.student_learning_element_visit.update_previous_learning_element_visit(
            student_id, visit_time
        )
        uow.commit()


def update_previous_topic_visit(
    uow: unit_of_work.AbstractUnitOfWork, student_id, visit_time
) -> dict:
    with uow:
        uow.student_topic_visit.update_previous_topic_visit(student_id, visit_time)
        uow.commit()


def update_settings_for_user(
    uow: unit_of_work.AbstractUnitOfWork, user_id, theme, pswd=None
) -> dict:
    with uow:
        settings = UA.Settings(user_id, theme, pswd)
        uow.settings.update_settings(user_id, settings)
        uow.commit()
        return settings.serialize()


def update_student_learning_element(
    uow: unit_of_work.AbstractUnitOfWork, student_id, learning_element_id, visit_time
):
    with uow:
        uow.student_learning_element.update_student_learning_element(
            student_id, learning_element_id, visit_time
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
    last_updated,
) -> dict:
    with uow:
        topic = DM.Topic(
            lms_id,
            is_topic,
            parent_id,
            contains_le,
            name,
            university,
            created_by,
            created_at,
            last_updated,
        )
        uow.topic.update_topic(topic_id, topic)
        uow.commit()
        return topic.serialize()


def update_user(
    uow: unit_of_work.AbstractUnitOfWork, user_id, lms_user_id, name, university
) -> dict:
    with uow:
        user = UA.User(name, university, lms_user_id)
        uow.user.update_user(user_id, lms_user_id, user)
        uow.commit()
        settings = uow.settings.get_settings(user_id)
        user.settings = settings[0].serialize()
        return user.serialize()


# ##### TEST ENDPOINT #####


def get_user_info(uow: unit_of_work.AbstractUnitOfWork, user_id: str) -> str:
    with uow:
        return "Admin"
        # user_info = uow.user_info.get(user_id)
        # if user_info is None:
        #     raise err.UserNotFoundError()
        # return user_info


# ##### LTI #####


def get_oidc_login(request: Request):
    """Return OIDC login url or error response\
        in case of wrong parameters, unsecure or request"""
    oidc_login = OIDCLoginFlask(request)
    return oidc_login.check_params().auth_redirect()


def get_lti_launch(request: Request):
    """Craft nonce and state, store them in session and return\
        LTI launch url to Frontend with nonce_jwt in url"""
    oidc_login = OIDCLoginFlask(request)
    return oidc_login.verify_state().verify_id_token().lti_launch_from_id_token()


def get_login(request):
    """Return cookie value or None"""
    oidc_login = OIDCLoginFlask(request)
    return oidc_login.get_cookie_expiration() or None


def get_logout(request: Request):
    """Return logout url or None"""
    oidc_login = OIDCLoginFlask(request)
    return oidc_login.get_logout() or None
