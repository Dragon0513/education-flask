from distutils.command.config import config
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
import config

from repositories.orm import metadata, start_mappers


@pytest.fixture
def in_memory_db():  # pragma: no cover
    engine = create_engine(config.get_postgres_uri())
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session_factory(in_memory_db):  # pragma: no cover
    start_mappers()
    yield sessionmaker(bind=in_memory_db)
    clear_mappers()
