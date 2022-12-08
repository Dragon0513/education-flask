import abc
from domain.tutoringModel import learning_path as LP
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, learning_path: LP.LearningPath): # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def add_course(self, course) -> DM.Module: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def add_element(self, element) -> DM.LearningElement: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def add_student(self, student) -> LM.Student: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def add_topic(self, topic) -> DM.Topic: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> LP.LearningPath: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_elements(self) -> DM.LearningElement: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_element_by_id(self, element_id) -> DM.LearningElement: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_modules(self) -> DM.Module: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_module_by_id(self, module_id) -> DM.Module: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_students(self) -> LM.Student: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_by_id(self, student_id) -> LM.Student: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_topics(self) -> DM.Topic: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_topics_for_module(self, module_id, order_depth) -> DM.Topic: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_topics_for_module_and_ancestor(self, module_id, order_depth, ancestor_id) -> DM.Topic: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def get_topic_by_id(self, topic_id) -> DM.Topic: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def update_student(self, student) -> LM.Student: # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def update_topic(self, topic) -> DM.Topic: # pragma: no cover
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, learning_path):
        self.session.add(learning_path)

    def add_course(self, course):
        self.session.add(course)

    def add_element(self, element):
        self.session.add(element)

    def add_student(self, student):
        self.session.add(student)

    def add_topic(self, topic):
        self.session.add(topic)

    def get(self, id):
        return self.session.query(LP.LearningPath).filter_by(id=id).all()

    def get_learning_elements(self):
        return self.session.query(DM.LearningElement).all()

    def get_learning_element_by_id(self, element_id):
        return self.session.query(DM.LearningElement).filter_by(id=element_id).all()

    def get_modules(self):
        return self.session.query(DM.Module).all()

    def get_module_by_id(self, module_id):
        return self.session.query(DM.Module).filter_by(id=module_id).all()

    def get_students(self):
        return self.session.query(LM.Student).all()

    def get_student_by_id(self, student_id):
        return self.session.query(LM.Student).filter_by(id=student_id).all()

    def get_topics(self):
        return self.session.query(DM.Topic).all()

    def get_topics_for_module(self, module_id, order_depth):
        return self.session.query(DM.Topic).filter_by(module_id=module_id).filter_by(order_depth=order_depth).all()

    def get_topics_for_module_and_ancestor(self, module_id, order_depth, ancestor_id):
        return self.session.query(DM.Topic).filter_by(module_id=module_id).filter_by(order_depth=order_depth).filter_by(ancestor_id=ancestor_id).all()

    def get_topic_by_id(self, topic_id):
        return self.session.query(DM.Topic).filter_by(id=topic_id).all()

    def update_student(self, student, id):
        return self.session.query(LM.Student).filter_by(id=id).update({LM.Student.name: student.name, LM.Student.learning_style: student.learning_style})

    def update_topic(self, topic, id):
        return self.session.query(DM.Topic).filter_by(id=id).update(
            {DM.Topic.name: topic.name,
             DM.Topic.module_id: topic.module_id,
             DM.Topic.order_depth: topic.order_depth,
             DM.Topic.ancestor_id: topic.ancestor_id,
             DM.Topic.prerequisite_id: topic.prerequisite_id})
