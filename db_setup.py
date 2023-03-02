import psycopg2
import os

# Establishing the connection
conn = psycopg2.connect(
    database="postgres",
    user='postgres',
    password=os.environ.get("DB_PASSWORD", "postgres"),
    host=os.environ.get("DB_HOST", "localhost"),
    port=os.environ.get("DB_PORT", 5432)
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
sql = '''CREATE database HASKI'''

# Creating a database
cursor.execute(sql)

conn.commit()
# Closing the connection
conn.close()

# Establishing the connection
conn = psycopg2.connect(
    database=os.environ.get("DB_NAME", "haski"),
    user='postgres',
    password=os.environ.get("DB_PASSWORD", "postgres"),
    host=os.environ.get("DB_HOST", "127.0.0.1"),
    port=os.environ.get("DB_PORT", 5432)
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS learning_element")
cursor.execute("DROP TABLE IF EXISTS learning_path")
cursor.execute("DROP TABLE IF EXISTS course")
cursor.execute("DROP TABLE IF EXISTS student")
cursor.execute("DROP TABLE IF EXISTS topic")
cursor.execute("DROP TABLE IF EXISTS student_element")
cursor.execute("DROP TABLE IF EXISTS student_topic")

# Creating table as per requirement
sql = '''
    CREATE TABLE student(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    learning_style VARCHAR(100)
    )
'''
cursor.execute(sql)

sql = '''
    CREATE TABLE course(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
    )
'''
cursor.execute(sql)

sql = '''
    CREATE TABLE learning_path(
    id BIGSERIAL PRIMARY KEY,
    student_id integer NOT NULL,
    course_id integer NOT NULL,
    contains_le boolean NOT NULL,
    order_depth integer NOT NULL,
    path VARCHAR(500),
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
'''
cursor.execute(sql)

sql = '''
    CREATE TABLE topic(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    course_id INTEGER NOT NULL,
    ancestor_id INTEGER,
    prerequisite_id INTEGER,
    order_depth INTEGER NOT NULL,
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
'''
cursor.execute(sql)

sql = '''
    CREATE TABLE learning_element(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    classification VARCHAR(100) NOT NULL,
    ancestor_id INTEGER NOT NULL,
    prerequisite_id INTEGER,
    order_depth INTEGER NOT NULL,
    CONSTRAINT learning_element_ancestor_id_fkey FOREIGN KEY (ancestor_id)
        REFERENCES topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
'''
cursor.execute(sql)

sql = '''
    CREATE TABLE student_element(
    id BIGSERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    element_id INTEGER NOT NULL,
    is_recommended BOOLEAN NOT NULL,
    done BOOLEAN NOT NULL,
    done_at DATE,
    CONSTRAINT student_element_element_id_fkey FOREIGN KEY (element_id)
        REFERENCES learning_element (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT student_element_student_id_fkey FOREIGN KEY (student_id)
        REFERENCES student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
'''
cursor.execute(sql)

sql = '''
    CREATE TABLE student_topic(
    id BIGSERIAL PRIMARY KEY,
    topic_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    is_recommended BOOLEAN NOT NULL,
    sequence_nr INTEGER NOT NULL,
    done BOOLEAN NOT NULL,
    done_at DATE,
    CONSTRAINT course_id FOREIGN KEY (course_id)
        REFERENCES course (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT student_id FOREIGN KEY (student_id)
        REFERENCES student (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT topic_id FOREIGN KEY (topic_id)
        REFERENCES topic (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
'''
cursor.execute(sql)

conn.commit()
# Closing the connection
conn.close()
