import os

import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password=os.environ.get("DB_PASSWORD", "postgres"),
    host=os.environ.get("DB_HOST", "localhost"),
    port=os.environ.get("DB_PORT", 5432),
)
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
sql = """CREATE database haski"""

# Creating a database
cursor.execute(sql)

conn.commit()
# Closing the connection
conn.close()

# Establishing the connection
conn = psycopg2.connect(
    database=os.environ.get("DB_NAME", "haski"),
    user="postgres",
    password=os.environ.get("DB_PASSWORD", "postgres"),
    host=os.environ.get("DB_HOST", "127.0.0.1"),
    port=os.environ.get("DB_PORT", 5432),
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Droping table if already exists.
cursor.execute("DROP TABLE IF EXISTS haski_user")
cursor.execute("DROP TABLE IF EXISTS settings")
cursor.execute("DROP TABLE IF EXISTS admin")
cursor.execute("DROP TABLE IF EXISTS course_creator")
cursor.execute("DROP TABLE IF EXISTS teacher")
cursor.execute("DROP TABLE IF EXISTS student")
cursor.execute("DROP TABLE IF EXISTS course")
cursor.execute("DROP TABLE IF EXISTS topic")
cursor.execute("DROP TABLE IF EXISTS learning_element")
cursor.execute("DROP TABLE IF EXISTS course_topic")
cursor.execute("DROP TABLE IF EXISTS topic_learning_element")
cursor.execute("DROP TABLE IF EXISTS learning_characteristics")
cursor.execute("DROP TABLE IF EXISTS learning_style")
cursor.execute("DROP TABLE IF EXISTS learning_strategy")
cursor.execute("DROP TABLE IF EXISTS knowledge")
cursor.execute("DROP TABLE IF EXISTS learning_analytics")
cursor.execute("DROP TABLE IF EXISTS course_creator_course")
cursor.execute("DROP TABLE IF EXISTS teacher_course")
cursor.execute("DROP TABLE IF EXISTS student_course")
cursor.execute("DROP TABLE IF EXISTS student_topic")
cursor.execute("DROP TABLE IF EXISTS student_topic_visit")
cursor.execute("DROP TABLE IF EXISTS student_learning_element")
cursor.execute("DROP TABLE IF EXISTS student_learning_element_visit")
cursor.execute("DROP TABLE IF EXISTS learning_element_rating")
cursor.execute("DROP TABLE IF EXISTS learning_path")
cursor.execute("DROP TABLE IF EXISTS learning_path_topic")
cursor.execute("DROP TABLE IF EXISTS learning_path_learning_element")
cursor.execute("DROP TABLE IF EXISTS questionnaire")
cursor.execute("DROP TABLE IF EXISTS ils_input_answers")
cursor.execute("DROP TABLE IF EXISTS ils_perception_answers")
cursor.execute("DROP TABLE IF EXISTS ils_processing_answers")
cursor.execute("DROP TABLE IF EXISTS ils_understanding_answers")
cursor.execute("DROP TABLE IF EXISTS list_k")

# Creating table as per requirement
sql = """
    CREATE TABLE IF NOT EXISTS public."haski_user"
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        name text COLLATE pg_catalog."default" NOT NULL,
        university text COLLATE pg_catalog."default" NOT NULL,
        lms_user_id integer NOT NULL,
        role text COLLATE pg_catalog."default" NOT NULL,
        CONSTRAINT user_pkey PRIMARY KEY (id)
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public."haski_user"
        OWNER to postgres;
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.settings
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.admin
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.course_creator
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.teacher
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.student
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.course
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        lms_id integer NOT NULL,
        name text COLLATE pg_catalog."default" NOT NULL,
        university text COLLATE pg_catalog."default" NOT NULL,
        CONSTRAINT course_pkey PRIMARY KEY (id)
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.course
        OWNER to postgres;
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.topic
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_element
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.course_topic
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.topic_learning_element
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_characteristics
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        student_id integer NOT NULL,
        CONSTRAINT learning_characteristics_pkey PRIMARY KEY (id),
        CONSTRAINT student_id FOREIGN KEY (student_id)
            REFERENCES public."student" (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.learning_characteristics
        OWNER to postgres;
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_style
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_strategy
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        characteristic_id integer NOT NULL,
        CONSTRAINT learning_strategy_pkey PRIMARY KEY (id),
        CONSTRAINT characteristic_id FOREIGN KEY (characteristic_id)
            REFERENCES public.learning_characteristics (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.learning_strategy
        OWNER to postgres;
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.knowledge
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        characteristic_id integer NOT NULL,
        CONSTRAINT knowledge_pkey PRIMARY KEY (id),
        CONSTRAINT characteristic_id FOREIGN KEY (characteristic_id)
            REFERENCES public.learning_characteristics (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.knowledge
        OWNER to postgres;
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_analytics
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        characteristic_id integer NOT NULL,
        CONSTRAINT learning_analytics_pkey PRIMARY KEY (id),
        CONSTRAINT characteristic_id FOREIGN KEY (characteristic_id)
            REFERENCES public.learning_characteristics (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.learning_analytics
        OWNER to postgres;
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.course_creator_course
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.teacher_course
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.student_course
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.student_topic
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.student_topic_visit
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.student_learning_element
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.student_learning_element_visit
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_element_rating
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_path
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        student_id integer NOT NULL,
        course_id integer NOT NULL,
        based_on text COLLATE pg_catalog."default" NOT NULL,
        topic_id integer,
        calculated_on timestamp with time zone,
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_path_topic
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.learning_path_learning_element
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.questionnaire
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.ils_input_answers
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.ils_perception_answers
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.ils_processing_answers
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.ils_understanding_answers
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
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
"""
cursor.execute(sql)

sql = """
    CREATE TABLE IF NOT EXISTS public.list_k
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY
        ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        org1_f1 integer NOT NULL,
        org2_f2 integer NOT NULL,
        org3_f3 integer NOT NULL,
        ela1_f4 integer NOT NULL,
        ela2_f5 integer NOT NULL,
        ela3_f6 integer NOT NULL,
        krp1_f7 integer NOT NULL,
        krp2_f8 integer NOT NULL,
        krp3_f9 integer NOT NULL,
        wie1_f10 integer NOT NULL,
        wie2_f11 integer NOT NULL,
        wie3_f12 integer NOT NULL,
        zp1_f13 integer NOT NULL,
        zp2_f14 integer NOT NULL,
        zp3_f15 integer NOT NULL,
        kon1_f16 integer NOT NULL,
        kon2_f17 integer NOT NULL,
        kon3_f18 integer NOT NULL,
        reg1_f19 integer NOT NULL,
        reg2_f20 integer NOT NULL,
        reg3_f21 integer NOT NULL,
        auf1_f22 integer NOT NULL,
        auf2_f23 integer NOT NULL,
        auf3_f24 integer NOT NULL,
        ans1_f25 integer NOT NULL,
        ans2_f26 integer NOT NULL,
        ans3_f27 integer NOT NULL,
        zei1_f28 integer NOT NULL,
        zei2_f29 integer NOT NULL,
        zei3_f30 integer NOT NULL,
        lms1_f31 integer NOT NULL,
        lms2_f32 integer NOT NULL,
        lms3_f33 integer NOT NULL,
        lit1_f34 integer NOT NULL,
        lit2_f35 integer NOT NULL,
        lit3_f36 integer NOT NULL,
        lu1_f37 integer NOT NULL,
        lu2_f38 integer NOT NULL,
        lu3_f39 integer NOT NULL,
        questionnaire_id integer NOT NULL,
        CONSTRAINT list_k_pkey PRIMARY KEY (id),
        CONSTRAINT questionnaire_id FOREIGN KEY (questionnaire_id)
            REFERENCES public.questionnaire (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.list_k
        OWNER to postgres;
"""
cursor.execute(sql)

conn.commit()
# Closing the connection
conn.close()
