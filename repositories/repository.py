import abc
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.userAdministartion import model as UA
from errors import errors as err
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
    def create_ils_input_answers(self,
                                 ils_input_answers: LM.IlsInputAnswers)\
            -> LM.IlsInputAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ils_perception_answers(self,
                                      ils_perception_answers:
                                      LM.IlsPerceptionAnswers)\
            -> LM.IlsPerceptionAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ils_processing_answers(self,
                                      ils_processing_answers:
                                      LM.IlsProcessingAnswers)\
            -> LM.IlsProcessingAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ils_understanding_answers(self,
                                         ils_understanding_answers:
                                         LM.IlsUnderstandingAnswers)\
            -> LM.IlsUnderstandingAnswers:
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
    def create_list_k(self,
                      list_k: LM.ListK)\
            -> LM.ListK:
        raise NotImplementedError

    @abc.abstractmethod
    def create_questionnaire(self,
                             questionnaire: LM.Questionnaire)\
            -> LM.Questionnaire:
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
    def delete_ils_input_answers(self, questionnaire_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ils_perception_answers(self, questionnaire_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ils_processing_answers(self, questionnaire_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ils_understanding_answers(self, questionnaire_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_knowledge(self,
                         characteristic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_list_k(self, questionnaire_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_questionnaire(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_analytics(self,
                                  characteristic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_characteristics(self,
                                        student_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_strategy(self,
                                 characteristic_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_learning_style(self,
                              characteristic_id):
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
    def get_ils_input_answers_by_id(self,
                                    questionnaire_id)\
            -> LM.IlsInputAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def get_ils_perception_answers_by_id(self,
                                         questionnaire_id)\
            -> LM.IlsPerceptionAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def get_ils_processing_answers_by_id(self,
                                         questionnaire_id)\
            -> LM.IlsProcessingAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def get_ils_understanding_answers_by_id(self,
                                            questionnaire_id)\
            -> LM.IlsUnderstandingAnswers:
        raise NotImplementedError

    @abc.abstractmethod
    def get_knowledge(self,
                      characteristic_id,
                      knowledge) -> LM.Knowledge:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_analytics(self,
                               characteristic_id) -> LM.LearningAnalytics:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_characteristics(self,
                                     student_id)\
            -> LM.LearningCharacteristic:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_strategy(self,
                              characteristic_id) -> LM.LearningStrategy:
        raise NotImplementedError

    @abc.abstractmethod
    def get_learning_style(self,
                           characteristic_id) -> LM.LearningStyle:
        raise NotImplementedError

    @abc.abstractmethod
    def get_list_k_by_id(self,
                         questionnaire_id)\
            -> LM.ListK:
        raise NotImplementedError

    @abc.abstractmethod
    def get_questionnaire_by_id(self,
                                id)\
            -> LM.Questionnaire:
        raise NotImplementedError

    @abc.abstractmethod
    def get_settings(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_student_by_id(self,
                          user_id) -> UA.Student:
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
    def update_knowledge(self,
                         characteristic_id,
                         knowledge)\
            -> LM.Knowledge:
        raise NotImplementedError

    @abc.abstractmethod
    def update_learning_analytics(self,
                                  characteristic_id,
                                  learning_analytics)\
            -> LM.LearningAnalytics:
        raise NotImplementedError

    @abc.abstractmethod
    def update_learning_strategy(self,
                                 characteristic_id,
                                 learning_strategy)\
            -> LM.LearningStrategy:
        raise NotImplementedError

    @abc.abstractmethod
    def update_learning_style(Self,
                              characteristic_id,
                              learning_style)\
            -> LM.LearningStyle:
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

    def create_ils_input_answers(self,
                                 ils_input_answers: LM.IlsInputAnswers)\
            -> LM.IlsInputAnswers:
        try:
            self.session.add(ils_input_answers)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_ils_perception_answers(self,
                                      ils_perception_answers:
                                      LM.IlsPerceptionAnswers)\
            -> LM.IlsPerceptionAnswers:
        try:
            self.session.add(ils_perception_answers)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_ils_processing_answers(self,
                                      ils_processing_answers:
                                      LM.IlsProcessingAnswers)\
            -> LM.IlsProcessingAnswers:
        try:
            self.session.add(ils_processing_answers)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_ils_understanding_answers(self,
                                         ils_understanding_answers:
                                         LM.IlsUnderstandingAnswers)\
            -> LM.IlsUnderstandingAnswers:
        try:
            self.session.add(ils_understanding_answers)
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

    def create_learning_analytics(self,
                                  learning_analytics)\
            -> LM.LearningAnalytics:
        try:
            self.session.add(learning_analytics)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_characteristics(self,
                                        learning_characteristic)\
            -> LM.LearningCharacteristic:
        try:
            self.session.add(learning_characteristic)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_strategy(self,
                                 learning_strategy)\
            -> LM.LearningStrategy:
        try:
            self.session.add(learning_strategy)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_learning_style(self,
                              learning_style)\
            -> LM.LearningStyle:
        try:
            self.session.add(learning_style)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_list_k(self,
                      list_k: LM.ListK)\
            -> LM.ListK:
        try:
            self.session.add(list_k)
        except IntegrityError:
            raise err.ForeignKeyViolation()
        except Exception:
            raise err.CreationError()

    def create_questionnaire(self,
                             questionnaire: LM.Questionnaire)\
            -> LM.Questionnaire:
        try:
            self.session.add(questionnaire)
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

    def delete_ils_input_answers(self, questionnaire_id):
        ils_input_answers = self.get_ils_input_answers_by_id(questionnaire_id)
        if ils_input_answers != []:
            self.session.query(LM.IlsInputAnswers).filter_by(
                questionnaire_id=questionnaire_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_ils_perception_answers(self, questionnaire_id):
        ils_perception_answers = self.get_ils_perception_answers_by_id(
            questionnaire_id)
        if ils_perception_answers != []:
            self.session.query(LM.IlsPerceptionAnswers).filter_by(
                questionnaire_id=questionnaire_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_ils_processing_answers(self, questionnaire_id):
        ils_processing_answers = self.get_ils_processing_answers_by_id(
            questionnaire_id)
        if ils_processing_answers != []:
            self.session.query(LM.IlsProcessingAnswers).filter_by(
                questionnaire_id=questionnaire_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_ils_understanding_answers(self, questionnaire_id):
        ils_understanding_answers = self.get_ils_understanding_answers_by_id(
            questionnaire_id)
        if ils_understanding_answers != []:
            self.session.query(LM.IlsUnderstandingAnswers).filter_by(
                questionnaire_id=questionnaire_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_knowledge(self,
                         characteristic_id):
        knowledge = self.get_knowledge(characteristic_id)
        if knowledge != []:
            self.session.query(LM.Knowledge).filter_by(
                characteristic_id=characteristic_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_analytics(self,
                                  characteristic_id):
        analytics = self.get_learning_analytics(characteristic_id)
        if analytics != []:
            self.session.query(LM.LearningAnalytics).filter_by(
                characteristic_id=characteristic_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_characteristics(self,
                                        student_id):
        characteristics = self.get_learning_characteristics(student_id)
        if characteristics != []:
            self.session.query(LM.LearningCharacteristic).filter_by(
                student_id=student_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_strategy(self,
                                 characteristic_id):
        strategy = self.get_learning_strategy(characteristic_id)
        if strategy != []:
            self.session.query(LM.LearningStrategy).filter_by(
                characteristic_id=characteristic_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_learning_style(self,
                              characteristic_id):
        style = self.get_learning_style(characteristic_id)
        if style != []:
            self.session.query(LM.LearningStyle).filter_by(
                characteristic_id=characteristic_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_list_k(self, questionnaire_id):
        list_k = self.get_list_k_by_id(questionnaire_id)
        if list_k != []:
            self.session.query(LM.ListK).filter_by(
                questionnaire_id=questionnaire_id).delete()
        else:
            raise err.NoValidIdError()

    def delete_questionnaire(self, id):
        questionnaire = self.get_questionnaire_by_id(id)
        if questionnaire != []:
            self.session.query(LM.Questionnaire).filter_by(
                questionnaire_id=id).delete()
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

    def get_knowledge(self, characteristic_id) -> LM.Knowledge:
        result = self.session.query(LM.Knowledge).filter_by(
            characteristic_id=characteristic_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_analytics(self,
                               characteristic_id)\
            -> LM.LearningAnalytics:
        result = self.session.query(LM.LearningAnalytics).filter_by(
            characteristic_id=characteristic_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_characteristics(self,
                                     student_id)\
            -> LM.LearningCharacteristic:
        result = self.session.query(LM.LearningCharacteristic).filter_by(
            student_id=student_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_strategy(self,
                              characteristic_id)\
            -> LM.LearningStrategy:
        result = self.session.query(LM.LearningStrategy).filter_by(
            characteristic_id=characteristic_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_learning_style(self,
                           characteristic_id)\
            -> LM.LearningStyle:
        result = self.session.query(LM.LearningStyle).filter_by(
            characteristic_id=characteristic_id).all()
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

    def get_ils_input_answers_by_id(self, questionnaire_id)\
            -> LM.IlsInputAnswers:
        result = self.session.query(LM.IlsInputAnswers).filter_by(
            questionnaire_id=questionnaire_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_ils_perception_answers_by_id(self, questionnaire_id)\
            -> LM.IlsPerceptionAnswers:
        result = self.session.query(LM.IlsPerceptionAnswers).filter_by(
            questionnaire_id=questionnaire_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_ils_processing_answers_by_id(self, questionnaire_id)\
            -> LM.IlsProcessingAnswers:
        result = self.session.query(LM.IlsProcessingAnswers).filter_by(
            questionnaire_id=questionnaire_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_ils_understanding_answers_by_id(self, questionnaire_id)\
            -> LM.IlsUnderstandingAnswers:
        result = self.session.query(LM.IlsUnderstandingAnswers).filter_by(
            questionnaire_id=questionnaire_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_list_k_by_id(self, questionnaire_id)\
            -> LM.ListK:
        result = self.session.query(LM.ListK).filter_by(
            questionnaire_id=questionnaire_id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

    def get_questionnaire_by_id(self, id)\
            -> LM.Questionnaire:
        result = self.session.query(LM.Questionnaire).filter_by(
            id=id).all()
        if result == []:
            raise err.NoValidIdError()
        else:
            return result

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
        except Exception as e:
            raise err.DatabaseQueryError()

    def update_knowledge(self,
                         characteristic_id,
                         knowledge)\
            -> LM.Knowledge:
        knowledge_exist = self.get_knowledge(characteristic_id)
        if knowledge_exist != []:
            knowledge.id = knowledge_exist[0].id
            return self.session.query(LM.Knowledge)\
                .filter_by(characteristic_id=characteristic_id)
        else:
            raise err.NoValidIdError

    def update_learning_analytics(self,
                                  characteristic_id,
                                  learning_analytics)\
            -> LM.Knowledge:
        analytics_exist = self.get_learning_analytics(characteristic_id)
        if analytics_exist != []:
            learning_analytics.id = analytics_exist[0].id
            return self.session.query(LM.LearningAnalytics)\
                .filter_by(characteristic_id=characteristic_id)
        else:
            raise err.NoValidIdError

    def update_learning_strategy(self,
                                 characteristic_id,
                                 learning_strategy)\
            -> LM.Knowledge:
        strategy_exist = self.get_learning_strategy(characteristic_id)
        if strategy_exist != []:
            learning_strategy.id = strategy_exist[0].id
            return self.session.query(LM.LearningStrategy)\
                .filter_by(characteristic_id=characteristic_id)
        else:
            raise err.NoValidIdError

    def update_learning_style(self,
                              characteristic_id,
                              learning_style)\
            -> LM.Knowledge:
        style_exist = self.get_learning_analytics(characteristic_id)
        if style_exist != []:
            learning_style.id = style_exist[0].id
            return self.session.query(LM.LearningStyle)\
                .filter_by(characteristic_id=characteristic_id).update(
                {
                    LM.LearningStyle.characteristic_id:
                    learning_style.characteristic_id,
                    LM.LearningStyle.perception_dimension:
                    learning_style.perception_dimension,
                    LM.LearningStyle.perception_value:
                    learning_style.perception_value,
                    LM.LearningStyle.input_dimension:
                    learning_style.input_dimension,
                    LM.LearningStyle.input_value:
                    learning_style.input_value,
                    LM.LearningStyle.processing_dimension:
                    learning_style.processing_dimension,
                    LM.LearningStyle.processing_value:
                    learning_style.processing_value,
                    LM.LearningStyle.understanding_dimension:
                    learning_style.understanding_dimension,
                    LM.LearningStyle.understanding_value:
                    learning_style.understanding_value
                }
            )
        else:
            raise err.NoValidIdError

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
