import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker

from repositories.orm import mapper_registry, start_mappers

engine = create_engine("sqlite+pysqlite:///:memory:", future=True, echo=True)
mapper_registry.metadata.create_all(engine)
# here, we set up postgresql in-memory:
# socket_dir = tempfile.TemporaryDirectory(dir=os.environ.get("TEST_TEMP_DIR", "./tmp"))
# postgresql_my_proc = factories.postgresql_proc(
#     port=None,
#     unixsocketdir=socket_dir.name,
# )
# postgresql_my = factories.postgresql("postgresql_my_proc")

# @pytest.fixture
# def in_memory_db():  # pragma: no cover
#     engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
#     mapper_registry.metadata.create_all(engine)
#     return engine


# @pytest.fixture
# def in_memory_db(postgresql_my):  # pragma: no cover
#     def db_creator():
#         return postgresql_my.cursor().connection

#     engine = create_engine("postgresql+psycopg2://", creator=db_creator)
#     mapper_registry.metadata.create_all(bind=engine)
#     return engine


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
    from entrypoints.flask_app import app

    app.testing = True

    # engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    # registry().metadata.create_all(engine)
    unit_of_work.DEFAULT_SESSION_FACTORY = session_factory

    # with patch.multiple(
    #     unit_of_work,
    #     DEFAULT_SESSION_FACTORY=session_factory,
    # ):
    with app.app_context():
        with app.test_client() as client:
            yield client
