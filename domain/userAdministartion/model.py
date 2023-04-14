class User():
    def __init__(self,
                 name,
                 university,
                 lms_user_id,
                 role=None,
                 role_id=None,
                 settings=None) -> None:
        self.name = name
        self.university = university
        self.lms_user_id = lms_user_id
        self.role = role
        self.role_id = role_id
        self.settings = settings

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'university': self.university,
            'lms_user_id': self.lms_user_id,
            'role': self.role,
            'role_id': self.role_id,
            'settings': self.settings
        }


class Admin(User):
    def __init__(self,
                 User) -> None:
        super().__init__(User.name,
                         User.university,
                         User.lms_user_id,
                         User.role)
        self.user_id = User.id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class CourseCreator(User):
    def __init__(self,
                 User) -> None:
        super().__init__(User.name,
                         User.university,
                         User.lms_user_id,
                         User.role)
        self.user_id = User.id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class Teacher(User):
    def __init__(self,
                 User) -> None:
        super().__init__(User.name,
                         User.university,
                         User.lms_user_id,
                         User.role)
        self.user_id = User.id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class Student(User):
    def __init__(self,
                 User) -> None:
        super().__init__(User.name,
                         User.university,
                         User.lms_user_id,
                         User.role)
        self.user_id = User.id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class Settings():
    def __init__(self,
                 user_id,
                 theme="Standard",
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
