class User():
    def __init__(self,
                 name,
                 university,
                 lms_user_id) -> None:
        self.name = name
        self.university = university
        self.lms_user_id = lms_user_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'university': self.university,
            'lms_user_id': self.lms_user_id
        }


class Admin(User):
    def __init__(self,
                 name,
                 university,
                 lms_user_id,
                 user_id) -> None:
        super().__init__(name, university, lms_user_id)
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class CourseCreator(User):
    def __init__(self,
                 name,
                 university,
                 lms_user_id,
                 user_id) -> None:
        super().__init__(name, university, lms_user_id)
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class Teacher(User):
    def __init__(self,
                 name,
                 university,
                 lms_user_id,
                 user_id) -> None:
        super().__init__(name, university, lms_user_id)
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class Student(User):
    def __init__(self,
                 user_id) -> None:
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class Settings():
    def __init__(self,
                 user_id,
                 theme,
                 pswd=None) -> None:
        self.user_id = user_id
        self.theme = theme
        self.pswd = pswd

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'theme': self.theme,
            'pswd': self.pswd
        }
