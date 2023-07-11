import psycopg2
import os

# Establishing the connection
conn = psycopg2.connect(
    database="haski",
    user="postgres",
    password=os.environ.get("DB_PASSWORD", "postgres"),
    host=os.environ.get("DB_HOST", "localhost"),
    port=os.environ.get("DB_PORT", 5432),
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
cursor.execute("DELETE FROM haski_user")

conn.commit()
# Closing the connection
conn.close()
