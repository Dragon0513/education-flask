import os
import shutil
import pytest
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from entrypoints.flask_app import app
from repositories.orm import metadata, start_mappers
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


def pytest_sessionstart(session):
    """
    Generate mock keys/private.pem and public.pem for testing.
    """
    if not os.path.exists("test_keys"):
        print("Generating test_keys directory")
        os.makedirs("test_keys")
    if not os.path.exists("test_keys/private.pem"):
        print("Generating test_keys/private.pem")
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend(),
        )
        with open("test_keys/private.pem", "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
        print("Generating test_keys/public.pem")
        with open("test_keys/public.pem", "wb") as f:
            f.write(
                private_key.public_key().public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
    # set the environment variables for the keys/ path
    os.environ["JWT_KEYS_LOCATION"] = "test_keys"


def pytest_sessionfinish(session, exitstatus):
    """
    Cleanup mock keys/private.pem and public.pem after testing.
    """
    print("Cleaning up test_keys directory")
    if os.path.exists("test_keys"):
        shutil.rmtree("test_keys")
        print("Removed test_keys directory")


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
