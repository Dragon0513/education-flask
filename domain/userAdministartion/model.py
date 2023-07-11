class User:
    id = None

    def __init__(
        self,
        name,
        university,
        lms_user_id,
        role=None,
        role_id=None,
        settings=None,
    ) -> None:
        self.name = name
        self.university = university
        self.lms_user_id = lms_user_id
        self.role = role
        self.role_id = role_id
        self.settings = settings

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "university": self.university,
            "lms_user_id": self.lms_user_id,
            "role": self.role,
            "role_id": self.role_id,
            "settings": self.settings,
        }


class Admin(User):
    def __init__(self, user: User) -> None:
        super().__init__(
            user.name, user.university, user.lms_user_id, role=user.role
        )
        self.user_id = user.id

    def serialize(self):
        return {"id": self.id, "user_id": self.user_id, **super().serialize()}


class CourseCreator(User):
    def __init__(self, user: User) -> None:
        super().__init__(
            user.name, user.university, user.lms_user_id, role=user.role
        )
        self.user_id = user.id

    def serialize(self):
        return {"id": self.id, "user_id": self.user_id, **super().serialize()}


class Teacher(User):
    def __init__(self, user: User) -> None:
        super().__init__(
            user.name, user.university, user.lms_user_id, role=user.role
        )
        self.user_id = user.id

    def serialize(self):
        return {"id": self.id, "user_id": self.user_id, **super().serialize()}


class Student(User):
    def __init__(self, user: User) -> None:
        super().__init__(
            user.name, user.university, user.lms_user_id, role=user.role
        )
        self.user_id = user.id

    def serialize(self):
        return {"id": self.id, "user_id": self.user_id, **super().serialize()}


class Settings:
    def __init__(self, user_id, theme="Standard", pswd=None) -> None:
        self.user_id = user_id
        self.theme = theme
        self.pswd = pswd

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "theme": self.theme,
            "pswd": self.pswd,
        }
