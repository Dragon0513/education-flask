from __future__ import annotations
import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repositories import repository
import config


class AbstractUnitOfWork(abc.ABC):
    learning_path: repository.AbstractRepository
    learning_element: repository.AbstractRepository
    module: repository.AbstractRepository
    student: repository.AbstractRepository
    topic: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork: # pragma: no cover
        return self

    def __exit__(self, *args): # pragma: no cover
        self.rollback()

    @abc.abstractmethod
    def commit(self): # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self): # pragma: no cover
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.learning_path = repository.SqlAlchemyRepository(self.session)
        self.learning_element = repository.SqlAlchemyRepository(self.session)
        self.module = repository.SqlAlchemyRepository(self.session)
        self.student = repository.SqlAlchemyRepository(self.session)
        self.topic = repository.SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
