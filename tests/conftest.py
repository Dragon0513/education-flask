import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker

from entrypoints.flask_app import app
from repositories.orm import mapper_registry, start_mappers

engine = create_engine("sqlite+pysqlite:///:memory:", future=True, echo=True)
mapper_registry.metadata.create_all(engine)


@pytest.fixture(scope="session")
def session_factory():  # pragma: no cover
    clear_mappers()
    start_mappers()
    yield sessionmaker(bind=engine)
    clear_mappers()


@pytest.fixture(scope="session")
def client(session_factory):  # pragma: no cover
    # Mock unit_of_work.SqlAlchemyUnitOfWork
    # DEFAULT_SESSION_FACTORY to use in-memory database
    # instead of the real database
    import service_layer.unit_of_work as unit_of_work

    app.testing = True
    unit_of_work.DEFAULT_SESSION_FACTORY = session_factory
    with app.app_context():
        with app.test_client() as client:
            yield client
