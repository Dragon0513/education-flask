import argparse

import psycopg2

from db_setup import (
    DEFAULT_DB_HOST,
    DEFAULT_DB_NAME,
    DEFAULT_DB_PASSWORD,
    DEFAULT_DB_PORT,
    DEFAULT_DB_USER,
    parse_args,
)


def clean_up_db(
    db_database=DEFAULT_DB_NAME,
    db_user=DEFAULT_DB_USER,
    db_password=DEFAULT_DB_PASSWORD,
    db_host=DEFAULT_DB_HOST,
    db_port=DEFAULT_DB_PORT,
    db_drop=False,
):
    """Cleans up the database by deleting all the data from all the tables.

    Args:
        db_database (str, optional): Databasename. Defaults to DEFAULT_DB_NAME.
        db_user (str, optional): db user. Defaults to DEFAULT_DB_USER.
        db_password (str, optional): Password for \
            connection. Keep private. Defaults to DEFAULT_DB_PASSWORD.
        db_host (str, optional): database address\
            (i.e. localhost). Defaults to DEFAULT_DB_HOST.
        db_port (str, optional): Port to connect\
            to. Defaults to DEFAULT_DB_PORT.
        db_drop (str, optional): Use with caution!\
            Drop the specified Databasename.\
                Dont use when you are unsure. Defaults to False.
    """

    if db_drop:
        conn = psycopg2.connect(
            database="postgres",
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        conn.autocommit = True

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Drop database
        cursor.execute("DROP DATABASE IF EXISTS {}".format(db_database))

        conn.commit()
        # Closing the connection
        conn.close()
        return

    # Establishing the connection to postgres
    conn = psycopg2.connect(
        database=db_database,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
    )
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Table Cleanup
    cursor.execute("DELETE FROM ils_understanding_answers")
    cursor.execute("DELETE FROM ils_processing_answers")
    cursor.execute("DELETE FROM ils_perception_answers")
    cursor.execute("DELETE FROM ils_input_answers")
    cursor.execute("DELETE FROM questionnaire_list_k")
    cursor.execute("DELETE FROM questionnaire_ils")
    cursor.execute("DELETE FROM learning_path_learning_element")
    cursor.execute("DELETE FROM learning_path_topic")
    cursor.execute("DELETE FROM learning_path")
    cursor.execute("DELETE FROM learning_element_rating")
    cursor.execute("DELETE FROM student_learning_element_visit")
    cursor.execute("DELETE FROM student_learning_element")
    cursor.execute("DELETE FROM student_topic_visit")
    cursor.execute("DELETE FROM student_topic")
    cursor.execute("DELETE FROM student_course")
    cursor.execute("DELETE FROM teacher_course")
    cursor.execute("DELETE FROM course_creator_course")
    cursor.execute("DELETE FROM learning_analytics")
    cursor.execute("DELETE FROM knowledge")
    cursor.execute("DELETE FROM learning_strategy")
    cursor.execute("DELETE FROM learning_style")
    cursor.execute("DELETE FROM learning_characteristics")
    cursor.execute("DELETE FROM topic_learning_element")
    cursor.execute("DELETE FROM course_topic")
    cursor.execute("DELETE FROM learning_element")
    cursor.execute("DELETE FROM topic")
    cursor.execute("DELETE FROM course")
    cursor.execute("DELETE FROM student")
    cursor.execute("DELETE FROM teacher")
    cursor.execute("DELETE FROM course_creator")
    cursor.execute("DELETE FROM admin")
    cursor.execute("DELETE FROM settings")
    cursor.execute("DELETE FROM contact_form")
    cursor.execute("DELETE FROM news")
    cursor.execute("DELETE FROM haski_user")

    conn.commit()

    # Closing the connection
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dropdatabase",
        action="store_true",
        help="Drop the whole database. Use with caution!",
    )
    # Add the same arguments as in db_setup.py
    args = parse_args(parser)
    clean_up_db(
        args.dbname,
        args.user,
        args.password,
        args.host,
        args.port,
        args.dropdatabase,  # Use with caution!
    )
