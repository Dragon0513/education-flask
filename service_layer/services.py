from service_layer import unit_of_work
from domain.userAdministartion import model as UA
from domain.learnersModel import model as LM


def create_admin(
        uow: unit_of_work.AbstractUnitOfWork,
        user
) -> dict:
    with uow:
        admin = UA.Admin(user)
        uow.admin.create_admin(admin)
        uow.commit()
        result = admin.serialize()
        return result


def create_course_creator(
        uow: unit_of_work.AbstractUnitOfWork,
        user
) -> dict:
    with uow:
        course_creator = UA.CourseCreator(user)
        uow.course_creator.create_course_creator(course_creator)
        uow.commit()
        result = course_creator.serialize()
        return result


def create_knowledge(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        knowledge = LM.Knowledge(characteristic_id)
        uow.knowledge.create_knowledge(knowledge)
        uow.commit()
        result = knowledge.serialize()
        return result


def create_learning_analytics(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        learning_analytics = LM.LearningAnalytics(characteristic_id)
        uow.learning_analytics.create_learning_analytics(learning_analytics)
        uow.commit()
        result = learning_analytics.serialize()
        return result


def create_learning_characteristics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristic = LM.LearningCharacteristic(student_id)
        uow.learning_characteristics.create_learning_characteristics(
            characteristic)
        uow.commit()
        create_knowledge(uow, characteristic.id)
        create_learning_analytics(uow, characteristic.id)
        create_learning_strategy(uow, characteristic.id)
        create_learning_style(uow, characteristic.id)
        result = characteristic.serialize()
        return result


def create_learning_strategy(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        learning_strategy = LM.LearningStrategy(characteristic_id)
        uow.learning_strategy.create_learning_strategy(learning_strategy)
        uow.commit()
        result = learning_strategy.serialize()
        return result


def create_learning_style(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        learning_style = LM.LearningStyle(characteristic_id)
        uow.learning_style.create_learning_style(learning_style)
        uow.commit()
        result = learning_style.serialize()
        return result


def create_settings(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
) -> dict:
    with uow:
        setting = UA.Settings(user_id)
        uow.settings.create_settings(setting)
        uow.commit()
        result = setting.serialize()
        return result


def create_student(
        uow: unit_of_work.AbstractUnitOfWork,
        user
) -> dict:
    with uow:
        student = UA.Student(user)
        uow.student.create_student(student)
        uow.commit()
        create_learning_characteristics(uow, student.id)
        result = student.serialize()
        return result


def create_teacher(
        uow: unit_of_work.AbstractUnitOfWork,
        user
) -> dict:
    with uow:
        teacher = UA.Teacher(user)
        uow.teacher.create_teacher(teacher)
        uow.commit()
        result = teacher.serialize()
        return result


def create_user(
        uow: unit_of_work.AbstractUnitOfWork,
        name,
        university,
        lms_user_id,
        role
) -> dict:
    with uow:
        user = UA.User(name, university, lms_user_id, role)
        uow.user.create_user(user)
        uow.commit()
        user.settings = create_settings(
            uow, user.id)
        match role.lower():
            case "admin":
                create_admin(uow, user)
            case "course_creator":
                create_course_creator(uow, user)
            case "student":
                create_student(uow, user)
            case "teacher":
                create_teacher(uow, user)
        result = user.serialize()
    return result


def delete_admin(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        uow.admin.delete_admin(user_id)
        uow.commit()
        return {}


def delete_course_creator(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        uow.course_creator.delete_course_creator(user_id)
        uow.commit()
        return {}


def delete_settings(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        uow.settings.delete_settings(user_id)
        uow.commit()
        return {}


def delete_student(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        student = uow.student.get_student_by_id(user_id)
        delete_learning_characteristics(uow, student[0].id)
        uow.student.delete_student(user_id)
        uow.commit()
        return {}


def delete_teacher(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        uow.teacher.delete_teacher(user_id)
        uow.commit()
        return {}


def delete_user(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id,
        lms_user_id
):
    with uow:
        user = get_user_by_id(uow, user_id, lms_user_id)
        match user['role']:
            case "admin":
                delete_admin(uow, user['id'])
            case "course_creator":
                delete_course_creator(uow, user['id'])
            case "student":
                delete_student(uow, user['id'])
            case "teacher":
                delete_teacher(uow, user['id'])
        delete_settings(uow, user_id)
        uow.user.delete_user(user_id, lms_user_id)
        uow.commit()
        return {}


def delete_knowledge(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
):
    with uow:
        uow.knowledge.delete_knowledge(characteristic_id)
        uow.commit()
        return {}


def delete_learning_analytics(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
):
    with uow:
        uow.learning_analytics.delete_learning_analytics(characteristic_id)
        uow.commit()
        return {}


def delete_learning_characteristics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
):
    with uow:
        characteristic = get_learning_characteristics(uow, student_id)
        delete_knowledge(uow, characteristic['id'])
        delete_learning_analytics(uow, characteristic['id'])
        delete_learning_strategy(uow, characteristic['id'])
        delete_learning_style(uow, characteristic['id'])
        uow.learning_characteristics.delete_learning_characteristics(
            student_id)
        uow.commit()
        return {}


def delete_learning_strategy(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
):
    with uow:
        uow.learning_strategy.delete_learning_strategy(characteristic_id)
        uow.commit()
        return {}


def delete_learning_style(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
):
    with uow:
        uow.learning_style.delete_learning_style(characteristic_id)
        uow.commit()
        return {}


def get_knowledge(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        knowledge = uow.knowledge.get_knowledge(characteristic_id)
        if knowledge == []:
            result = {}
        else:
            result = knowledge[0].serialize()
        return result


def get_learning_analytics(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        analytics = uow.learning_analytics\
            .get_learning_analytics(
                characteristic_id)
        if analytics == []:
            result = {}
        else:
            result = analytics[0].serialize()
        return result


def get_learning_characteristics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristics = uow.learning_characteristics\
            .get_learning_characteristics(
                student_id)
        if characteristics == []:
            result = {}
        else:
            characteristics = characteristics[0]
            characteristics.knowledge = get_knowledge(
                uow,
                characteristics.id
            )
            characteristics.learning_analytics = get_learning_analytics(
                uow,
                characteristics.id
            )
            characteristics.learning_strategy = get_learning_strategy(
                uow,
                characteristics.id
            )
            characteristics.learning_style = get_learning_style(
                uow,
                characteristics.id
            )
            result = characteristics.serialize()
        return result


def get_learning_strategy(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        strategy = uow.learning_strategy.get_learning_strategy(
            characteristic_id)
        if strategy == []:
            result = {}
        else:
            result = strategy[0].serialize()
        return result


def get_learning_style(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        style = uow.learning_style.get_learning_style(characteristic_id)
        if style == []:
            result = {}
        else:
            result = style[0].serialize()
        return result


def reset_knowledge(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        knowledge = LM.Knowledge(characteristic_id)
        uow.knowledge.update_knowledge(characteristic_id, knowledge)
        uow.commit()
        return knowledge.serialize()


def reset_learning_analytics(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        analytics = LM.LearningAnalytics(characteristic_id)
        uow.learning_analytics.update_learning_analytics(
            characteristic_id, analytics)
        uow.commit()
        return analytics.serialize()


def reset_learning_characteristics(
        uow: unit_of_work.AbstractUnitOfWork,
        student_id
) -> dict:
    with uow:
        characteristics = uow.learning_characteristics\
            .get_learning_characteristics(
                student_id)
        characteristics[0].knowledge = reset_knowledge(
            uow, characteristics[0].id)
        characteristics[0].learning_analytics = reset_learning_analytics(
            uow, characteristics[0].id)
        characteristics[0].learning_strategy = reset_learning_strategy(
            uow, characteristics[0].id)
        characteristics[0].learning_style = reset_learning_style(
            uow, characteristics[0].id)
        return characteristics[0].serialize()


def reset_learning_strategy(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        strategy = LM.LearningStrategy(characteristic_id)
        uow.learning_strategy.update_learning_strategy(
            characteristic_id, strategy)
        uow.commit()
        return strategy.serialize()


def reset_learning_style(
        uow: unit_of_work.AbstractUnitOfWork,
        characteristic_id
) -> dict:
    with uow:
        style = LM.LearningStyle(characteristic_id)
        uow.learning_style.update_learning_style(characteristic_id, style)
        uow.commit()
        return style.serialize()


def reset_settings(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
):
    with uow:
        settings = UA.Settings(user_id)
        uow.settings.update_settings(user_id, settings)
        uow.commit()
        return settings.serialize()


def get_settings_for_user(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id
) -> dict:
    with uow:
        settings = uow.settings.get_settings(user_id)
        if settings == []:
            result = {}
        else:
            result = settings[0].serialize()
        return result


def get_user_by_id(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id,
        lms_user_id
) -> dict:
    with uow:
        user = uow.user.get_user_by_id(user_id, lms_user_id)
        settings = uow.settings.get_settings(user_id)
        if user == []:
            result = {}
        else:
            user[0].settings = settings[0].serialize()
            result = user[0].serialize()
        return result


def update_settings_for_user(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id,
        theme,
        pswd=None
) -> dict:
    with uow:
        settings = UA.Settings(user_id, theme, pswd)
        uow.settings.update_settings(user_id, settings)
        uow.commit()
        return settings.serialize()


def update_user(
        uow: unit_of_work.AbstractUnitOfWork,
        user_id,
        lms_user_id,
        name,
        university
) -> dict:
    with uow:
        user = UA.User(name, university, lms_user_id)
        uow.user.update_user(user_id, lms_user_id, user)
        uow.commit()
        settings = uow.settings.get_settings(user_id)
        user.settings = settings[0].serialize()
        return user.serialize()
