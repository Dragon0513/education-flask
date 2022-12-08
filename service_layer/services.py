from service_layer import unit_of_work
from domain.tutoringModel import learning_path
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from sqlalchemy.exc import IntegrityError


def create_course(
    uow: unit_of_work.AbstractUnitOfWork,
    name
) -> dict:
    with uow:
        course = DM.Module(name)
        uow.module.add_course(course)
        uow.commit()
        result = course.serialize()
    return result


def create_student(
    uow: unit_of_work.AbstractUnitOfWork,
    name
) -> dict:
    with uow:
        student = LM.Student(name, None)
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
    prerequiste_id=None
) -> dict:
    with uow:
        try:
            element = DM.LearningElement(
                name,
                classification,
                ancestor_id,
                prerequiste_id,
                order_depth)
            uow.learning_element.add_element(element)
            uow.commit()
            result = element.serialize()
            return result
        except IntegrityError as e:
            return e


def create_topic(
    uow: unit_of_work.AbstractUnitOfWork,
    name,
    module_id,
    order_depth,
    ancestor_id=None,
    prerequisite_id=None
) -> dict:
    with uow:
        topic = DM.Topic(name, module_id, ancestor_id,
                         prerequisite_id, order_depth)
        try:
            uow.topic.add_topic(topic)
            uow.commit()
            result = topic.serialize()
            return result
        except IntegrityError as e:
            return {'error':
                    'There is a foreign key violation for the module_id\
                         parameter. Please check again!'}


def get_learning_path(
    uow: unit_of_work.AbstractUnitOfWork,
    student_id,
    learning_style: dict = {"AKT": 0, "INT": 0, "VIS": 0, "GLO": 0}
) -> str:
    with uow:
        path = learning_path.LearningPath(
            student_id=student_id, learning_style=learning_style)
        result = ', '.join(path.learning_path)
        if type(result) != "":
            uow.learning_path.add(path)
            uow.commit()
    return result


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


def get_modules(
    uow: unit_of_work.AbstractUnitOfWork
) -> dict:
    with uow:
        modules = uow.module.get_modules()
        if modules == []:
            result = {}
        else:
            result = {}
            temp = []
            for module in modules:
                temp.append(module.serialize())
            result['modules'] = temp
    return result


def get_module_by_id(
    uow: unit_of_work.AbstractUnitOfWork,
    module_id
) -> dict:
    with uow:
        module = uow.module.get_module_by_id(module_id)
        if module == [] or module == [None]:
            result = {}
        else:
            result = module[0].serialize()
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


def get_topics_for_module(
    uow: unit_of_work.AbstractUnitOfWork,
    module_id,
    order_depth
) -> dict:
    with uow:
        topics = uow.topic.get_topics_for_module(module_id, order_depth)
        if topics == []:
            result = {}
        else:
            result = {}
            temp = []
            for topic in topics:
                temp.append(topic.serialize())
            result['topics'] = temp
            result['module'] = module_id
    return result


def get_topics_for_module_and_ancestor(
    uow: unit_of_work.AbstractUnitOfWork,
    module_id,
    order_depth,
    ancestor_id
) -> dict:
    with uow:
        topics = uow.topic.get_topics_for_module_and_ancestor(
            module_id, order_depth, ancestor_id)
        if topics == []:
            result = {}
        else:
            result = {}
            temp = []
            for topic in topics:
                temp.append(topic.serialize())
            result['topics'] = temp
            result['module'] = module_id
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
    module_id,
    order_depth,
    ancestor_id=None,
    prerequisite_id=None
) -> dict:
    with uow:
        topic = DM.Topic(name, module_id, ancestor_id,
                         prerequisite_id, order_depth)
        uow.topic.update_topic(topic, id)
        uow.commit()
        topic.id = id
        result = topic.serialize()
        return result
