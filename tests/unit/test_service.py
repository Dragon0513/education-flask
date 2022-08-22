import pytest
from repositories import repository
from service_layer import services, unit_of_work


class FakeRepository(repository.AbstractRepository):
    def __init__(self, products):
        self._products = set(products)

    def add(self, product):
        self._products.add(product)

    def get(self, sku):
        return next((p for p in self._products if p.sku == sku), None)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.products = FakeRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_get_learning_path_for_learning_style():
    uow = FakeUnitOfWork()
    learning_path = services.get_learning_path(uow, {
        "AKT": 5, "INT": 9, "VIS": 9, "GLO": 9
    })
    learning_path_expected = {
        'ZF': 99, 'UB': 14, 'SE': 5, 'AN': 5,
        'RQ': 4, 'AB': 0, 'ZL': -5, 'BE': -5, 'FO': -13}
    assert learning_path == learning_path_expected


def test_get_learning_path_for_no_learning_style():
    uow = FakeUnitOfWork()
    learning_path = services.get_learning_path(uow)
    learning_path_expected = {'ZF': 0, 'AN': 0, 'SE': 0, 'UB': 0,
                              'AB': 0, 'BE': 0, 'FO': 0, 'RQ': 0, 'ZL': 0}
    assert learning_path == learning_path_expected
