class Student:
    def __init__(self, name, learning_style) -> None:
        self.name = name
        self.learning_style = learning_style

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'learning_style': self.learning_style
        }
