import abc

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def func(self):
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def func(self):
        raise NotImplementedError