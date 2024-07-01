from __future__ import annotations

import abc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from repositories import repository


class AbstractUnitOfWork(abc.ABC):
    admin: repository.AbstractRepository
    course: repository.AbstractRepository
    course_creator: repository.AbstractRepository
    course_creator_course: repository.AbstractRepository
    course_topic: repository.AbstractRepository
    default_learning_path: repository.AbstractRepository
    user: repository.AbstractRepository
    ils_input_answers: repository.AbstractRepository
    ils_perception_answers: repository.AbstractRepository
    ils_processing_answers: repository.AbstractRepository
    ils_understanding_answers: repository.AbstractRepository
    knowledge: repository.AbstractRepository
    learning_analytics: repository.AbstractRepository
    learning_characteristics: repository.AbstractRepository
    learning_element: repository.AbstractRepository
    learning_element_rating: repository.AbstractRepository
    learning_path: repository.AbstractRepository
    learning_path_learning_element: repository.AbstractRepository
    learning_path_topic: repository.AbstractRepository
    learning_strategy: repository.AbstractRepository
    learning_style: repository.AbstractRepository
    questionnaire_ils: repository.AbstractRepository
    questionnaire_list_k: repository.AbstractRepository
    settings: repository.AbstractRepository
    contact_form: repository.AbstractRepository
    student: repository.AbstractRepository
    student_course: repository.AbstractRepository
    student_learning_element: repository.AbstractRepository
    student_learning_element_visit: repository.AbstractRepository
    student_topic: repository.AbstractRepository
    student_topic_visit: repository.AbstractRepository
    teacher: repository.AbstractRepository
    teacher_course: repository.AbstractRepository
    topic: repository.AbstractRepository
    topic_learning_element: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:  # pragma: no cover
        return self

    def __exit__(self, *args):  # pragma: no cover
        self.rollback()

    @abc.abstractmethod
    def commit(self):  # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):  # pragma: no cover
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
        max_overflow=-1,
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):  # pragma: no cover
    def __init__(self, session_factory=None):
        self.session_factory = session_factory or DEFAULT_SESSION_FACTORY

    def __enter__(self):
        self.session = self.session_factory()
        self.admin = repository.SqlAlchemyRepository(self.session)
        self.course = repository.SqlAlchemyRepository(self.session)
        self.course_creator = repository.SqlAlchemyRepository(self.session)
        self.course_creator_course = repository.SqlAlchemyRepository(self.session)
        self.course_topic = repository.SqlAlchemyRepository(self.session)
        self.user = repository.SqlAlchemyRepository(self.session)
        self.ils_input_answers = repository.SqlAlchemyRepository(self.session)
        self.ils_perception_answers = repository.SqlAlchemyRepository(self.session)
        self.ils_processing_answers = repository.SqlAlchemyRepository(self.session)
        self.ils_understanding_answers = repository.SqlAlchemyRepository(self.session)
        self.knowledge = repository.SqlAlchemyRepository(self.session)
        self.learning_analytics = repository.SqlAlchemyRepository(self.session)
        self.learning_characteristics = repository.SqlAlchemyRepository(self.session)
        self.learning_element = repository.SqlAlchemyRepository(self.session)
        self.learning_element_rating = repository.SqlAlchemyRepository(self.session)
        self.learning_path = repository.SqlAlchemyRepository(self.session)
        self.learning_path_learning_element = repository.SqlAlchemyRepository(
            self.session
        )
        self.learning_path_topic = repository.SqlAlchemyRepository(self.session)
        self.learning_strategy = repository.SqlAlchemyRepository(self.session)
        self.learning_style = repository.SqlAlchemyRepository(self.session)
        self.questionnaire_ils = repository.SqlAlchemyRepository(self.session)
        self.questionnaire_list_k = repository.SqlAlchemyRepository(self.session)
        self.settings = repository.SqlAlchemyRepository(self.session)
        self.contact_form = repository.SqlAlchemyRepository(self.session)
        self.default_learning_path = repository.SqlAlchemyRepository(self.session)
        self.student = repository.SqlAlchemyRepository(self.session)
        self.student_course = repository.SqlAlchemyRepository(self.session)
        self.student_learning_element = repository.SqlAlchemyRepository(self.session)
        self.student_learning_element_visit = repository.SqlAlchemyRepository(
            self.session
        )
        self.student_topic = repository.SqlAlchemyRepository(self.session)
        self.student_topic_visit = repository.SqlAlchemyRepository(self.session)
        self.teacher = repository.SqlAlchemyRepository(self.session)
        self.teacher_course = repository.SqlAlchemyRepository(self.session)
        self.topic = repository.SqlAlchemyRepository(self.session)
        self.topic_learning_element = repository.SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
