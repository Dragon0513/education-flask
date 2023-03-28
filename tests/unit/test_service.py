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
                 learning_analytics=[],
                 questionnaire=[],
                 ils_input_answers=[],
                 ils_perception_answers=[],
                 ils_processing_answers=[],
                 ils_understanding_answers=[],
                 list_k=[]):
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
        self.questionnaire = set(questionnaire)
        self.ils_input_answers = set(ils_input_answers)
        self.ils_perception_answers = set(ils_perception_answers)
        self.ils_processing_answers = set(ils_processing_answers)
        self.ils_understanding_answers = set(ils_understanding_answers)
        self.list_k = set(list_k)

    def create_admin(self, admin):
        admin.id = len(self.admin) + 1
        self.admin.add(admin)

    def create_course_creator(self, course_creator):
        course_creator.id = len(self.course_creator) + 1
        self.course_creator.add(course_creator)

    def create_ils_input_answers(self, ils_input_answers):
        ils_input_answers.id = len(self.ils_input_answers) + 1
        self.ils_input_answers.add(ils_input_answers)

    def create_ils_perception_answers(self, ils_perception_answers):
        ils_perception_answers.id = len(self.ils_perception_answers) + 1
        self.ils_perception_answers.add(ils_perception_answers)

    def create_ils_processing_answers(self, ils_processing_answers):
        ils_processing_answers.id = len(self.ils_processing_answers) + 1
        self.ils_processing_answers.add(ils_processing_answers)

    def create_ils_understanding_answers(self, ils_understanding_answers):
        ils_understanding_answers.id = len(self.ils_understanding_answers) + 1
        self.ils_understanding_answers.add(ils_understanding_answers)

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

    def create_list_k(self, list_k):
        list_k.id = len(self.list_k) + 1
        self.list_k.add(list_k)

    def create_questionnaire(self, questionnaire):
        questionnaire.id = len(self.questionnaire) + 1
        self.questionnaire.add(questionnaire)

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
        to_remove = next((p for p in self.admin if p.user_id == user_id), 'a')
        self.admin.remove(to_remove)

    def delete_course_creator(self, user_id):
        to_remove = next(
            (p for p in self.course_creator if p.user_id == user_id), None)
        self.course_creator.remove(to_remove)

    def delete_ils_input_answers(self, questionnaire_id):
        to_remove = next(
            (p for p in self.ils_input_answers
             if p.questionnaire_id == questionnaire_id), None)
        self.ils_input_answers.remove(to_remove)

    def delete_ils_perception_answers(self, questionnaire_id):
        to_remove = next(
            (p for p in self.ils_perception_answers
             if p.questionnaire_id == questionnaire_id), None)
        self.ils_perception_answers.remove(to_remove)

    def delete_ils_processing_answers(self, questionnaire_id):
        to_remove = next(
            (p for p in self.ils_processing_answers
             if p.questionnaire_id == questionnaire_id), None)
        self.ils_processing_answers.remove(to_remove)

    def delete_ils_understanding_answers(self, questionnaire_id):
        to_remove = next(
            (p for p in self.ils_understanding_answers
             if p.questionnaire_id == questionnaire_id), None)
        self.ils_understanding_answers.remove(to_remove)

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

    def delete_list_k(self, questionnaire_id):
        to_remove = next(
            (p for p in self.list_k
             if p.questionnaire_id == questionnaire_id), None)
        self.list_k.remove(to_remove)

    def delete_questionnaire(self, id):
        to_remove = next(
            (p for p in self.questionnaire
             if p.id == id), None)
        self.questionnaire.remove(to_remove)

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

    def get_ils_input_answers_by_id(self, questionnaire_id):
        result = next((p for p in self.ils_input_answers if
                       p.questionnaire_id == questionnaire_id), None)
        return [result]

    def get_ils_perception_answers_by_id(self, questionnaire_id):
        result = next((p for p in self.ils_perception_answers if
                       p.questionnaire_id == questionnaire_id), None)
        return [result]

    def get_ils_processing_answers_by_id(self, questionnaire_id):
        result = next((p for p in self.ils_processing_answers if
                       p.questionnaire_id == questionnaire_id), None)
        return [result]

    def get_ils_understanding_answers_by_id(self, questionnaire_id):
        result = next((p for p in self.ils_understanding_answers if
                       p.questionnaire_id == questionnaire_id), None)
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

    def get_list_k_by_id(self, questionnaire_id):
        result = next((p for p in self.list_k if
                       p.questionnaire_id == questionnaire_id), None)
        return [result]

    def get_questionnaire_by_id(self, id):
        result = next((p for p in self.questionnaire if
                       p.id == id), None)
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
        self.questionnaire = FakeRepository()
        self.ils_input_answers = FakeRepository()
        self.ils_perception_answers = FakeRepository()
        self.ils_processing_answers = FakeRepository()
        self.ils_understanding_answers = FakeRepository()
        self.list_k = FakeRepository()
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


@pytest.mark.parametrize("vv_2_f7, vv_5_f19, vv_7_f27, vv_10_f39,\
                         vv_11_f43, vv_1_f3, vv_3_f11, vv_4_f15,\
                         vv_6_f23, vv_8_f31, vv_9_f35", [
    # Working Example Short Form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None
    ),
    # Working Example long Form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a'
    ),
    # Working Example with mixture
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None
    )
])
def test_create_ils_input_answers(vv_2_f7, vv_5_f19, vv_7_f27, vv_10_f39,
                                  vv_11_f43, vv_1_f3, vv_3_f11, vv_4_f15,
                                  vv_6_f23, vv_8_f31, vv_9_f35):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.ils_input_answers.ils_input_answers)
    result = services.create_ils_input_answers(
        uow=uow,
        questionnaire_id=1,
        vv_2_f7=vv_2_f7,
        vv_5_f19=vv_5_f19,
        vv_7_f27=vv_7_f27,
        vv_10_f39=vv_10_f39,
        vv_11_f43=vv_11_f43,
        vv_1_f3=vv_1_f3,
        vv_3_f11=vv_3_f11,
        vv_4_f15=vv_4_f15,
        vv_6_f23=vv_6_f23,
        vv_8_f31=vv_8_f31,
        vv_9_f35=vv_9_f35
    )
    entries_after = len(uow.ils_input_answers.ils_input_answers)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("si_1_f2, si_4_f14, si_7_f26, si_10_f38,\
                         si_11_f42, si_2_f6, si_3_f10, si_5_f18,\
                         si_6_f22,si_8_f30, si_9_f34", [
    # Working Example Short Form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None
    ),
    # Working Example long Form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a'
    ),
    # Working Example with mixture
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None
    )
])
def test_create_ils_perception_answers(si_1_f2, si_4_f14, si_7_f26, si_10_f38,
                                       si_11_f42, si_2_f6, si_3_f10, si_5_f18,
                                       si_6_f22, si_8_f30, si_9_f34):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.ils_perception_answers.ils_perception_answers)
    result = services.create_ils_perception_answers(
        uow=uow,
        questionnaire_id=1,
        si_1_f2=si_1_f2,
        si_4_f14=si_4_f14,
        si_7_f26=si_7_f26,
        si_10_f38=si_10_f38,
        si_11_f42=si_11_f42,
        si_2_f6=si_2_f6,
        si_3_f10=si_3_f10,
        si_5_f18=si_5_f18,
        si_6_f22=si_6_f22,
        si_8_f30=si_8_f30,
        si_9_f34=si_9_f34
    )
    entries_after = len(uow.ils_perception_answers.ils_perception_answers)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("ar_3_f9, ar_4_f13, ar_6_f21, ar_7_f25,\
                         ar_8_f29, ar_1_f1, ar_2_f5, ar_5_f17,\
                         ar_9_f33, ar_10_f37, ar_11_f41", [
    # Working Example Short Form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None
    ),
    # Working Example long Form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a'
    ),
    # Working Example with mixture
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None
    )
])
def test_create_ils_processing_answers(ar_3_f9, ar_4_f13, ar_6_f21, ar_7_f25,
                                       ar_8_f29, ar_1_f1, ar_2_f5, ar_5_f17,
                                       ar_9_f33, ar_10_f37, ar_11_f41):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.ils_processing_answers.ils_processing_answers)
    result = services.create_ils_processing_answers(
        uow=uow,
        questionnaire_id=1,
        ar_3_f9=ar_3_f9,
        ar_4_f13=ar_4_f13,
        ar_6_f21=ar_6_f21,
        ar_7_f25=ar_7_f25,
        ar_8_f29=ar_8_f29,
        ar_1_f1=ar_1_f1,
        ar_2_f5=ar_2_f5,
        ar_5_f17=ar_5_f17,
        ar_9_f33=ar_9_f33,
        ar_10_f37=ar_10_f37,
        ar_11_f41=ar_11_f41
    )
    entries_after = len(uow.ils_processing_answers.ils_processing_answers)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("sg_1_f4, sg_2_f8, sg_4_f16, sg_10_f40,\
                         sg_11_f44, sg_3_f12, sg_5_f20, sg_6_f24,\
                         sg_7_f28, sg_8_f32, sg_9_f36", [
    # Working Example Short Form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None
    ),
    # Working Example long Form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a'
    ),
    # Working Example with mixture
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None
    )
])
def test_create_ils_understanding_answers(sg_1_f4, sg_2_f8, sg_4_f16,
                                          sg_10_f40, sg_11_f44, sg_3_f12,
                                          sg_5_f20, sg_6_f24, sg_7_f28,
                                          sg_8_f32, sg_9_f36):
    uow = FakeUnitOfWork()
    entries_beginning = len(
        uow.ils_understanding_answers.ils_understanding_answers)
    result = services.create_ils_understanding_answers(
        uow=uow,
        questionnaire_id=1,
        sg_1_f4=sg_1_f4,
        sg_2_f8=sg_2_f8,
        sg_4_f16=sg_4_f16,
        sg_10_f40=sg_10_f40,
        sg_11_f44=sg_11_f44,
        sg_3_f12=sg_3_f12,
        sg_5_f20=sg_5_f20,
        sg_6_f24=sg_6_f24,
        sg_7_f28=sg_7_f28,
        sg_8_f32=sg_8_f32,
        sg_9_f36=sg_9_f36
    )
    entries_after = len(
        uow.ils_understanding_answers.ils_understanding_answers)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("org1_f1, org2_f2, org3_f3, ela1_f4, ela2_f5,\
                         ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10,\
                         wie2_f11, wie3_f12, zp1_f13, zp2_f14, zp3_f15,\
                         kon1_f16, kon2_f17, kon3_f18, reg1_f19, reg2_f20,\
                         reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25,\
                         ans2_f26, ans3_f27, zei1_f28, zei2_f29, zei3_f30,\
                         lms1_f31, lms2_f32, lms3_f33, lit1_f34, lit2_f35,\
                         lit3_f36, lu1_f37, lu2_f38, lu3_f39", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
    )
])
def test_create_list_k(org1_f1, org2_f2, org3_f3, ela1_f4, ela2_f5,
                       ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10,
                       wie2_f11, wie3_f12, zp1_f13, zp2_f14, zp3_f15,
                       kon1_f16, kon2_f17, kon3_f18, reg1_f19, reg2_f20,
                       reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25,
                       ans2_f26, ans3_f27, zei1_f28, zei2_f29, zei3_f30,
                       lms1_f31, lms2_f32, lms3_f33, lit1_f34, lit2_f35,
                       lit3_f36, lu1_f37, lu2_f38, lu3_f39):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.list_k.list_k)
    result = services.create_list_k(
        uow=uow,
        questionnaire_id=1,
        org1_f1=org1_f1,
        org2_f2=org2_f2,
        org3_f3=org3_f3,
        ela1_f4=ela1_f4,
        ela2_f5=ela2_f5,
        ela3_f6=ela3_f6,
        krp1_f7=krp1_f7,
        krp2_f8=krp2_f8,
        krp3_f9=krp3_f9,
        wie1_f10=wie1_f10,
        wie2_f11=wie2_f11,
        wie3_f12=wie3_f12,
        zp1_f13=zp1_f13,
        zp2_f14=zp2_f14,
        zp3_f15=zp3_f15,
        kon1_f16=kon1_f16,
        kon2_f17=kon2_f17,
        kon3_f18=kon3_f18,
        reg1_f19=reg1_f19,
        reg2_f20=reg2_f20,
        reg3_f21=reg3_f21,
        auf1_f22=auf1_f22,
        auf2_f23=auf2_f23,
        auf3_f24=auf3_f24,
        ans1_f25=ans1_f25,
        ans2_f26=ans2_f26,
        ans3_f27=ans3_f27,
        zei1_f28=zei1_f28,
        zei2_f29=zei2_f29,
        zei3_f30=zei3_f30,
        lms1_f31=lms1_f31,
        lms2_f32=lms2_f32,
        lms3_f33=lms3_f33,
        lit1_f34=lit1_f34,
        lit2_f35=lit2_f35,
        lit3_f36=lit3_f36,
        lu1_f37=lu1_f37,
        lu2_f38=lu2_f38,
        lu3_f39=lu3_f39
    )
    entries_after = len(uow.list_k.list_k)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("vv_2_f7, vv_5_f19, vv_7_f27, vv_10_f39,\
                         vv_11_f43, vv_1_f3, vv_3_f11, vv_4_f15,\
                         vv_6_f23, vv_8_f31, vv_9_f35,\
                         si_1_f2, si_4_f14, si_7_f26, si_10_f38,\
                         si_11_f42, si_2_f6, si_3_f10, si_5_f18,\
                         si_6_f22,si_8_f30, si_9_f34,\
                         ar_3_f9, ar_4_f13, ar_6_f21, ar_7_f25,\
                         ar_8_f29, ar_1_f1, ar_2_f5, ar_5_f17,\
                         ar_9_f33, ar_10_f37, ar_11_f41,\
                         sg_1_f4, sg_2_f8, sg_4_f16, sg_10_f40,\
                         sg_11_f44, sg_3_f12, sg_5_f20, sg_6_f24,\
                         sg_7_f28, sg_8_f32, sg_9_f36,\
                         org1_f1, org2_f2, org3_f3, ela1_f4, ela2_f5,\
                         ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10,\
                         wie2_f11, wie3_f12, zp1_f13, zp2_f14, zp3_f15,\
                         kon1_f16, kon2_f17, kon3_f18, reg1_f19, reg2_f20,\
                         reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25,\
                         ans2_f26, ans3_f27, zei1_f28, zei2_f29, zei3_f30,\
                         lms1_f31, lms2_f32, lms3_f33, lit1_f34, lit2_f35,\
                         lit3_f36, lu1_f37, lu2_f38, lu3_f39", [
    # Working Example short form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None,
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None,
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None,
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
    ),
    # Working Example full form
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        'a',
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
    )
])
def test_create_questionnaire(vv_2_f7, vv_5_f19, vv_7_f27, vv_10_f39,
                              vv_11_f43, vv_1_f3, vv_3_f11, vv_4_f15,
                              vv_6_f23, vv_8_f31, vv_9_f35,
                              si_1_f2, si_4_f14, si_7_f26, si_10_f38,
                              si_11_f42, si_2_f6, si_3_f10, si_5_f18,
                              si_6_f22, si_8_f30, si_9_f34,
                              ar_3_f9, ar_4_f13, ar_6_f21, ar_7_f25,
                              ar_8_f29, ar_1_f1, ar_2_f5, ar_5_f17,
                              ar_9_f33, ar_10_f37, ar_11_f41,
                              sg_1_f4, sg_2_f8, sg_4_f16, sg_10_f40,
                              sg_11_f44, sg_3_f12, sg_5_f20, sg_6_f24,
                              sg_7_f28, sg_8_f32, sg_9_f36,
                              org1_f1, org2_f2, org3_f3, ela1_f4, ela2_f5,
                              ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10,
                              wie2_f11, wie3_f12, zp1_f13, zp2_f14, zp3_f15,
                              kon1_f16, kon2_f17, kon3_f18, reg1_f19, reg2_f20,
                              reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25,
                              ans2_f26, ans3_f27, zei1_f28, zei2_f29, zei3_f30,
                              lms1_f31, lms2_f32, lms3_f33, lit1_f34, lit2_f35,
                              lit3_f36, lu1_f37, lu2_f38, lu3_f39):
    uow = FakeUnitOfWork()
    entries_beginning = len(uow.questionnaire.questionnaire)
    result = services.create_questionnaire(
        uow=uow,
        student_id=1,
        vv_2_f7=vv_2_f7,
        vv_5_f19=vv_5_f19,
        vv_7_f27=vv_7_f27,
        vv_10_f39=vv_10_f39,
        vv_11_f43=vv_11_f43,
        vv_1_f3=vv_1_f3,
        vv_3_f11=vv_3_f11,
        vv_4_f15=vv_4_f15,
        vv_6_f23=vv_6_f23,
        vv_8_f31=vv_8_f31,
        vv_9_f35=vv_9_f35,
        si_1_f2=si_1_f2,
        si_4_f14=si_4_f14,
        si_7_f26=si_7_f26,
        si_10_f38=si_10_f38,
        si_11_f42=si_11_f42,
        si_2_f6=si_2_f6,
        si_3_f10=si_3_f10,
        si_5_f18=si_5_f18,
        si_6_f22=si_6_f22,
        si_8_f30=si_8_f30,
        si_9_f34=si_9_f34,
        ar_3_f9=ar_3_f9,
        ar_4_f13=ar_4_f13,
        ar_6_f21=ar_6_f21,
        ar_7_f25=ar_7_f25,
        ar_8_f29=ar_8_f29,
        ar_1_f1=ar_1_f1,
        ar_2_f5=ar_2_f5,
        ar_5_f17=ar_5_f17,
        ar_9_f33=ar_9_f33,
        ar_10_f37=ar_10_f37,
        ar_11_f41=ar_11_f41,
        sg_1_f4=sg_1_f4,
        sg_2_f8=sg_2_f8,
        sg_4_f16=sg_4_f16,
        sg_10_f40=sg_10_f40,
        sg_11_f44=sg_11_f44,
        sg_3_f12=sg_3_f12,
        sg_5_f20=sg_5_f20,
        sg_6_f24=sg_6_f24,
        sg_7_f28=sg_7_f28,
        sg_8_f32=sg_8_f32,
        sg_9_f36=sg_9_f36,
        org1_f1=org1_f1,
        org2_f2=org2_f2,
        org3_f3=org3_f3,
        ela1_f4=ela1_f4,
        ela2_f5=ela2_f5,
        ela3_f6=ela3_f6,
        krp1_f7=krp1_f7,
        krp2_f8=krp2_f8,
        krp3_f9=krp3_f9,
        wie1_f10=wie1_f10,
        wie2_f11=wie2_f11,
        wie3_f12=wie3_f12,
        zp1_f13=zp1_f13,
        zp2_f14=zp2_f14,
        zp3_f15=zp3_f15,
        kon1_f16=kon1_f16,
        kon2_f17=kon2_f17,
        kon3_f18=kon3_f18,
        reg1_f19=reg1_f19,
        reg2_f20=reg2_f20,
        reg3_f21=reg3_f21,
        auf1_f22=auf1_f22,
        auf2_f23=auf2_f23,
        auf3_f24=auf3_f24,
        ans1_f25=ans1_f25,
        ans2_f26=ans2_f26,
        ans3_f27=ans3_f27,
        zei1_f28=zei1_f28,
        zei2_f29=zei2_f29,
        zei3_f30=zei3_f30,
        lms1_f31=lms1_f31,
        lms2_f32=lms2_f32,
        lms3_f33=lms3_f33,
        lit1_f34=lit1_f34,
        lit2_f35=lit2_f35,
        lit3_f36=lit3_f36,
        lu1_f37=lu1_f37,
        lu2_f38=lu2_f38,
        lu3_f39=lu3_f39
    )
    entries_after = len(uow.questionnaire.questionnaire)
    assert type(result) == dict
    assert result != {}
    assert entries_beginning + 1 == entries_after


@pytest.mark.parametrize("vv_2_f7, vv_5_f19, vv_7_f27, vv_10_f39,\
                         vv_11_f43, vv_1_f3, vv_3_f11, vv_4_f15,\
                         vv_6_f23, vv_8_f31, vv_9_f35", [
    # Working Example
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None
    )
])
def test_delete_ils_input_answers(vv_2_f7, vv_5_f19, vv_7_f27, vv_10_f39,
                                  vv_11_f43, vv_1_f3, vv_3_f11, vv_4_f15,
                                  vv_6_f23, vv_8_f31, vv_9_f35):
    uow = FakeUnitOfWork()
    services.create_ils_input_answers(
        uow=uow,
        questionnaire_id=1,
        vv_2_f7=vv_2_f7,
        vv_5_f19=vv_5_f19,
        vv_7_f27=vv_7_f27,
        vv_10_f39=vv_10_f39,
        vv_11_f43=vv_11_f43,
        vv_1_f3=vv_1_f3,
        vv_3_f11=vv_3_f11,
        vv_4_f15=vv_4_f15,
        vv_6_f23=vv_6_f23,
        vv_8_f31=vv_8_f31,
        vv_9_f35=vv_9_f35
    )
    entries_beginning = len(uow.ils_input_answers.ils_input_answers)
    result = services.delete_ils_input_answers(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.ils_input_answers.ils_input_answers)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("si_1_f2, si_4_f14, si_7_f26, si_10_f38,\
                         si_11_f42, si_2_f6, si_3_f10, si_5_f18,\
                         si_6_f22,si_8_f30, si_9_f34", [
    # Working Example
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None
    )
])
def test_delete_ils_perception_answers(si_1_f2, si_4_f14, si_7_f26, si_10_f38,
                                       si_11_f42, si_2_f6, si_3_f10, si_5_f18,
                                       si_6_f22, si_8_f30, si_9_f34):
    uow = FakeUnitOfWork()
    services.create_ils_perception_answers(
        uow=uow,
        questionnaire_id=1,
        si_1_f2=si_1_f2,
        si_4_f14=si_4_f14,
        si_7_f26=si_7_f26,
        si_10_f38=si_10_f38,
        si_11_f42=si_11_f42,
        si_2_f6=si_2_f6,
        si_3_f10=si_3_f10,
        si_5_f18=si_5_f18,
        si_6_f22=si_6_f22,
        si_8_f30=si_8_f30,
        si_9_f34=si_9_f34
    )
    entries_beginning = len(uow.ils_perception_answers.ils_perception_answers)
    result = services.delete_ils_perception_answers(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.ils_perception_answers.ils_perception_answers)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("ar_3_f9, ar_4_f13, ar_6_f21, ar_7_f25,\
                         ar_8_f29, ar_1_f1, ar_2_f5, ar_5_f17,\
                         ar_9_f33, ar_10_f37, ar_11_f41", [
    # Working Example
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None
    )
])
def test_delete_ils_processing_answers(ar_3_f9, ar_4_f13, ar_6_f21, ar_7_f25,
                                       ar_8_f29, ar_1_f1, ar_2_f5, ar_5_f17,
                                       ar_9_f33, ar_10_f37, ar_11_f41):
    uow = FakeUnitOfWork()
    services.create_ils_processing_answers(
        uow=uow,
        questionnaire_id=1,
        ar_3_f9=ar_3_f9,
        ar_4_f13=ar_4_f13,
        ar_6_f21=ar_6_f21,
        ar_7_f25=ar_7_f25,
        ar_8_f29=ar_8_f29,
        ar_1_f1=ar_1_f1,
        ar_2_f5=ar_2_f5,
        ar_5_f17=ar_5_f17,
        ar_9_f33=ar_9_f33,
        ar_10_f37=ar_10_f37,
        ar_11_f41=ar_11_f41
    )
    entries_beginning = len(uow.ils_processing_answers.ils_processing_answers)
    result = services.delete_ils_processing_answers(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.ils_processing_answers.ils_processing_answers)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("sg_1_f4, sg_2_f8, sg_4_f16, sg_10_f40,\
                         sg_11_f44, sg_3_f12, sg_5_f20, sg_6_f24,\
                         sg_7_f28, sg_8_f32, sg_9_f36", [
    # Working Example
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None
    )
])
def test_delete_ils_understanding_answers(sg_1_f4, sg_2_f8, sg_4_f16,
                                          sg_10_f40, sg_11_f44, sg_3_f12,
                                          sg_5_f20, sg_6_f24, sg_7_f28,
                                          sg_8_f32, sg_9_f36):
    uow = FakeUnitOfWork()
    services.create_ils_understanding_answers(
        uow=uow,
        questionnaire_id=1,
        sg_1_f4=sg_1_f4,
        sg_2_f8=sg_2_f8,
        sg_4_f16=sg_4_f16,
        sg_10_f40=sg_10_f40,
        sg_11_f44=sg_11_f44,
        sg_3_f12=sg_3_f12,
        sg_5_f20=sg_5_f20,
        sg_6_f24=sg_6_f24,
        sg_7_f28=sg_7_f28,
        sg_8_f32=sg_8_f32,
        sg_9_f36=sg_9_f36
    )
    entries_beginning = len(
        uow.ils_understanding_answers.ils_understanding_answers)
    result = services.delete_ils_understanding_answers(
        uow=uow,
        questionnaire_id=1,
    )
    entries_after = len(
        uow.ils_understanding_answers.ils_understanding_answers)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("org1_f1, org2_f2, org3_f3, ela1_f4, ela2_f5,\
                         ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10,\
                         wie2_f11, wie3_f12, zp1_f13, zp2_f14, zp3_f15,\
                         kon1_f16, kon2_f17, kon3_f18, reg1_f19, reg2_f20,\
                         reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25,\
                         ans2_f26, ans3_f27, zei1_f28, zei2_f29, zei3_f30,\
                         lms1_f31, lms2_f32, lms3_f33, lit1_f34, lit2_f35,\
                         lit3_f36, lu1_f37, lu2_f38, lu3_f39", [
    # Working Example
    (
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
    )
])
def test_delete_list_k(org1_f1, org2_f2, org3_f3, ela1_f4, ela2_f5,
                       ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10,
                       wie2_f11, wie3_f12, zp1_f13, zp2_f14, zp3_f15,
                       kon1_f16, kon2_f17, kon3_f18, reg1_f19, reg2_f20,
                       reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25,
                       ans2_f26, ans3_f27, zei1_f28, zei2_f29, zei3_f30,
                       lms1_f31, lms2_f32, lms3_f33, lit1_f34, lit2_f35,
                       lit3_f36, lu1_f37, lu2_f38, lu3_f39):
    uow = FakeUnitOfWork()
    services.create_list_k(
        uow=uow,
        questionnaire_id=1,
        org1_f1=org1_f1,
        org2_f2=org2_f2,
        org3_f3=org3_f3,
        ela1_f4=ela1_f4,
        ela2_f5=ela2_f5,
        ela3_f6=ela3_f6,
        krp1_f7=krp1_f7,
        krp2_f8=krp2_f8,
        krp3_f9=krp3_f9,
        wie1_f10=wie1_f10,
        wie2_f11=wie2_f11,
        wie3_f12=wie3_f12,
        zp1_f13=zp1_f13,
        zp2_f14=zp2_f14,
        zp3_f15=zp3_f15,
        kon1_f16=kon1_f16,
        kon2_f17=kon2_f17,
        kon3_f18=kon3_f18,
        reg1_f19=reg1_f19,
        reg2_f20=reg2_f20,
        reg3_f21=reg3_f21,
        auf1_f22=auf1_f22,
        auf2_f23=auf2_f23,
        auf3_f24=auf3_f24,
        ans1_f25=ans1_f25,
        ans2_f26=ans2_f26,
        ans3_f27=ans3_f27,
        zei1_f28=zei1_f28,
        zei2_f29=zei2_f29,
        zei3_f30=zei3_f30,
        lms1_f31=lms1_f31,
        lms2_f32=lms2_f32,
        lms3_f33=lms3_f33,
        lit1_f34=lit1_f34,
        lit2_f35=lit2_f35,
        lit3_f36=lit3_f36,
        lu1_f37=lu1_f37,
        lu2_f38=lu2_f38,
        lu3_f39=lu3_f39
    )
    entries_beginning = len(uow.list_k.list_k)
    result = services.delete_list_k(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.list_k.list_k)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after


@pytest.mark.parametrize("vv_2_f7, vv_5_f19, vv_7_f27, vv_10_f39,\
                         vv_11_f43, vv_1_f3, vv_3_f11, vv_4_f15,\
                         vv_6_f23, vv_8_f31, vv_9_f35,\
                         si_1_f2, si_4_f14, si_7_f26, si_10_f38,\
                         si_11_f42, si_2_f6, si_3_f10, si_5_f18,\
                         si_6_f22,si_8_f30, si_9_f34,\
                         ar_3_f9, ar_4_f13, ar_6_f21, ar_7_f25,\
                         ar_8_f29, ar_1_f1, ar_2_f5, ar_5_f17,\
                         ar_9_f33, ar_10_f37, ar_11_f41,\
                         sg_1_f4, sg_2_f8, sg_4_f16, sg_10_f40,\
                         sg_11_f44, sg_3_f12, sg_5_f20, sg_6_f24,\
                         sg_7_f28, sg_8_f32, sg_9_f36,\
                         org1_f1, org2_f2, org3_f3, ela1_f4, ela2_f5,\
                         ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10,\
                         wie2_f11, wie3_f12, zp1_f13, zp2_f14, zp3_f15,\
                         kon1_f16, kon2_f17, kon3_f18, reg1_f19, reg2_f20,\
                         reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25,\
                         ans2_f26, ans3_f27, zei1_f28, zei2_f29, zei3_f30,\
                         lms1_f31, lms2_f32, lms3_f33, lit1_f34, lit2_f35,\
                         lit3_f36, lu1_f37, lu2_f38, lu3_f39", [
    # Working Example
    (
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None,
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None,
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None,
        'a',
        'a',
        'a',
        'a',
        'a',
        None,
        None,
        None,
        None,
        None,
        None,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
    )
])
def test_delete_questionnaire(vv_2_f7, vv_5_f19, vv_7_f27, vv_10_f39,
                              vv_11_f43, vv_1_f3, vv_3_f11, vv_4_f15,
                              vv_6_f23, vv_8_f31, vv_9_f35,
                              si_1_f2, si_4_f14, si_7_f26, si_10_f38,
                              si_11_f42, si_2_f6, si_3_f10, si_5_f18,
                              si_6_f22, si_8_f30, si_9_f34,
                              ar_3_f9, ar_4_f13, ar_6_f21, ar_7_f25,
                              ar_8_f29, ar_1_f1, ar_2_f5, ar_5_f17,
                              ar_9_f33, ar_10_f37, ar_11_f41,
                              sg_1_f4, sg_2_f8, sg_4_f16, sg_10_f40,
                              sg_11_f44, sg_3_f12, sg_5_f20, sg_6_f24,
                              sg_7_f28, sg_8_f32, sg_9_f36,
                              org1_f1, org2_f2, org3_f3, ela1_f4, ela2_f5,
                              ela3_f6, krp1_f7, krp2_f8, krp3_f9, wie1_f10,
                              wie2_f11, wie3_f12, zp1_f13, zp2_f14, zp3_f15,
                              kon1_f16, kon2_f17, kon3_f18, reg1_f19, reg2_f20,
                              reg3_f21, auf1_f22, auf2_f23, auf3_f24, ans1_f25,
                              ans2_f26, ans3_f27, zei1_f28, zei2_f29, zei3_f30,
                              lms1_f31, lms2_f32, lms3_f33, lit1_f34, lit2_f35,
                              lit3_f36, lu1_f37, lu2_f38, lu3_f39):
    uow = FakeUnitOfWork()
    services.create_questionnaire(
        uow=uow,
        student_id=1,
        vv_2_f7=vv_2_f7,
        vv_5_f19=vv_5_f19,
        vv_7_f27=vv_7_f27,
        vv_10_f39=vv_10_f39,
        vv_11_f43=vv_11_f43,
        vv_1_f3=vv_1_f3,
        vv_3_f11=vv_3_f11,
        vv_4_f15=vv_4_f15,
        vv_6_f23=vv_6_f23,
        vv_8_f31=vv_8_f31,
        vv_9_f35=vv_9_f35,
        si_1_f2=si_1_f2,
        si_4_f14=si_4_f14,
        si_7_f26=si_7_f26,
        si_10_f38=si_10_f38,
        si_11_f42=si_11_f42,
        si_2_f6=si_2_f6,
        si_3_f10=si_3_f10,
        si_5_f18=si_5_f18,
        si_6_f22=si_6_f22,
        si_8_f30=si_8_f30,
        si_9_f34=si_9_f34,
        ar_3_f9=ar_3_f9,
        ar_4_f13=ar_4_f13,
        ar_6_f21=ar_6_f21,
        ar_7_f25=ar_7_f25,
        ar_8_f29=ar_8_f29,
        ar_1_f1=ar_1_f1,
        ar_2_f5=ar_2_f5,
        ar_5_f17=ar_5_f17,
        ar_9_f33=ar_9_f33,
        ar_10_f37=ar_10_f37,
        ar_11_f41=ar_11_f41,
        sg_1_f4=sg_1_f4,
        sg_2_f8=sg_2_f8,
        sg_4_f16=sg_4_f16,
        sg_10_f40=sg_10_f40,
        sg_11_f44=sg_11_f44,
        sg_3_f12=sg_3_f12,
        sg_5_f20=sg_5_f20,
        sg_6_f24=sg_6_f24,
        sg_7_f28=sg_7_f28,
        sg_8_f32=sg_8_f32,
        sg_9_f36=sg_9_f36,
        org1_f1=org1_f1,
        org2_f2=org2_f2,
        org3_f3=org3_f3,
        ela1_f4=ela1_f4,
        ela2_f5=ela2_f5,
        ela3_f6=ela3_f6,
        krp1_f7=krp1_f7,
        krp2_f8=krp2_f8,
        krp3_f9=krp3_f9,
        wie1_f10=wie1_f10,
        wie2_f11=wie2_f11,
        wie3_f12=wie3_f12,
        zp1_f13=zp1_f13,
        zp2_f14=zp2_f14,
        zp3_f15=zp3_f15,
        kon1_f16=kon1_f16,
        kon2_f17=kon2_f17,
        kon3_f18=kon3_f18,
        reg1_f19=reg1_f19,
        reg2_f20=reg2_f20,
        reg3_f21=reg3_f21,
        auf1_f22=auf1_f22,
        auf2_f23=auf2_f23,
        auf3_f24=auf3_f24,
        ans1_f25=ans1_f25,
        ans2_f26=ans2_f26,
        ans3_f27=ans3_f27,
        zei1_f28=zei1_f28,
        zei2_f29=zei2_f29,
        zei3_f30=zei3_f30,
        lms1_f31=lms1_f31,
        lms2_f32=lms2_f32,
        lms3_f33=lms3_f33,
        lit1_f34=lit1_f34,
        lit2_f35=lit2_f35,
        lit3_f36=lit3_f36,
        lu1_f37=lu1_f37,
        lu2_f38=lu2_f38,
        lu3_f39=lu3_f39
    )
    entries_beginning = len(uow.questionnaire.questionnaire)
    result = services.delete_questionnaire(
        uow=uow,
        questionnaire_id=1
    )
    entries_after = len(uow.questionnaire.questionnaire)
    assert type(result) == dict
    assert result == {}
    assert entries_beginning - 1 == entries_after
