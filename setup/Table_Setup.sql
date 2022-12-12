--Table: public.learning_path_test

DROP TABLE IF EXISTS public.learning_path_test;

CREATE TABLE IF NOT EXISTS public.learning_path_test
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    learning_path text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT learning_path_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_path_test
    OWNER to postgres;


-- Table: public.learning_element

DROP TABLE IF EXISTS public.learning_element;

CREATE TABLE IF NOT EXISTS public.learning_element
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 25 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name text COLLATE pg_catalog."default" NOT NULL,
    classification text COLLATE pg_catalog."default" NOT NULL,
    ancestor_id integer NOT NULL,
    prerequisite_id text COLLATE pg_catalog."default",
    order_depth integer NOT NULL,
    CONSTRAINT learning_element_pkey PRIMARY KEY (id),
    CONSTRAINT learning_element_ancestor_id_fkey FOREIGN KEY (ancestor_id)
        REFERENCES public.topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_element
    OWNER to postgres;


-- Table: public.learning_path

DROP TABLE IF EXISTS public.learning_path;

CREATE TABLE IF NOT EXISTS public.learning_path
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    course_id integer NOT NULL,
    contains_le boolean NOT NULL,
    order_depth integer NOT NULL,
    path text COLLATE pg_catalog."default",
    CONSTRAINT learning_path_pkey1 PRIMARY KEY (id),
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

ALTER TABLE IF EXISTS public.learning_path
    OWNER to postgres;


-- Table: public.course

DROP TABLE IF EXISTS public.course;

CREATE TABLE IF NOT EXISTS public.course
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 2 MINVALUE 2 MAXVALUE 2147483647 CACHE 1 ),
    name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT course_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.course
    OWNER to postgres;


-- Table: public.student

DROP TABLE IF EXISTS public.student;

CREATE TABLE IF NOT EXISTS public.student
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 3 MINVALUE 3 MAXVALUE 2147483647 CACHE 1 ),
    name text COLLATE pg_catalog."default" NOT NULL,
    learning_style text COLLATE pg_catalog."default",
    CONSTRAINT student_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student
    OWNER to postgres;


-- Table: public.student_element

DROP TABLE IF EXISTS public.student_element;

CREATE TABLE IF NOT EXISTS public.student_element
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    element_id integer NOT NULL,
    is_recommended boolean NOT NULL,
    done boolean NOT NULL,
    done_at date,
    CONSTRAINT student_element_pkey PRIMARY KEY (id),
    CONSTRAINT student_element_element_id_fkey FOREIGN KEY (element_id)
        REFERENCES public.learning_element (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT student_element_student_id_fkey FOREIGN KEY (student_id)
        REFERENCES public.student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.student_element
    OWNER to postgres;


-- Table: public.student_topic

DROP TABLE IF EXISTS public.student_topic;

CREATE TABLE IF NOT EXISTS public.student_topic
(
    id integer NOT NULL,
    topic_id integer NOT NULL,
    course_id integer NOT NULL,
    student_id integer NOT NULL,
    is_recommended boolean NOT NULL,
    sequence_nr integer NOT NULL,
    done boolean NOT NULL DEFAULT false,
    done_at date,
    CONSTRAINT student_topic_pkey PRIMARY KEY (id),
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

ALTER TABLE IF EXISTS public.student_topic
    OWNER to postgres;


-- Table: public.topic

DROP TABLE IF EXISTS public.topic;

CREATE TABLE IF NOT EXISTS public.topic
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 17 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name text COLLATE pg_catalog."default" NOT NULL,
    course_id integer NOT NULL,
    ancestor_id integer,
    prerequisite_id integer,
    order_depth integer NOT NULL,
    CONSTRAINT topic_pkey PRIMARY KEY (id),
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES public.course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.topic
    OWNER to postgres;
