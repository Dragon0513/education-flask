from service_layer import unit_of_work
from domain.userAdministartion import model as UA


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
