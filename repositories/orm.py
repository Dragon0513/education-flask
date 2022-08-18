from importlib.metadata import metadata
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

metadata = MetaData(schema="public")


class LearningPath(Base):
    __tablename__ = "LearningPath"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(255), nullable=False)
    schema = 'public'


class ALearningPath(LearningPath):
    pass


def start_mappers():
    pass
