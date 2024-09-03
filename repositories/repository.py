import abc

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.userAdministartion import model as UA
from errors import errors as err


class AbstractRepository(abc.ABC):  # pragma: no cover
    @abc.abstractmethod
    def add_course_creator_to_course(
        self, course_creator_cours
    ) -> DM.CourseCreatorCourse:
        raise NotImplementedError

    @abc.abstractmethod
    def add_student_to_course(self, student_course) -> DM.StudentCourse:
        raise NotImplementedError

    @abc.abstractmethod
    def add_student_to_learning_element(self, student_learning_element):
        raise NotImplementedError

    @abc.abstractmethod
    def add_student_to_topic(self, student_topic):
        raise NotImplementedError

    @abc.abstractmethod
    def add_student_learning_element_visit(self, student_learning_element_visit):
        raise NotImplementedError

    @abc.abstractmethod
    def add_student_topic_visit(self, student_topic_visit):
        raise NotImplementedError

    @abc.abstractmethod
    def add_teacher_to_course(self, teacher_course) -> DM.TeacherCourse:
        raise NotImplementedError

    @abc.abstractmethod
    def create_admin(self, admin: UA.Admin) -> UA.Admin:
        raise NotImplementedError

    @abc.abstractmethod
    def create_course(self, course) -> DM.Course:
        raise NotImplementedError

    @abc.abstractmethod
    def create_course_creator(
        self, course_creator: UA.CourseCreator
    ) -> UA.CourseCreator:
        raise NotImplementedError

    @abc.abstractmethod
    def create_course_topic(self, course_topic) -> DM.CourseTopic:
        raise NotImplementedError

    @abc.abstractmethod
    def create_default_learning_path_element(
        self, default_learning_path_element: TM.DefaultLearningPathElement
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ils_input_answers(
        self, ils_input_answers: LM.IlsInputAnswers
    ) -> LM.IlsInputAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ils_perception_answers(
        self, ils_perception_answers: LM.IlsPerceptionAnswers
    ) -> LM.IlsPerceptionAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ils_processing_answers(
        self, ils_processing_answers: LM.IlsProcessingAnswers
    ) -> LM.IlsProcessingAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ils_understanding_answers(
        self, ils_understanding_answers: LM.IlsUnderstandingAnswers
    ) -> LM.IlsUnderstandingAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def create_knowledge(self, knowledge) -> LM.Knowledge:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_analytics(self, learning_analytics) -> LM.LearningAnalytics:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_characteristics(
        self, learning_characteristic
    ) -> LM.LearningCharacteristic:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_element(self, learning_element) -> DM.LearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_path(self, learning_path) -> TM.LearningPath:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_path_algorithm(
        self, learning_path_algorithm: TM.LearningPathAlgorithm
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_path_learning_element(
        self, learning_path_learning_element
    ) -> TM.LearningPathLearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_strategy(self, learning_strategy) -> LM.LearningStrategy:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_style(self, learning_style) -> LM.LearningStyle:
        raise NotImplementedError

    @abc.abstractmethod
    def create_questionnaire_list_k(
        self, questionnaire_list_k: LM.QuestionnaireListK
    ) -> LM.QuestionnaireListK:
        raise NotImplementedError

    @abc.abstractmethod
    def create_questionnaire_ils(
        self, questionnaire_ils: LM.QuestionnaireIls
    ) -> LM.QuestionnaireIls:
        raise NotImplementedError

    @abc.abstractmethod
    def create_settings(self, settings) -> UA.Settings:
        raise NotImplementedError

    @abc.abstractmethod
    def create_contact_form(self, contact_form: UA.ContactForm) -> UA.ContactForm:
        raise NotImplementedError

    @abc.abstractmethod
    def create_news(self, news: UA.News) -> UA.News:
        raise NotImplementedError

    @abc.abstractmethod
    def create_student(self, student: UA.Student) -> UA.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def add_student_lpath_le_algorithm(
        self,
        student_lpath_le_algorithm: DM.StudentLearningPathLearningElementAlgorithm,
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def create_teacher(self, teacher: UA.Teacher) -> UA.Teacher:
        raise NotImplementedError

    @abc.abstractmethod
    def create_topic(self, topic) -> DM.Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def create_topic_learning_element(
        self, topic_learning_element
    ) -> DM.TopicLearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def create_user(self, user: UA.User) -> UA.User:
        raise NotImplementedError

    @abc.abstractmethod
    def create_student_rating(self, student_rating: LM.StudentRating):
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_element_rating(
        self, learning_element_rating: DM.LearningElementRating
    ):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_admin(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_contact_form(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_news(self):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_course(self, course_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_course_topic_by_course(self, course_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_course_topic_by_topic(self, topic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_course_creator(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_course_creator_course(self, course_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ils_input_answers(self, questionnaire_ils_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ils_perception_answers(self, questionnaire_ils_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ils_processing_answers(self, questionnaire_ils_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ils_understanding_answers(self, questionnaire_ils_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_knowledge(self, characteristic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_questionnaire_list_k(self, questionnaire_list_k_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_questionnaire_ils(self, questionnaire_ils_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_analytics(self, characteristic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_characteristics(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_element(self, learning_element_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_path(self, learning_path_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_path_learning_element(self, learning_path_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_path_topic(self, learning_path_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_strategy(self, characteristic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_style(self, characteristic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_settings(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_student(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_student_course(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_student_learning_element(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_student_learning_element_visit(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_student_topic(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_student_topic_visit(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_teacher(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_teacher_course(self, teacher_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_topic(self, topic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_topic_learning_element_by_topic(self, topic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_topic_learning_element_by_learning_element(self, learning_element_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_user(self, user_id, lms_user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_admin_by_id(self, user_id, lms_user_id, admin_id) -> UA.Admin:
        raise NotImplementedError

    @abc.abstractmethod
    def get_admins_by_uni(self, university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_courses_by_uni(self, university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_course_by_id(self, course_id) -> DM.Course:
        raise NotImplementedError

    @abc.abstractmethod
    def get_course_topic_by_course(self, course_id) -> DM.CourseTopic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_course_topic_by_topic(self, topic_id) -> DM.CourseTopic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_course_creator_by_id(self, user_id) -> UA.CourseCreator:
        raise NotImplementedError

    @abc.abstractmethod
    def get_course_creators_by_uni(self, university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_courses_by_student_id(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_courses_for_teacher(self, teacher_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_ils_input_answers_by_id(self, questionnaire_ils_id) -> LM.IlsInputAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def get_ils_perception_answers_by_id(
        self, questionnaire_ils_id
    ) -> LM.IlsPerceptionAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def get_ils_processing_answers_by_id(
        self, questionnaire_ils_id
    ) -> LM.IlsProcessingAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def get_ils_understanding_answers_by_id(
        self, questionnaire_ils_id
    ) -> LM.IlsUnderstandingAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def get_knowledge(self, characteristic_id, knowledge) -> LM.Knowledge:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_analytics(self, characteristic_id) -> LM.LearningAnalytics:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_characteristics(self, student_id) -> LM.LearningCharacteristic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_element_by_id(self, learning_element_id) -> DM.LearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_elements_by_uni(self, university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_element_recommendation(self, learning_path_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_path(self, student_id, course_id, topic_id) -> TM.LearningPath:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_paths(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_path_algorithm_by_id(self, id: int) -> TM.LearningPathAlgorithm:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_path_algorithm_by_short_name(
        self, short_name: str
    ) -> TM.LearningPathAlgorithm:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_path_learning_element(
        self, learning_path_id
    ) -> TM.LearningPathLearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_strategy(self, characteristic_id) -> LM.LearningStrategy:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_style(self, characteristic_id) -> LM.LearningStyle:
        raise NotImplementedError

    @abc.abstractmethod
    def get_questionnaire_list_k_by_id(
        self, questionnaire_list_k_id: LM.QuestionnaireListK
    ) -> LM.QuestionnaireListK:
        raise NotImplementedError

    @abc.abstractmethod
    def get_questionnaire_ils_by_id(self, questionnaire_ils_id) -> LM.QuestionnaireIls:
        raise NotImplementedError

    @abc.abstractmethod
    def get_questionnaire_list_k_by_student_id(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_questionnaire_ils_by_student_id(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_settings(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_default_learning_path_by_university(
        self, university: str
    ) -> list[TM.DefaultLearningPathElement]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_by_id(self, user_id) -> UA.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_by_student_id(self, student_id) -> UA.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def get_students_by_uni(self, university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_course(self, student_id, course_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_learning_element(
        self, student_id, learning_element_id
    ) -> DM.StudentLearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_lpath_le_algorithm(
        self, student_id, topic_id
    ) -> DM.StudentLearningPathLearningElementAlgorithm:
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_topic(self, student_id, topic_id) -> DM.StudentTopic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_topic_visit(self, student_id, topic_id) -> DM.StudentTopicVisit:
        raise NotImplementedError

    @abc.abstractmethod
    def get_sub_topics_for_topic_id(self, topic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_teacher_by_id(self, user_id) -> UA.Teacher:
        raise NotImplementedError

    @abc.abstractmethod
    def get_teacher_by_teacher_id(self, teacher_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_teacher_by_uni(self, university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_topics_by_uni(self, university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_topic_by_id(self, topic_id) -> DM.Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_topic_learning_element_by_topic(self, topic_id) -> DM.TopicLearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def get_topic_learning_element_by_learning_element(
        self, learning_element_id
    ) -> DM.TopicLearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_id(self, user_id, lms_user_id) -> list[UA.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_lms_id(self, lms_user_id) -> list[UA.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_users_by_uni(self, university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_news(self, language, university, created_at) -> UA.News:
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_ratings_on_topic(
        self, student_id: int, topic_id: int
    ) -> list[LM.StudentRating]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_ratings(self) -> list[LM.StudentRating]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_element_ratings_on_topic(
        self, learning_element_id: int, topic_id: int
    ) -> list[DM.LearningElementRating]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_element_ratings(self) -> list[DM.LearningElementRating]:
        raise NotImplementedError

    @abc.abstractmethod
    def update_course(self, course_id, course) -> DM.Course:
        raise NotImplementedError

    @abc.abstractmethod
    def update_knowledge(self, characteristic_id, knowledge) -> LM.Knowledge:
        raise NotImplementedError

    @abc.abstractmethod
    def update_learning_analytics(
        self, characteristic_id, learning_analytics
    ) -> LM.LearningAnalytics:
        raise NotImplementedError

    @abc.abstractmethod
    def update_learning_element(
        self, learning_element_id, learning_element
    ) -> DM.LearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def update_learning_strategy(
        self, characteristic_id, learning_strategy
    ) -> LM.LearningStrategy:
        raise NotImplementedError

    @abc.abstractmethod
    def update_learning_style(
        self, characteristic_id, learning_style
    ) -> LM.LearningStyle:
        raise NotImplementedError

    @abc.abstractmethod
    def update_previous_learning_element_visit(self, student_id, visit_time):
        raise NotImplementedError

    @abc.abstractmethod
    def update_previous_topic_visit(self, student_id, visit_time):
        raise NotImplementedError

    @abc.abstractmethod
    def update_settings(self, user_id, settings) -> UA.Settings:
        raise NotImplementedError

    @abc.abstractmethod
    def update_student_learning_element(
        self, student_id, learning_element_id, visit_time
    ):
        raise NotImplementedError

    @abc.abstractmethod
    def update_topic(self, topic_id, topic) -> DM.Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def update_user(self, user_id, lms_user_id, user: UA.User) -> UA.User:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):  # pragma: no cover
    def __init__(self, session: Session):
        self.session = session

    def add_course_creator_to_course(
        self, course_creator_course
    ) -> DM.CourseCreatorCourse:
        try:
            self.session.add(course_creator_course)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_student_to_course(self, student_course) -> DM.StudentCourse:
        course_exist = self.get_courses_by_student_id(student_course.student_id)
        for c in course_exist:
            if c.course_id == student_course.course_id:
                raise err.AlreadyExisting()
        try:
            self.session.add(student_course)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_student_to_learning_element(self, student_learning_element):
        try:
            self.session.add(student_learning_element)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_student_to_topic(self, student_topic):
        try:
            self.session.add(student_topic)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_student_learning_element_visit(self, student_learning_element_visit):
        try:
            self.session.add(student_learning_element_visit)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_student_topic_visit(self, student_topic_visit):
        try:
            self.session.add(student_topic_visit)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_teacher_to_course(self, teacher_course) -> DM.TeacherCourse:
        course_exist = self.get_courses_for_teacher(teacher_course.teacher_id)
        for c in course_exist:
            if c.course_id == teacher_course.course_id:
                raise err.AlreadyExisting()
        try:
            self.session.add(teacher_course)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_admin(self, admin: UA.Admin) -> UA.Admin:
        try:
            self.session.add(admin)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_course(self, course: DM.Course) -> DM.Course:
        course_exist = self.get_courses_by_uni(course.university)
        for c in course_exist:
            if c.lms_id == course.lms_id:
                raise err.AlreadyExisting()
        try:
            self.session.add(course)
        except Exception:
            raise err.CreationError()

    def create_course_creator(
        self, course_creator: UA.CourseCreator
    ) -> UA.CourseCreator:
        try:
            self.session.add(course_creator)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_course_topic(self, course_topic: DM.CourseTopic) -> DM.CourseTopic:
        try:
            self.session.add(course_topic)
        except Exception:
            raise err.CreationError()

    def create_default_learning_path_element(
        self, default_learning_path_element: TM.DefaultLearningPathElement
    ) -> None:
        try:
            self.session.add(default_learning_path_element)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_ils_input_answers(
        self, ils_input_answers: LM.IlsInputAnswers
    ) -> LM.IlsInputAnswers:
        try:
            self.session.add(ils_input_answers)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_ils_perception_answers(
        self, ils_perception_answers: LM.IlsPerceptionAnswers
    ) -> LM.IlsPerceptionAnswers:
        try:
            self.session.add(ils_perception_answers)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_ils_processing_answers(
        self, ils_processing_answers: LM.IlsProcessingAnswers
    ) -> LM.IlsProcessingAnswers:
        try:
            self.session.add(ils_processing_answers)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_ils_understanding_answers(
        self, ils_understanding_answers: LM.IlsUnderstandingAnswers
    ) -> LM.IlsUnderstandingAnswers:
        try:
            self.session.add(ils_understanding_answers)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_knowledge(self, knowledge) -> LM.Knowledge:
        try:
            self.session.add(knowledge)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_analytics(self, learning_analytics) -> LM.LearningAnalytics:
        try:
            self.session.add(learning_analytics)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_characteristics(
        self, learning_characteristic
    ) -> LM.LearningCharacteristic:
        try:
            self.session.add(learning_characteristic)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_element(self, learning_element) -> DM.LearningElement:
        learning_element_exist = self.get_learning_elements_by_uni(
            learning_element.university
        )
        for le in learning_element_exist:
            if learning_element.lms_id == le.lms_id:
                raise err.AlreadyExisting()
        try:
            self.session.add(learning_element)
        except Exception:
            raise err.CreationError()

    def create_learning_path(self, learning_path) -> TM.LearningPath:
        try:
            self.session.add(learning_path)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_path_learning_element(
        self, learning_path_learning_element
    ) -> TM.LearningPathLearningElement:
        try:
            self.session.add(learning_path_learning_element)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_path_algorithm(
        self, learning_path_algorithm: TM.LearningPathAlgorithm
    ) -> None:
        try:
            self.session.add(learning_path_algorithm)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_strategy(self, learning_strategy) -> LM.LearningStrategy:
        try:
            self.session.add(learning_strategy)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_style(self, learning_style) -> LM.LearningStyle:
        try:
            self.session.add(learning_style)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_questionnaire_list_k(
        self, questionnaire_list_k
    ) -> LM.QuestionnaireListK:
        try:
            self.session.add(questionnaire_list_k)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_questionnaire_ils(self, questionnaire_ils) -> LM.QuestionnaireIls:
        try:
            self.session.add(questionnaire_ils)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_settings(self, settings) -> UA.Settings:
        try:
            self.session.add(settings)
        except Exception:
            raise err.CreationError()

    def create_contact_form(self, contact_form: UA.ContactForm) -> UA.ContactForm:
        try:
            self.session.add(contact_form)
        except Exception:
            raise err.CreationError()

    def create_news(self, news: UA.News) -> UA.News:
        try:
            self.session.add(news)
        except Exception:
            raise err.CreationError()

    def create_student(self, student: UA.Student) -> UA.Student:
        try:
            self.session.add(student)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_student_lpath_le_algorithm(
        self,
        student_lpath_le_algorithm: DM.StudentLearningPathLearningElementAlgorithm,
    ) -> None:
        try:
            self.session.add(student_lpath_le_algorithm)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_teacher(self, teacher: UA.Teacher) -> UA.Teacher:
        try:
            self.session.add(teacher)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_topic(self, topic: DM.Topic) -> DM.Topic:
        topic_exist = self.get_topics_by_uni(topic.university)
        for t in topic_exist:
            if topic.lms_id == t.lms_id:
                raise err.AlreadyExisting()
        try:
            self.session.add(topic)
        except Exception:
            raise err.CreationError()

    def create_topic_learning_element(
        self, topic_learning_element: DM.TopicLearningElement
    ) -> DM.TopicLearningElement:
        try:
            self.session.add(topic_learning_element)
        except Exception:
            raise err.CreationError()

    def create_user(self, user: UA.User) -> UA.User:
        user_exist = self.get_users_by_uni(user.university)
        for u in user_exist:
            if user.lms_user_id == u.lms_user_id:
                raise err.AlreadyExisting()
        try:
            self.session.add(user)
        except Exception:
            raise err.CreationError()

    def create_learning_element_rating(
        self, learning_element_rating: DM.LearningElementRating
    ):
        try:
            self.session.add(learning_element_rating)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_student_rating(self, student_rating: LM.StudentRating):
        try:
            self.session.add(student_rating)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def delete_admin(self, user_id):
        admin = self.get_admin_by_id(user_id)
        if admin != []:
            self.session.query(UA.Admin).filter_by(user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_contact_form(self, user_id):
        self.session.query(UA.ContactForm).filter_by(user_id=user_id).delete()

    def delete_news(self):
        self.session.query(UA.News).delete()

    def delete_course(self, course_id):
        course = self.get_course_by_id(course_id)
        if course != []:
            self.session.query(DM.Course).filter_by(id=course_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_course_creator(self, user_id):
        course_creator = self.get_course_creator_by_id(user_id)
        if course_creator != []:
            self.session.query(UA.CourseCreator).filter_by(user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_course_creator_course(self, course_id):
        self.session.query(DM.CourseCreatorCourse).filter_by(
            course_id=course_id
        ).delete()

    def delete_course_topic_by_course(self, course_id):
        course_topic = self.get_course_topic_by_course(course_id)
        if course_topic != []:
            self.session.query(DM.CourseTopic).filter_by(course_id=course_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_course_topic_by_topic(self, topic_id):
        course_topic = self.get_course_topic_by_topic(topic_id)
        if course_topic != []:
            self.session.query(DM.CourseTopic).filter_by(id=course_topic[0].id).delete()
        else:
            raise err.NoValidIdError()

    def delete_ils_input_answers(self, questionnaire_ils_id):
        ils_input_answers = self.get_ils_input_answers_by_id(questionnaire_ils_id)
        if ils_input_answers != []:
            self.session.query(LM.IlsInputAnswers).filter_by(
                questionnaire_ils_id=questionnaire_ils_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_ils_perception_answers(self, questionnaire_ils_id):
        ils_perception_answers = self.get_ils_perception_answers_by_id(
            questionnaire_ils_id
        )
        if ils_perception_answers != []:
            self.session.query(LM.IlsPerceptionAnswers).filter_by(
                questionnaire_ils_id=questionnaire_ils_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_ils_processing_answers(self, questionnaire_ils_id):
        ils_processing_answers = self.get_ils_processing_answers_by_id(
            questionnaire_ils_id
        )
        if ils_processing_answers != []:
            self.session.query(LM.IlsProcessingAnswers).filter_by(
                questionnaire_ils_id=questionnaire_ils_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_ils_understanding_answers(self, questionnaire_ils_id):
        ils_understanding_answers = self.get_ils_understanding_answers_by_id(
            questionnaire_ils_id
        )
        if ils_understanding_answers != []:
            self.session.query(LM.IlsUnderstandingAnswers).filter_by(
                questionnaire_ils_id=questionnaire_ils_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_knowledge(self, characteristic_id):
        knowledge = self.get_knowledge(characteristic_id)
        if knowledge != []:
            self.session.query(LM.Knowledge).filter_by(
                characteristic_id=characteristic_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_analytics(self, characteristic_id):
        analytics = self.get_learning_analytics(characteristic_id)
        if analytics != []:
            self.session.query(LM.LearningAnalytics).filter_by(
                characteristic_id=characteristic_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_characteristics(self, student_id):
        characteristics = self.get_learning_characteristics(student_id)
        if characteristics != []:
            self.session.query(LM.LearningCharacteristic).filter_by(
                student_id=student_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_element(self, learning_element_id):
        learning_element = self.get_learning_element_by_id(learning_element_id)
        if learning_element != []:
            self.session.query(DM.LearningElement).filter_by(
                id=learning_element_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_path(self, learning_path_id):
        self.session.query(TM.LearningPath).filter_by(id=learning_path_id).delete()

    def delete_learning_path_learning_element(self, learning_path_id):
        self.session.query(TM.LearningPathLearningElement).filter_by(
            learning_path_id=learning_path_id
        ).delete()

    def delete_learning_path_topic(self, learning_path_id):
        self.session.query(TM.LearningPathTopic).filter_by(
            learning_path_id=learning_path_id
        ).delete()

    def delete_learning_strategy(self, characteristic_id):
        strategy = self.get_learning_strategy(characteristic_id)
        if strategy != []:
            self.session.query(LM.LearningStrategy).filter_by(
                characteristic_id=characteristic_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_style(self, characteristic_id):
        style = self.get_learning_style(characteristic_id)
        if style != []:
            self.session.query(LM.LearningStyle).filter_by(
                characteristic_id=characteristic_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_questionnaire_list_k(self, questionnaire_list_k_id):
        questionnaire_list_k = self.get_questionnaire_list_k_by_id(
            questionnaire_list_k_id
        )
        if questionnaire_list_k != []:
            self.session.query(LM.QuestionnaireListK).filter_by(
                id=questionnaire_list_k_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_questionnaire_ils(self, questionnaire_ils_id):
        questionnaire_ils = self.get_questionnaire_ils_by_id(questionnaire_ils_id)
        if questionnaire_ils != []:
            self.session.query(LM.QuestionnaireIls).filter_by(
                id=questionnaire_ils_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_settings(self, user_id):
        settings = self.get_settings(user_id)
        if settings != []:
            self.session.query(UA.Settings).filter_by(user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_student(self, user_id):
        student = self.get_student_by_id(user_id)
        if student != []:
            self.session.query(UA.Student).filter_by(user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_student_course(self, student_id):
        self.session.query(DM.StudentCourse).filter_by(student_id=student_id).delete()

    def delete_student_learning_element(self, student_id):
        self.session.query(DM.StudentLearningElement).filter_by(
            student_id=student_id
        ).delete()

    def delete_student_learning_element_visit(self, student_id):
        self.session.query(DM.StudentLearningElementVisit).filter_by(
            student_id=student_id
        ).delete()

    def delete_student_topic(self, student_id):
        self.session.query(DM.StudentTopic).filter_by(student_id=student_id).delete()

    def delete_student_topic_visit(self, student_id):
        self.session.query(DM.StudentTopicVisit).filter_by(
            student_id=student_id
        ).delete()

    def delete_teacher(self, user_id):
        teacher = self.get_teacher_by_id(user_id)
        if teacher != []:
            self.session.query(UA.Teacher).filter_by(user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_teacher_course(self, teacher_id):
        self.session.query(DM.TeacherCourse).filter_by(teacher_id=teacher_id).delete()

    def delete_topic(self, topic_id):
        topic = self.get_topic_by_id(topic_id)
        if topic != []:
            self.session.query(DM.Topic).filter_by(id=topic_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_topic_learning_element_by_topic(self, topic_id):
        topic_learning_element = self.get_topic_learning_element_by_topic(topic_id)
        if topic_learning_element != []:
            self.session.query(DM.TopicLearningElement).filter_by(
                topic_id=topic_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_topic_learning_element_by_learning_element(self, learning_elememt_id):
        topic_learning_element = self.get_topic_learning_element_by_learning_element(
            learning_elememt_id
        )
        if topic_learning_element != []:
            self.session.query(DM.TopicLearningElement).filter_by(
                id=topic_learning_element[0].id
            ).delete()
        else:
            raise err.NoValidIdError()

    def delete_user(self, user_id, lms_user_id):
        teacher = self.get_user_by_id(user_id, lms_user_id)
        if teacher != []:
            self.session.query(UA.User).filter_by(id=user_id).filter_by(
                lms_user_id=lms_user_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def get_admin_by_id(
        self,
        user_id,
    ) -> UA.Admin:
        result = self.session.query(UA.Admin).filter_by(user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_admins_by_uni(self, university):
        try:
            return self.session.query(UA.Admin).filter_by(university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_courses_by_uni(self, university):
        try:
            return self.session.query(DM.Course).filter_by(university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_course_by_id(self, course_id) -> DM.Course:
        result = self.session.query(DM.Course).filter_by(id=course_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_courses_by_student_id(self, student_id):
        try:
            return (
                self.session.query(DM.StudentCourse)
                .filter_by(student_id=student_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_course_creator_by_id(self, user_id) -> UA.CourseCreator:
        result = self.session.query(UA.CourseCreator).filter_by(user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_courses_for_teacher(self, teacher_id):
        try:
            return (
                self.session.query(DM.TeacherCourse)
                .filter_by(teacher_id=teacher_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_course_topic_by_course(self, course_id) -> DM.CourseTopic:
        result = self.session.query(DM.CourseTopic).filter_by(course_id=course_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_course_topic_by_topic(self, topic_id) -> DM.CourseTopic:
        result = self.session.query(DM.CourseTopic).filter_by(topic_id=topic_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_knowledge(self, characteristic_id) -> LM.Knowledge:
        result = (
            self.session.query(LM.Knowledge)
            .filter_by(characteristic_id=characteristic_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_analytics(self, characteristic_id) -> LM.LearningAnalytics:
        result = (
            self.session.query(LM.LearningAnalytics)
            .filter_by(characteristic_id=characteristic_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_characteristics(self, student_id) -> LM.LearningCharacteristic:
        result = (
            self.session.query(LM.LearningCharacteristic)
            .filter_by(student_id=student_id)
            .all()
        )
        return result

    def get_learning_element_by_id(self, learning_element_id) -> DM.LearningElement:
        result = (
            self.session.query(DM.LearningElement)
            .filter_by(id=learning_element_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_elements_by_uni(self, university):
        try:
            return (
                self.session.query(DM.LearningElement)
                .filter_by(university=university)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_learning_element_recommendation(self, learning_path_id):
        result = (
            self.session.query(TM.LearningPathLearningElement)
            .filter_by(learning_path_id=learning_path_id)
            .filter_by(recommended=True)
            .all()
        )
        return result

    def get_learning_path(self, student_id, course_id, topic_id) -> TM.LearningPath:
        result = (
            self.session.query(TM.LearningPath)
            .filter_by(student_id=student_id)
            .filter_by(course_id=course_id)
            .filter_by(topic_id=topic_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_paths(self, student_id):
        result = (
            self.session.query(TM.LearningPath).filter_by(student_id=student_id).all()
        )
        return result

    def get_learning_path_algorithm_by_id(self, id: int) -> TM.LearningPathAlgorithm:
        try:
            return self.session.query(TM.LearningPathAlgorithm).filter_by(id=id).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_learning_path_algorithm_by_short_name(
        self, short_name: str
    ) -> TM.LearningPathAlgorithm:
        try:
            return (
                self.session.query(TM.LearningPathAlgorithm)
                .filter_by(short_name=short_name)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_learning_path_learning_element(
        self, learning_path_id
    ) -> TM.LearningPathLearningElement:
        result = (
            self.session.query(TM.LearningPathLearningElement)
            .filter_by(learning_path_id=learning_path_id)
            .all()
        )
        return result

    def get_learning_strategy(self, characteristic_id) -> LM.LearningStrategy:
        result = (
            self.session.query(LM.LearningStrategy)
            .filter_by(characteristic_id=characteristic_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_style(self, characteristic_id) -> LM.LearningStyle:
        result = (
            self.session.query(LM.LearningStyle)
            .filter_by(characteristic_id=characteristic_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_course_creators_by_uni(self, university):
        try:
            return (
                self.session.query(UA.CourseCreator)
                .filter_by(university=university)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_ils_input_answers_by_id(self, questionnaire_ils_id) -> LM.IlsInputAnswers:
        result = (
            self.session.query(LM.IlsInputAnswers)
            .filter_by(questionnaire_ils_id=questionnaire_ils_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_ils_perception_answers_by_id(
        self, questionnaire_ils_id
    ) -> LM.IlsPerceptionAnswers:
        result = (
            self.session.query(LM.IlsPerceptionAnswers)
            .filter_by(questionnaire_ils_id=questionnaire_ils_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_ils_processing_answers_by_id(
        self, questionnaire_ils_id
    ) -> LM.IlsProcessingAnswers:
        result = (
            self.session.query(LM.IlsProcessingAnswers)
            .filter_by(questionnaire_ils_id=questionnaire_ils_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_ils_understanding_answers_by_id(
        self, questionnaire_ils_id
    ) -> LM.IlsUnderstandingAnswers:
        result = (
            self.session.query(LM.IlsUnderstandingAnswers)
            .filter_by(questionnaire_ils_id=questionnaire_ils_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_questionnaire_list_k_by_id(
        self, questionnaire_list_k
    ) -> LM.QuestionnaireListK:
        result = (
            self.session.query(LM.QuestionnaireListK)
            .filter_by(id=questionnaire_list_k)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_questionnaire_ils_by_id(self, questionnaire_ils) -> LM.QuestionnaireIls:
        result = (
            self.session.query(LM.QuestionnaireIls)
            .filter_by(id=questionnaire_ils)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_questionnaire_list_k_by_student_id(
        self, student_id
    ) -> LM.QuestionnaireListK:
        result = (
            self.session.query(LM.QuestionnaireListK)
            .filter_by(student_id=student_id)
            .all()
        )
        return result

    def get_questionnaire_ils_by_student_id(self, student_id) -> LM.QuestionnaireIls:
        result = (
            self.session.query(LM.QuestionnaireIls)
            .filter_by(student_id=student_id)
            .all()
        )
        return result

    def get_settings(self, user_id) -> UA.Settings:
        result = self.session.query(UA.Settings).filter_by(user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_default_learning_path_by_university(
        self, university: str
    ) -> list[TM.DefaultLearningPathElement]:
        try:
            return (
                self.session.query(TM.DefaultLearningPathElement)
                .filter_by(university=university)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_student_by_id(self, user_id) -> UA.Student:
        result = self.session.query(UA.Student).filter_by(user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_student_by_student_id(self, student_id) -> UA.Student:
        result = self.session.query(UA.Student).filter_by(id=student_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_students_by_uni(self, university):
        try:
            return self.session.query(UA.Student).filter_by(university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_student_learning_element(
        self, student_id, learning_element_id
    ) -> DM.StudentLearningElement:
        try:
            return (
                self.session.query(DM.StudentLearningElement)
                .filter_by(student_id=student_id)
                .filter_by(learning_element_id=learning_element_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_student_lpath_le_algorithm(
        self, student_id, topic_id
    ) -> DM.StudentLearningPathLearningElementAlgorithm:
        try:
            return (
                self.session.query(DM.StudentLearningPathLearningElementAlgorithm)
                .filter_by(student_id=student_id)
                .filter_by(topic_id=topic_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_student_course(self, student_id, course_id):
        try:
            return (
                self.session.query(DM.StudentCourse)
                .filter_by(student_id=student_id)
                .filter_by(course_id=course_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_student_topic(self, student_id, topic_id) -> DM.StudentTopic:
        try:
            return (
                self.session.query(DM.StudentTopic)
                .filter_by(student_id=student_id)
                .filter_by(topic_id=topic_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_student_topic_visit(self, student_id, topic_id) -> DM.StudentTopicVisit:
        try:
            return (
                self.session.query(DM.StudentTopicVisit)
                .filter_by(student_id=student_id)
                .filter_by(topic_id=topic_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_sub_topics_for_topic_id(self, topic_id):
        try:
            return self.session.query(DM.Topic).filter_by(parent_id=topic_id).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_teacher_by_id(self, user_id) -> UA.Teacher:
        result = self.session.query(UA.Teacher).filter_by(user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_teacher_by_teacher_id(self, teacher_id) -> UA.Teacher:
        result = self.session.query(UA.Teacher).filter_by(id=teacher_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_teacher_by_uni(self, university):
        try:
            return self.session.query(UA.Teacher).filter_by(university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_topics_by_uni(self, university):
        try:
            return self.session.query(DM.Topic).filter_by(university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_topic_by_id(self, topic_id) -> DM.Topic:
        result = self.session.query(DM.Topic).filter_by(id=topic_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_topic_learning_element_by_topic(self, topic_id) -> DM.TopicLearningElement:
        result = (
            self.session.query(DM.TopicLearningElement)
            .filter_by(topic_id=topic_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_topic_learning_element_by_learning_element(
        self, learning_element_id
    ) -> DM.TopicLearningElement:
        result = (
            self.session.query(DM.TopicLearningElement)
            .filter_by(learning_element_id=learning_element_id)
            .all()
        )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_user_by_id(self, user_id, lms_user_id=None):
        if lms_user_id is None:
            result = self.session.query(UA.User).filter_by(id=user_id).all()
        else:
            result = (
                self.session.query(UA.User)
                .filter_by(id=user_id)
                .filter_by(lms_user_id=lms_user_id)
                .all()
            )
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_user_by_lms_id(self, lms_user_id):
        result = self.session.query(UA.User).filter_by(lms_user_id=lms_user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_users_by_uni(self, university):
        try:
            return self.session.query(UA.User).filter_by(university=university).all()
        except Exception as e:
            raise err.DatabaseQueryError(exception=e)

    def get_news(self, language, university, created_at) -> UA.News:
        try:
            result = (
                self.session.query(UA.News)
                .filter_by(language_id=language, university=university)
                .filter(UA.News.expiration_date >= created_at)
                .all()
            )
            return result
        except Exception:
            raise err.CreationError()

    def get_student_ratings_on_topic(
        self, student_id: int, topic_id: int
    ) -> list[LM.StudentRating]:
        try:
            return (
                self.session.query(LM.StudentRating)
                .filter_by(student_id=student_id)
                .filter_by(topic_id=topic_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_student_ratings(self) -> list[LM.StudentRating]:
        try:
            return self.session.query(LM.StudentRating).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_learning_element_ratings_on_topic(
        self, learning_element_id: int, topic_id: int
    ) -> list[DM.LearningElementRating]:
        try:
            return (
                self.session.query(DM.LearningElementRating)
                .filter_by(learning_element_id=learning_element_id)
                .filter_by(topic_id=topic_id)
                .all()
            )
        except Exception:
            raise err.DatabaseQueryError()

    def get_learning_element_ratings(self) -> list[DM.LearningElementRating]:
        try:
            return self.session.query(DM.LearningElementRating).all()
        except Exception:
            raise err.DatabaseQueryError()

    def update_course(self, course_id, course) -> DM.Course:
        course_exist = self.get_course_by_id(course_id)
        if course_exist != []:
            course.id = course_exist[0].id
            return (
                self.session.query(DM.Course)
                .filter_by(id=course_id)
                .update(
                    {
                        DM.Course.lms_id: course.lms_id,
                        DM.Course.name: course.name,
                        DM.Course.university: course.university,
                    }
                )
            )
        else:
            raise err.NoValidIdError

    def update_knowledge(self, characteristic_id, knowledge) -> LM.Knowledge:
        knowledge_exist = self.get_knowledge(characteristic_id)
        if knowledge_exist != []:
            knowledge.id = knowledge_exist[0].id
            return self.session.query(LM.Knowledge).filter_by(
                characteristic_id=characteristic_id
            )
        else:
            raise err.NoValidIdError

    def update_learning_analytics(
        self, characteristic_id, learning_analytics
    ) -> LM.Knowledge:
        analytics_exist = self.get_learning_analytics(characteristic_id)
        if analytics_exist != []:
            learning_analytics.id = analytics_exist[0].id
            return self.session.query(LM.LearningAnalytics).filter_by(
                characteristic_id=characteristic_id
            )
        else:
            raise err.NoValidIdError

    def update_learning_element(
        self, learning_element_id, learning_element
    ) -> DM.LearningElement:
        learning_element_exist = self.get_learning_element_by_id(learning_element_id)
        if learning_element_exist != []:
            learning_element.id = learning_element_exist[0].id
            updated_learning_element = {
                DM.LearningElement.lms_id: learning_element.lms_id,
                DM.LearningElement.activity_type: learning_element.activity_type,
                DM.LearningElement.classification: learning_element.classification,
                DM.LearningElement.name: learning_element.name,
                DM.LearningElement.created_by: learning_element.created_by,
                DM.LearningElement.created_at: learning_element.created_at,
                DM.LearningElement.last_updated: learning_element.last_updated,
                DM.LearningElement.university: learning_element.university,
            }

            return (
                self.session.query(DM.LearningElement)
                .filter_by(id=learning_element_id)
                .update(updated_learning_element)
            )
        else:
            raise err.NoValidIdError

    def update_learning_strategy(
        self, characteristic_id, learning_strategy
    ) -> LM.Knowledge:
        strategy_exist = self.get_learning_strategy(characteristic_id)
        if strategy_exist != []:
            learning_strategy.id = strategy_exist[0].id
            return (
                # ignore E501 line too long flake8 error since there is
                # no way to make this shorter without making it unreadable
                self.session.query(LM.LearningStrategy)
                .filter_by(characteristic_id=characteristic_id)
                .update(
                    {
                        LM.LearningStrategy.characteristic_id: learning_strategy.characteristic_id,  # noqa
                        LM.LearningStrategy.cogn_str: learning_strategy.cogn_str,  # noqa
                        LM.LearningStrategy.org: learning_strategy.org,  # noqa
                        LM.LearningStrategy.elab: learning_strategy.elab,  # noqa
                        LM.LearningStrategy.crit_rev: learning_strategy.crit_rev,  # noqa
                        LM.LearningStrategy.rep: learning_strategy.rep,  # noqa
                        LM.LearningStrategy.metacogn_str: learning_strategy.metacogn_str,  # noqa
                        LM.LearningStrategy.goal_plan: learning_strategy.goal_plan,  # noqa
                        LM.LearningStrategy.con: learning_strategy.con,  # noqa
                        LM.LearningStrategy.reg: learning_strategy.reg,  # noqa
                        LM.LearningStrategy.int_res_mng_str: learning_strategy.int_res_mng_str,  # noqa
                        LM.LearningStrategy.att: learning_strategy.att,  # noqa
                        LM.LearningStrategy.eff: learning_strategy.eff,  # noqa
                        LM.LearningStrategy.time: learning_strategy.time,  # noqa
                        LM.LearningStrategy.ext_res_mng_str: learning_strategy.ext_res_mng_str,  # noqa
                        LM.LearningStrategy.lrn_w_cls: learning_strategy.lrn_w_cls,  # noqa
                        LM.LearningStrategy.lit_res: learning_strategy.lit_res,  # noqa
                        LM.LearningStrategy.lrn_env: learning_strategy.lrn_env,  # noqa
                    }
                )
            )
        else:
            raise err.NoValidIdError

    def update_learning_style(self, characteristic_id, learning_style) -> LM.Knowledge:
        style_exist = self.get_learning_analytics(characteristic_id)
        if style_exist != []:
            learning_style.id = style_exist[0].id
            # ignore E501 line too long flake8 error since there is
            # no way to make this shorter without making it unreadable
            updated_learning_style = {
                LM.LearningStyle.characteristic_id: learning_style.characteristic_id,  # noqa
                LM.LearningStyle.perception_dimension: learning_style.perception_dimension,  # noqa
                LM.LearningStyle.perception_value: learning_style.perception_value,  # noqa
                LM.LearningStyle.input_dimension: learning_style.input_dimension,  # noqa
                LM.LearningStyle.input_value: learning_style.input_value,  # noqa
                LM.LearningStyle.processing_dimension: learning_style.processing_dimension,  # noqa
                LM.LearningStyle.processing_value: learning_style.processing_value,  # noqa
                LM.LearningStyle.understanding_dimension: learning_style.understanding_dimension,  # noqa
                LM.LearningStyle.understanding_value: learning_style.understanding_value,  # noqa
            }

            return (
                self.session.query(LM.LearningStyle)
                .filter_by(characteristic_id=characteristic_id)
                .update(updated_learning_style)
            )
        else:
            raise err.NoValidIdError

    def update_previous_learning_element_visit(self, student_id, visit_time):
        try:
            self.session.query(DM.StudentLearningElementVisit).filter_by(
                student_id=student_id
            ).filter_by(visit_end=None).update(
                {DM.StudentLearningElementVisit.visit_end: visit_time}
            )
        except Exception:
            raise err.NoValidIdError

    def update_previous_topic_visit(self, student_id, visit_time):
        try:
            self.session.query(DM.StudentTopicVisit).filter_by(
                student_id=student_id
            ).filter_by(visit_end=None).update(
                {DM.StudentTopicVisit.visit_end: visit_time}
            )
        except Exception:
            raise err.NoValidIdError

    def update_settings(self, user_id, settings) -> UA.Settings:
        settings_exist = self.get_settings(user_id)
        if settings_exist != []:
            settings.id = settings_exist[0].id
            return (
                self.session.query(UA.Settings)
                .filter_by(user_id=user_id)
                .update(
                    {
                        UA.Settings.theme: settings.theme,
                        UA.Settings.pswd: settings.pswd,
                    }
                )
            )
        else:
            raise err.NoValidIdError

    def update_student_learning_element(
        self, student_id, learning_element_id, visit_time
    ):
        try:
            self.session.query(DM.StudentLearningElement).filter_by(
                student_id=student_id
            ).filter_by(learning_element_id=learning_element_id).update(
                {
                    DM.StudentLearningElement.done: True,
                    DM.StudentLearningElement.done_at: visit_time,
                }
            )
        except Exception:
            raise err.NoValidIdError

    def update_topic(self, topic_id, topic) -> DM.Topic:
        topic_exist = self.get_topic_by_id(topic_id)
        if topic_exist != []:
            topic.id = topic_exist[0].id
            return (
                self.session.query(DM.Topic)
                .filter_by(id=topic_id)
                .update(
                    {
                        DM.Topic.lms_id: topic.lms_id,
                        DM.Topic.is_topic: topic.is_topic,
                        DM.Topic.parent_id: topic.parent_id,
                        DM.Topic.contains_le: topic.contains_le,
                        DM.Topic.name: topic.name,
                        DM.Topic.university: topic.university,
                        DM.Topic.created_by: topic.created_by,
                        DM.Topic.created_at: topic.created_at,
                        DM.Topic.last_updated: topic.last_updated,
                    }
                )
            )
        else:
            raise err.NoValidIdError

    def update_user(self, user_id, lms_user_id, user) -> UA.User:
        user_exist = self.get_user_by_id(user_id, lms_user_id)
        if user_exist != []:
            user.role = user_exist[0].role
            return (
                self.session.query(UA.User)
                .filter_by(id=user_id)
                .update(
                    {
                        UA.User.name: user.name,
                        UA.User.university: user.university,
                        UA.User.lms_user_id: user.lms_user_id,
                        UA.User.role: user.role,
                    }
                )
            )
        else:
            raise err.NoValidIdError
