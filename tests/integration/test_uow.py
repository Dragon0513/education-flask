import pytest
from service_layer import unit_of_work
from datetime import datetime

"""
def insert_learning_path(session, timestamp):
    session.execute(
        "INSERT INTO test (timestamp) \
        VALUES (:timestamp)",
        dict(timestamp=timestamp)
    )


def test_uow_can_access_db(session_factory):
    timestamp = datetime.timestamp(datetime.now())
    session = session_factory()
    insert_learning_path(session, timestamp)
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        learning_path = uow.learning_path.get(id=round(timestamp))
        uow.commit()
    assert learning_path[0].timestamp == timestamp
"""
