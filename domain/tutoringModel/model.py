from domain.tutoringModel import graf
import errors as err

class LearningPath:
    def __init__(self,
                 id = None,
                 student_id = None,
                 course_id = None,
                 contains_le = False,
                 order_depth = None,
                 path = None) -> None:
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
        self.contains_le = contains_le
        self.order_depth = order_depth
        self.path = path

    def serialize(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'contains_le': self.contains_le,
            'order_depth': self.order_depth,
            'path': self.path
        }

    def get_learning_path(self, student_id, learning_style, algorithm):
        if algorithm == "Graf":
            path = graf.GrafAlgorithm(student_id=student_id, learning_style = learning_style)
            temp = path.get_learning_path(input_learning_style = learning_style)
            self.path = ", ".join(temp)
        else:
            raise err.NoValidAlgorithmError()