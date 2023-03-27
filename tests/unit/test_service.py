import pytest
from repositories import repository
from service_layer import services, unit_of_work
from domain.userAdministartion import model as UA
from domain.learnersModel import model as LM


class FakeRepository(repository.AbstractRepository):
    def __init__(self,
                 user=[],
                 settings=[],
                 admin=[],
                 course_creator=[],
                 teacher=[],
                 student=[],
                 learning_characteristics=[],
                 learning_style=[],
                 learning_strategy=[],
                 knowledge=[],
                 learning_analytics=[]):
        self.user = set(user)
        self.settings = set(settings)
        self.admin = set(admin)
        self.course_creator = set(course_creator)
        self.teacher = set(teacher)
        self.student = set(student)
        self.learning_characteristics = set(learning_characteristics)
        self.learning_style = set(learning_style)
        self.learning_strategy = set(learning_strategy)
        self.knowledge = set(knowledge)
        self.learning_analytics = set(learning_analytics)

    def create_admin(self, admin):
        admin.id = len(self.admin) + 1
        self.admin.add(admin)

    def create_course_creator(self, course_creator):
        course_creator.id = len(self.course_creator) + 1
        self.course_creator.add(course_creator)

    def create_knowledge(self, knowledge):
        knowledge.id = len(self.knowledge) + 1
        self.knowledge.add(knowledge)

    def create_learning_analytics(self, learning_analytics):
        learning_analytics.id = len(self.learning_analytics) + 1
        self.learning_analytics.add(learning_analytics)

    def create_learning_characteristics(self, learning_characteristics):
        learning_characteristics.id = len(self.learning_characteristics) + 1
        self.learning_characteristics.add(learning_characteristics)

    def create_learning_strategy(self, learning_strategy):
        learning_strategy.id = len(self.learning_strategy) + 1
        self.learning_strategy.add(learning_strategy)

    def create_learning_style(self, learning_style):
        learning_style.id = len(self.learning_style) + 1
        self.learning_style.add(learning_style)

    def create_settings(self, settings):
        settings.id = len(self.settings) + 1
        self.settings.add(settings)

    def create_student(self, student):
        student.id = len(self.student) + 1
        self.student.add(student)

    def create_teacher(self, teacher):
        teacher.id = len(self.teacher) + 1
        self.teacher.add(teacher)

    def create_user(self, user):
        user.id = len(self.user) + 1
        self.user.add(user)

    def delete_admin(self, user_id):
        to_remove = next((p for p in self.admin if p.user_id == user_id), None)
        self.admin.remove(to_remove)

    def delete_course_creator(self, user_id):
        to_remove = next(
            (p for p in self.course_creator if p.user_id == user_id), None)
        self.course_creator.remove(to_remove)

    def delete_knowledge(self, characteristic_id):
        to_remove = next(
            (p for p in self.knowledge
             if p.characteristic_id == characteristic_id), None)
        self.knowledge.remove(to_remove)

    def delete_learning_analytics(self, characteristic_id):
        to_remove = next(
            (p for p in self.learning_analytics
             if p.characteristic_id == characteristic_id), None)
        self.learning_analytics.remove(to_remove)

    def delete_learning_characteristics(self, student_id):
        to_remove = next(
            (p for p in self.learning_characteristics
             if p.student_id == student_id), None)
        self.learning_characteristics.remove(to_remove)

    def delete_learning_strategy(self, characteristic_id):
        to_remove = next(
            (p for p in self.learning_strategy
             if p.characteristic_id == characteristic_id), None)
        self.learning_strategy.remove(to_remove)

    def delete_learning_style(self, characteristic_id):
        to_remove = next(
            (p for p in self.learning_style
             if p.characteristic_id == characteristic_id), None)
        self.learning_style.remove(to_remove)

    def delete_settings(self, user_id):
        to_remove = next(
            (p for p in self.settings if p.user_id == user_id), None)
        self.settings.remove(to_remove)

    def delete_student(self, user_id):
        to_remove = next(
            (p for p in self.student if p.user_id == user_id), None)
        self.student.remove(to_remove)

    def delete_teacher(self, user_id):
        to_remove = next(
            (p for p in self.teacher if p.user_id == user_id), None)
        self.teacher.remove(to_remove)

    def delete_user(self, user_id, lms_user_id):
        to_remove = next((p for p in self.user if p.id ==
                         user_id and p.lms_user_id == lms_user_id), None)
        self.user.remove(to_remove)

    def get_admin_by_id(self, user_id):
        result = next((p for p in self.admin if
                       p.user_id == user_id), None)
        return [result]

    def get_admins_by_uni(self, university):
        result = next((p for p in self.admin if
                       p.university == university), None)
        return [result]

    def get_course_creator_by_id(self,
                                 user_id):
        result = next((p for p in self.course_creator if
                       p.user_id == user_id), None)
        return [result]

    def get_course_creators_by_uni(self, university):
        result = next((p for p in self.course_creator if
                       p.university == university), None)
        return [result]

    def get_knowledge(self, characteristic_id):
        result = next((p for p in self.knowledge if
                       p.characteristic_id == characteristic_id), None)
        return [result]

    def get_learning_analytics(self, characteristic_id):
        result = next((p for p in self.learning_analytics if
                       p.characteristic_id == characteristic_id), None)
        return [result]

    def get_learning_characteristics(self, student_id):
        result = next((p for p in self.learning_characteristics if
                       p.student_id == student_id), None)
        return [result]

    def get_learning_strategy(self, characteristic_id):
        result = next((p for p in self.learning_strategy if
                       p.characteristic_id == characteristic_id), None)
        return [result]

    def get_learning_style(self, characteristic_id):
        result = next((p for p in self.learning_style if
                       p.characteristic_id == characteristic_id), None)
        return [result]

    def get_settings(self, user_id):
        result = next((p for p in self.settings if
                       p.user_id == user_id), None)
        return [result]

    def get_student_by_id(self, user_id):
        result = next((p for p in self.student if
                       p.user_id == user_id), None)
        return [result]

    def get_students_by_uni(self, university):
        result = next((p for p in self.student if
                       p.university == university), None)
        return [result]

    def get_teacher_by_id(self, user_id):
        result = next((p for p in self.teacher if
                       p.user_id == user_id), None)
        return [result]

    def get_teacher_by_uni(self, university):
        result = next((p for p in self.teacher if
                       p.university == university), None)
        return [result]

    def get_user_by_id(self, user_id, lms_user_id):
        result = next((p for p in self.user if
                       p.id == user_id and
                       p.lms_user_id == lms_user_id), None)
        return [result]

    def get_users_by_uni(self, university):
        result = next((p for p in self.user if
                       p.university == university), None)
        return [result]

    def update_knowledge(self, characteristic_id, knowledge):
        to_remove = next(
            (p for p in self.knowledge
             if p.characteristic_id == characteristic_id), None)
        self.knowledge.remove(to_remove)
        knowledge.id = len(self.knowledge)
        self.knowledge.add(knowledge)

    def update_learning_analytics(self, characteristic_id, learning_analytics):
        to_remove = next(
            (p for p in self.learning_analytics
             if p.characteristic_id == characteristic_id), None)
        self.learning_analytics.remove(to_remove)
        learning_analytics.id = len(self.learning_analytics)
        self.learning_analytics.add(learning_analytics)

    def update_learning_strategy(self, characteristic_id, learning_strategy):
        to_remove = next(
            (p for p in self.learning_strategy
             if p.characteristic_id == characteristic_id), None)
        self.learning_strategy.remove(to_remove)
        learning_strategy.id = len(self.learning_strategy)
        self.learning_strategy.add(learning_strategy)

    def update_learning_style(self, characteristic_id, learning_style):
        to_remove = next(
            (p for p in self.learning_style
             if p.characteristic_id == characteristic_id), None)
        self.learning_style.remove(to_remove)
        learning_style.id = len(self.learning_style)
        self.learning_style.add(learning_style)

    def update_settings(self, user_id, settings):
        to_remove = next(
            (p for p in self.settings if p.user_id == user_id), None)
        self.settings.remove(to_remove)
        settings.id = len(self.settings)
        self.settings.add(settings)

    def update_user(self, user_id, lms_user_id, user):
        to_remove = next((p for p in self.user if p.id == user_id
                          and p.lms_user_id == lms_user_id), None)
        self.user.remove(to_remove)
        user.id = len(self.user)
        self.user.add(user)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.user = FakeRepository()
        self.settings = FakeRepository()
        self.admin = FakeRepository()
        self.course_creator = FakeRepository()
        self.teacher = FakeRepository()
        self.student = FakeRepository()
        self.learning_characteristics = FakeRepository()
        self.learning_style = FakeRepository()
        self.learning_strategy = FakeRepository()
        self.knowledge = FakeRepository()
        self.learning_analytics = FakeRepository()
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass  # Just needed for working, has no function in test


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "admin"
    )
])
def test_create_admin(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.admin.admin)
    user = UA.User(
        name,
        university,
        lms_user_id,
        role
    )
    result = services.create_admin(
        uow=uow,
        user=user
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.admin.admin)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "course_creator"
    )
])
def test_create_course_creator(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.course_creator.course_creator)
    user = UA.User(
        name,
        university,
        lms_user_id,
        role
    )
    result = services.create_course_creator(
        uow=uow,
        user=user
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.course_creator.course_creator)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("user_id", [
    # Working Example
    (
        1
    )
])
def test_create_settings(user_id):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.settings.settings)
    result = services.create_settings(
        uow=uow,
        user_id=user_id
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.settings.settings)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    )
])
def test_create_student(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    student_entries_beginning = len(uow.student.student)
    characteristic_entries_beginning = len(
        uow.learning_characteristics.learning_characteristics)
    style_entries_beginning = len(uow.learning_style.learning_style)
    user = UA.User(
        name,
        university,
        lms_user_id,
        role
    )
    result = services.create_student(
        uow=uow,
        user=user
    )
    assert type(result) is dict
    assert result != {}
    student_entries_after = len(uow.student.student)
    characteristic_entries_after = len(
        uow.learning_characteristics.learning_characteristics)
    style_entries_after = len(uow.learning_style.learning_style)
    assert student_entries_beginning + 1 == student_entries_after
    assert characteristic_entries_beginning + 1 == characteristic_entries_after
    assert style_entries_beginning + 1 == style_entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "teacher"
    )
])
def test_create_teacher(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.teacher.teacher)
    user = UA.User(
        name,
        university,
        lms_user_id,
        role
    )
    result = services.create_teacher(
        uow=uow,
        user=user
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.teacher.teacher)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example Admin
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "admin"
    ),
    # Working Example Course Creator
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "course_creator"
    ),
    # Working Example Student
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    ),
    # Working Example Teacher
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "teacher"
    )
])
def test_create_user(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user_entries_beginning = len(uow.user.user)
    settings_entries_beginning = len(uow.settings.settings)
    result = services.create_user(
        uow=uow,
        name=name,
        university=university,
        lms_user_id=lms_user_id,
        role=role
    )
    assert type(result) is dict
    assert result != {}
    user_entries_after = len(uow.user.user)
    settings_entries_after = len(uow.settings.settings)
    assert user_entries_beginning + 1 == user_entries_after
    assert settings_entries_beginning + 1 == settings_entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    )
])
def test_create_learning_characteristics(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    entries_beginning = len(
        uow.learning_characteristics.learning_characteristics)
    result = services.create_learning_characteristics(
        uow=uow,
        student_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_characteristics.learning_characteristics)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    )
])
def test_create_learning_style(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.learning_style.learning_style)
    result = services.create_learning_style(
        uow=uow,
        characteristic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_style.learning_style)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    )
])
def test_create_learning_strategy(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.learning_strategy.learning_strategy)
    result = services.create_learning_strategy(
        uow=uow,
        characteristic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_strategy.learning_strategy)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    )
])
def test_create_knowledge(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.knowledge.knowledge)
    result = services.create_knowledge(
        uow=uow,
        characteristic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.knowledge.knowledge)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    )
])
def test_create_learning_analytics(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.learning_analytics.learning_analytics)
    result = services.create_learning_analytics(
        uow=uow,
        characteristic_id=1
    )
    assert type(result) is dict
    assert result != {}
    entries_after = len(uow.learning_analytics.learning_analytics)
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "admin"
    )
])
def test_delete_admin(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user = UA.User(
        name,
        university,
        lms_user_id,
        role
    )
    admin = services.create_admin(
        uow=uow,
        user=user
    )
    entries_beginning = len(uow.admin.admin)
    result = services.delete_admin(uow, admin['user_id'])
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.admin.admin)
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "course_creator"
    )
])
def test_delete_course_creator(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user = UA.User(
        name,
        university,
        lms_user_id,
        role
    )
    course_creator = services.create_course_creator(
        uow=uow,
        user=user
    )
    entries_beginning = len(uow.course_creator.course_creator)
    result = services.delete_course_creator(uow, course_creator['user_id'])
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.course_creator.course_creator)
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    )
])
def test_delete_student(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user = UA.User(
        name,
        university,
        lms_user_id,
        role
    )
    student = services.create_student(
        uow=uow,
        user=user
    )
    entries_beginning = len(uow.student.student)
    result = services.delete_student(uow, student['user_id'])
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.student.student)
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "teacher"
    )
])
def test_delete_teacher(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user = UA.User(
        name,
        university,
        lms_user_id,
        role
    )
    teacher = services.create_teacher(
        uow=uow,
        user=user
    )
    entries_beginning = len(uow.teacher.teacher)
    result = services.delete_teacher(uow, teacher['user_id'])
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.teacher.teacher)
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example Admin
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "admin"
    ),
    # Working Example Course Creator
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "course_creator"
    ),
    # Working Example Student
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "student"
    ),
    # Working Example Teacher
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "teacher"
    )
])
def test_delete_user(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user = services.create_user(
        uow=uow,
        name=name,
        university=university,
        lms_user_id=lms_user_id,
        role=role
    )
    entries_beginning = len(uow.user.user)
    settings_entries_beginning = len(uow.settings.settings)
    characteristics_entries_beginning = len(
        uow.learning_characteristics.learning_characteristics)
    result = services.delete_user(
        uow=uow,
        user_id=user['id'],
        lms_user_id=lms_user_id
    )
    assert type(result) is dict
    assert result == {}
    entries_after = len(uow.user.user)
    settings_entries_end = len(uow.settings.settings)
    characteristics_entries_after = len(
        uow.learning_characteristics.learning_characteristics)
    assert settings_entries_beginning - 1 == settings_entries_end
    assert entries_beginning - 1 == entries_after
    if role == 'student':
        assert characteristics_entries_beginning - 1\
            == characteristics_entries_after


@pytest.mark.parametrize("name, university, lms_user_id, role, theme", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "admin",
        "dark"
    )
])
def test_update_settings(name, university, lms_user_id, role, theme):
    uow = FakeUnitOfWork()
    user = services.create_user(
        uow=uow,
        name=name,
        university=university,
        lms_user_id=lms_user_id,
        role=role
    )
    result = services.update_settings_for_user(
        uow=uow,
        user_id=user['id'],
        theme=theme
    )
    assert type(result) is dict
    assert result != {}
    assert result['theme'] == theme


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "admin"
    )
])
def test_reset_settings(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user = services.create_user(
        uow=uow,
        name=name,
        university=university,
        lms_user_id=lms_user_id,
        role=role
    )
    services.update_settings_for_user(
        uow=uow,
        user_id=user['id'],
        theme="dark"
    )
    result = services.reset_settings(
        uow=uow,
        user_id=user['id']
    )
    assert type(result) is dict
    assert result != {}
    assert result['theme'] == "Standard"


@pytest.mark.parametrize("name, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "TH-AB",
        1,
        "admin"
    )
])
def test_get_settings_for_user(name, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user = services.create_user(
        uow=uow,
        name=name,
        university=university,
        lms_user_id=lms_user_id,
        role=role
    )
    result = services.get_settings_for_user(uow, user['id'])
    assert type(result) == dict
    assert result != {}


@pytest.mark.parametrize("name, name_new, university, lms_user_id, role", [
    # Working Example
    (
        "Max Mustermann",
        "Maria Musterfrau",
        "TH-AB",
        1,
        "admin"
    )
])
def test_update_user(name, name_new, university, lms_user_id, role):
    uow = FakeUnitOfWork()
    user = services.create_user(
        uow=uow,
        name=name,
        university=university,
        lms_user_id=lms_user_id,
        role=role
    )
    result = services.update_user(
        uow, user['id'], lms_user_id, name_new, university)
    assert type(result) == dict
    assert result != {}


@pytest.mark.parametrize("name, name_new, university,\
                         lms_user_id, role, keys_expected", [
    # Working Example
    (
        "Max Mustermann",
        "Maria Musterfrau",
        "TH-AB",
        1,
        "student",
        ['knowledge', 'learning_analytics',\
         'learning_strategy', 'learning_style']
    )
])
def test_get_learning_characteristics(name,
                                      name_new,
                                      university,
                                      lms_user_id,
                                      role,
                                      keys_expected):
    uow = FakeUnitOfWork()
    user = services.create_user(
        uow=uow,
        name=name,
        university=university,
        lms_user_id=lms_user_id,
        role=role
    )
    result = services.get_learning_characteristics(
        uow,
        1
    )
    assert type(result) == dict
    assert result != {}
    for key in keys_expected:
        assert key in result.keys()
        assert result[key] is not None


def test_reset_learning_characteristics():
    uow = FakeUnitOfWork()
    services.create_learning_characteristics(
        uow=uow,
        student_id=1
    )
    entries_beginning = len(
        uow.learning_characteristics.learning_characteristics)
    result = services.reset_learning_characteristics(
        uow=uow,
        student_id=1
    )
    entries_after = len(
        uow.learning_characteristics.learning_characteristics)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning == entries_after
    assert result['learning_style']['perception_value'] == 0
