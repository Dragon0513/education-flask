from select import select
import pytest
from domain.tutoringModel.model import LearningPath
from repositories.orm import ALearningPath
from service_layer import unit_of_work
from datetime import datetime


def insert_learning_path(session, id, name):
    learning_path_added = ALearningPath(id=id, name=name)
    session.add(learning_path_added)
    session.commit()


def test_uow_can_access_db(session_factory):
    test_name = "Test path"
    timestamp = datetime.timestamp(datetime.now())
    session = session_factory()
    insert_learning_path(session, timestamp, test_name)

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        learning_path = uow.learning_path.get(id=timestamp)
        session.commit()
    assert learning_path.name == test_name
