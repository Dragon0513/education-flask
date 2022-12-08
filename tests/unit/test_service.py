import pytest
from repositories import repository
from service_layer import services, unit_of_work


class FakeRepository(repository.AbstractRepository):
    def __init__(self, learning_path, course, element, student, topic):
        self.learning_path = set(learning_path)
        self.course = set(course)
        self.element = set(element)
        self.student = set(student)
        self.topic = set(topic)

    def add(self, learning_path):
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

    def get(self, id):
        return next((p for p in self.learning_path if p.id == id), None)

    def get_learning_elements(self):
        return self.element

    def get_learning_element_by_id(self, element_id):
        element = next((p for p in self.element if p.id == element_id), None)
        return [element]

    def get_modules(self):
        return self.course

    def get_module_by_id(self, module_id):
        result = next((p for p in self.course if p.id == module_id), None)
        return [result]

    def get_students(self):
        return self.student

    def get_student_by_id(self, student_id):
        result = next((p for p in self.student if p.id == student_id), None)
        return [result]

    def get_topics(self):
        return self.topic

    def get_topics_for_module(self, module_id, order_depth):
        result = next((p for p in self.topic if p.module_id ==
                      module_id and p.order_depth == order_depth), None)
        return [result]

    def get_topics_for_module_and_ancestor(self,
                                           module_id,
                                           order_depth,
                                           ancestor_id):
        result = next((p for p in self.topic if p.module_id == module_id
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
        self.module = FakeRepository([], [], [], [], [])
        self.student = FakeRepository([], [], [], [], [])
        self.topic = FakeRepository([], [], [], [], [])
        self.learning_element = FakeRepository([], [], [], [], [])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_get_learning_path_for_learning_style():
    uow = FakeUnitOfWork()
    learning_path = services.get_learning_path(uow=uow,
                                               student_id=123,
                                               learning_style={
                                                   "AKT": 5,
                                                   "INT": 9,
                                                   "VIS": 9,
                                                   "GLO": 9
                                               })
    learning_path_expected = ['ZF', 'UB', 'SE', 'AN',
                              'RQ', 'AB', 'ZL', 'BE', 'FO']
    assert learning_path == ', '.join(learning_path_expected)


def test_get_learning_path_for_no_learning_style():
    uow = FakeUnitOfWork()
    learning_path = services.get_learning_path(uow=uow, student_id=123)
    learning_path_expected = ['RQ', 'SE', 'FO', 'ZL',
                              'AN', 'UB', 'BE', 'AB', 'ZF']
    assert learning_path == ', '.join(learning_path_expected)


def test_add_course():
    uow = FakeUnitOfWork()
    course = services.create_course(
        uow=uow,
        name="Test Course"
    )
    assert type(course) is dict
    assert uow.learning_path.get_modules() is not None
    assert uow.committed


def test_add_student():
    uow = FakeUnitOfWork()
    student = services.create_student(
        uow=uow,
        name="Max Mustermann"
    )
    assert type(student) is dict
    assert uow.student.get_students() is not None
    assert uow.committed


def test_add_element():
    uow = FakeUnitOfWork()
    element = services.create_element(
        uow=uow,
        name="Test Element",
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
        name="Test Topic",
        module_id=1,
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
        name="Test Element",
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
        name="Test Element",
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


def test_get_modules():
    uow = FakeUnitOfWork()
    services.create_course(
        uow=uow,
        name="Test Course"
    )
    result = services.get_modules(uow)
    assert type(result) is dict
    assert result['modules'] != []


def test_get_modules_without_modules():
    uow = FakeUnitOfWork()
    result = services.get_modules(uow)
    assert type(result) is dict
    assert result is not None
    assert result['modules'] == []


def test_get_module_by_id():
    uow = FakeUnitOfWork()
    services.create_course(
        uow=uow,
        name="Test Course"
    )
    result = services.get_module_by_id(uow, 1)
    assert type(result) is dict
    assert result['id'] == 1


def test_get_module_by_id_with_wrong_id():
    uow = FakeUnitOfWork()
    result = services.get_module_by_id(uow, 1)
    assert type(result) is dict
    assert result is not None
    assert result == {}


def test_get_students():
    uow = FakeUnitOfWork()
    services.create_student(
        uow=uow,
        name="Max Mustermann"
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
        name="Max Mustermann"
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
        name="Test Topic",
        module_id=1,
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
        name="Test Topic",
        module_id=1,
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
        name="Max Mustermann"
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
        name="Test Topic",
        module_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    result = services.update_topic(
        uow=uow,
        id=1,
        name="New Test Topic",
        module_id=1,
        order_depth=3,
        ancestor_id=2,
        prerequisite_id=None
    )
    assert type(result) is dict
    assert result is not None
    assert result['id'] == 1
    assert result['name'] == "New Test Topic"
