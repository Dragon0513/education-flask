import pytest
import repositories.repository as repository
from service_layer import services, unit_of_work
from domain.userAdministartion import model as UA
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.domainModel import model as DM
import time
import errors as err


class FakeRepository(repository.AbstractRepository):  # pragma: no cover
    def __init__(self,
                 admin=[],
                 course=[],
                 course_creator=[],
                 course_creator_course=[],
                 course_topic=[],
                 ils_input_answers=[],
                 ils_perception_answers=[],
                 ils_processing_answers=[],
                 ils_understanding_answers=[],
                 knowledge=[],
                 learning_analytics=[],
                 learning_characteristics=[],
                 learning_element=[],
                 learning_element_rating=[],
                 learning_path=[],
                 learning_path_learning_element=[],
                 learning_path_topic=[],
                 learning_strategy=[],
                 learning_style=[],
                 list_k=[],
                 questionnaire=[],
                 settings=[],
                 student=[],
                 student_course=[],
                 student_learning_element=[],
                 student_learning_element_visit=[],
                 student_topic=[],
                 student_topic_visit=[],
                 teacher=[],
                 teacher_course=[],
                 topic=[],
                 topic_learning_element=[],
                 user=[],
                 ):
        self.admin = set(admin)
        self.course = set(course)
        self.course_creator = set(course_creator)
        self.course_creator_course = set(course_creator_course)
        self.course_topic = set(course_topic)
        self.knowledge = set(knowledge)
        self.ils_input_answers = set(ils_input_answers)
        self.ils_perception_answers = set(ils_perception_answers)
        self.ils_processing_answers = set(ils_processing_answers)
        self.ils_understanding_answers = set(ils_understanding_answers)
        self.learning_analytics = set(learning_analytics)
        self.learning_characteristics = set(learning_characteristics)
        self.learning_element = set(learning_element)
        self.learning_element_rating = set(learning_element_rating)
        self.learning_path = set(learning_path)
        self.learning_path_learning_element = set(
            learning_path_learning_element)
        self.learning_path_topic = set(learning_path_topic)
        self.learning_strategy = set(learning_strategy)
        self.learning_style = set(learning_style)
        self.list_k = set(list_k)
        self.questionnaire = set(questionnaire)
        self.settings = set(settings)
        self.student = set(student)
        self.student_course = set(student_course)
        self.student_learning_element = set(student_learning_element)
        self.student_learning_element_visit = set(
            student_learning_element_visit)
        self.student_topic = set(student_topic)
        self.student_topic_visit = set(student_topic_visit)
        self.teacher = set(teacher)
        self.teacher_course = set(teacher_course)
        self.topic = set(topic)
        self.topic_learning_element = set(topic_learning_element)
        self.user = set(user)

    def add_course_creator_to_course(self, course_creator_course):
        course_creator_course.id = len(self.course_creator_course) + 1
        self.course_creator_course.add(course_creator_course)

    def add_student_learning_element_visit(self,
                                           student_learning_element_vist):
        student_learning_element_vist.id = len(
            self.student_learning_element_visit) + 1
        self.student_learning_element_visit\
            .add(student_learning_element_vist)

    def add_student_to_course(self, student_course):
        student_course.id = len(self.student_course) + 1
        self.student_course.add(student_course)

    def add_student_to_learning_element(self,
                                        student_learning_element):
        student_learning_element.id =\
            len(self.student_learning_element) + 1
        self.student_learning_element.add(student_learning_element)

    def add_student_to_topic(self,
                             student_topic):
        student_topic.id = len(self.student_topic) + 1
        self.student_topic.add(student_topic)

    def add_student_topic_visit(self, student_topic_visit):
        student_topic_visit.id = len(self.student_topic_visit) + 1
        self.student_topic_visit.add(student_topic_visit)

    def add_teacher_to_course(self, teacher_course):
        teacher_course.id = len(self.teacher_course) + 1
        self.teacher_course.add(teacher_course)

    def create_admin(self, admin):
        admin.id = len(self.admin) + 1
        self.admin.add(admin)

    def create_course(self, course):
        course.id = len(self.course) + 1
        self.course.add(course)

    def create_course_creator(self, course_creator):
        course_creator.id = len(self.course_creator) + 1
        self.course_creator.add(course_creator)

    def create_course_topic(self, course_topic):
        course_topic.id = len(self.course_topic) + 1
        self.course_topic.add(course_topic)

    def create_ils_input_answers(self, ils_input_answers):
        ils_input_answers.id = len(self.ils_input_answers) + 1
        self.ils_input_answers.add(ils_input_answers)

    def create_ils_perception_answers(self, ils_perception_answers):
        ils_perception_answers.id = len(self.ils_perception_answers) + 1
        self.ils_perception_answers.add(ils_perception_answers)

    def create_ils_processing_answers(self, ils_processing_answers):
        ils_processing_answers.id = len(self.ils_processing_answers) + 1
        self.ils_processing_answers.add(ils_processing_answers)

    def create_ils_understanding_answers(self, ils_understanding_answers):
        ils_understanding_answers.id = len(self.ils_understanding_answers) + 1
        self.ils_understanding_answers.add(ils_understanding_answers)

    def create_knowledge(self, knowledge):
        knowledge.id = len(self.knowledge) + 1
        self.knowledge.add(knowledge)

    def create_learning_analytics(self, learning_analytics):
        learning_analytics.id = len(self.learning_analytics) + 1
        self.learning_analytics.add(learning_analytics)

    def create_learning_characteristics(self, learning_characteristics):
        learning_characteristics.id = len(self.learning_characteristics) + 1
        self.learning_characteristics.add(learning_characteristics)

    def create_learning_element(self, learning_element):
        learning_element.id = len(self.learning_element) + 1
        self.learning_element.add(learning_element)

    def create_learning_path(self, learning_path):
        learning_path.id = len(self.learning_path) + 1
        self.learning_path.add(learning_path)

    def create_learning_path_learning_element(self,
                                              learning_path_learning_element):
        learning_path_learning_element.id =\
            len(self.learning_path_learning_element) + 1
        self.learning_path_learning_element\
            .add(learning_path_learning_element)

    def create_learning_path_topic(self, learning_path_topic):
        learning_path_topic.id = len(self.learning_path_topic) + 1
        self.learning_path_topic.add(learning_path_topic)

    def create_learning_strategy(self, learning_strategy):
        learning_strategy.id = len(self.learning_strategy) + 1
        self.learning_strategy.add(learning_strategy)

    def create_learning_style(self, learning_style):
        learning_style.id = len(self.learning_style) + 1
        self.learning_style.add(learning_style)

    def create_list_k(self, list_k):
        list_k.id = len(self.list_k) + 1
        self.list_k.add(list_k)

    def create_questionnaire(self, questionnaire):
        questionnaire.id = len(self.questionnaire) + 1
        self.questionnaire.add(questionnaire)

    def create_settings(self, settings):
        settings.id = len(self.settings) + 1
        self.settings.add(settings)

    def create_student(self, student):
        student.id = len(self.student) + 1
        self.student.add(student)

    def create_teacher(self, teacher):
        teacher.id = len(self.teacher) + 1
        self.teacher.add(teacher)

    def create_topic(self, topic):
        topic.id = len(self.topic) + 1
        self.topic.add(topic)

    def create_topic_learning_element(self, topic_learning_elemnt):
        topic_learning_elemnt.id = len(self.topic_learning_element) + 1
        self.topic_learning_element.add(topic_learning_elemnt)

    def create_user(self, user):
        user.id = len(self.user) + 1
        self.user.add(user)

    def delete_admin(self, user_id):
        to_remove = []
        for i in self.admin:
            if i.user_id == user_id:
                to_remove.append(i)
        for remove in to_remove:
            self.admin.remove(remove)

    def delete_course(self, course_id):
        to_remove = []
        for i in self.course:
            if i.id == course_id:
                to_remove.append(i)
        for remove in to_remove:
            self.course.remove(remove)

    def delete_course_creator(self, user_id):
        to_remove = []
        for i in self.course_creator:
            if i.user_id == user_id:
                to_remove.append(i)
        for remove in to_remove:
            self.course_creator.remove(remove)

    def delete_course_creator_course(self, course_id):
        to_remove = []
        for i in self.course_creator_course:
            if i.course_id == course_id:
                to_remove.append(i)
        for remove in to_remove:
            self.course_creator_course.remove(remove)

    def delete_course_topic_by_course(self, course_id):
        to_remove = []
        for i in self.course_topic:
            if i.course_id == course_id:
                to_remove.append(i)
        for remove in to_remove:
            self.course_topic.remove(remove)

    def delete_course_topic_by_topic(self, topic_id):
        to_remove = []
        for i in self.course_topic:
            if i.topic_id == topic_id:
                to_remove.append(i)
        for remove in to_remove:
            self.course_topic.remove(remove)

    def delete_ils_input_answers(self, questionnaire_id):
        to_remove = []
        for i in self.ils_input_answers:
            if i.questionnaire_id == questionnaire_id:
                to_remove.append(i)
        for remove in to_remove:
            self.ils_input_answers.remove(remove)

    def delete_ils_perception_answers(self, questionnaire_id):
        to_remove = []
        for i in self.ils_perception_answers:
            if i.questionnaire_id == questionnaire_id:
                to_remove.append(i)
        for remove in to_remove:
            self.ils_perception_answers.remove(remove)

    def delete_ils_processing_answers(self, questionnaire_id):
        to_remove = []
        for i in self.ils_processing_answers:
            if i.questionnaire_id == questionnaire_id:
                to_remove.append(i)
        for remove in to_remove:
            self.ils_processing_answers.remove(remove)

    def delete_ils_understanding_answers(self, questionnaire_id):
        to_remove = []
        for i in self.ils_understanding_answers:
            if i.questionnaire_id == questionnaire_id:
                to_remove.append(i)
        for remove in to_remove:
            self.ils_understanding_answers.remove(remove)

    def delete_knowledge(self, characteristic_id):
        to_remove = []
        for i in self.knowledge:
            if i.characteristic_id == characteristic_id:
                to_remove.append(i)
        for remove in to_remove:
            self.knowledge.remove(remove)

    def delete_learning_analytics(self, characteristic_id):
        to_remove = []
        for i in self.learning_analytics:
            if i.characteristic_id == characteristic_id:
                to_remove.append(i)
        for remove in to_remove:
            self.learning_analytics.remove(remove)

    def delete_learning_characteristics(self, student_id):
        to_remove = []
        for i in self.learning_characteristics:
            if i.student_id == student_id:
                to_remove.append(i)
        for remove in to_remove:
            self.learning_characteristics.remove(remove)

    def delete_learning_element(self, learning_element_id):
        to_remove = []
        for i in self.learning_element:
            if i.id == learning_element_id:
                to_remove.append(i)
        for remove in to_remove:
            self.learning_element.remove(remove)

    def delete_learning_path(self, learning_path_id):
        to_remove = []
        for i in self.learning_path:
            if i.id == learning_path_id:
                to_remove.append(i)
        for remove in to_remove:
            self.learning_path.remove(remove)

    def delete_learning_path_learning_element(self, learning_path_id):
        to_remove = []
        for i in self.learning_path_learning_element:
            if i.learning_path_id == learning_path_id:
                to_remove.append(i)
        for remove in to_remove:
            self.learning_path_learning_element.remove(remove)

    def delete_learning_path_topic(self, learning_path_id):
        to_remove = []
        for i in self.learning_path_topic:
            if i.learning_path_id == learning_path_id:
                to_remove.append(i)
        for remove in to_remove:
            self.learning_path_topic.remove(remove)

    def delete_learning_strategy(self, characteristic_id):
        to_remove = []
        for i in self.learning_strategy:
            if i.characteristic_id == characteristic_id:
                to_remove.append(i)
        for remove in to_remove:
            self.learning_strategy.remove(remove)

    def delete_learning_style(self, characteristic_id):
        to_remove = []
        for i in self.learning_style:
            if i.characteristic_id == characteristic_id:
                to_remove.append(i)
        for remove in to_remove:
            self.learning_style.remove(remove)

    def delete_list_k(self, questionnaire_id):
        to_remove = []
        for i in self.list_k:
            if i.questionnaire_id == questionnaire_id:
                to_remove.append(i)
        for remove in to_remove:
            self.list_k.remove(remove)

    def delete_questionnaire(self, id):
        to_remove = []
        for i in self.questionnaire:
            if i.id == id:
                to_remove.append(i)
        for remove in to_remove:
            self.questionnaire.remove(remove)

    def delete_settings(self, user_id):
        to_remove = []
        for i in self.settings:
            if i.user_id == user_id:
                to_remove.append(i)
        for remove in to_remove:
            self.settings.remove(remove)

    def delete_student(self, user_id):
        to_remove = []
        for i in self.student:
            if i.user_id == user_id:
                to_remove.append(i)
        for remove in to_remove:
            self.student.remove(remove)

    def delete_student_course(self, student_id):
        to_remove = []
        for i in self.student_course:
            if i.student_id == student_id:
                to_remove.append(i)
        for remove in to_remove:
            self.student_course.remove(remove)

    def delete_student_learning_element(self, student_id):
        to_remove = []
        for i in self.student_learning_element:
            if i.student_id == student_id:
                to_remove.append(i)
        for remove in to_remove:
            self.student_learning_element.remove(remove)

    def delete_student_learning_element_visit(self, student_id):
        to_remove = []
        for i in self.student_learning_element_visit:
            if i.self.student_id == student_id:
                to_remove.append(i)
        for remove in to_remove:
            self.student_learning_element_visit.remove(remove)

    def delete_student_topic(self, student_id):
        to_remove = []
        for i in self.student_topic:
            if i.student_id == student_id:
                to_remove.append(i)
        for remove in to_remove:
            self.student_topic.remove(remove)

    def delete_student_topic_visit(self, student_id):
        to_remove = []
        for i in self.student_topic_visit:
            if i.student_id == student_id:
                to_remove.append(i)
        for remove in to_remove:
            self.student_topic_visit.remove(remove)

    def delete_teacher(self, user_id):
        to_remove = []
        for i in self.teacher:
            if i.user_id == user_id:
                to_remove.append(i)
        for remove in to_remove:
            self.teacher.remove(remove)

    def delete_teacher_course(self, teacher_id):
        to_remove = []
        for i in self.teacher_course:
            if i.teacher_id == teacher_id:
                to_remove.append(i)
        for remove in to_remove:
            self.teacher_course.remove(remove)

    def delete_topic(self, topic_id):
        to_remove = []
        for i in self.topic:
            if i.id == topic_id:
                to_remove.append(i)
        for remove in to_remove:
            self.topic.remove(remove)

    def delete_topic_learning_element_by_topic(self,
                                               topic_id):
        to_remove = []
        for i in self.topic_learning_element:
            if i.topic_id == topic_id:
                to_remove.append(i)
        for remove in to_remove:
            self.topic_learning_element.remove(remove)

    def delete_topic_learning_element_by_learning_element(self,
                                                          learning_element_id):
        to_remove = []
        for i in self.topic_learning_element:
            if i.learning_element_id == learning_element_id:
                to_remove.append(i)
        for remove in to_remove:
            self.topic_learning_element.remove(remove)

    def delete_user(self, user_id, lms_user_id):
        to_remove = []
        for i in self.user:
            if i.id == user_id and\
                    i.lms_user_id == lms_user_id:
                to_remove.append(i)
        for remove in to_remove:
            self.user.remove(remove)

    def get_admin_by_id(self, user_id):
        result = []
        for i in self.admin:
            if i.user_id == user_id:
                result.append(i)
        return result

    def get_admins_by_uni(self, university):
        result = []
        for i in self.admin:
            if i.university == university:
                result.append(i)
        return result

    def get_courses_by_uni(self, university):
        result = []
        for i in self.course:
            if i.university == university:
                result.append(i)
        return result

    def get_course_by_id(self, course_id):
        result = []
        for i in self.course:
            if i.id == course_id:
                result.append(i)
        return result

    def get_courses_by_student_id(self, student_id):
        result = []
        for i in self.student_course:
            if i.student_id == student_id:
                result.append(i)
        return result

    def get_course_creator_by_id(self,
                                 user_id):
        result = []
        for i in self.course_creator:
            if i.user_id == user_id:
                result.append(i)
        return result

    def get_courses_for_teacher(self, teacher_id):
        result = []
        for i in self.teacher_course:
            if i.teacher_id == teacher_id:
                result.append(i)
        return result

    def get_course_topic_by_course(self, course_id):
        result = []
        for i in self.course_topic:
            if i.course_id == course_id:
                result.append(i)
        return result

    def get_course_topic_by_topic(self, topic_id):
        result = []
        for i in self.course_topic:
            if i.topic_id == topic_id:
                result.append(i)
        return result

    def get_course_creators_by_uni(self, university):
        result = []
        for i in self.course_creator:
            if i.university == university:
                result.append(i)
        return result

    def get_ils_input_answers_by_id(self, questionnaire_id):
        result = []
        for i in self.ils_input_answers:
            if i.questionnaire_id == questionnaire_id:
                result.append(i)
        return result

    def get_ils_perception_answers_by_id(self, questionnaire_id):
        result = []
        for i in self.ils_perception_answers:
            if i.questionnaire_id == questionnaire_id:
                result.append(i)
        return result

    def get_ils_processing_answers_by_id(self, questionnaire_id):
        result = []
        for i in self.ils_processing_answers:
            if i.questionnaire_id == questionnaire_id:
                result.append(i)
        return result

    def get_ils_understanding_answers_by_id(self, questionnaire_id):
        result = []
        for i in self.ils_understanding_answers:
            if i.questionnaire_id == questionnaire_id:
                result.append(i)
        return result

    def get_knowledge(self, characteristic_id):
        result = []
        for i in self.knowledge:
            if i.characteristic_id == characteristic_id:
                result.append(i)
        return result

    def get_learning_analytics(self, characteristic_id):
        result = []
        for i in self.learning_analytics:
            if i.characteristic_id == characteristic_id:
                result.append(i)
        return result

    def get_learning_characteristics(self, student_id):
        result = []
        for i in self.learning_characteristics:
            if i.student_id == student_id:
                result.append(i)
        return result

    def get_learning_element_by_id(self, learning_element_id):
        result = []
        for i in self.learning_element:
            if i.id == learning_element_id:
                result.append(i)
        return result

    def get_learning_elements_by_uni(self, university):
        result = []
        for i in self.learning_element:
            if i.university == university:
                result.append(i)
        return result

    def get_learning_element_recommendation(self, learning_path_id):
        result = []
        for i in self.learning_path_learning_element:
            if i.learning_path_id == learning_path_id and i.recommended:
                result.append(i)
        return result

    def get_learning_path(self, student_id, course_id, topic_id):
        result = []
        for i in self.learning_path:
            if i.student_id == student_id and\
                i.course_id == course_id and\
                    i.topic_id == topic_id:
                result.append(i)
        return result

    def get_learning_paths(self, student_id):
        result = []
        for i in self.learning_path:
            if i.student_id == student_id:
                result.append(i)
        return result

    def get_learning_path_learning_element(self, learning_path_id):
        result = []
        for i in self.learning_path_learning_element:
            if i.learning_path_id == learning_path_id:
                result.append(i)
        return result

    def get_learning_strategy(self, characteristic_id):
        result = []
        for i in self.learning_strategy:
            if i.characteristic_id == characteristic_id:
                result.append(i)
        return result

    def get_learning_style(self, characteristic_id):
        result = []
        for i in self.learning_style:
            if i.characteristic_id == characteristic_id:
                result.append(i)
        return result

    def get_list_k_by_id(self, questionnaire_id):
        result = []
        for i in self.list_k:
            if i.questionnaire_id == questionnaire_id:
                result.append(i)
        return result

    def get_questionnaire_by_id(self, id):
        result = []
        for i in self.questionnaire:
            if i.id == id:
                result.append(i)
        return result

    def get_questionnaire_by_student_id(self, student_id):
        result = []
        for i in self.questionnaire:
            if i.student_id == student_id:
                result.append(i)
        return result

    def get_settings(self, user_id):
        result = []
        for i in self.settings:
            if i.user_id == user_id:
                result.append(i)
        return result

    def get_student_by_id(self, user_id):
        result = []
        for i in self.student:
            if i.user_id == user_id:
                result.append(i)
        return result

    def get_student_by_student_id(self, student_id):
        result = []
        for i in self.student:
            if i.id == student_id:
                result.append(i)
        return result

    def get_students_by_uni(self, university):
        result = []
        for i in self.student:
            if i.university == university:
                result.append(i)
        return result

    def get_student_learning_element(self,
                                     student_id,
                                     learning_element_id):
        result = []
        for i in self.student_learning_element:
            if i.student_id == student_id and\
                    i.learning_element_id == learning_element_id:
                result.append(i)
        return result

    def get_student_course(self, student_id, course_id):
        result = []
        for i in self.student_course:
            if i.student_id == student_id and\
                    i.course_id == course_id:
                result.append(i)
        return result

    def get_student_topic(self, student_id, topic_id):
        result = []
        for i in self.student_topic:
            if i.student_id == student_id and\
                    i.topic_id == topic_id:
                result.append(i)
        return result

    def get_sub_topics_for_topic_id(self, topic_id):
        result = []
        for i in self.topic:
            if i.parent_id == topic_id:
                result.append(i)
        return result

    def get_student_topic_visit(self, student_id, topic_id):
        result = []
        for i in self.student_topic_visit:
            if i.student_id == student_id and\
                    i.topic_id == topic_id:
                result.append(i)
        return result

    def get_teacher_by_id(self, user_id):
        result = []
        for i in self.teacher:
            if i.user_id == user_id:
                result.append(i)
        return result

    def get_teacher_by_teacher_id(self, teacher_id):
        result = []
        for i in self.teacher:
            if i.id == teacher_id:
                result.append(i)
        return result

    def get_teacher_by_uni(self, university):
        result = []
        for i in self.teacher:
            if i.university == university:
                result.append(i)
        return result

    def get_topics_by_uni(self, university):
        result = []
        for i in self.topic:
            if i.university == university:
                result.append(i)
        return result

    def get_topic_by_id(self, topic_id):
        result = []
        for i in self.topic:
            if i.id == topic_id:
                result.append(i)
        return result

    def get_topic_learning_element_by_topic(self, topic_id):
        result = []
        for i in self.topic_learning_element:
            if i.topic_id == topic_id:
                result.append(i)
        return result

    def get_topic_learning_element_by_learning_element(self,
                                                       learning_element_id):
        result = []
        for i in self.topic_learning_element:
            if i.learning_element_id == learning_element_id:
                result.append(i)
        return result

    def get_user_by_id(self, user_id, lms_user_id):
        result = []
        for i in self.user:
            if i.id == user_id and\
                    i.lms_user_id == lms_user_id:
                result.append(i)
        return result
    
    def get_user_by_lms_user_id(self, lms_user_id):
        result = []
        for i in self.user:
            if i.lms_user_id == lms_user_id:
                result.append(i)
        return result

    def get_users_by_uni(self, university):
        result = []
        for i in self.user:
            if i.university == university:
                result.append(i)
        return result

    def update_course(self, course_id, course):
        to_remove = next(
            (p for p in self.course if p.id == course_id), None)
        if to_remove is not None:
            self.course.remove(to_remove)
        course.id = len(self.course)
        self.course.add(course)

    def update_knowledge(self, characteristic_id, knowledge):
        to_remove = next(
            (p for p in self.knowledge
             if p.characteristic_id == characteristic_id), None)
        if to_remove is not None:
            self.knowledge.remove(to_remove)
        knowledge.id = len(self.knowledge)
        self.knowledge.add(knowledge)

    def update_learning_analytics(self, characteristic_id, learning_analytics):
        to_remove = next(
            (p for p in self.learning_analytics
             if p.characteristic_id == characteristic_id), None)
        if to_remove is not None:
            self.learning_analytics.remove(to_remove)
        learning_analytics.id = len(self.learning_analytics)
        self.learning_analytics.add(learning_analytics)

    def update_learning_element(self, learning_element_id, learning_element):
        to_remove = next(
            (p for p in self.learning_element
             if p.id == learning_element_id), None)
        if to_remove is not None:
            self.learning_element.remove(to_remove)
        learning_element.id = len(self.learning_element)
        self.learning_element.add(learning_element)

    def update_learning_strategy(self, characteristic_id, learning_strategy):
        to_remove = next(
            (p for p in self.learning_strategy
             if p.characteristic_id == characteristic_id), None)
        if to_remove is not None:
            self.learning_strategy.remove(to_remove)
        learning_strategy.id = len(self.learning_strategy)
        self.learning_strategy.add(learning_strategy)

    def update_learning_style(self, characteristic_id, learning_style):
        to_remove = next(
            (p for p in self.learning_style
             if p.characteristic_id == characteristic_id), None)
        if to_remove is not None:
            self.learning_style.remove(to_remove)
        learning_style.id = len(self.learning_style)
        self.learning_style.add(learning_style)

    def update_previous_learning_element_visit(self,
                                               student_id,
                                               visit_time):
        to_update = next(
            (p for p in self.student_learning_element_visit
             if p.student_id == student_id and
                p.visit_start is None), None)
        if to_update is not None:
            self.student_learning_element_visit.remove(to_update)
            to_update.id = len(self.student_learning_element_visit)
            to_update.visit_end = visit_time
            self.student_learning_element_visit.add(to_update)

    def update_previous_topic_visit(self,
                                    student_id,
                                    visit_time):
        to_update = next(
            (p for p in self.student_topic_visit
             if p.student_id == student_id and
                p.visit_start is None), None)
        if to_update is not None:
            self.student_topic_visit.remove(to_update)
            to_update.id = len(self.student_topic_visit)
            to_update.visit_end = visit_time
            self.student_topic_visit.add(to_update)

    def update_settings(self, user_id, settings):
        to_remove = next(
            (p for p in self.settings if p.user_id == user_id), None)
        if to_remove is not None:
            self.settings.remove(to_remove)
        settings.id = len(self.settings)
        self.settings.add(settings)

    def update_student_learning_element(self,
                                        student_id,
                                        learning_element_id,
                                        visit_time):
        to_update = next(
            (p for p in self.student_learning_element
             if p.student_id == student_id and
                p.learning_element_id == learning_element_id and
                p.visit_start is None), None)
        if to_update is not None:
            self.student_learning_element.remove(to_update)
            to_update.id = len(self.student_learning_element)
            to_update.done_at = visit_time
            to_update.done = True
            self.student_learning_element.add(to_update)

    def update_topic(self, topic_id, topic):
        to_remove = next(
            (p for p in self.topic if p.id == topic_id), None)
        if to_remove is not None:
            self.topic.remove(to_remove)
        topic.id = len(self.topic)
        self.topic.add(topic)

    def update_user(self, user_id, lms_user_id, user):
        to_remove = next((p for p in self.user if p.id == user_id
                          and p.lms_user_id == lms_user_id), None)
        if to_remove is not None:
            self.user.remove(to_remove)
        user.id = len(self.user)
        self.user.add(user)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):  # pragma: no cover
    def __init__(self):
        self.admin = FakeRepository()
        self.course = FakeRepository()
        self.course_creator = FakeRepository()
        self.course_creator_course = FakeRepository()
        self.course_topic = FakeRepository()
        self.ils_input_answers = FakeRepository()
        self.ils_perception_answers = FakeRepository()
        self.ils_processing_answers = FakeRepository()
        self.ils_understanding_answers = FakeRepository()
        self.knowledge = FakeRepository()
        self.learning_analytics = FakeRepository()
        self.learning_characteristics = FakeRepository()
        self.learning_element = FakeRepository()
        self.learning_element_rating = FakeRepository()
        self.learning_path = FakeRepository()
        self.learning_path_learning_element = FakeRepository()
        self.learning_path_topic = FakeRepository()
        self.learning_strategy = FakeRepository()
        self.learning_style = FakeRepository()
        self.list_k = FakeRepository()
        self.questionnaire = FakeRepository()
        self.settings = FakeRepository()
        self.student = FakeRepository()
        self.student_course = FakeRepository()
        self.student_learning_element = FakeRepository()
        self.student_learning_element_visit = FakeRepository()
        self.student_topic = FakeRepository()
        self.student_topic_visit = FakeRepository()
        self.teacher = FakeRepository()
        self.teacher_course = FakeRepository()
        self.topic = FakeRepository()
        self.topic_learning_element = FakeRepository()
        self.user = FakeRepository()
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass  # Just needed for working, has no function in test


user_name_example = "Max Mustermann"
university_example = "TH-AB"
creation_date_example = "2023-03-31T09:00:00Z"


ils_complete = [
    "ar_1_f1",
    "ar_2_f5",
    "ar_3_f9",
    "ar_4_f13",
    "ar_5_f17",
    "ar_6_f21",
    "ar_7_f25",
    "ar_8_f29",
    "ar_9_f33",
    "ar_10_f37",
    "ar_11_f41",
    "si_1_f2",
    "si_2_f6",
    "si_3_f10",
    "si_4_f14",
    "si_5_f18",
    "si_6_f22",
    "si_7_f26",
    "si_8_f30",
    "si_9_f34",
    "si_10_f38",
    "si_11_f42",
    "vv_1_f3",
    "vv_2_f7",
    "vv_3_f11",
    "vv_4_f15",
    "vv_5_f19",
    "vv_6_f23",
    "vv_7_f27",
    "vv_8_f31",
    "vv_9_f35",
    "vv_10_f39",
    "vv_11_f43",
    "sg_1_f4",
    "sg_2_f8",
    "sg_3_f12",
    "sg_4_f16",
    "sg_5_f20",
    "sg_6_f24",
    "sg_7_f28",
    "sg_8_f32",
    "sg_9_f36",
    "sg_10_f40",
    "sg_11_f44"
]
ils_short = [
    "ar_3_f9",
    "ar_4_f13",
    "ar_6_f21",
    "ar_7_f25",
    "ar_8_f29",
    "si_1_f2",
    "si_4_f14",
    "si_7_f26",
    "si_10_f38",
    "si_11_f42",
    "vv_2_f7",
    "vv_5_f19",
    "vv_7_f27",
    "vv_10_f39",
    "vv_11_f43",
    "sg_1_f4",
    "sg_2_f8",
    "sg_4_f16",
    "sg_10_f40",
    "sg_11_f44"
]
list_k_ids = [
    'org1_f1',
    'org2_f2',
    'org3_f3',
    'ela1_f4',
    'ela2_f5',
    'ela3_f6',
    'krp1_f7',
    'krp2_f8',
    'krp3_f9',
    'wie1_f10',
    'wie2_f11',
    'wie3_f12',
    'zp1_f13',
    'zp2_f14',
    'zp3_f15',
    'kon1_f16',
    'kon2_f17',
    'kon3_f18',
    'reg1_f19',
    'reg2_f20',
    'reg3_f21',
    'auf1_f22',
    'auf2_f23',
    'auf3_f24',
    'ans1_f25',
    'ans2_f26',
    'ans3_f27',
    'zei1_f28',
    'zei2_f29',
    'zei3_f30',
    'lms1_f31',
    'lms2_f32',
    'lms3_f33',
    'lit1_f34',
    'lit2_f35',
    'lit3_f36',
    'lu1_f37',
    'lu2_f38',
    'lu3_f39'
]
wrong_test_id = "Test ID"


# Helper Functions
def create_student_for_tests(uow):
    services.create_user(
        uow=uow,
        name="Sonja Studentin",
        university=university_example,
        lms_user_id=1,
        role="student"
    )


def create_teacher_for_tests(uow):
    services.create_user(
        uow=uow,
        name="Tim Teacher",
        university=university_example,
        lms_user_id=2,
        role="teacher"
    )


def create_course_creator_for_tests(uow):
    services.create_user(
        uow=uow,
        name="Claus Creator",
        university=university_example,
        lms_user_id=3,
        role="course creator"
    )


def create_admin_for_tests(uow):
    services.create_user(
        uow=uow,
        name="Achim Admin",
        university=university_example,
        lms_user_id=4,
        role="admin"
    )


def create_course_for_tests(uow):
    services.create_course(
        uow=uow,
        lms_id=1,
        name="Test",
        university=university_example,
        created_by=1,
        created_at="2023-01-01"
    )


def create_topic_for_tests(uow):
    services.create_topic(
        uow=uow,
        course_id=1,
        lms_id=1,
        is_topic=True,
        contains_le=False,
        parent_id=None,
        name="Test Topic",
        university=university_example,
        created_at="2023-01-01",
        created_by="Test"
    )


def create_sub_topic_for_tests(uow):
    services.create_topic(
        uow=uow,
        course_id=1,
        lms_id=2,
        is_topic=False,
        contains_le=True,
        parent_id=1,
        name="Test Sub-Topic",
        university=university_example,
        created_at="2023-01-01",
        created_by="Test"
    )


def create_learning_element_for_tests_1(uow):
    services.create_learning_element(
        uow=uow,
        topic_id=1,
        lms_id=1,
        activity_type="quiz",
        classification="RQ",
        name="Test LE",
        created_at="2017-01-01",
        created_by=user_name_example,
        university=university_example
    )


def create_learning_element_for_tests_2(uow):
    services.create_learning_element(
        uow=uow,
        topic_id=1,
        lms_id=2,
        activity_type="lesson",
        classification="BE",
        name="Test LE",
        created_at="2017-01-01",
        created_by=user_name_example,
        university=university_example
    )


def create_course_topic_for_tests(uow):
    services.create_course_topic(
        uow=uow,
        course_id=1,
        topic_id=1
    )


def create_topic_learning_element_for_tests(uow):
    services.create_topic_learning_element(
        uow=uow,
        topic_id=1,
        learning_element_id=1
    )


def create_learning_path_for_tests(uow):
    return services.create_learning_path(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        course_id=1,
        topic_id=1,
        algorithm="aco"
    )


def add_student_to_course_for_tests(uow):
    services.add_student_to_course(
        uow=uow,
        student_id=1,
        course_id=1
    )


def add_student_topic_visit_for_tests(uow):
    services.add_student_topic_visit(
        uow=uow,
        student_id=1,
        topic_id=1,
        visit_start="2023-01-01",
        previous_topic_id=None
    )


def add_student_sub_topic_visit_for_tests(uow):
    services.add_student_topic_visit(
        uow=uow,
        student_id=1,
        topic_id=2,
        visit_start="2023-01-01",
        previous_topic_id=1
    )


# Starting with Tests
def test_create_admin():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.admin.admin)
    user = UA.User(
        user_name_example,
        university_example,
        1,
        "admin"
    )
    result = services.create_admin(
        uow=uow,
        user=user
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.admin.admin)
    assert entries_beginning + 1 == entries_after


def test_create_course_creator():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.course_creator.course_creator)
    user = UA.User(
        user_name_example,
        university_example,
        1,
        "course creator"
    )
    result = services.create_course_creator(
        uow=uow,
        user=user
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.course_creator.course_creator)
    assert entries_beginning + 1 == entries_after


def test_create_settings():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.settings.settings)
    result = services.create_settings(
        uow=uow,
        user_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.settings.settings)
    assert entries_beginning + 1 == entries_after


def test_create_student():
    uow = FakeUnitOfWork()
    student_entries_beginning = len(uow.student.student)
    characteristic_entries_beginning = len(
        uow.learning_characteristics.learning_characteristics)
    style_entries_beginning = len(uow.learning_style.learning_style)
    user = UA.User(
        user_name_example,
        university_example,
        1,
        "student"
    )
    result = services.create_student(
        uow=uow,
        user=user
    )
    assert type(result) is dict
    assert result != {}
    student_entries_after = len(uow.student.student)
    characteristic_entries_after = len(
        uow.learning_characteristics.learning_characteristics)
    style_entries_after = len(uow.learning_style.learning_style)
    assert student_entries_beginning + 1 == student_entries_after
    assert characteristic_entries_beginning + 1 == characteristic_entries_after
    assert style_entries_beginning + 1 == style_entries_after


def test_create_teacher():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.teacher.teacher)
    user = UA.User(
        user_name_example,
        university_example,
        1,
        "teacher"
    )
    result = services.create_teacher(
        uow=uow,
        user=user
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.teacher.teacher)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example Admin
    (
        user_name_example,
        university_example,
        1,
        "admin"
    ),
    # Working Example Course Creator
    (
        user_name_example,
        university_example,
        1,
        "course creator"
    ),
    # Working Example Student
    (
        user_name_example,
        university_example,
        1,
        "student"
    ),
    # Working Example Teacher
    (
        user_name_example,
        university_example,
        1,
        "teacher"
    )
])
def test_create_user(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user_entries_beginning = len(uow.user.user)
    settings_entries_beginning = len(uow.settings.settings)
    result = services.create_user(
        uow=uow,
        name=name,
        university=university,
        lms_user_id=lms_user_id,
        role=role
    )
    assert type(result) is dict
    assert result != {}
    user_entries_after = len(uow.user.user)
    settings_entries_after = len(uow.settings.settings)
    assert user_entries_beginning + 1 == user_entries_after
    assert settings_entries_beginning + 1 == settings_entries_after


def test_create_learning_characteristics():
    uow = FakeUnitOfWork()
    entries_beginning = len(
        uow.learning_characteristics.learning_characteristics)
    result = services.create_learning_characteristics(
        uow=uow,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_characteristics.learning_characteristics)
    assert entries_beginning + 1 == entries_after


def test_create_learning_style():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.learning_style.learning_style)
    result = services.create_learning_style(
        uow=uow,
        characteristic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_style.learning_style)
    assert entries_beginning + 1 == entries_after


def test_create_learning_strategy():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.learning_strategy.learning_strategy)
    result = services.create_learning_strategy(
        uow=uow,
        characteristic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_strategy.learning_strategy)
    assert entries_beginning + 1 == entries_after


def test_create_knowledge():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.knowledge.knowledge)
    result = services.create_knowledge(
        uow=uow,
        characteristic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.knowledge.knowledge)
    assert entries_beginning + 1 == entries_after


def test_create_learning_analytics():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.learning_analytics.learning_analytics)
    result = services.create_learning_analytics(
        uow=uow,
        characteristic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_analytics.learning_analytics)
    assert entries_beginning + 1 == entries_after


def test_delete_admin():
    uow = FakeUnitOfWork()
    create_admin_for_tests(uow)
    entries_beginning = len(uow.admin.admin)
    result = services.delete_admin(uow, 1)
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.admin.admin)
    assert entries_beginning - 1 == entries_after


def test_delete_course_creator():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    entries_beginning = len(uow.course_creator.course_creator)
    result = services.delete_course_creator(uow, 1)
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.course_creator.course_creator)
    assert entries_beginning - 1 == entries_after


def test_delete_student():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    entries_beginning = len(uow.student.student)
    result = services.delete_student(uow, 1)
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.student.student)
    assert entries_beginning - 1 == entries_after


def test_delete_teacher():
    uow = FakeUnitOfWork()
    create_teacher_for_tests(uow)
    entries_beginning = len(uow.teacher.teacher)
    result = services.delete_teacher(uow, 1)
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.teacher.teacher)
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("role, lms_id", [
    # Working Example Admin
    (
        "admin",
        4
    ),
    # Working Example Course Creator
    (
        "course creator",
        3
    ),
    # Working Example Student
    (
        "student",
        1
    ),
    # Working Example Teacher
    (
        "teacher",
        2
    )
])
def test_delete_user(role, lms_id):
    uow = FakeUnitOfWork()
    match role:
        case "admin":
            create_admin_for_tests(uow)
        case "course creator":
            create_course_creator_for_tests(uow)
        case "student":
            create_student_for_tests(uow)
        case "teacher":
            create_teacher_for_tests(uow)
    entries_beginning = len(uow.user.user)
    settings_entries_beginning = len(uow.settings.settings)
    characteristics_entries_beginning = len(
        uow.learning_characteristics.learning_characteristics)
    result = services.delete_user(
        uow=uow,
        user_id=1,
        lms_user_id=lms_id
    )
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.user.user)
    settings_entries_end = len(uow.settings.settings)
    characteristics_entries_after = len(
        uow.learning_characteristics.learning_characteristics)
    assert settings_entries_beginning - 1 == settings_entries_end
    assert entries_beginning - 1 == entries_after
    if role == 'student':
        assert characteristics_entries_beginning - 1\
            == characteristics_entries_after


def test_update_settings():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.update_settings_for_user(
        uow=uow,
        user_id=1,
        theme="dark"
    )
    assert type(result) is dict
    assert result != {}
    assert result['theme'] == "dark"


def test_reset_settings():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    services.update_settings_for_user(
        uow=uow,
        user_id=1,
        theme="dark"
    )
    result = services.reset_settings(
        uow=uow,
        user_id=1
    )
    assert type(result) is dict
    assert result != {}
    assert result['theme'] == "Standard"


def test_get_settings_for_user():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.get_settings_for_user(uow, 1)
    assert type(result) == dict
    assert result != {}


def test_update_user():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.update_user(
        uow, 1, 1, "Maria Musterfraun", university_example)
    assert type(result) == dict
    assert result != {}


def test_get_learning_characteristics():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.get_learning_characteristics(
        uow,
        1
    )
    assert type(result) == dict
    assert result != {}
    keys_expected = ['knowledge', 'learning_analytics',
                     'learning_strategy', 'learning_style']
    for key in keys_expected:
        assert key in result.keys()
        assert result[key] is not None


def test_reset_learning_characteristics():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    entries_beginning = len(
        uow.learning_characteristics.learning_characteristics)
    result = services.reset_learning_characteristics(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1
    )
    entries_after = len(
        uow.learning_characteristics.learning_characteristics)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning == entries_after
    assert result['learning_style']['perception_value'] == 0


def test_create_ils_input_answers():
    uow = FakeUnitOfWork()
    ils_input_answers = {}
    for key in ils_complete:
        if key.startswith("vv"):
            ils_input_answers[key] = "a"
    entries_beginning = len(uow.ils_input_answers.ils_input_answers)
    result = services.create_ils_input_answers(
        uow=uow,
        questionnaire_id=1,
        answers=ils_input_answers
    )
    entries_after = len(uow.ils_input_answers.ils_input_answers)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


def test_create_ils_perception_answers():
    uow = FakeUnitOfWork()
    ils_perception_answers = {}
    for key in ils_complete:
        if key.startswith("si"):
            ils_perception_answers[key] = "a"
    entries_beginning = len(uow.ils_perception_answers.ils_perception_answers)
    result = services.create_ils_perception_answers(
        uow=uow,
        questionnaire_id=1,
        answers=ils_perception_answers
    )
    entries_after = len(uow.ils_perception_answers.ils_perception_answers)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


def test_create_ils_processing_answers():
    uow = FakeUnitOfWork()
    ils_processing_answers = {}
    for key in ils_complete:
        if key.startswith("ar"):
            ils_processing_answers[key] = "a"
    entries_beginning = len(uow.ils_processing_answers.ils_processing_answers)
    result = services.create_ils_processing_answers(
        uow=uow,
        questionnaire_id=1,
        answers=ils_processing_answers
    )
    entries_after = len(uow.ils_processing_answers.ils_processing_answers)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


def test_create_ils_understanding_answers():
    uow = FakeUnitOfWork()
    ils_understanding_answers = {}
    for key in ils_complete:
        if key.startswith("sg"):
            ils_understanding_answers[key] = "a"
    entries_beginning = len(
        uow.ils_understanding_answers.ils_understanding_answers)
    result = services.create_ils_understanding_answers(
        uow=uow,
        questionnaire_id=1,
        answers=ils_understanding_answers
    )
    entries_after = len(
        uow.ils_understanding_answers.ils_understanding_answers)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


def test_create_list_k():
    uow = FakeUnitOfWork()
    list_k_answers = {}
    for key in list_k_ids:
        list_k_answers[key] = 1
    entries_beginning = len(uow.list_k.list_k)
    result = services.create_list_k(
        uow=uow,
        questionnaire_id=1,
        answers=list_k_answers
    )
    entries_after = len(uow.list_k.list_k)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("full_version", [
    # Working Example short form
    (
        True
    ),
    # Working Example full form
    (
        False
    )
])
def test_create_questionnaire(full_version):
    uow = FakeUnitOfWork()
    services.create_learning_characteristics(
        uow=uow,
        student_id=1
    )
    entries_beginning = len(uow.questionnaire.questionnaire)
    ils_answers = {}
    list_k_answers = {}
    if full_version:
        for key in ils_complete:
            ils_answers[key] = "a"
    else:
        for key in ils_short:
            ils_answers[key] = "a"
    for key in list_k_ids:
        list_k_answers[key] = 1
    result = services.create_questionnaire(
        uow=uow,
        student_id=1,
        ils_answers=ils_answers,
        list_k_answers=list_k_answers
    )
    entries_after = len(uow.questionnaire.questionnaire)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after
    services.create_questionnaire(
        uow=uow,
        student_id=1,
        ils_answers=ils_answers,
        list_k_answers=list_k_answers
    )
    entries_after2 = len(uow.questionnaire.questionnaire)
    assert type(result) == dict
    assert result != {}
    assert entries_after == entries_after2


def test_delete_ils_input_answers():
    uow = FakeUnitOfWork()
    ils_input_answers = {}
    for key in ils_complete:
        if key.startswith("vv"):
            ils_input_answers[key] = "a"
    services.create_ils_input_answers(
        uow=uow,
        questionnaire_id=1,
        answers=ils_input_answers
    )
    entries_beginning = len(uow.ils_input_answers.ils_input_answers)
    result = services.delete_ils_input_answers(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.ils_input_answers.ils_input_answers)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


def test_delete_ils_perception_answers():
    uow = FakeUnitOfWork()
    ils_perception_answers = {}
    for key in ils_complete:
        if key.startswith("si"):
            ils_perception_answers[key] = "a"
    services.create_ils_perception_answers(
        uow=uow,
        questionnaire_id=1,
        answers=ils_perception_answers
    )
    entries_beginning = len(uow.ils_perception_answers.ils_perception_answers)
    result = services.delete_ils_perception_answers(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.ils_perception_answers.ils_perception_answers)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


def test_delete_ils_processing_answers():
    uow = FakeUnitOfWork()
    ils_processing_answers = {}
    for key in ils_complete:
        if key.startswith("ar"):
            ils_processing_answers[key] = "a"
    services.create_ils_processing_answers(
        uow=uow,
        questionnaire_id=1,
        answers=ils_processing_answers
    )
    entries_beginning = len(uow.ils_processing_answers.ils_processing_answers)
    result = services.delete_ils_processing_answers(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.ils_processing_answers.ils_processing_answers)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


def test_delete_ils_understanding_answers():
    uow = FakeUnitOfWork()
    ils_understanding_answers = {}
    for key in ils_complete:
        if key.startswith("sg"):
            ils_understanding_answers[key] = "a"
    services.create_ils_understanding_answers(
        uow=uow,
        questionnaire_id=1,
        answers=ils_understanding_answers
    )
    entries_beginning = len(
        uow.ils_understanding_answers.ils_understanding_answers)
    result = services.delete_ils_understanding_answers(
        uow=uow,
        questionnaire_id=1,
    )
    entries_after = len(
        uow.ils_understanding_answers.ils_understanding_answers)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


def test_delete_list_k():
    uow = FakeUnitOfWork()
    list_k_answers = {}
    for key in list_k_ids:
        list_k_answers[key] = 1
    services.create_list_k(
        uow=uow,
        questionnaire_id=1,
        answers=list_k_answers
    )
    entries_beginning = len(uow.list_k.list_k)
    result = services.delete_list_k(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.list_k.list_k)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("full_version", [
    # Working Example complete ILS
    (
        True
    ),
    # Working Example Short Form
    (
        False
    )
])
def test_delete_questionnaire(full_version):
    uow = FakeUnitOfWork()
    services.create_learning_characteristics(
        uow=uow,
        student_id=1
    )
    ils_answers = {}
    list_k_answers = {}
    if full_version:
        for key in ils_complete:
            ils_answers[key] = "a"
    else:
        for key in ils_short:
            ils_answers[key] = "a"
    for key in list_k_ids:
        list_k_answers[key] = 1
    services.create_questionnaire(
        uow=uow,
        student_id=1,
        ils_answers=ils_answers,
        list_k_answers=list_k_answers
    )
    entries_beginning = len(uow.questionnaire.questionnaire)
    result = services.delete_questionnaire(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.questionnaire.questionnaire)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


def test_create_course():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    entries_beginning = len(uow.course.course)
    entries_beginning_course_creator_course =\
        len(uow.course_creator_course.course_creator_course)
    result = services.create_course(
        uow=uow,
        lms_id=1,
        name="Test Course",
        university=university_example,
        created_by=1,
        created_at="2023-01-01"
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.course.course)
    entries_after_course_creator_course =\
        len(uow.course_creator_course.course_creator_course)
    assert entries_beginning + 1 == entries_after
    assert entries_beginning_course_creator_course + 1 ==\
        entries_after_course_creator_course


def test_get_course_by_id():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_course_for_tests(uow)
    result = services.get_course_by_id(
        uow=uow,
        user_id=1,
        lms_user_id=3,
        course_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_update_course():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_course_for_tests(uow)
    entries_beginning = len(uow.course.course)
    result = services.update_course(
        uow=uow,
        course_id=1,
        lms_id=1,
        name="Test Course 2",
        university=university_example
    )
    assert type(result) is dict
    entries_after = len(uow.course.course)
    assert entries_beginning == entries_after


def test_delete_course():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_course_for_tests(uow)
    entries_beginning = len(uow.course.course)
    result = services.delete_course(
        uow=uow,
        course_id=1
    )
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.course.course)
    assert entries_beginning - 1 == entries_after


def test_create_course_topic():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.course_topic.course_topic)
    result = services.create_course_topic(
        uow=uow,
        course_id=1,
        topic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.course_topic.course_topic)
    assert entries_beginning + 1 == entries_after


def test_get_course_topic_by_course():
    uow = FakeUnitOfWork()
    create_course_topic_for_tests(uow)
    result = services.get_course_topic_by_course(
        uow=uow,
        course_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_course_topic_by_topic():
    uow = FakeUnitOfWork()
    create_course_topic_for_tests(uow)
    result = services.get_course_topic_by_topic(
        uow=uow,
        topic_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_delete_course_topic_by_course():
    uow = FakeUnitOfWork()
    create_course_topic_for_tests(uow)
    entries_beginning = len(uow.course_topic.course_topic)
    result = services.delete_course_topic_by_course(
        uow=uow,
        course_id=1
    )
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.course_topic.course_topic)
    assert entries_beginning - 1 == entries_after


def test_delete_course_topic_by_topic():
    uow = FakeUnitOfWork()
    create_course_topic_for_tests(uow)
    entries_beginning = len(uow.course_topic.course_topic)
    result = services.delete_course_topic_by_topic(
        uow=uow,
        topic_id=1
    )
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.course_topic.course_topic)
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("lms_id, is_topic, parent_id, contains_le,\
                         name, university, created_by,\
                         created_at", [
    # Working Example Topic
    (
        1,
        True,
        None,
        False,
        "Test Topic",
        university_example,
        user_name_example,
        time.time()
    ),
    # Working Example Sub-Topic
    (
        2,
        False,
        1,
        True,
        "Test Sub-Topic",
        university_example,
        user_name_example,
        time.time()
    ),
])
def test_create_topic(lms_id, is_topic, parent_id, contains_le,
                      name, university, created_by,
                      created_at):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.topic.topic)
    result = services.create_topic(
        uow=uow,
        course_id=1,
        lms_id=lms_id,
        is_topic=is_topic,
        parent_id=parent_id,
        contains_le=contains_le,
        name=name,
        university=university,
        created_at=created_at,
        created_by=created_by
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.topic.topic)
    assert entries_beginning + 1 == entries_after
    assert len(uow.course_topic.course_topic) == 1


def test_get_topic_by_id():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_sub_topic_for_tests(uow)
    result = services.get_topic_by_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        course_id=1,
        student_id=1,
        topic_id=1
    )
    assert type(result) is dict
    assert result != {}
    result2 = services.get_topic_by_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        course_id=1,
        student_id=1,
        topic_id=2
    )
    assert type(result2) is dict
    assert result2 != {}


def test_update_topic():
    uow = FakeUnitOfWork()
    create_topic_for_tests(uow)
    create_sub_topic_for_tests(uow)
    entries_beginning = len(uow.topic.topic)
    last_updated = time.time()
    result = services.update_topic(
        uow=uow,
        topic_id=1,
        lms_id=1,
        is_topic=True,
        parent_id=None,
        contains_le=False,
        name="Test Topic Updated",
        university=university_example,
        created_at=last_updated,
        created_by=1,
        last_updated=last_updated
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.topic.topic)
    assert entries_beginning == entries_after
    assert result['last_updated'] == last_updated
    last_updated2 = time.time()
    result2 = services.update_topic(
        uow=uow,
        topic_id=2,
        lms_id=1,
        is_topic=False,
        parent_id=1,
        contains_le=True,
        name="Test Sub-Topic Updated",
        university=university_example,
        created_at=last_updated2,
        created_by=1,
        last_updated=last_updated2
    )
    assert type(result2) is dict
    assert result2 != {}
    entries_after = len(uow.topic.topic)
    assert entries_beginning == entries_after
    assert result2['last_updated'] == last_updated2


def test_delete_topic():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_sub_topic_for_tests(uow)
    entries_beginning = len(uow.topic.topic)
    result = services.delete_topic(
        uow=uow,
        topic_id=2
    )
    entries_after = len(uow.topic.topic)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after
    result2 = services.delete_topic(
        uow=uow,
        topic_id=1
    )
    entries_after2 = len(uow.topic.topic)
    assert type(result2) == dict
    assert result2 == {}
    assert entries_beginning - 2 == entries_after2


def test_create_topic_learning_element():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.topic_learning_element.topic_learning_element)
    result = services.create_topic_learning_element(
        uow=uow,
        topic_id=1,
        learning_element_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.topic_learning_element.topic_learning_element)
    assert entries_beginning + 1 == entries_after


def test_get_topic_learning_element_by_topic():
    uow = FakeUnitOfWork()
    create_topic_learning_element_for_tests(uow)
    result = services.get_topic_learning_element_by_topic(
        uow=uow,
        topic_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_topic_learning_element_by_le():
    uow = FakeUnitOfWork()
    create_topic_learning_element_for_tests(uow)
    result = services.get_topic_learning_element_by_learning_element(
        uow=uow,
        learning_element_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_delete_topic_learning_element_by_topic():
    uow = FakeUnitOfWork()
    create_topic_learning_element_for_tests(uow)
    entries_beginning = len(uow.topic_learning_element.topic_learning_element)
    result = services.delete_topic_learning_element_by_topic(
        uow=uow,
        topic_id=1
    )
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.topic_learning_element.topic_learning_element)
    assert entries_beginning - 1 == entries_after


def test_delete_topic_learning_element_by_le():
    uow = FakeUnitOfWork()
    create_topic_learning_element_for_tests(uow)
    entries_beginning = len(uow.topic_learning_element.topic_learning_element)
    result = services.delete_topic_learning_element_by_learning_element(
        uow=uow,
        learning_element_id=1
    )
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.topic_learning_element.topic_learning_element)
    assert entries_beginning - 1 == entries_after


def test_create_learning_element():
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.learning_element.learning_element)
    result = services.create_learning_element(
        uow=uow,
        topic_id=1,
        lms_id=1,
        activity_type="quiz",
        classification="RQ",
        name="Test Quiz",
        created_at=time.time(),
        created_by=user_name_example,
        university=university_example
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_element.learning_element)
    assert entries_beginning + 1 == entries_after
    assert len(uow.topic_learning_element.topic_learning_element) == 1


def test_get_learning_element_by_id():
    uow = FakeUnitOfWork()
    create_learning_element_for_tests_1(uow)
    result = services.get_learning_element_by_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        course_id=1,
        topic_id=1,
        learning_element_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_update_learning_element():
    uow = FakeUnitOfWork()
    create_learning_element_for_tests_1(uow)
    entries_beginning = len(uow.learning_element.learning_element)
    last_updated = time.time()
    result = services.update_learning_element(
        uow=uow,
        learning_element_id=1,
        lms_id=1,
        activity_type="quiz",
        classification="RQ",
        name="Test Quiz",
        created_at=last_updated,
        created_by=user_name_example,
        university=university_example,
        last_updated=last_updated
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_element.learning_element)
    assert entries_beginning == entries_after
    assert result['last_updated'] == last_updated


def test_delete_learning_element():
    uow = FakeUnitOfWork()
    create_learning_element_for_tests_1(uow)
    entries_beginning = len(uow.learning_element.learning_element)
    result = services.delete_learning_element(
        uow=uow,
        course_id=1,
        topic_id=1,
        learning_element_id=1
    )
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.learning_element.learning_element)
    assert entries_beginning - 1 == entries_after


def test_add_student_to_course():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_learning_element_for_tests_1(uow)
    entries_beginning_course = len(uow.student_course.student_course)
    entries_beginning_topic = len(uow.student_topic.student_topic)
    entries_beginning_le = len(uow.student_learning_element
                               .student_learning_element)
    result = services.add_student_to_course(
        uow=uow,
        student_id=1,
        course_id=1
    )
    entries_after_course = len(uow.student_course.student_course)
    entries_after_topic = len(uow.student_topic.student_topic)
    entries_after_le = len(uow.student_learning_element
                           .student_learning_element)
    assert type(result) is dict
    assert result != {}
    assert entries_beginning_course + 1 == entries_after_course
    assert entries_after_topic > entries_beginning_topic
    assert entries_after_le > entries_beginning_le
    with pytest.raises(err.AlreadyExisting):
        services.add_student_to_course(
            uow=uow,
            student_id=1,
            course_id=1
        )


def test_add_teacher_to_course():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_teacher_for_tests(uow)
    create_course_for_tests(uow)
    entries_beginning_course = len(uow.teacher_course.teacher_course)
    result = services.add_teacher_to_course(
        uow=uow,
        teacher_id=1,
        course_id=1
    )
    entries_after_course = len(uow.teacher_course.teacher_course)
    assert type(result) is dict
    assert result != {}
    assert entries_beginning_course + 1 == entries_after_course
    with pytest.raises(err.AlreadyExisting):
        services.add_teacher_to_course(
            uow=uow,
            teacher_id=1,
            course_id=1
        )


def test_create_course_creator_course():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    entries_beginning = len(uow.course_creator_course.course_creator_course)
    result = services.add_course_creator_to_course(
        uow=uow,
        created_by=1,
        course_id=1,
        created_at="2023-01-01"
    )
    entries_after = len(uow.course_creator_course.course_creator_course)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


def test_student_learning_element_visit():
    uow = FakeUnitOfWork()
    create_learning_element_for_tests_1(uow)
    create_student_for_tests(uow)
    entries_beginning = len(uow.student_learning_element_visit
                            .student_learning_element_visit)
    result = services.add_student_learning_element_visit(
        uow=uow,
        student_id=1,
        learning_element_id=1,
        visit_start="2023-01-01"
    )
    entries_after = len(uow.student_learning_element_visit
                        .student_learning_element_visit)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


def test_student_topic_visit():
    uow = FakeUnitOfWork()
    create_topic_for_tests(uow)
    create_student_for_tests(uow)
    entries_beginning = len(uow.student_topic_visit
                            .student_topic_visit)
    result = services.add_student_topic_visit(
        uow=uow,
        student_id=1,
        topic_id=1,
        visit_start="2023-01-01",
        previous_topic_id=None
    )
    entries_after = len(uow.student_topic_visit
                        .student_topic_visit)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after
    result = services.add_student_topic_visit(
        uow=uow,
        student_id=1,
        topic_id=1,
        visit_start="2023-01-02",
        previous_topic_id=1
    )
    entries_after2 = len(uow.student_topic_visit
                            .student_topic_visit)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 2 == entries_after2


@pytest.mark.parametrize("number_of_les", [
    # 0
    (0),
    # 1
    (1),
    # 2
    (2)
])
def test_create_learning_path(number_of_les):
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    if number_of_les > 0:
        create_learning_element_for_tests_1(uow)
    if number_of_les > 1:
        create_learning_element_for_tests_2(uow)
    entries_beginning_path = len(uow.learning_path
                                 .learning_path)
    entries_beginning_path_le = len(uow.learning_path_learning_element
                                    .learning_path_learning_element)
    if number_of_les == 0:
        with pytest.raises(err.NoLearningElementsError):
            create_learning_path_for_tests(uow)
    else:
        result = create_learning_path_for_tests(uow)
        assert type(result) == dict
        assert result != {}
        entries_after_path = len(uow.learning_path
                                 .learning_path)
        entries_after_path_le = len(uow.learning_path_learning_element
                                    .learning_path_learning_element)
        assert entries_beginning_path + 1 == entries_after_path
        assert entries_beginning_path_le + number_of_les \
            == entries_after_path_le
        result = create_learning_path_for_tests(uow)
        assert type(result) == dict
        assert result != {}
        entries_after_path_2 = len(uow.learning_path
                                   .learning_path)
        entries_after_path_le_2 = len(uow.learning_path_learning_element
                                      .learning_path_learning_element)
        assert entries_after_path == entries_after_path_2
        assert entries_after_path_le == entries_after_path_le_2


def test_delete_learning_paths():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_learning_element_for_tests_1(uow)
    create_learning_path_for_tests(uow)
    entries_beginning_path = len(uow.learning_path
                                 .learning_path)
    entries_beginning_path_le = len(uow.learning_path_learning_element
                                    .learning_path_learning_element)
    result = services.delete_learning_paths(
        uow=uow,
        student_id=1
    )
    assert result is None
    entries_after_path = len(uow.learning_path
                             .learning_path)
    entries_after_path_le = len(uow.learning_path_learning_element
                                .learning_path_learning_element)
    assert entries_beginning_path - 1 == entries_after_path
    assert entries_beginning_path_le - 1 == entries_after_path_le


def test_get_courses_by_student_id():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    add_student_to_course_for_tests(uow)
    result = services.get_courses_by_student_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_knowledge_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.get_knowledge_by_student_id(
        uow=uow,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_learning_analytics_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.get_learning_analytics_by_student_id(
        uow=uow,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_learning_style_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.get_learning_style_by_student_id(
        uow=uow,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_learning_strategy_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.get_learning_strategy_by_student_id(
        uow=uow,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_les_for_course_id():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_learning_element_for_tests_1(uow)
    add_student_to_course_for_tests(uow)
    result = services.get_learning_elements_for_course_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        course_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_les_for_course_and_topic_id():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_learning_element_for_tests_1(uow)
    add_student_to_course_for_tests(uow)
    result = services.get_learning_elements_for_course_and_topic_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        course_id=1,
        topic_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_get_learning_element_recommendation():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_learning_element_for_tests_1(uow)
    add_student_to_course_for_tests(uow)
    create_learning_path_for_tests(uow)
    result = services.get_learning_element_recommendation(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        course_id=1,
        topic_id=1
    )
    assert type(result) == dict
    assert result != {}


def test_get_learning_path():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_learning_element_for_tests_1(uow)
    add_student_to_course_for_tests(uow)
    create_learning_path_for_tests(uow)
    result = services.get_learning_path(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        course_id=1,
        topic_id=1
    )
    assert type(result) == dict
    assert result != {}


def test_get_sub_topics():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_sub_topic_for_tests(uow)
    create_learning_element_for_tests_1(uow)
    add_student_to_course_for_tests(uow)
    add_student_topic_visit_for_tests(uow)
    add_student_sub_topic_visit_for_tests(uow)
    result = services.get_sub_topic_by_topic_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        course_id=1,
        topic_id=1
    )
    assert type(result) == dict
    assert result != {}


def test_get_topics_by_student_and_course_id():
    uow = FakeUnitOfWork()
    create_course_creator_for_tests(uow)
    create_student_for_tests(uow)
    create_course_for_tests(uow)
    create_topic_for_tests(uow)
    create_sub_topic_for_tests(uow)
    create_learning_element_for_tests_1(uow)
    add_student_to_course_for_tests(uow)
    add_student_topic_visit_for_tests(uow)
    add_student_sub_topic_visit_for_tests(uow)
    result = services.get_topics_by_student_and_course_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        course_id=1
    )
    assert type(result) == dict
    assert result != {}


def test_get_user_by_admin():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    create_admin_for_tests(uow)
    result = services.get_users_by_admin(
        uow=uow,
        user_id=1,
        lms_user_id=1
    )
    assert type(result) == dict
    assert result != {}


def test_reset_knowledge_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.reset_knowledge_by_student_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_reset_learning_analytics_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.reset_learning_analytics_by_student_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_reset_learning_style_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.reset_learning_style_by_student_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_reset_learning_strategy_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.reset_learning_strategy_by_student_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}


def test_update_learning_style_by_student_id():
    uow = FakeUnitOfWork()
    create_student_for_tests(uow)
    result = services.update_learning_style_by_student_id(
        uow=uow,
        user_id=1,
        lms_user_id=1,
        student_id=1,
        perception_dimension="act",
        perception_value=11,
        input_dimension="vis",
        input_value=11,
        processing_dimension="sns",
        processing_value=11,
        understanding_dimension="glo",
        understanding_value=11
    )
    assert type(result) is dict
    assert result != {}
