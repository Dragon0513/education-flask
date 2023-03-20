from domain.tutoringModel import graf
import errors as err


class LearningPath:
    def __init__(self,
                 student_id,
                 course_id,
                 topic_id=None) -> None:
        self.student_id = student_id
        self.course_id = course_id
        self.topic_id = topic_id

    def serialize(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'topic_id': self.topic_id,
        }

    def get_learning_path(self, student_id, learning_style, algorithm):
        if algorithm == "Graf":
            path = graf.GrafAlgorithm(
                student_id=student_id, learning_style=learning_style)
            temp = path.get_learning_path(input_learning_style=learning_style)
            self.path = ", ".join(temp)
        else:
            raise err.NoValidAlgorithmError()


class LearningPathTopic(LearningPath):
    def __init__(self,
                 student_id,
                 course_id,
                 topic_id,
                 learning_path_id,
                 recommended,
                 position) -> None:
        super().__init__(student_id, course_id, topic_id)
        self.topic_id = topic_id
        self.learning_path_id = learning_path_id
        self.recommended = recommended
        self.position = position

    def serialize(self):
        return {
            'id': self.id,
            'topic_id': self.topic_id,
            'learning_path_id': self.learning_path_id,
            'recommended': self.recommended,
            'position': self.position
        }


class LearningPathLearningElement(LearningPath):
    def __init__(self,
                 student_id,
                 course_id,
                 topic_id,
                 learning_element_id,
                 learning_path_id,
                 recommended,
                 position) -> None:
        super().__init__(student_id, course_id, topic_id=None)
        self.learning_element_id = learning_element_id
        self.learning_path_id = learning_path_id
        self.recommended = recommended
        self.position = position

    def serialize(self):
        return {
            'id': self.id,
            'learning_element_id': self.learning_element_id,
            'learning_path_id': self.learning_path_id,
            'recommended': self.recommended,
            'position': self.position
        }
