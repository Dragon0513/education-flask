from importlib.metadata import metadata
from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

metadata = MetaData()

learning_path = Table(
    "LearningPath",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
)


def start_mappers():
    pass
