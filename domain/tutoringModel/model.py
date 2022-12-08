class LearningPath:
    def __init__(self,
                 id,
                 student_id,
                 module_id,
                 contains_le,
                 order_depth,
                 path) -> None:
        self.id = id
        self.student_id = student_id
        self.moduel_id = module_id
        self.contains_le = contains_le,
        self.order_depth = order_depth,
        self.path = path

    def serialize(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'module_id': self.module_id,
            'contains_le': self.contains_le,
            'order_depth': self.order_depth,
            'path': self.path
        }
