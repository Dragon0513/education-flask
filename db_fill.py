import psycopg2
import os

# Establishing the connection
conn = psycopg2.connect(
    database=os.environ.get('DB_NAME', 'haski'),
    user='postgres',
    password=os.environ.get('DB_PASSWORD', 'genericPassword'),
    host=os.environ.get('DB_HOST', '127.0.0.1'),
    port=os.environ.get('DB_PORT', 5432)
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Fill Database with example data. Insert the following data into DB:

# Create admin user
sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Dimitri Bigler', 'HS-KE', 1, 'admin')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (1, 'light', 'admin')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO admin (user_id)
    VALUES (1)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('David Fischer', 'HS-KE', 2, 'admin')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (2, 'dark', 'admin')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO admin (user_id)
    VALUES (2)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jim Haug', 'HS-KE', 3, 'admin')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (3, 'Standard', 'admin')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO admin (user_id)
    VALUES (3)
'''
cursor.execute(sql)


# Create course creator user
sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Julian Manz', 'HS-KE', 4, 'course creator')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (4, 'light', 'course creator')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_creator (user_id)
    VALUES (4)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Marc Normann', 'HS-AS', 5, 'course creator')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (5, 'dark', 'course creator')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_creator (user_id)
    VALUES (5)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Gesine Wagner', 'HS-KE', 6, 'course creator')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (6, 'Standard', 'course creator')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_creator (user_id)
    VALUES (6)
'''
cursor.execute(sql)


# Create student user
sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Emily Johnson', 'HS-AS', 7, 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (7, 'light', 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO student (user_id)
    VALUES (7)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Liam Anderson', 'HS-KE', 8, 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (8, 'dark', 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO student (user_id)
    VALUES (8)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Sophia Martinez', 'HS-RE', 9, 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (9, 'Standard', 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO student (user_id)
    VALUES (9)
'''
cursor.execute(sql)


# Create teacher user
sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Emma Johnson', 'HS-AS', 10, 'teacher')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (10, 'light', 'teacher')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO teacher (user_id)
    VALUES (10)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Liam Smith', 'HS-KE', 11, 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (11, 'dark', 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO teacher (user_id)
    VALUES (11)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Sophia Martinez', 'HS-RE', 12, 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (12, 'Standard', 'student')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO teacher (user_id)
    VALUES (12)
'''
cursor.execute(sql)

#create courses

sql = '''
    INSERT INTO course (lms_id, name, university)
    VALUES (2, 'Software Engineering', 'HS-RE')   
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course (lms_id, name, university)
    VALUES (3, 'Software Architecture', 'HS-AS')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_creator_course (course_creator_id, course_id, created_at, last_updated)
    VALUES (1, 1, '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_creator_course (course_creator_id, course_id, created_at, last_updated)
    VALUES (2, 2, '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

# create topics

sql = '''
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (1, true, true, 'General', 'HS-KE', '', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (2, true, true, 'Metrics', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (3, true, true, 'Something Else', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (4, true, true, 'General', 'HS-AS', 'Marc Normann', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (5, true, true, 'Design Pattern', 'HS-AS', 'Marc Normann', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (6, true, false, 'Nothing else', 'HS-AS', 'Marc Normann', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 1)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 2)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 3)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 4)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 5)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 6)
'''
cursor.execute(sql)

# create learning elements

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (1, 'h5pactivity', 'KÜ', 'Introduction', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (2, 'h5pactivity', 'EK', 'General Something', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (3, 'h5pactivity', 'ÜB', 'Metric-1', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (4, 'h5pactivity', 'ÜB', 'Metric-2', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (5, 'h5pactivity', 'ÜB', 'Something-Else-1', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (6, 'h5pactivity', 'ÜB', 'Something-Else-2', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (7, 'h5pactivity', 'KÜ', 'Einführung', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (8, 'h5pactivity', 'ÜB', 'Design Pattern Allgemein', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (9, 'h5pactivity', 'ÜB', 'Design Pattern Erweitert', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (10, 'h5pactivity', 'ÜB', 'Übung - 1', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO learning_element (lms_id, activity_type, classification, name, university, created_by, created_at, last_updated)
    VALUES (11, 'h5pactivity', 'ÜB', 'Übung - 2', 'HS-KE', 'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (1, 1)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (1, 2)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 3)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 4)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (3, 5)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (3, 6)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (4, 7)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (5, 8)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (5, 9)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 10)
'''
cursor.execute(sql)

sql = '''
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 11)
'''
cursor.execute(sql)


conn.commit()
# Closing the connection
conn.close()