from sqlalchemy import MetaData, Column, Integer, String, Table, Date, Boolean
from sqlalchemy.orm import mapper
from domain.tutoringModel import graf as LP
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.userAdministartion import model as UA

metadata = MetaData()

admin = Table(
    "admin",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False)
)

course = Table(
    "course",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("lms_id", Integer, nullable=False),
    Column("name", String, nullable=False),
    Column("university", String, nullable=False)
)

course_creator = Table(
    "course_creator",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False)
)

course_creator_course = Table(
    "course_creator_course",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("course_creator_id", Integer, nullable=False),
    Column("course_id", Integer, nullable=False),
    Column("created_at", Date, nullable=False),
    Column("last_updated", Date, nullable=True)
)

course_topic = Table(
    "course_topic",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("course_id", Integer, nullable=False),
    Column("topic_id", Integer, nullable=False)
)

haski_user = Table(
    "haski_user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("university", String, nullable=False),
    Column("lms_user_id", Integer, nullable=False)
)

knowledge = Table(
    "knowledge",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("characteristic_id", Integer, nullable=False)
)

learning_analytics = Table(
    "learning_analytics",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("characteristic_id", Integer, nullable=False)
)

learning_charcteristics = Table(
    "learning_characteristics",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False)
)

learning_element = Table(
    "learning_element",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("lms_id", Integer, nullable=False),
    Column("activity_type", String, nullable=False),
    Column("classification", String, nullable=False),
    Column("name", String, nullable=False),
    Column("university", String, nullable=False),
    Column("created_at", Date, nullable=False),
    Column("created_by", String, nullable=False),
    Column("last_updated", Date, nullable=True)
)

learning_element_rating = Table(
    "learning_element_rating",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("learning_element_id", Integer, nullable=False),
    Column("rating", Integer, nullable=False),
    Column("message", String, nullable=True),
    Column("date", Date, nullable=False)
)

learning_path = Table(
    "learning_path",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("course_id", Integer, nullable=False),
    Column("topic_id", Integer, nullable=True)
)

learning_path_learning_element = Table(
    "learning_path_learning_element",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("learning_element_id", Integer, nullable=False),
    Column("learning_path_id", Integer, nullable=False),
    Column("recommended", Boolean, nullable=False),
    Column("position", Integer, nullable=False)
)

learning_path_topic = Table(
    "learning_path_topic",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("topic_id", Integer, nullable=False),
    Column("learning_path_id", Integer, nullable=False),
    Column("recommended", Boolean, nullable=False),
    Column("position", Integer, nullable=False)
)

learning_strategy = Table(
    "learning_strategy",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("characteristic_id", Integer, nullable=False)
)

learning_style = Table(
    "learning_style",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("characteristic_id", Integer, nullable=False),
    Column("perception_dimension", String, nullable=False),
    Column("perception_value", Integer, nullable=False),
    Column("input_dimension", String, nullable=False),
    Column("input_value", Integer, nullable=False),
    Column("processing_dimension", String, nullable=False),
    Column("processing_value", Integer, nullable=False),
    Column("understanding_dimension", String, nullable=False),
    Column("understanding_value", Integer, nullable=False)
)

settings = Table(
    "settings",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
    Column("theme", String, nullable=True),
    Column("pswd", String, nullable=True)
)

student = Table(
    "student",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False)
)

student_course = Table(
    "student_course",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("course_id", Integer, nullable=False),
    Column("perception_dimension", String, nullable=False),
    Column("perception_value", Integer, nullable=False),
    Column("input_dimension", String, nullable=False),
    Column("input_value", Integer, nullable=False),
    Column("processing_dimension", String, nullable=False),
    Column("processing_value", Integer, nullable=False),
    Column("understanding_dimension", String, nullable=False),
    Column("understanding_value", Integer, nullable=False)
)

student_learning_element = Table(
    "student_learning_element",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("learning_element_id", Integer, nullable=False),
    Column("done", Boolean, nullable=False),
    Column("done_at", Date, nullable=True)
)

student_learning_element_visit = Table(
    "student_learning_element_visit",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("learning_element_id", Integer, nullable=False),
    Column("visit_start", Date, nullable=False),
    Column("visit_end", Date, nullable=True)
)

student_topic = Table(
    "student_topic",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("topic_id", Integer, nullable=False),
    Column("done", Boolean, nullable=False),
    Column("done_at", Date, nullable=True)
)

student_topic_visit = Table(
    "student_topic_visit",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("topic_id", Integer, nullable=False),
    Column("visit_start", Date, nullable=False),
    Column("visit_end", Date, nullable=True)
)

teacher = Table(
    "teacher",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False)
)

teacher_course = Table(
    "teacher_course",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("teacher_id", Integer, nullable=False),
    Column("course_id", Integer, nullable=False)
)

topic = Table(
    "topic",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("lms_id", Integer, nullable=False),
    Column("is_topic", Boolean, nullable=False),
    Column("parent_id", Integer, nullable=True),
    Column("contains_le", Boolean, nullable=False),
    Column("name", String, nullable=False),
    Column("university", String, nullable=False),
    Column("created_by", String, nullable=False),
    Column("created_at", Date, nullable=False),
    Column("last_updated", Date, nullable=True)
)

topic_learning_element = Table(
    "topic_learning_element",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("topic_id", Integer, nullable=False),
    Column("learning_element_id", Integer, nullable=False)
)


def start_mappers():
    mapper(
        UA.Admin, admin
    )
    mapper(
        DM.Course, course
    )
    mapper(
        UA.CourseCreator, course_creator
    )
    mapper(
        DM.CourseCreatorCourse, course_creator_course
    )
    mapper(
        DM.CourseTopic, course_topic
    )
    mapper(
        UA.User, haski_user
    )
    mapper(
        LM.Knowledge, knowledge
    )
    mapper(
        LM.LearningAnalytics, learning_analytics
    )
    mapper(
        LM.LearningCharacteristic, learning_charcteristics
    )
    mapper(
        DM.LearningElement, learning_element
    )
    mapper(
        DM.LearningElementRating, learning_element_rating
    )
    mapper(
        TM.LearningPath, learning_path
    )
    mapper(
        TM.LearningPathLearningElement, learning_path_learning_element
    )
    mapper(
        TM.LearningPathTopic, learning_path_topic
    )
    mapper(
        LM.LearningStrategy, learning_strategy
    )
    mapper(
        LM.LearningStyle, learning_style
    )
    mapper(
        UA.Settings, settings
    )
    mapper(
        LM.Student, student
    )
    mapper(
        DM.StudentCourse, student_course
    )
    mapper(
        DM.StudentLearningElement, student_learning_element
    )
    mapper(
        DM.StudentLearningElementVisit, student_learning_element_visit
    )
    mapper(
        DM.StudentTopic, student_topic
    )
    mapper(
        DM.StudentTopicVisit, student_topic_visit
    )
    mapper(
        UA.Teacher, teacher
    )
    mapper(
        DM.TeacherCourse, teacher_course
    )
    mapper(
        DM.Topic, topic
    )
    mapper(
        DM.TopicLearningElement, topic_learning_element
    )
