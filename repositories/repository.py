import abc
from domain.tutoringModel import model
from repositories.orm import LearningPathOrm


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, learning_path: model.LearningPath):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> model.LearningPath:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, learning_path):
        self.session.add(learning_path)

    def get(self, id):
        result = self.session.query(
            LearningPathOrm).filter_by(id=round(id)).first()
        found_learning_path = LearningPathOrm(id=result.id, name=result.name)
        return found_learning_path
