import pytest
from service_layer import unit_of_work
from domain.tutoringModel import model
from datetime import datetime


def insert_learning_path(session, id, name):
    session.execute(
        'INSERT INTO public."LearningPath" (id, name) VALUES (:id, :name)',
        dict(id=id, name=name)
    )


def test_uow_can_access_db(session_factory):
    test_name = "Test path"
    timestamp = datetime.timestamp(datetime.now())
    session = session_factory()
    insert_learning_path(session, timestamp, test_name)
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        learning_path = uow.learning_path.get(id=timestamp)
        session.commit()
    assert learning_path.name == test_name
