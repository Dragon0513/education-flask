-- User
DROP TABLE IF EXISTS public."haski_user";

CREATE TABLE IF NOT EXISTS public."haski_user"
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name text COLLATE pg_catalog."default" NOT NULL,
    university text COLLATE pg_catalog."default" NOT NULL,
    lms_user_id integer NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."haski_user"
    OWNER to postgres;

--Settings
DROP TABLE IF EXISTS public.settings;

CREATE TABLE IF NOT EXISTS public.settings
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_id integer NOT NULL,
    theme text COLLATE pg_catalog."default",
    pswd text COLLATE pg_catalog."default",
    CONSTRAINT settings_pkey PRIMARY KEY (id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public."haski_user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.settings
    OWNER to postgres;

-- Admin
DROP TABLE IF EXISTS public.admin;

CREATE TABLE IF NOT EXISTS public.admin
(
    id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT admin_pkey PRIMARY KEY (id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public."haski_user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.admin
    OWNER to postgres;

-- Course Creator
DROP TABLE IF EXISTS public.course_creator;

CREATE TABLE IF NOT EXISTS public.course_creator
(
    id integer NOT NULL,
    user_id integer,
    CONSTRAINT course_creator_pkey PRIMARY KEY (id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public."haski_user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.course_creator
    OWNER to postgres;

-- Teacher
DROP TABLE IF EXISTS public.teacher;

CREATE TABLE IF NOT EXISTS public.teacher
(
    id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT teacher_pkey PRIMARY KEY (id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public."haski_user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.teacher
    OWNER to postgres;

-- Student
DROP TABLE IF EXISTS public.student;

CREATE TABLE IF NOT EXISTS public.student
(
    id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT student_pkey PRIMARY KEY (id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public."haski_user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student
    OWNER to postgres;

-- Course
DROP TABLE IF EXISTS public.course;

CREATE TABLE IF NOT EXISTS public.course
(
    id integer NOT NULL,
    lms_id integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    university text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT course_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.course
    OWNER to postgres;

-- Topic
DROP TABLE IF EXISTS public.topic;

CREATE TABLE IF NOT EXISTS public.topic
(
    id integer NOT NULL,
    lms_id integer NOT NULL,
    is_topic boolean NOT NULL,
    parent_id integer,
    contains_le boolean NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    university text COLLATE pg_catalog."default" NOT NULL,
    created_by text COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp without time zone NOT NULL,
    last_updated timestamp without time zone,
    CONSTRAINT topic_pkey PRIMARY KEY (id),
    CONSTRAINT topic_id FOREIGN KEY (parent_id)
        REFERENCES public.topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.topic
    OWNER to postgres;

-- Learning Element
DROP TABLE IF EXISTS public.learning_element;

CREATE TABLE IF NOT EXISTS public.learning_element
(
    id integer NOT NULL,
    lms_id integer NOT NULL,
    activity_type text COLLATE pg_catalog."default" NOT NULL,
    classification text COLLATE pg_catalog."default" NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    university text COLLATE pg_catalog."default" NOT NULL,
    created_by text COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp without time zone NOT NULL,
    last_updated timestamp without time zone,
    CONSTRAINT learning_element_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_element
    OWNER to postgres;

-- Course Topic
DROP TABLE IF EXISTS public.course_topic;

CREATE TABLE IF NOT EXISTS public.course_topic
(
    id integer NOT NULL,
    course_id integer NOT NULL,
    topic_id integer NOT NULL,
    CONSTRAINT course_topic_pkey PRIMARY KEY (id),
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES public.course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT topic_id FOREIGN KEY (topic_id)
        REFERENCES public.topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.course_topic
    OWNER to postgres;

-- Topic Learning Element
DROP TABLE IF EXISTS public.topic_learning_element;

CREATE TABLE IF NOT EXISTS public.topic_learning_element
(
    id integer NOT NULL,
    topic_id integer NOT NULL,
    learning_element_id integer NOT NULL,
    CONSTRAINT topic_learninf_element_pkey PRIMARY KEY (id),
    CONSTRAINT learning_element_id FOREIGN KEY (learning_element_id)
        REFERENCES public.learning_element (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT topic_id FOREIGN KEY (topic_id)
        REFERENCES public.topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.topic_learning_element
    OWNER to postgres;

-- Learning Characteristic
DROP TABLE IF EXISTS public.learning_characteristics;

CREATE TABLE IF NOT EXISTS public.learning_characteristics
(
    id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT learning_characteristics_pkey PRIMARY KEY (id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES public."haski_user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_characteristics
    OWNER to postgres;

-- Learning Style
DROP TABLE IF EXISTS public.learning_style;

CREATE TABLE IF NOT EXISTS public.learning_style
(
    id integer NOT NULL,
    characteristic_id integer NOT NULL,
    perception_dimension text COLLATE pg_catalog."default" NOT NULL,
    perception_value integer NOT NULL,
    input_dimension text COLLATE pg_catalog."default" NOT NULL,
    input_value integer NOT NULL,
    processing_dimension text COLLATE pg_catalog."default" NOT NULL,
    processing_value integer NOT NULL,
    understanding_dimension text COLLATE pg_catalog."default" NOT NULL,
    understanding_value integer NOT NULL,
    CONSTRAINT learning_style_pkey PRIMARY KEY (id),
    CONSTRAINT characteristic_id FOREIGN KEY (characteristic_id)
        REFERENCES public.learning_characteristics (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_style
    OWNER to postgres;

-- Learning Strategy
DROP TABLE IF EXISTS public.learning_strategy;

CREATE TABLE IF NOT EXISTS public.learning_strategy
(
    id integer NOT NULL,
    characterisitc_id integer NOT NULL,
    CONSTRAINT learning_strategy_pkey PRIMARY KEY (id),
    CONSTRAINT characterisitc_id FOREIGN KEY (characterisitc_id)
        REFERENCES public.learning_characteristics (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_strategy
    OWNER to postgres;

-- Knowledge
DROP TABLE IF EXISTS public.knowledge;

CREATE TABLE IF NOT EXISTS public.knowledge
(
    id integer NOT NULL,
    characterisitc_id integer NOT NULL,
    CONSTRAINT knowledge_pkey PRIMARY KEY (id),
    CONSTRAINT characterisitc_id FOREIGN KEY (characterisitc_id)
        REFERENCES public.learning_characteristics (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.knowledge
    OWNER to postgres;

-- Learning Analytics
DROP TABLE IF EXISTS public.learning_analytics;

CREATE TABLE IF NOT EXISTS public.learning_analytics
(
    id integer NOT NULL,
    characterisitc_id integer NOT NULL,
    CONSTRAINT learning_analytics_pkey PRIMARY KEY (id),
    CONSTRAINT characterisitc_id FOREIGN KEY (characterisitc_id)
        REFERENCES public.learning_characteristics (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_analytics
    OWNER to postgres;

-- Course Creator Course
DROP TABLE IF EXISTS public.course_creator_course;

CREATE TABLE IF NOT EXISTS public.course_creator_course
(
    id integer NOT NULL,
    course_creator_id integer NOT NULL,
    course_id integer NOT NULL,
    created_at timestamp without time zone NOT NULL,
    last_updated timestamp without time zone,
    CONSTRAINT course_creator_course_pkey PRIMARY KEY (id),
    CONSTRAINT course_creator_id FOREIGN KEY (course_creator_id)
        REFERENCES public.course_creator (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES public.course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.course_creator_course
    OWNER to postgres;

-- Teacher Course
DROP TABLE IF EXISTS public.teacher_course;

CREATE TABLE IF NOT EXISTS public.teacher_course
(
    id integer NOT NULL,
    teacher_id integer NOT NULL,
    course_id integer NOT NULL,
    CONSTRAINT teacher_course_pkey PRIMARY KEY (id),
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES public.course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT teacher_id FOREIGN KEY (teacher_id)
        REFERENCES public.teacher (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.teacher_course
    OWNER to postgres;

-- Student Course
DROP TABLE IF EXISTS public.student_course;

CREATE TABLE IF NOT EXISTS public.student_course
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    course_id integer NOT NULL,
    perception_dimension text COLLATE pg_catalog."default" NOT NULL,
    perception_value integer NOT NULL,
    input_dimension text COLLATE pg_catalog."default" NOT NULL,
    input_value integer NOT NULL,
    processing_dimension text COLLATE pg_catalog."default" NOT NULL,
    processing_value integer NOT NULL,
    understanding_dimension text COLLATE pg_catalog."default" NOT NULL,
    understanding_value integer NOT NULL,
    CONSTRAINT student_course_pkey PRIMARY KEY (id),
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES public.course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES public.student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student_course
    OWNER to postgres;

-- Student Topic
DROP TABLE IF EXISTS public.student_topic;

CREATE TABLE IF NOT EXISTS public.student_topic
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    topic_id integer NOT NULL,
    done boolean NOT NULL,
    done_at timestamp without time zone,
    CONSTRAINT student_topic_pkey PRIMARY KEY (id),
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES public.student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT topic_id FOREIGN KEY (topic_id)
        REFERENCES public.topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student_topic
    OWNER to postgres;

-- Student Topic Visit
DROP TABLE IF EXISTS public.student_topic_visit;

CREATE TABLE IF NOT EXISTS public.student_topic_visit
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    topic_id integer NOT NULL,
    visit_start timestamp without time zone NOT NULL,
    visit_end timestamp without time zone,
    CONSTRAINT student_topic_visit_pkey PRIMARY KEY (id),
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES public.student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT topic_id FOREIGN KEY (topic_id)
        REFERENCES public.topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student_topic_visit
    OWNER to postgres;

-- Student Learning Element
DROP TABLE IF EXISTS public.student_learning_element;

CREATE TABLE IF NOT EXISTS public.student_learning_element
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    learning_element_id integer NOT NULL,
    done boolean NOT NULL,
    done_at timestamp without time zone,
    CONSTRAINT student_learning_element_pkey PRIMARY KEY (id),
    CONSTRAINT learning_element_id FOREIGN KEY (learning_element_id)
        REFERENCES public.learning_element (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES public.student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student_learning_element
    OWNER to postgres;

-- Student Learning Element Visit
DROP TABLE IF EXISTS public.student_learning_element_visit;

CREATE TABLE IF NOT EXISTS public.student_learning_element_visit
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    learning_element_id integer NOT NULL,
    visit_start timestamp without time zone NOT NULL,
    visit_end timestamp without time zone,
    CONSTRAINT student_learning_element_visit_pkey PRIMARY KEY (id),
    CONSTRAINT learning_element_id FOREIGN KEY (learning_element_id)
        REFERENCES public.learning_element (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES public.student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student_learning_element_visit
    OWNER to postgres;

-- Learning Element Rating
DROP TABLE IF EXISTS public.learning_element_rating;

CREATE TABLE IF NOT EXISTS public.learning_element_rating
(
    id integer NOT NULL,
    learning_element_id integer NOT NULL,
    rating integer NOT NULL,
    message text COLLATE pg_catalog."default",
    date timestamp without time zone NOT NULL,
    CONSTRAINT learning_element_rating_pkey PRIMARY KEY (id),
    CONSTRAINT learning_element_id FOREIGN KEY (learning_element_id)
        REFERENCES public.learning_element (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_element_rating
    OWNER to postgres;

-- Learning Path
DROP TABLE IF EXISTS public.learning_path;

CREATE TABLE IF NOT EXISTS public.learning_path
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    course_id integer NOT NULL,
    topic_id integer,
    CONSTRAINT learning_path_pkey PRIMARY KEY (id),
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES public.course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES public.student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT topic_id FOREIGN KEY (topic_id)
        REFERENCES public.topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_path
    OWNER to postgres;

-- Learning Path Topic
DROP TABLE IF EXISTS public.learning_path_topic;

CREATE TABLE IF NOT EXISTS public.learning_path_topic
(
    id integer NOT NULL,
    topic_id integer NOT NULL,
    learning_path_id integer NOT NULL,
    recommended boolean NOT NULL,
    "position" integer NOT NULL,
    CONSTRAINT learning_path_topic_pkey PRIMARY KEY (id),
    CONSTRAINT learning_path_id FOREIGN KEY (learning_path_id)
        REFERENCES public.learning_path (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT topic_id FOREIGN KEY (topic_id)
        REFERENCES public.topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_path_topic
    OWNER to postgres;

-- Learning Path Learning Element
DROP TABLE IF EXISTS public.learning_path_learning_element;

CREATE TABLE IF NOT EXISTS public.learning_path_learning_element
(
    id integer NOT NULL,
    learning_element_id integer NOT NULL,
    learning_path_id integer NOT NULL,
    recommended boolean NOT NULL,
    "position" integer NOT NULL,
    CONSTRAINT learning_path_learning_element_pkey PRIMARY KEY (id),
    CONSTRAINT learning_element_id FOREIGN KEY (learning_element_id)
        REFERENCES public.learning_element (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT learning_path_id FOREIGN KEY (learning_path_id)
        REFERENCES public.learning_path (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_path_learning_element
    OWNER to postgres;

-- Questionnaire
DROP TABLE IF EXISTS public.questionnaire;

CREATE TABLE IF NOT EXISTS public.questionnaire
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    student_id integer NOT NULL,
    CONSTRAINT questionnaire_pkey PRIMARY KEY (id),
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES public.student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.questionnaire
    OWNER to postgres;

-- ILS Input Answers
DROP TABLE IF EXISTS public.ils_input_answers;

CREATE TABLE IF NOT EXISTS public.ils_input_answers
(
    id integer NOT NULL,
    questionnaire_id integer NOT NULL,
    vv_1_f3 text COLLATE pg_catalog."default",
    vv_2_f7 text COLLATE pg_catalog."default" NOT NULL,
    vv_3_f11 text COLLATE pg_catalog."default",
    vv_4_f15 text COLLATE pg_catalog."default",
    vv_5_f19 text COLLATE pg_catalog."default" NOT NULL,
    vv_6_f23 text COLLATE pg_catalog."default",
    vv_7_f27 text COLLATE pg_catalog."default" NOT NULL,
    vv_8_f31 text COLLATE pg_catalog."default",
    vv_9_f35 text COLLATE pg_catalog."default",
    vv_10_f39 text COLLATE pg_catalog."default" NOT NULL,
    vv_11_f43 text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ils_input_answers_pkey PRIMARY KEY (id),
    CONSTRAINT questionnaire_id FOREIGN KEY (questionnaire_id)
        REFERENCES public.questionnaire (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.ils_input_answers
    OWNER to postgres;

-- ILS Perception Answers
DROP TABLE IF EXISTS public.ils_perception_answers;

CREATE TABLE IF NOT EXISTS public.ils_perception_answers
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    questionnaire_id integer NOT NULL,
    si_1_f2 text COLLATE pg_catalog."default" NOT NULL,
    si_2_f6 text COLLATE pg_catalog."default",
    si_3_f10 text COLLATE pg_catalog."default",
    si_4_f14 text COLLATE pg_catalog."default" NOT NULL,
    si_5_f18 text COLLATE pg_catalog."default",
    si_6_f22 text COLLATE pg_catalog."default",
    si_7_f26 text COLLATE pg_catalog."default" NOT NULL,
    si_8_f30 text COLLATE pg_catalog."default",
    si_9_f34 text COLLATE pg_catalog."default",
    si_10_f38 text COLLATE pg_catalog."default" NOT NULL,
    si_11_f42 text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ils_perception_answers_pkey PRIMARY KEY (id),
    CONSTRAINT questionnaire_id FOREIGN KEY (questionnaire_id)
        REFERENCES public.questionnaire (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.ils_perception_answers
    OWNER to postgres;

-- ILS Processing Answers
DROP TABLE IF EXISTS public.ils_processing_answers;

CREATE TABLE IF NOT EXISTS public.ils_processing_answers
(
    id integer NOT NULL,
    questionnaire_id integer NOT NULL,
    ar_1_f1 text COLLATE pg_catalog."default",
    ar_2_f5 text COLLATE pg_catalog."default",
    ar_3_f9 text COLLATE pg_catalog."default" NOT NULL,
    ar_4_f13 text COLLATE pg_catalog."default" NOT NULL,
    ar_5_f17 text COLLATE pg_catalog."default",
    ar_6_f21 text COLLATE pg_catalog."default" NOT NULL,
    ar_7_f25 text COLLATE pg_catalog."default" NOT NULL,
    ar_8_f29 text COLLATE pg_catalog."default" NOT NULL,
    ar_9_f33 text COLLATE pg_catalog."default",
    ar_10_f37 text COLLATE pg_catalog."default",
    ar_11_f41 text COLLATE pg_catalog."default",
    CONSTRAINT ils_processing_answers_pkey PRIMARY KEY (id),
    CONSTRAINT questionnaire_id FOREIGN KEY (questionnaire_id)
        REFERENCES public.questionnaire (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.ils_processing_answers
    OWNER to postgres;

-- ILS Understanding Answers
DROP TABLE IF EXISTS public.ils_understanding_answers;

CREATE TABLE IF NOT EXISTS public.ils_understanding_answers
(
    id integer NOT NULL,
    questionnaire_id integer NOT NULL,
    sg_1_f4 text COLLATE pg_catalog."default" NOT NULL,
    sg_2_f8 text COLLATE pg_catalog."default" NOT NULL,
    sg_3_f12 text COLLATE pg_catalog."default",
    sg_4_f16 text COLLATE pg_catalog."default" NOT NULL,
    sg_5_f20 text COLLATE pg_catalog."default",
    sg_6_f24 text COLLATE pg_catalog."default",
    sg_7_f28 text COLLATE pg_catalog."default",
    sg_8_f32 text COLLATE pg_catalog."default",
    sg_9_f36 text COLLATE pg_catalog."default",
    sg_10_f40 text COLLATE pg_catalog."default" NOT NULL,
    sg_11_f44 text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ils_understanding_answers_pkey PRIMARY KEY (id),
    CONSTRAINT questionnaire_id FOREIGN KEY (questionnaire_id)
        REFERENCES public.questionnaire (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.ils_understanding_answers
    OWNER to postgres;