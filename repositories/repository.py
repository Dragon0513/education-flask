import abc
from operator import mod
from domain.tutoringModel import learning_path as LP


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, learning_path: LP.LearningPath):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> LP.LearningPath:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, learning_path):
        self.session.add(learning_path)

    def get(self, id):
        return self.session.query(LP.LearningPath).filter_by(id=id).all()
