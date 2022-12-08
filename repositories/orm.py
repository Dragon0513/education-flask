from sqlalchemy import MetaData, Column, Integer, String, Table, Date, Boolean, Identity
from sqlalchemy.orm import mapper
from domain.tutoringModel import learning_path as LP
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM

metadata = MetaData()

learning_element = Table(
    "learning_element",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("classification", String, nullable=False),
    Column("ancestor_id", Integer, nullable=True),
    Column("prerequisite_id", String, nullable=True),
    Column("order_depth", Integer, nullable=False)
)

learning_path = Table(
    "learning_path",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("module_id", Integer, nullable=False),
    Column("contains_le", Boolean, nullable=False),
    Column("order_depth", Integer, nullable=False),
    Column("path", String, nullable=False)
)

learning_path_test = Table(
    "learning_path_test",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("learning_path", String(255), nullable=False)
)

module = Table(
    "module",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False)
)

student = Table(
    "student",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("learning_style", String, nullable=True)
)

student_element = Table(
    "student_element",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("element_id", Integer, nullable=False),
    Column("is_recommended", Boolean, nullable=False),
    Column("done", Boolean, nullable=False),
    Column("done_at", Date, nullable=True)
)

student_topic = Table(
    "student_topic",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("topic_id", Integer, nullable=False),
    Column("module_id", Integer, nullable=False),
    Column("student_id", Integer, nullable=False),
    Column("is_recommended", Boolean, nullable=False),
    Column("sequence_nr", Integer, nullable=False),
    Column("done", Boolean, nullable=False),
    Column("done_at", Date, nullable=True)
)

topic = Table(
    "topic",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("module_id", Integer, nullable=False),
    Column("ancestor_id", Integer, nullable=True),
    Column("prerequisite_id", Integer, nullable=True),
    Column("order_depth", Integer, nullable=False)
)


def start_mappers():
    mapper(
        DM.LearningElement, learning_element
    )
    mapper(
        LP.LearningPath, learning_path_test
    )
    mapper(
        TM.LearningPath, learning_path
    )
    mapper(
        DM.Module, module
    )
    mapper(
        LM.Student, student
    )
    mapper(
        DM.Topic, topic
    )
