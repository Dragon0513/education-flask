import pytest
from repositories import repository
from service_layer import services, unit_of_work


class FakeRepository(repository.AbstractRepository):
    def __init__(self, learning_path):
        self._learning_path = set(learning_path)

    def add(self, product):
        self._learning_path.add(product)

    def get(self, sku):
        return next((p for p in self._learning_path if p.sku == sku), None)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.learning_path = FakeRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_get_learning_path_for_learning_style():
    uow = FakeUnitOfWork()
    learning_path = services.get_learning_path(uow=uow,
                                               student_id=123,
                                               learning_style={
                                                   "AKT": 5,
                                                   "INT": 9,
                                                   "VIS": 9,
                                                   "GLO": 9
                                               })
    learning_path_expected = ['ZF', 'UB', 'SE', 'AN',
                              'RQ', 'AB', 'ZL', 'BE', 'FO']
    assert learning_path == ', '.join(learning_path_expected)


def test_get_learning_path_for_no_learning_style():
    uow = FakeUnitOfWork()
    learning_path = services.get_learning_path(uow=uow, student_id=123)
    learning_path_expected = ['RQ', 'SE', 'FO', 'ZL',
                              'AN', 'UB', 'BE', 'AB', 'ZF']
    assert learning_path == ', '.join(learning_path_expected)
