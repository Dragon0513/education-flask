import os

import psycopg2

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

# Fill Database with example data. Insert the following data into DB:

# Create admin user
sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Dimitri Bigler', 'HS-KE', 1, 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (1, 'light', 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO admin (user_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('David Fischer', 'HS-KE', 2, 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (2, 'dark', 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO admin (user_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jim Haug', 'HS-KE', 3, 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (3, 'Standard', 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO admin (user_id)
    VALUES (3)
"""
cursor.execute(sql)


# Create course creator user
sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Julian Manz', 'HS-KE', 4, 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (4, 'light', 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator (user_id)
    VALUES (4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Marc Normann', 'HS-AS', 5, 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (5, 'dark', 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator (user_id)
    VALUES (5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Gesine Wagner', 'HS-KE', 6, 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (6, 'Standard', 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator (user_id)
    VALUES (6)
"""
cursor.execute(sql)


# Create student user
sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Emily Johnson', 'HS-AS', 7, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (7, 'light', 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (7)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Liam Anderson', 'HS-KE', 8, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (8, 'dark', 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (8)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Sophia Martinez', 'HS-RE', 9, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (9, 'Standard', 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (9)
"""
cursor.execute(sql)


# Create teacher user
sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Emma Johnson', 'HS-AS', 10, 'teacher')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (10, 'light', 'teacher')
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher (user_id)
    VALUES (10)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Liam Smith', 'HS-KE', 11, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (11, 'dark', 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher (user_id)
    VALUES (11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Sophia Martinez', 'HS-RE', 12, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (12, 'Standard', 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher (user_id)
    VALUES (12)
"""
cursor.execute(sql)

# create courses
sql = """
    INSERT INTO course (lms_id, name, university)
    VALUES (2, 'Software Engineering', 'HS-RE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course (lms_id, name, university)
    VALUES (3, 'Software Architecture', 'HS-AS')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator_course (course_creator_id, course_id,\
    created_at, last_updated)
    VALUES (1, 1, '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator_course (course_creator_id, course_id,\
    created_at, last_updated)
    VALUES (2, 2, '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

# create topics
sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (1, true, true, 'General', 'HS-KE', '', '2023-07-13 16:00:00',\
    '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (2, true, true, 'Metrics', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (3, true, true, 'Something Else', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (4, true, true, 'General', 'HS-AS', 'Marc Normann',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (5, true, true, 'Design Pattern', 'HS-AS', 'Marc Normann',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (6, true, false, 'Nothing else', 'HS-AS', 'Marc Normann',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 6)
"""
cursor.execute(sql)

# create learning elements

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (1, 'h5pactivity', 'KÜ', 'Introduction', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (2, 'h5pactivity', 'EK', 'General Something', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (3, 'h5pactivity', 'ÜB', 'Metric-1', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (4, 'h5pactivity', 'ÜB', 'Metric-2', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (5, 'h5pactivity', 'ÜB', 'Something-Else-1', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (6, 'h5pactivity', 'ÜB', 'Something-Else-2', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (7, 'h5pactivity', 'KÜ', 'Einführung', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (8, 'h5pactivity', 'ÜB', 'Design Pattern Allgemein', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (9, 'h5pactivity', 'ÜB', 'Design Pattern Erweitert', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (10, 'h5pactivity', 'ÜB', 'Übung - 1', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (11, 'h5pactivity', 'ÜB', 'Übung - 2', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (1, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (1, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (3, 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (3, 6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (4, 7)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (5, 8)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (5, 9)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 10)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 11)
"""
cursor.execute(sql)

# create Learning Element rating
sql = """
    INSERT INTO learning_element_rating (learning_element_id, rating, message,\
    date)
    VALUES (1, 5, 'Sehr Gut', '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element_rating (learning_element_id, rating, message,\
    date)
    VALUES (2, 4, 'Gut', '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element_rating (learning_element_id, rating, message,\
    date)
    VALUES (3, 3, 'Befriedigend', '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element_rating (learning_element_id, rating, message,\
    date)
    VALUES (4, 2, 'Ausreichend', '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element_rating (learning_element_id, rating, message,\
    date)
    VALUES (5, 1, 'Mangelhaft', '2023-07-13 16:00:00')
"""
cursor.execute(sql)

# create contactform
sql = """
    INSERT INTO contact_form (user_id, report_topic, report_type, date)
    VALUES (1, 'General Error', 'Elemente werden nicht angezeigt',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO contact_form (user_id, report_topic, report_type, date)
    VALUES (2, 'Bug', 'Wenn ich auf Button klicke, dann...',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO contact_form (user_id, report_topic, report_type, date)
    VALUES (3, 'Feedback', 'Übersicht verbessern', '2023-07-13 16:00:00')
"""
cursor.execute(sql)

# Add student to course
sql = """
    INSERT INTO student_course (student_id, course_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (1, 1, 'act', 7, 'Sensory', 5, 'vis', 11, 'seq', 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course (student_id, course_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (2, 1, 'ref', 3, 'int', 7, 'vrb', 5, 'glb', 11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course (student_id, course_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (2, 2, 'ref', 9, 'int', 3, 'vrb', 11, 'glb', 11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course (student_id, course_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (3, 2, 'act', 7, 'int', 3, 'vis', 7, 'glb', 11)
"""
cursor.execute(sql)


# Add teacher to course
sql = """
    INSERT INTO teacher_course (teacher_id, course_id)
    VALUES (1, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher_course (teacher_id, course_id)
    VALUES (2, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher_course (teacher_id, course_id)
    VALUES (3, 2)
"""
cursor.execute(sql)

# Add learning path to course / topic path
sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (1, 1, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (1, 2, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (2, 1, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (2, 2, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (3, 1, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (3, 2, 'aco')
"""
cursor.execute(sql)

# Add learning path to course / element path
sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 1, 'aco', 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 1, 'aco', 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 1, 'aco', 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 2, 'aco', 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 2, 'aco', 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 2, 'aco', 6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 1, 'aco', 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 1, 'aco', 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 1, 'aco', 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 2, 'aco', 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 2, 'aco', 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 2, 'aco', 6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 1, 'aco', 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 1, 'aco', 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 1, 'aco', 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 2, 'aco', 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 2, 'aco', 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 2, 'aco', 6)
"""
cursor.execute(sql)

# Topic path
sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (1, 1, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (2, 1, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (3, 1, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (4, 2, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (5, 2, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (6, 2, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (1, 3, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (2, 3, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (3, 3, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (4, 4, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (5, 4, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (6, 4, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (1, 5, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (2, 5, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (3, 5, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (4, 6, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (5, 6, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (6, 6, false, 3)
"""
cursor.execute(sql)

# Element Path
sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (1, 7, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (2, 7, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (3, 8, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (4, 8, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (5, 9, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (6, 9, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (7, 10, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (8, 11, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (9, 11, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (10, 11, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (11, 12, false, 4)
"""
cursor.execute(sql)

###
sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (1, 13, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (2, 13, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (3, 14, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (4, 14, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (5, 15, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (6, 15, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (7, 16, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (8, 17, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (9, 17, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (10, 17, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (11, 17, false, 4)
"""
cursor.execute(sql)

###

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (1, 19, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (2, 19, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (3, 20, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (4, 20, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (5, 21, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (6, 21, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (7, 22, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (8, 23, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (9, 23, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (10, 23, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (11, 23, false, 4)
"""
cursor.execute(sql)

# create Student visited learning element
sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 1, '2023-07-14 14:03:30', '2023-07-14 15:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 2, '2023-07-14 15:05:45', '2023-07-14 15:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 3, '2023-07-14 15:45:45', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 4, '2023-07-14 16:05:45', '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 5, '2023-07-14 16:45:45', '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 6, '2023-07-14 17:05:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 7, '2023-07-14 17:45:45', '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 8, '2023-07-14 18:05:45', '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 9, '2023-07-15 08:45:45', '2023-07-15 09:55:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 10, '2023-07-15 09:55:45', '2023-07-15 15:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 11, '2023-07-16 14:03:30', '2023-07-16 14:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 1, '2023-07-14 16:03:30', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 2, '2023-07-14 15:05:45', '2023-07-14 15:30:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 3, '2023-07-14 16:05:45', '2023-07-14 16:07:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 4, '2023-07-14 16:07:45', '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 5, '2023-07-14 16:45:45', '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 6, '2023-07-14 17:05:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 7, '2023-07-14 17:45:45', '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 8, '2023-07-14 18:05:45', '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 1, '2023-07-14 16:03:30', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 2, '2023-07-14 15:05:45', '2023-07-14 15:30:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 5, '2023-07-14 16:45:45', '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 6, '2023-07-14 17:05:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 8, '2023-07-14 20:05:45', '2023-07-14 21:45:45')
"""
cursor.execute(sql)

# create Student completed learning element
sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 1, true, '2023-07-14 15:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 2, true, '2023-07-14 15:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 3, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 4, true, '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 5, true, '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 6, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 7, true, '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 8, true, '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 9, true, '2023-07-15 9:55:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 10, true, '2023-07-15 15:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 11, true, '2023-07-16 14:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 1, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 2, true, '2023-07-14 15:30:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 3, true, '2023-07-14 16:07:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 4, true, '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 5, true, '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 6, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 7, true, '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 8, true, '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 1, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 2, true, '2023-07-14 15:30:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 5, true, '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 6, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 8, true, '2023-07-14 21:45:45')
"""
cursor.execute(sql)

# Student visited topic
sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 1, '2023-07-14 14:03:30', '2023-07-14 15:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 2, '2023-07-14 15:45:45', '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 3, '2023-07-14 16:45:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 4, '2023-07-14 17:45:45', '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 5, '2023-07-14 18:05:45', '2023-07-16 14:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 6, '2023-07-16 14:05:45', '2023-07-16 14:05:47')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 1, '2023-07-14 15:05:45', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 2, '2023-07-14 16:05:45', '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 3, '2023-07-14 16:45:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 4, '2023-07-14 17:45:45', '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 5, '2023-07-14 18:05:45', '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (3, 1, '2023-07-14 15:05:45', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (3, 3, '2023-07-14 16:45:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (3, 5, '2023-07-14 20:05:45', '2023-07-14 21:45:45')
"""
cursor.execute(sql)

# Student completed topic
sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 1, true, '2023-07-14 15:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 2, true, '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 3, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 4, true, '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 5, true, '2023-07-16 14:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 6, true, '2023-07-16 14:05:47')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 1, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 2, true, '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 3, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 4, true, '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 5, true, '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (3, 1, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (3, 3, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (3, 5, true, '2023-07-14 21:45:45')
"""
cursor.execute(sql)

# create learning_characteristics
sql = """
    INSERT INTO learning_characteristics (student_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_characteristics (student_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_characteristics (student_id)
    VALUES (3)
"""
cursor.execute(sql)

# create learning_strategy
sql = """
    INSERT INTO learning_strategy (characteristic_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_strategy (characteristic_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_strategy (characteristic_id)
    VALUES (3)
"""
cursor.execute(sql)

# create learning_style
sql = """
    INSERT INTO learning_style (characteristic_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (1, 'sns', 7, 'vis', 3, 'act', 9, 'seq', 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_style (characteristic_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (2, 'sns', 7, 'vis', 5, 'act', 11, 'glb', 11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_style (characteristic_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (3, 'sns', 1, 'vrb', 11, 'ref', 3, 'glb', 1)
"""
cursor.execute(sql)

# create ils questionnaire answers
sql = """
    INSERT INTO questionnaire (student_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_input_answers (questionnaire_id, vv_1_f3, vv_2_f7,\
    vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, vv_7_f27, vv_8_f31, vv_9_f35,\
    vv_10_f39, vv_11_f43)
    VALUES (1, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_perception_answers (questionnaire_id, si_1_f2, si_2_f6,\
    si_3_f10, si_4_f14, si_5_f18, si_6_f22, si_7_f26, si_8_f30, si_9_f34,\
     si_10_f38, si_11_f42)
    VALUES (1, 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_processing_answers (questionnaire_id, ar_1_f1, ar_2_f5,\
    ar_3_f9, ar_4_f13, ar_5_f17, ar_6_f21, ar_7_f25, ar_8_f29, ar_9_f33,\
    ar_10_f37, ar_11_f41)
    VALUES (1, 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_understanding_answers (questionnaire_id, sg_1_f4, sg_2_f8,\
    sg_3_f12, sg_4_f16, sg_5_f20, sg_6_f24, sg_7_f28, sg_8_f32, sg_9_f36,\
    sg_10_f40, sg_11_f44)
    VALUES (1, 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO questionnaire (student_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_input_answers (questionnaire_id, vv_1_f3, vv_2_f7,\
    vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, vv_7_f27, vv_8_f31, vv_9_f35,\
    vv_10_f39, vv_11_f43)
    VALUES (2, 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_perception_answers (questionnaire_id, si_1_f2, si_2_f6,\
    si_3_f10, si_4_f14, si_5_f18, si_6_f22, si_7_f26, si_8_f30, si_9_f34,\
    si_10_f38, si_11_f42)
    VALUES (2, 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_processing_answers (questionnaire_id, ar_1_f1, ar_2_f5,\
    ar_3_f9, ar_4_f13, ar_5_f17, ar_6_f21, ar_7_f25, ar_8_f29, ar_9_f33,\
    ar_10_f37, ar_11_f41)
    VALUES (2, 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_understanding_answers (questionnaire_id, sg_1_f4, sg_2_f8,\
    sg_3_f12, sg_4_f16, sg_5_f20, sg_6_f24, sg_7_f28, sg_8_f32, sg_9_f36,\
    sg_10_f40, sg_11_f44)
    VALUES (2, 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO questionnaire (student_id)
    VALUES (3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_input_answers (questionnaire_id, vv_1_f3, vv_2_f7,\
    vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, vv_7_f27, vv_8_f31, vv_9_f35,\
    vv_10_f39, vv_11_f43)
    VALUES (3, 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_perception_answers (questionnaire_id, si_1_f2, si_2_f6,\
    si_3_f10, si_4_f14, si_5_f18, si_6_f22, si_7_f26, si_8_f30, si_9_f34,\
    si_10_f38, si_11_f42)
    VALUES (3, 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_processing_answers (questionnaire_id, ar_1_f1, ar_2_f5,\
    ar_3_f9, ar_4_f13, ar_5_f17, ar_6_f21, ar_7_f25, ar_8_f29, ar_9_f33,\
    ar_10_f37, ar_11_f41)
    VALUES (3, 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_understanding_answers (questionnaire_id, sg_1_f4, sg_2_f8,\
    sg_3_f12, sg_4_f16, sg_5_f20, sg_6_f24, sg_7_f28, sg_8_f32, sg_9_f36,\
    sg_10_f40, sg_11_f44)
    VALUES (3, 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
"""
cursor.execute(sql)

# Create questionnaire list k
sql = """
    INSERT INTO list_k (questionnaire_id, org1_f1, org2_f2, org3_f3, ela1_f4,\
    ela2_f5, ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10, wie2_f11, wie3_f12,\
    zp1_f13, zp2_f14, zp3_f15, kon1_f16, kon2_f17, kon3_f18, reg1_f19,\
    reg2_f20, reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25, ans2_f26,\
    ans3_f27, zei1_f28, zei2_f29, zei3_f30, lms1_f31, lms2_f32, lms3_f33,\
    lit1_f34, lit2_f35, lit3_f36, lu1_f37, lu2_f38, lu3_f39)
    VALUES (1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,\
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO list_k (questionnaire_id, org1_f1, org2_f2, org3_f3, ela1_f4,\
    ela2_f5, ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10, wie2_f11, wie3_f12,\
    zp1_f13, zp2_f14, zp3_f15, kon1_f16, kon2_f17, kon3_f18, reg1_f19,\
    reg2_f20, reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25, ans2_f26,\
    ans3_f27, zei1_f28, zei2_f29, zei3_f30, lms1_f31, lms2_f32, lms3_f33,\
    lit1_f34, lit2_f35, lit3_f36, lu1_f37, lu2_f38, lu3_f39)
    VALUES (2, 3, 5, 3, 1, 1, 2, 3, 3, 5, 3, 4, 3, 3, 1, 2, 3, 5, 3, 4, 3, 2,\
    3, 1, 3, 5, 3, 1, 3, 3, 3, 2, 3, 5, 3, 5, 3, 1, 3, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO list_k (questionnaire_id, org1_f1, org2_f2, org3_f3, ela1_f4,\
    ela2_f5, ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10, wie2_f11, wie3_f12,\
    zp1_f13, zp2_f14, zp3_f15, kon1_f16, kon2_f17, kon3_f18, reg1_f19,\
    reg2_f20, reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25, ans2_f26,\
    ans3_f27, zei1_f28, zei2_f29, zei3_f30, lms1_f31, lms2_f32, lms3_f33,\
    lit1_f34, lit2_f35, lit3_f36, lu1_f37, lu2_f38, lu3_f39)
    VALUES (3, 1, 1, 3, 1, 1, 2, 3, 3, 5, 3, 4, 3, 3, 1, 2, 3, 5, 3, 4, 3, 2,\
    3, 1, 3, 5, 3, 1, 3, 3, 3, 2, 3, 5, 3, 5, 4, 5, 5, 1)
"""
cursor.execute(sql)

# Create Knowledge
sql = """
    INSERT INTO knowledge (characteristic_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO knowledge (characteristic_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO knowledge (characteristic_id)
    VALUES (3)
"""
cursor.execute(sql)

# Create Learning analytics
sql = """
    INSERT INTO learning_analytics (characteristic_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_analytics (characteristic_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_analytics (characteristic_id)
    VALUES (3)
"""
cursor.execute(sql)


conn.commit()
# Closing the connection
conn.close()
