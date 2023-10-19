from sqlalchemy import Boolean, Column, Date, Float, Integer, String, Table
from sqlalchemy.orm import registry

from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.userAdministartion import model as UA

mapper_registry = registry()

admin = Table(
    "admin",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
)

course = Table(
    "course",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("lms_id", Integer, nullable=False),
    Column("name", String, nullable=False),
    Column("university", String, nullable=False),
)

course_creator = Table(
    "course_creator",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
)

course_creator_course = Table(
    "course_creator_course",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("course_creator_id", Integer, nullable=False),
    Column("course_id", Integer, nullable=False),
    Column("created_at", Date, nullable=False),
    Column("last_updated", Date, nullable=True),
)

course_topic = Table(
    "course_topic",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("course_id", Integer, nullable=False),
    Column("topic_id", Integer, nullable=False),
)

haski_user = Table(
    "haski_user",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("university", String, nullable=False),
    Column("lms_user_id", Integer, nullable=False),
    Column("role", String, nullable=False),
)

ils_input_answers = Table(
    "ils_input_answers",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("questionnaire_ils_id", Integer, nullable=False),
    Column("vv_1_f3", Integer, nullable=True),
    Column("vv_2_f7", Integer, nullable=False),
    Column("vv_3_f11", Integer, nullable=True),
    Column("vv_4_f15", Integer, nullable=True),
    Column("vv_5_f19", Integer, nullable=False),
    Column("vv_6_f23", Integer, nullable=True),
    Column("vv_7_f27", Integer, nullable=False),
    Column("vv_8_f31", Integer, nullable=True),
    Column("vv_9_f35", Integer, nullable=True),
    Column("vv_10_f39", Integer, nullable=False),
    Column("vv_11_f43", Integer, nullable=False),
)

ils_perception_answers = Table(
    "ils_perception_answers",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("questionnaire_ils_id", Integer, nullable=False),
    Column("si_1_f2", Integer, nullable=False),
    Column("si_2_f6", Integer, nullable=True),
    Column("si_3_f10", Integer, nullable=True),
    Column("si_4_f14", Integer, nullable=False),
    Column("si_5_f18", Integer, nullable=True),
    Column("si_6_f22", Integer, nullable=True),
    Column("si_7_f26", Integer, nullable=False),
    Column("si_8_f30", Integer, nullable=True),
    Column("si_9_f34", Integer, nullable=True),
    Column("si_10_f38", Integer, nullable=False),
    Column("si_11_f42", Integer, nullable=False),
)

ils_processing_answers = Table(
    "ils_processing_answers",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("questionnaire_ils_id", Integer, nullable=False),
    Column("ar_1_f1", Integer, nullable=True),
    Column("ar_2_f5", Integer, nullable=True),
    Column("ar_3_f9", Integer, nullable=False),
    Column("ar_4_f13", Integer, nullable=False),
    Column("ar_5_f17", Integer, nullable=True),
    Column("ar_6_f21", Integer, nullable=False),
    Column("ar_7_f25", Integer, nullable=False),
    Column("ar_8_f29", Integer, nullable=False),
    Column("ar_9_f33", Integer, nullable=True),
    Column("ar_10_f37", Integer, nullable=True),
    Column("ar_11_f41", Integer, nullable=True),
)

ils_understanding_answers = Table(
    "ils_understanding_answers",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("questionnaire_ils_id", Integer, nullable=False),
    Column("sg_1_f4", Integer, nullable=False),
    Column("sg_2_f8", Integer, nullable=False),
    Column("sg_3_f12", Integer, nullable=True),
    Column("sg_4_f16", Integer, nullable=False),
    Column("sg_5_f20", Integer, nullable=True),
    Column("sg_6_f24", Integer, nullable=True),
    Column("sg_7_f28", Integer, nullable=True),
    Column("sg_8_f32", Integer, nullable=True),
    Column("sg_9_f36", Integer, nullable=True),
    Column("sg_10_f40", Integer, nullable=False),
    Column("sg_11_f44", Integer, nullable=False),
)

knowledge = Table(
    "knowledge",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("characteristic_id", Integer, nullable=False),
)

learning_analytics = Table(
    "learning_analytics",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("characteristic_id", Integer, nullable=False),
)

learning_charcteristics = Table(
    "learning_characteristics",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
)

learning_element = Table(
    "learning_element",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("lms_id", Integer, nullable=False),
    Column("activity_type", String, nullable=False),
    Column("classification", String, nullable=False),
    Column("name", String, nullable=False),
    Column("university", String, nullable=False),
    Column("created_at", Date, nullable=False),
    Column("created_by", String, nullable=False),
    Column("last_updated", Date, nullable=True),
)

learning_element_rating = Table(
    "learning_element_rating",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("learning_element_id", Integer, nullable=False),
    Column("rating", Integer, nullable=False),
    Column("message", String, nullable=True),
    Column("date", Date, nullable=False),
)

learning_path = Table(
    "learning_path",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("course_id", Integer, nullable=False),
    Column("based_on", String, nullable=False),
    Column("topic_id", Integer, nullable=True),
    Column("calculated_on", String, nullable=True),
)

learning_path_learning_element = Table(
    "learning_path_learning_element",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("learning_element_id", Integer, nullable=False),
    Column("learning_path_id", Integer, nullable=False),
    Column("recommended", Boolean, nullable=False),
    Column("position", Integer, nullable=False),
)

learning_path_topic = Table(
    "learning_path_topic",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("topic_id", Integer, nullable=False),
    Column("learning_path_id", Integer, nullable=False),
    Column("recommended", Boolean, nullable=False),
    Column("position", Integer, nullable=False),
)

learning_strategy = Table(
    "learning_strategy",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("characteristic_id", Integer, nullable=False),
    Column("cogn_str", Float, nullable=False),
    Column("org", Float, nullable=False),
    Column("elab", Float, nullable=False),
    Column("crit_rev", Float, nullable=False),
    Column("rep", Float, nullable=False),
    Column("metacogn_str", Float, nullable=False),
    Column("goal_plan", Float, nullable=False),
    Column("con", Float, nullable=False),
    Column("reg", Float, nullable=False),
    Column("int_res_mng_str", Float, nullable=False),
    Column("att", Float, nullable=False),
    Column("eff", Float, nullable=False),
    Column("time", Float, nullable=False),
    Column("ext_res_mng_str", Float, nullable=False),
    Column("lrn_w_cls", Float, nullable=False),
    Column("lit_res", Float, nullable=False),
    Column("lrn_env", Float, nullable=False)
)

learning_style = Table(
    "learning_style",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("characteristic_id", Integer, nullable=False),
    Column("perception_dimension", String, nullable=False),
    Column("perception_value", Integer, nullable=False),
    Column("input_dimension", String, nullable=False),
    Column("input_value", Integer, nullable=False),
    Column("processing_dimension", String, nullable=False),
    Column("processing_value", Integer, nullable=False),
    Column("understanding_dimension", String, nullable=False),
    Column("understanding_value", Integer, nullable=False),
)

questionnaire_list_k = Table(
    "questionnaire_list_k",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("org1_f1", Integer, nullable=False),
    Column("org2_f2", Integer, nullable=False),
    Column("org3_f3", Integer, nullable=False),
    Column("elab1_f4", Integer, nullable=False),
    Column("elab2_f5", Integer, nullable=False),
    Column("elab3_f6", Integer, nullable=False),
    Column("crit_rev1_f7", Integer, nullable=False),
    Column("crit_rev2_f8", Integer, nullable=False),
    Column("crit_rev3_f9", Integer, nullable=False),
    Column("rep1_f10", Integer, nullable=False),
    Column("rep2_f11", Integer, nullable=False),
    Column("rep3_f12", Integer, nullable=False),
    Column("goal_plan1_f13", Integer, nullable=False),
    Column("goal_plan2_f14", Integer, nullable=False),
    Column("goal_plan3_f15", Integer, nullable=False),
    Column("con1_f16", Integer, nullable=False),
    Column("con2_f17", Integer, nullable=False),
    Column("con3_f18", Integer, nullable=False),
    Column("reg1_f19", Integer, nullable=False),
    Column("reg2_f20", Integer, nullable=False),
    Column("reg3_f21", Integer, nullable=False),
    Column("att1_f22", Integer, nullable=False),
    Column("att2_f23", Integer, nullable=False),
    Column("att3_f24", Integer, nullable=False),
    Column("eff1_f25", Integer, nullable=False),
    Column("eff2_f26", Integer, nullable=False),
    Column("eff3_f27", Integer, nullable=False),
    Column("time1_f28", Integer, nullable=False),
    Column("time2_f29", Integer, nullable=False),
    Column("time3_f30", Integer, nullable=False),
    Column("lrn_w_cls1_f31", Integer, nullable=False),
    Column("lrn_w_cls2_f32", Integer, nullable=False),
    Column("lrn_w_cls3_f33", Integer, nullable=False),
    Column("lit_res1_f34", Integer, nullable=False),
    Column("lit_res2_f35", Integer, nullable=False),
    Column("lit_res3_f36", Integer, nullable=False),
    Column("lrn_env1_f37", Integer, nullable=False),
    Column("lrn_env2_f38", Integer, nullable=False),
    Column("lrn_env3_f39", Integer, nullable=False)
)

questionnaire_ils = Table(
    "questionnaire_ils",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
)

settings = Table(
    "settings",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
    Column("theme", String, nullable=True),
    Column("pswd", String, nullable=True),
)

contact_form = Table(
    "contact_form",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
    Column("report_topic", String, nullable=False),
    Column("report_type", String, nullable=False),
    Column("report_description", String, nullable=False),
    Column("date", Date, nullable=False),
)

student = Table(
    "student",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
)

student_course = Table(
    "student_course",
    mapper_registry.metadata,
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
    Column("understanding_value", Integer, nullable=False),
)

student_learning_element = Table(
    "student_learning_element",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("learning_element_id", Integer, nullable=False),
    Column("done", Boolean, nullable=False),
    Column("done_at", Date, nullable=True),
)

student_learning_element_visit = Table(
    "student_learning_element_visit",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("learning_element_id", Integer, nullable=False),
    Column("visit_start", Date, nullable=False),
    Column("visit_end", Date, nullable=True),
)

student_topic = Table(
    "student_topic",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("topic_id", Integer, nullable=False),
    Column("done", Boolean, nullable=False),
    Column("done_at", Date, nullable=True),
)

student_topic_visit = Table(
    "student_topic_visit",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_id", Integer, nullable=False),
    Column("topic_id", Integer, nullable=False),
    Column("visit_start", Date, nullable=False),
    Column("visit_end", Date, nullable=True),
)

teacher = Table(
    "teacher",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
)

teacher_course = Table(
    "teacher_course",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("teacher_id", Integer, nullable=False),
    Column("course_id", Integer, nullable=False),
)

topic = Table(
    "topic",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("lms_id", Integer, nullable=False),
    Column("is_topic", Boolean, nullable=False),
    Column("parent_id", Integer, nullable=True),
    Column("contains_le", Boolean, nullable=False),
    Column("name", String, nullable=False),
    Column("university", String, nullable=False),
    Column("created_by", String, nullable=False),
    Column("created_at", Date, nullable=False),
    Column("last_updated", Date, nullable=True),
)

topic_learning_element = Table(
    "topic_learning_element",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("topic_id", Integer, nullable=False),
    Column("learning_element_id", Integer, nullable=False),
)


def start_mappers():
    mapper_registry.map_imperatively(
        UA.Admin,
        admin,
    )
    mapper_registry.map_imperatively(
        DM.Course,
        course,
    )
    mapper_registry.map_imperatively(
        UA.CourseCreator,
        course_creator,
    )
    mapper_registry.map_imperatively(
        DM.CourseCreatorCourse,
        course_creator_course,
    )
    mapper_registry.map_imperatively(
        DM.CourseTopic,
        course_topic,
    )
    mapper_registry.map_imperatively(
        UA.User,
        haski_user,
    )
    mapper_registry.map_imperatively(
        LM.IlsInputAnswers,
        ils_input_answers,
    )
    mapper_registry.map_imperatively(
        LM.IlsPerceptionAnswers,
        ils_perception_answers,
    )
    mapper_registry.map_imperatively(
        LM.IlsProcessingAnswers,
        ils_processing_answers,
    )
    mapper_registry.map_imperatively(
        LM.IlsUnderstandingAnswers,
        ils_understanding_answers,
    )
    mapper_registry.map_imperatively(
        LM.Knowledge,
        knowledge,
    )
    mapper_registry.map_imperatively(
        LM.LearningAnalytics,
        learning_analytics,
    )
    mapper_registry.map_imperatively(
        LM.LearningCharacteristic,
        learning_charcteristics,
    )
    mapper_registry.map_imperatively(
        DM.LearningElement,
        learning_element,
    )
    mapper_registry.map_imperatively(
        DM.LearningElementRating,
        learning_element_rating,
    )
    mapper_registry.map_imperatively(
        TM.LearningPath,
        learning_path,
    )
    mapper_registry.map_imperatively(
        TM.LearningPathLearningElement,
        learning_path_learning_element,
    )
    mapper_registry.map_imperatively(
        TM.LearningPathTopic,
        learning_path_topic,
    )
    mapper_registry.map_imperatively(
        LM.LearningStrategy,
        learning_strategy,
    )
    mapper_registry.map_imperatively(
        LM.LearningStyle,
        learning_style,
    )

    mapper_registry.map_imperatively(
        LM.QuestionnaireListK,
        questionnaire_list_k,
    )

    mapper_registry.map_imperatively(
        LM.QuestionnaireIls,
        questionnaire_ils,
    )

    mapper_registry.map_imperatively(
        UA.Settings,
        settings,
    )

    mapper_registry.map_imperatively(
        UA.ContactForm,
        contact_form,
    )

    mapper_registry.map_imperatively(
        UA.Student,
        student,
    )

    mapper_registry.map_imperatively(
        DM.StudentCourse,
        student_course,
    )

    mapper_registry.map_imperatively(
        DM.StudentLearningElement,
        student_learning_element,
    )

    mapper_registry.map_imperatively(
        DM.StudentLearningElementVisit,
        student_learning_element_visit,
    )

    mapper_registry.map_imperatively(
        DM.StudentTopic,
        student_topic,
    )

    mapper_registry.map_imperatively(
        DM.StudentTopicVisit,
        student_topic_visit,
    )

    mapper_registry.map_imperatively(
        UA.Teacher,
        teacher,
    )

    mapper_registry.map_imperatively(
        DM.TeacherCourse,
        teacher_course,
    )

    mapper_registry.map_imperatively(
        DM.Topic,
        topic,
    )

    mapper_registry.map_imperatively(
        DM.TopicLearningElement,
        topic_learning_element,
    )
