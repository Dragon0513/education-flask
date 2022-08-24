from os import times
import pytest
from service_layer import unit_of_work
from datetime import datetime
from domain.tutoringModel import learning_path as LP


def insert_learning_path(session, id, student_id, learning_path):
    session.execute(
        "INSERT INTO learning_path (id, student_id, learning_path) \
        VALUES (:id, :student_id, :learning_path)",
        dict(id=id, student_id=student_id, learning_path=learning_path)
    )


def test_uow_can_access_db(session_factory):
    test_name = ["Test path"]
    test_student_id = 123
    timestamp = datetime.timestamp(datetime.now())
    session = session_factory()
    insert_learning_path(session, timestamp, test_student_id, test_name)
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        learning_path = uow.learning_path.get(id=round(timestamp))
        uow.commit()
        path = LP.LearningPath(
            student_id=learning_path[0].student_id,
            learning_path=learning_path[0].learning_path,
            id=learning_path[0].id)
    assert path.student_id == test_student_id
