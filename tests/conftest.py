import types
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from entrypoints.flask_app import app
from repositories.orm import metadata, start_mappers


@pytest.fixture(autouse=True)
def mock_jwt_management_module(monkeypatch):
    mock_module = types.ModuleType("service_layer.crypto.JWTKeyManagement")

    monkeypatch.setattr('service_layer.crypto.JWTKeyManagement', mock_module)


@pytest.fixture
def in_memory_db():  # pragma: no cover
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session_factory(in_memory_db):  # pragma: no cover
    start_mappers()
    yield sessionmaker(bind=in_memory_db)
    clear_mappers()


@pytest.fixture
def client():  # pragma: no cover
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client
