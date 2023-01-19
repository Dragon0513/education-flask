from service_layer import unit_of_work
from domain.tutoringModel import graf
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from sqlalchemy.exc import IntegrityError


def create_course(
    uow: unit_of_work.AbstractUnitOfWork,
    name
) -> dict:
    with uow:
        course = DM.Course(name)
        uow.course.add_course(course)
        uow.commit()
        result = course.serialize()
    return result


def create_student(
    uow: unit_of_work.AbstractUnitOfWork,
    name,
    learning_style=None
) -> dict:
    with uow:
        student = LM.Student(name, learning_style)
        uow.student.add_student(student)
        uow.commit()
        result = student.serialize()
    return result


def create_element(
    uow: unit_of_work.AbstractUnitOfWork,
    name,
    classification,
    ancestor_id,
    order_depth,
    prerequisite_id=None
) -> dict:
    with uow:
        element = DM.LearningElement(
            name,
            classification,
            ancestor_id,
            prerequisite_id,
            order_depth)
        uow.learning_element.add_element(element)
        uow.commit()
        result = element.serialize()
        return result


def create_learning_path(
    uow: unit_of_work.AbstractUnitOfWork,
    student_id,
    course_id,
    order_depth,
    learning_style: dict = {"AKT": 0, "INT": 0, "VIS": 0, "GLO": 0},
    algorithm="Graf"
) -> dict:
    with uow:
        path = TM.LearningPath(student_id=student_id,
                               course_id=course_id, order_depth=order_depth)
        path.get_learning_path(
            student_id=student_id,
            learning_style=learning_style,
            algorithm=algorithm)
        uow.learning_path.add_learning_path(path)
        uow.commit()
        result = path.serialize()
        return result


def create_topic(
    uow: unit_of_work.AbstractUnitOfWork,
    name,
    course_id,
    order_depth,
    ancestor_id=None,
    prerequisite_id=None
) -> dict:
    with uow:
        topic = DM.Topic(name, course_id, ancestor_id,
                         prerequisite_id, order_depth)
        try:
            uow.topic.add_topic(topic)
            uow.commit()
            result = topic.serialize()
            return result
        except IntegrityError:
            return {'error':
                    'There is a foreign key violation for the course_id\
                         parameter. Please check again!'}


def delete_course(
    uow: unit_of_work.AbstractUnitOfWork,
    course_id
):
    with uow:
        uow.course.delete_course(course_id)
        uow.commit()


def delete_learning_element(
    uow: unit_of_work.AbstractUnitOfWork,
    element_id
):
    with uow:
        uow.learning_element.delete_learning_element(element_id)
        uow.commit()


def delete_student(
    uow: unit_of_work.AbstractUnitOfWork,
    student_id
):
    with uow:
        uow.student.delete_student(student_id)
        uow.commit()


def delete_topic(
    uow: unit_of_work.AbstractUnitOfWork,
    topic_id
):
    with uow:
        uow.topic.delete_topic(topic_id)
        uow.commit()


def get_learning_elements(
    uow: unit_of_work.AbstractUnitOfWork
) -> dict:
    with uow:
        elements = uow.learning_element.get_learning_elements()
        if elements == []:
            result = {}
        else:
            result = {}
            temp = []
            for element in elements:
                temp.append(element.serialize())
            result['learning_elements'] = temp
    return result


def get_learning_element_by_id(
    uow: unit_of_work.AbstractUnitOfWork,
    element_id
) -> dict:
    with uow:
        element = uow.learning_element.get_learning_element_by_id(element_id)
        if element == [] or element == [None]:
            result = {}
        else:
            result = element[0].serialize()
    return result


def get_learning_path(
    uow: unit_of_work.AbstractUnitOfWork,
    student_id,
    course_id,
    order_depth
) -> dict:
    with uow:
        path = uow.learning_path.get_learning_path(
            student_id, course_id, order_depth)
        if path == [] or path == [None]:
            result = {}
        else:
            result = path[0].serialize()
    return result


def get_courses(
    uow: unit_of_work.AbstractUnitOfWork
) -> dict:
    with uow:
        courses = uow.course.get_courses()
        if courses == []:
            result = {}
        else:
            result = {}
            temp = []
            for course in courses:
                temp.append(course.serialize())
            result['courses'] = temp
    return result


def get_course_by_id(
    uow: unit_of_work.AbstractUnitOfWork,
    course_id
) -> dict:
    with uow:
        course = uow.course.get_course_by_id(course_id)
        if course == [] or course == [None]:
            result = {}
        else:
            result = course[0].serialize()
    return result


def get_students(
    uow: unit_of_work.AbstractUnitOfWork
) -> dict:
    with uow:
        students = uow.student.get_students()
        if students == []:
            result = {}
        else:
            result = {}
            temp = []
            for student in students:
                temp.append(student.serialize())
            result['students'] = temp
    return result


def get_student_by_id(
    uow: unit_of_work.AbstractUnitOfWork,
    student_id
) -> dict:
    with uow:
        student = uow.student.get_student_by_id(student_id)
        if student == [] or student == [None]:
            result = {}
        else:
            result = student[0].serialize()
    return result


def get_topics(
    uow: unit_of_work.AbstractUnitOfWork
) -> dict:
    with uow:
        topics = uow.topic.get_topics()
        if topics == []:
            result = {}
        else:
            result = {}
            temp = []
            for topic in topics:
                temp.append(topic.serialize())
            result['topics'] = temp
    return result


def get_topics_for_course(
    uow: unit_of_work.AbstractUnitOfWork,
    course_id,
    order_depth
) -> dict:
    with uow:
        topics = uow.topic.get_topics_for_course(course_id, order_depth)
        if topics == []:
            result = {}
        else:
            result = {}
            temp = []
            for topic in topics:
                temp.append(topic.serialize())
            result['topics'] = temp
            result['course'] = course_id
    return result


def get_topics_for_course_and_ancestor(
    uow: unit_of_work.AbstractUnitOfWork,
    course_id,
    order_depth,
    ancestor_id
) -> dict:
    with uow:
        topics = uow.topic.get_topics_for_course_and_ancestor(
            course_id, order_depth, ancestor_id)
        if topics == []:
            result = {}
        else:
            result = {}
            temp = []
            for topic in topics:
                temp.append(topic.serialize())
            result['topics'] = temp
            result['course'] = course_id
    return result


def get_topic_by_id(
    uow: unit_of_work.AbstractUnitOfWork,
    topic_id
) -> dict:
    with uow:
        topic = uow.topic.get_topic_by_id(topic_id)
        if topic == [] or topic == [None]:
            result = {}
        else:
            result = topic[0].serialize()
    return result


def update_course(
    uow: unit_of_work.AbstractUnitOfWork,
    id,
    name
) -> DM.Course:
    with uow:
        course = DM.Course(name)
        uow.course.update_course(course, id)
        uow.commit()
        course.id = id
        result = course.serialize()
        return result


def update_learning_element(
    uow: unit_of_work.AbstractUnitOfWork,
    id,
    name,
    classification,
    ancestor_id,
    prerequisite_id,
    order_depth
) -> DM.LearningElement:
    with uow:
        learning_element = DM.LearningElement(
            name, classification, ancestor_id, prerequisite_id, order_depth)
        uow.learning_element.update_learning_element(learning_element, id)
        uow.commit()
        learning_element.id = id
        result = learning_element.serialize()
        return result


def update_student(
    uow: unit_of_work.AbstractUnitOfWork,
    id,
    name,
    learning_style
) -> LM.Student:
    with uow:
        student = LM.Student(name, learning_style)
        uow.student.update_student(student, id)
        uow.commit()
        student.id = id
        result = student.serialize()
        return result


def update_topic(
    uow: unit_of_work.AbstractUnitOfWork,
    id,
    name,
    course_id,
    order_depth,
    ancestor_id=None,
    prerequisite_id=None
) -> dict:
    with uow:
        topic = DM.Topic(name, course_id, ancestor_id,
                         prerequisite_id, order_depth)
        uow.topic.update_topic(topic, id)
        uow.commit()
        topic.id = id
        result = topic.serialize()
        return result
