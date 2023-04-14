from domain.tutoringModel import graf
#from domain.tutoringModel import ga
from domain.domainModel import model as v
import errors as err
import time


class LearningPath:
    def __init__(self,
                 student_id,
                 course_id,
                 based_on,
                 topic_id=None,
                 path=None) -> None:
        self.student_id = student_id
        self.course_id = course_id
        self.based_on = based_on
        self.path = path
        self.topic_id = topic_id
        self.calculated_on = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    def serialize(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'topic_id': self.topic_id,
            'based_on': self.based_on,
            'path': self.path,
            'calculated_on': self.calculated_on
        }

    def get_learning_path(self, student_id, learning_style, algorithm, list_Learning_element):
        
        list_Learning_element={}

        if algorithm == "Graf":
            path = graf.GrafAlgorithm(
                student_id=student_id, learning_style=learning_style)
            temp = path.get_learning_path(input_learning_style=learning_style, list_Learning_element=list_Learning_element)
            self.path = ", ".join(temp)
        elif algorithm == "GA":
            path = ga.GA_Algorithm(
                student_id=student_id, learning_style=learning_style)
            temp = path.get_learning_path(input_learning_style=learning_style, list_Learning_element=list_Learning_element)
            self.path = ", ".join(temp)
        else:
            raise err.NoValidAlgorithmError()


class LearningPathTopic():
    def __init__(self,
                 topic_id,
                 learning_path_id,
                 recommended,
                 position) -> None:
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


class LearningPathLearningElement():
    def __init__(self,
                 learning_element_id,
                 learning_path_id,
                 recommended,
                 position,
                 learning_element=None) -> None:
        self.learning_element_id = learning_element_id
        self.learning_path_id = learning_path_id
        self.recommended = recommended
        self.position = position
        self.learning_element = learning_element

    def serialize(self):
        return {
            'id': self.id,
            'learning_element_id': self.learning_element_id,
            'learning_path_id': self.learning_path_id,
            'recommended': self.recommended,
            'position': self.position,
            'learning_element': self.learning_element
        }
