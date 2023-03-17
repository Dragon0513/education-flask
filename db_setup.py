import psycopg2
import os

# Establishing the connection
conn = psycopg2.connect(
    database="postgres",
    user='postgres',
    password="HASKI-Adm",
    host=os.environ.get("DB_HOST", "localhost"),
    port=os.environ.get("DB_PORT", 5432)
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
sql = '''CREATE database HASKI_test'''

# Creating a database
cursor.execute(sql)

conn.commit()
# Closing the connection
conn.close()

# Establishing the connection
conn = psycopg2.connect(
    database="haski_test",
    user='postgres',
    password=os.environ.get("DB_PASSWORD", "HASKI-Adm"),
    host=os.environ.get("DB_HOST", "127.0.0.1"),
    port=os.environ.get("DB_PORT", 5432)
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

# Creating table as per requirement
sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

sql = '''
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
'''
cursor.execute(sql)

conn.commit()
# Closing the connection
conn.close()
