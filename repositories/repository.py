import abc
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.userAdministartion import model as UA
import errors as err
from sqlalchemy.exc import IntegrityError


class AbstractRepository(abc.ABC):  # pragma: no cover
    @abc.abstractmethod
    def create_admin(self,
                     admin: UA.Admin) -> UA.Admin:
        raise NotImplementedError

    @abc.abstractmethod
    def create_course_creator(self,
                              course_creator: UA.CourseCreator) \
            -> UA.CourseCreator:
        raise NotImplementedError

    @abc.abstractmethod
    def create_knowledge(self, knowledge) -> LM.Knowledge:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_analytics(self,
                                  learning_analytics)\
            -> LM.LearningAnalytics:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_characteristics(self,
                                        learning_characteristic)\
            -> LM.LearningCharacteristic:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_strategy(self,
                                 learning_strategy)\
            -> LM.LearningStrategy:
        raise NotImplementedError

    @abc.abstractmethod
    def create_learning_style(self,
                              learning_style)\
            -> LM.LearningStyle:
        raise NotImplementedError

    @abc.abstractmethod
    def create_settings(self, settings)\
            -> UA.Settings:
        raise NotImplementedError

    @abc.abstractmethod
    def create_student(self,
                       student: UA.Student) -> UA.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def create_teacher(self,
                       teacher: UA.Teacher) -> UA.Teacher:
        raise NotImplementedError

    @abc.abstractmethod
    def create_user(self,
                    user: UA.User) -> UA.User:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_admin(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_course_creator(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_settings(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_student(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_teacher(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_user(self, user_id, lms_user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_admin_by_id(self,
                        user_id,
                        lms_user_id,
                        admin_id) -> UA.Admin:
        raise NotImplementedError

    @abc.abstractmethod
    def get_admins_by_uni(self,
                          university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_course_creator_by_id(self,
                                 user_id,
                                 lms_user_id,
                                 course_creator_id) \
            -> UA.CourseCreator:
        raise NotImplementedError

    @abc.abstractmethod
    def get_course_creators_by_uni(self,
                                   university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_settings(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_by_id(self,
                          user_id,
                          lms_user_id,
                          student_id) -> UA.Student:
        raise NotImplementedError

    @abc.abstractmethod
    def get_students_by_uni(self,
                            university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_teacher_by_id(self,
                          user_id,
                          lms_user_id,
                          teacher_id) -> UA.Teacher:
        raise NotImplementedError

    @abc.abstractmethod
    def get_teacher_by_uni(self,
                           university):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_id(self,
                       user_id,
                       lms_user_id) -> UA.User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_users_by_uni(self,
                         university):
        raise NotImplementedError

    @abc.abstractmethod
    def update_settings(self, user_id,
                        settings) -> UA.Settings:
        raise NotImplementedError

    @abc.abstractmethod
    def update_user(self,
                    user_id,
                    lms_user_id,
                    user: UA.User) -> UA.User:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):  # pragma: no cover
    def __init__(self, session):
        self.session = session

    def create_admin(self, admin: UA.Admin) -> UA.Admin:
        try:
            self.session.add(admin)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_course_creator(self,
                              course_creator: UA.CourseCreator) \
            -> UA.CourseCreator:
        try:
            self.session.add(course_creator)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_knowledge(self, knowledge) -> LM.Knowledge:
        try:
            self.session.add(knowledge)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_analytics(self, learning_analytics)\
            -> LM.LearningAnalytics:
        try:
            self.session.add(learning_analytics)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_characteristics(self, learning_characteristic)\
            -> LM.LearningCharacteristic:
        try:
            self.session.add(learning_characteristic)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_strategy(self, learning_strategy)\
            -> LM.LearningStrategy:
        try:
            self.session.add(learning_strategy)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_style(self, learning_style)\
            -> LM.LearningStyle:
        try:
            self.session.add(learning_style)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_settings(self, settings) -> UA.Settings:
        try:
            self.session.add(settings)
        except Exception:
            raise err.CreationError()

    def create_student(self, student: UA.Student) -> UA.Student:
        try:
            self.session.add(student)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_teacher(self, teacher: UA.Teacher) -> UA.Teacher:
        try:
            self.session.add(teacher)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_user(self, user: UA.User) -> UA.User:
        user_exist = self.get_users_by_uni(user.university)
        for u in user_exist:
            if user.lms_user_id == u.lms_user_id:
                raise err.AlreadyExisting()
        try:
            self.session.add(user)
        except Exception:
            raise err.CreationError()

    def delete_admin(self, user_id):
        admin = self.get_admin_by_id(user_id)
        if admin != []:
            self.session.query(UA.Admin).filter_by(
                user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_course_creator(self, user_id):
        course_creator = self.get_course_creator_by_id(user_id)
        if course_creator != []:
            self.session.query(UA.CourseCreator).filter_by(
                user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_settings(self, user_id):
        settings = self.get_settings(user_id)
        if settings != []:
            self.session.query(UA.Settings).filter_by(
                user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_student(self, user_id):
        student = self.get_student_by_id(user_id)
        if student != []:
            self.session.query(UA.Student).filter_by(
                user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_teacher(self, user_id):
        teacher = self.get_teacher_by_id(user_id)
        if teacher != []:
            self.session.query(UA.Teacher).filter_by(
                user_id=user_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_user(self, user_id, lms_user_id):
        teacher = self.get_user_by_id(user_id, lms_user_id)
        if teacher != []:
            self.session.query(UA.User).filter_by(
                id=user_id).filter_by(
                lms_user_id=lms_user_id
            ).delete()
        else:
            raise err.NoValidIdError()

    def get_admin_by_id(self, user_id,) -> UA.Admin:
        result = self.session.query(UA.Admin).filter_by(
            user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_admins_by_uni(self, university):
        try:
            return self.session.query(UA.Admin).filter_by(
                university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_course_creator_by_id(self, user_id) -> UA.CourseCreator:
        result = self.session.query(UA.CourseCreator).filter_by(
            user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_course_creators_by_uni(self, university):
        try:
            return self.session.query(UA.CourseCreator).filter_by(
                university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_settings(self, user_id) -> UA.Settings:
        result = self.session.query(UA.Settings).filter_by(
            user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_student_by_id(self, user_id) -> UA.Admin:
        result = self.session.query(UA.Student).filter_by(
            user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_students_by_uni(self, university):
        try:
            return self.session.query(UA.Student).filter_by(
                university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_teacher_by_id(self, user_id) -> UA.Admin:
        result = self.session.query(UA.Teacher).filter_by(
            user_id=user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_teacher_by_uni(self, university):
        try:
            return self.session.query(UA.Teacher).filter_by(
                university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def get_user_by_id(self, user_id, lms_user_id) -> UA.Admin:
        result = self.session.query(UA.User)\
            .filter_by(id=user_id)\
            .filter_by(lms_user_id=lms_user_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_users_by_uni(self, university):
        try:
            return self.session.query(UA.User).filter_by(
                university=university).all()
        except Exception:
            raise err.DatabaseQueryError()

    def update_settings(self, user_id, settings) -> UA.Settings:
        settings_exist = self.get_settings(user_id)
        if settings_exist != []:
            settings.id = settings_exist[0].id
            return self.session.query(UA.Settings)\
                .filter_by(user_id=user_id).update(
                {
                    UA.Settings.theme: settings.theme,
                    UA.Settings.pswd: settings.pswd,
                }
            )
        else:
            raise err.NoValidIdError

    def update_user(self, user_id, lms_user_id, user) -> UA.User:
        user_exist = self.get_user_by_id(user_id, lms_user_id)
        if user_exist != []:
            user.role = user_exist[0].role
            return self.session.query(UA.User)\
                .filter_by(id=user_id).update(
                {
                    UA.User.name: user.name,
                    UA.User.university: user.university,
                    UA.User.lms_user_id: user.lms_user_id,
                    UA.User.role: user.role
                }
            )
        else:
            raise err.NoValidIdError
