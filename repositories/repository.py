import abc
from domain.tutoringModel import model


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
        """
        ToDo: Need to investigate why .query method is
        not working correctly here.

        Error: FAILED integration/test_uow.py::test_uow_can_access_db
        - sqlalchemy.exc.ArgumentError: Column expression or FROM
        clause expected, got <class 'domain.tutoringModel.model.LearningPath'>.
        """

        # return self.session.query(model.LearningPath).filter_by(id=id).first()

        query = 'SELECT * FROM public."LearningPath" WHERE ID = ' + \
            str(round(id))
        result = self.session.execute(
            query
        )
        return result.mappings().first()
