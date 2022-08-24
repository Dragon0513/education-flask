from sqlalchemy import MetaData, Column, Integer, String, Table
from sqlalchemy.orm import mapper, relationship
from domain.tutoringModel import learning_path as LP

metadata = MetaData()

learning_path = Table(
    "learning_path",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("learning_path", String(255), nullable=False)
)


def start_mappers():
    mapper(
        LP.LearningPath, learning_path
    )
