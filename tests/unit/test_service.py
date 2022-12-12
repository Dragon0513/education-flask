import pytest
from repositories import repository
from service_layer import services, unit_of_work


test_course_name = "Test Course"
test_person_name = "Max Mustermann"
test_element_name = "Test Element"
test_topic_name = "Test Topic"


class FakeRepository(repository.AbstractRepository):
    def __init__(self, learning_path, course, element, student, topic):
        self.learning_path = set(learning_path)
        self.course = set(course)
        self.element = set(element)
        self.student = set(student)
        self.topic = set(topic)

    def add_learning_path(self, learning_path):
        learning_path.id = len(self.learning_path) + 1
        self.learning_path.add(learning_path)

    def add_course(self, course):
        course.id = len(self.course) + 1
        self.course.add(course)

    def add_element(self, element):
        element.id = len(self.element) + 1
        self.element.add(element)

    def add_student(self, student):
        student.id = len(self.student) + 1
        self.student.add(student)

    def add_topic(self, topic):
        topic.id = len(self.topic) + 1
        self.topic.add(topic)

    def get_learning_path(self, student_id, course_id, order_depth):
        result = next((p for p in self.learning_path if p.student_id == student_id and p.course_id ==
                      course_id and p.order_depth == order_depth), None)
        return [result]

    def get_learning_elements(self):
        return self.element

    def get_learning_element_by_id(self, element_id):
        element = next((p for p in self.element if p.id == element_id), None)
        return [element]

    def get_courses(self):
        return self.course

    def get_course_by_id(self, course_id):
        result = next((p for p in self.course if p.id == course_id), None)
        return [result]

    def get_students(self):
        return self.student

    def get_student_by_id(self, student_id):
        result = next((p for p in self.student if p.id == student_id), None)
        return [result]

    def get_topics(self):
        return self.topic

    def get_topics_for_course(self, course_id, order_depth):
        result = next((p for p in self.topic if p.course_id ==
                      course_id and p.order_depth == order_depth), None)
        return [result]

    def get_topics_for_course_and_ancestor(self,
                                           course_id,
                                           order_depth,
                                           ancestor_id):
        result = next((p for p in self.topic if p.course_id == course_id
                       and p.order_depth == order_depth
                       and p.ancestor_id == ancestor_id),
                      None)
        return [result]

    def get_topic_by_id(self, topic_id):
        result = next((p for p in self.topic if p.id == topic_id), None)
        if result is None:
            return []
        return [result]

    def update_student(self, student, id):
        to_remove = next((p for p in self.student if p.id == id), None)
        self.student.remove(to_remove)
        student.id = len(self.student)
        self.student.add(student)

    def update_topic(self, topic, id):
        to_remove = next((p for p in self.topic if p.id == id), None)
        self.topic.remove(to_remove)
        topic.id = len(self.topic)
        self.topic.add(topic)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.learning_path = FakeRepository([], [], [], [], [])
        self.course = FakeRepository([], [], [], [], [])
        self.student = FakeRepository([], [], [], [], [])
        self.topic = FakeRepository([], [], [], [], [])
        self.learning_element = FakeRepository([], [], [], [], [])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass #Just needed for working, has no function in test


def test_get_learning_path_for_learning_style():
    uow = FakeUnitOfWork()
    services.create_learning_path(uow=uow,
                                student_id=123,
                                course_id=1,
                                order_depth=3,
                                learning_style={
                                    "AKT": 5,
                                    "INT": 9,
                                    "VIS": 9,
                                    "GLO": 9
                                })
    result = services.get_learning_path(uow, 
                                student_id=123,
                                course_id=1,
                                order_depth=3)
    assert type(result) is dict
    assert result != {}


def test_get_learning_path_for_no_learning_style():
    uow = FakeUnitOfWork()
    learning_path = services.create_learning_path(uow=uow,
                                                  student_id=123,
                                                  course_id=1,
                                                  order_depth=3,)
    learning_path_expected = ['RQ, SE, FO, ZL, AN, UB, BE, AB, ZF']
    assert learning_path['path'] == ', '.join(learning_path_expected)


def test_add_course():
    uow = FakeUnitOfWork()
    course = services.create_course(
        uow=uow,
        name=test_course_name
    )
    assert type(course) is dict
    assert uow.learning_path.get_courses() is not None
    assert uow.committed


def test_add_student():
    uow = FakeUnitOfWork()
    student = services.create_student(
        uow=uow,
        name=test_person_name
    )
    assert type(student) is dict
    assert uow.student.get_students() is not None
    assert uow.committed


def test_add_element():
    uow = FakeUnitOfWork()
    element = services.create_element(
        uow=uow,
        name=test_element_name,
        classification="LK",
        ancestor_id=1,
        order_depth=2,
        prerequiste_id=None
    )
    assert type(element) is dict
    assert uow.learning_element.get_learning_elements() is not None
    assert uow.committed


def test_add_topic():
    uow = FakeUnitOfWork()
    topic = services.create_topic(
        uow=uow,
        name=test_topic_name,
        course_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    assert type(topic) is dict
    assert uow.topic.get_topics() is not None
    assert uow.committed


def test_get_learning_elements():
    uow = FakeUnitOfWork()
    services.create_element(
        uow=uow,
        name=test_element_name,
        classification="LK",
        ancestor_id=1,
        order_depth=2,
        prerequiste_id=None
    )
    result = services.get_learning_elements(uow)
    assert type(result) is dict
    assert result['learning_elements'] != []


def test_get_learning_elements_without_learning_elements():
    uow = FakeUnitOfWork()
    result = services.get_learning_elements(uow)
    assert type(result) is dict
    assert result is not None
    assert result['learning_elements'] == []


def test_get_learning_element_by_id():
    uow = FakeUnitOfWork()
    services.create_element(
        uow=uow,
        name=test_element_name,
        classification="LK",
        ancestor_id=1,
        order_depth=2,
        prerequiste_id=None
    )
    result = services.get_learning_element_by_id(uow, 1)
    assert type(result) is dict
    assert result['id'] == 1


def test_get_learning_element_by_id_with_wrong_id():
    uow = FakeUnitOfWork()
    result = services.get_learning_element_by_id(uow, 1)
    assert type(result) is dict
    assert result is not None
    assert result == {}


def test_get_courses():
    uow = FakeUnitOfWork()
    services.create_course(
        uow=uow,
        name=test_course_name
    )
    result = services.get_courses(uow)
    assert type(result) is dict
    assert result['courses'] != []


def test_get_courses_without_courses():
    uow = FakeUnitOfWork()
    result = services.get_courses(uow)
    assert type(result) is dict
    assert result is not None
    assert result['courses'] == []


def test_get_course_by_id():
    uow = FakeUnitOfWork()
    services.create_course(
        uow=uow,
        name=test_course_name
    )
    result = services.get_course_by_id(uow, 1)
    assert type(result) is dict
    assert result['id'] == 1


def test_get_course_by_id_with_wrong_id():
    uow = FakeUnitOfWork()
    result = services.get_course_by_id(uow, 1)
    assert type(result) is dict
    assert result is not None
    assert result == {}


def test_get_students():
    uow = FakeUnitOfWork()
    services.create_student(
        uow=uow,
        name=test_person_name
    )
    result = services.get_students(uow)
    assert type(result) is dict
    assert result['students'] != []


def test_get_students_without_students():
    uow = FakeUnitOfWork()
    result = services.get_students(uow)
    assert type(result) is dict
    assert result is not None
    assert result['students'] == []


def test_get_student_by_id():
    uow = FakeUnitOfWork()
    services.create_student(
        uow=uow,
        name=test_person_name
    )
    result = services.get_student_by_id(uow, 1)
    assert type(result) is dict
    assert result['id'] == 1


def test_get_student_by_id_with_wrong_id():
    uow = FakeUnitOfWork()
    result = services.get_student_by_id(uow, 1)
    assert type(result) is dict
    assert result is not None
    assert result == {}


def test_get_topics():
    uow = FakeUnitOfWork()
    services.create_topic(
        uow=uow,
        name=test_topic_name,
        course_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    result = services.get_topics(uow)
    assert type(result) is dict
    assert result['topics'] != []


def test_get_topics_without_topics():
    uow = FakeUnitOfWork()
    result = services.get_topics(uow)
    assert type(result) is dict
    assert result is not None
    assert result['topics'] == []


def test_get_topic_by_id():
    uow = FakeUnitOfWork()
    services.create_topic(
        uow=uow,
        name=test_topic_name,
        course_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    result = services.get_topic_by_id(uow, 1)
    assert type(result) is dict
    assert result is not None
    assert result['id'] == 1


def test_get_topic_by_id_with_wrong_id():
    uow = FakeUnitOfWork()
    result = services.get_topic_by_id(uow, 1)
    assert type(result) is dict
    assert result is not None
    assert result == {}


def test_update_student():
    uow = FakeUnitOfWork()
    services.create_student(
        uow=uow,
        name=test_person_name
    )
    result = services.update_student(
        uow=uow,
        id=1,
        name="Maria Musterfrau",
        learning_style=None
    )
    assert type(result) is dict
    assert result is not None
    assert result['id'] == 1
    assert result['name'] == "Maria Musterfrau"


def test_update_topic():
    uow = FakeUnitOfWork()
    services.create_topic(
        uow=uow,
        name=test_topic_name,
        course_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    result = services.update_topic(
        uow=uow,
        id=1,
        name="New Test Topic",
        course_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    assert type(result) is dict
    assert result is not None
    assert result['id'] == 1
    assert result['name'] == "New Test Topic"


def test_get_topic_by_course_order_depth():
    uow = FakeUnitOfWork()
    services.create_topic(
        uow=uow,
        name=test_topic_name,
        course_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    result = services.get_topics_for_course(uow, 1, 3)
    assert type(result) is dict
    assert result is not None
    assert result['topics'] != []
    assert result.keys() == {'course', 'topics'}
    assert result['topics'][0]['id'] == 1


def test_get_topic_by_course_order_depth_ancestor():
    uow = FakeUnitOfWork()
    services.create_topic(
        uow=uow,
        name=test_topic_name,
        course_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    result = services.get_topics_for_course_and_ancestor(uow, 1, 3, 2)
    assert type(result) is dict
    assert result is not None
    assert result['topics'] != []
    assert result['topics'][0]['id'] == 1
