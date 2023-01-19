import abc
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
import errors as err
from sqlalchemy.exc import IntegrityError


class AbstractRepository(abc.ABC):  # pragma: no cover
    @abc.abstractmethod
    def add_learning_path(self,
                          learning_path: TM.LearningPath):
        raise NotImplementedError

    @abc.abstractmethod
    def add_course(self, course) -> DM.Course:
        raise NotImplementedError

    @abc.abstractmethod
    def add_element(self, element) -> DM.LearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def add_student(self, student) -> LM.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def add_topic(self, topic) -> DM.Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_course(self, course_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_element(self, element_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_student(self, student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_topic(self, topic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_elements(self) -> DM.LearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_element_by_id(self,
                                   element_id) \
            -> DM.LearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def get_courses(self) -> DM.Course:
        raise NotImplementedError

    @abc.abstractmethod
    def get_course_by_id(self, course_id) -> DM.Course:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_path(self,
                          student_id,
                          course_id,
                          order_depth) -> TM.LearningPath:
        raise NotImplementedError

    @abc.abstractmethod
    def get_students(self) -> LM.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_by_id(self, student_id) -> LM.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def get_topics(self) -> DM.Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_topics_for_course(self,
                              course_id,
                              order_depth) -> DM.Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_topics_for_course_and_ancestor(self,
                                           course_id,
                                           order_depth,
                                           ancestor_id)\
            -> DM.Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_topic_by_id(self, topic_id) -> DM.Topic:
        raise NotImplementedError

    @abc.abstractmethod
    def update_course(self, course) -> DM.Course:
        raise NotImplementedError

    @abc.abstractmethod
    def update_learning_element(self,
                                learning_element) \
            -> DM.LearningElement:
        raise NotImplementedError

    @abc.abstractmethod
    def update_student(self, student) -> LM.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def update_topic(self, topic) -> DM.Topic:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):  # pragma: no cover
    def __init__(self, session):
        self.session = session

    def add_learning_path(self, learning_path):
        try:
            return self.session.add(learning_path)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_course(self, course):
        try:
            self.session.add(course)
        except Exception:
            raise err.CreationError()

    def add_element(self, element):
        try:
            self.session.add(element)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def add_student(self, student):
        try:
            self.session.add(student)
        except Exception:
            raise err.CreationError()

    def add_topic(self, topic):
        try:
            self.session.add(topic)
        except Exception:
            raise err.CreationError()

    def delete_course(self, course_id):
        course = self.get_course_by_id(course_id)
        if course != []:
            self.session.query(DM.Course).filter_by(id=course_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_element(self, element_id):
        element = self.get_learning_element_by_id(element_id)
        if element != []:
            self.session.query(DM.LearningElement).filter_by(
                id=element_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        if student != []:
            self.session.query(LM.Student).filter_by(id=student_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_topic(self, topic_id):
        topic = self.get_topic_by_id(topic_id)
        if topic != []:
            self.session.query(DM.Topic).filter_by(id=topic_id).delete()
        else:
            raise err.NoValidIdError()

    def get_learning_elements(self):
        result = self.session.query(DM.LearningElement).all()
        if result == []:
            raise err.NoContentWarning()
        else:
            return result

    def get_learning_element_by_id(self, element_id):
        result = self.session.query(DM.LearningElement)\
            .filter_by(id=element_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_courses(self):
        try:
            return self.session.query(DM.Course).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_course_by_id(self, course_id):
        result = self.session.query(DM.Course).filter_by(id=course_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_path(self, student_id, course_id, order_depth):
        try:
            return self.session.query(TM.LearningPath)\
                .filter_by(student_id=student_id)\
                .filter_by(course_id=course_id)\
                .filter_by(order_depth=order_depth).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_students(self):
        try:
            return self.session.query(LM.Student).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_student_by_id(self, student_id):
        result = self.session.query(LM.Student).filter_by(id=student_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_topics(self):
        try:
            return self.session.query(DM.Topic).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_topics_for_course(self, course_id, order_depth):
        try:
            return self.session.query(DM.Topic)\
                .filter_by(course_id=course_id)\
                .filter_by(order_depth=order_depth).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_topics_for_course_and_ancestor(self,
                                           course_id,
                                           order_depth,
                                           ancestor_id):
        try:
            return self.session.query(DM.Topic)\
                .filter_by(course_id=course_id)\
                .filter_by(order_depth=order_depth)\
                .filter_by(ancestor_id=ancestor_id).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_topic_by_id(self, topic_id):
        result = self.session.query(DM.Topic).filter_by(id=topic_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def update_course(self, course, id):
        course_exist = self.get_course_by_id(id)
        if course_exist != []:
            return self.session.query(DM.Course).filter_by(id=id).update(
                {DM.Course.name: course.name}
            )
        else:
            raise err.NoValidIdError()

    def update_learning_element(self, learning_element, id):
        element_exist = self.get_learning_element_by_id(id)
        if element_exist != []:
            try:
                return self.session.query(DM.LearningElement)\
                    .filter_by(id=id).update(
                    {DM.LearningElement.name:
                     learning_element.name,
                     DM.LearningElement.classification:
                     learning_element.classification,
                     DM.LearningElement.ancestor_id:
                     learning_element.ancestor_id,
                     DM.LearningElement.prerequisite_id:
                     learning_element.prerequisite_id,
                     DM.LearningElement.order_depth:
                     learning_element.order_depth, }
                )
            except IntegrityError:
                raise err.ForeignKeyViolation()
        else:
            raise err.NoValidIdError()

    def update_student(self, student, id):
        student_exist = self.get_student_by_id(id)
        if student_exist != []:
            return self.session.query(LM.Student).filter_by(id=id).update(
                {LM.Student.name: student.name,
                 LM.Student.learning_style: student.learning_style}
            )
        else:
            raise err.NoValidIdError()

    def update_topic(self, topic, id):
        topic_exist = self.get_topic_by_id(id)
        if topic_exist != []:
            return self.session.query(DM.Topic).filter_by(id=id).update(
                {DM.Topic.name: topic.name,
                 DM.Topic.course_id: topic.course_id,
                 DM.Topic.order_depth: topic.order_depth,
                 DM.Topic.ancestor_id: topic.ancestor_id,
                 DM.Topic.prerequisite_id: topic.prerequisite_id})
        else:
            raise err.NoValidIdError()
