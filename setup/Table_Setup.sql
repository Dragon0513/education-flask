--Table: public.learning_path

DROP TABLE IF EXISTS public.learning_path;

CREATE TABLE IF NOT EXISTS public.learning_path
(
    id integer NOT NULL,
    student_id integer NOT NULL,
    learning_path text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT learning_path_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.learning_path
    OWNER to postgres;