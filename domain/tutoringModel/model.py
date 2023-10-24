import time

from domain.tutoringModel import aco, ga, graf
from domain.tutoringModel.utils import get_coordinates
from errors import errors as err
from utils import constants as cons


class LearningPath:
    def __init__(
        self, student_id, course_id, based_on, topic_id=None, path=None
    ) -> None:
        self.student_id = student_id
        self.course_id = course_id
        self.based_on = based_on
        self.path = path
        self.topic_id = topic_id
        self.calculated_on = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(time.time())
        )

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "topic_id": self.topic_id,
            "based_on": self.based_on,
            "path": self.path,
            "calculated_on": self.calculated_on,
        }

    def get_learning_path(self, student_id, learning_style, _algorithm, list_of_les):
        algorithm = _algorithm.lower()
        if algorithm == "graf":
            path = graf.GrafAlgorithm(
                student_id=student_id, learning_style=learning_style
            )
            temp = path.get_learning_path(input_learning_style=learning_style)
            self.path = ", ".join(temp)
        elif algorithm == "aco":
            list_of_les_classifications = self.prepare_le_for_aco(list_of_les)
            coordinates = get_coordinates(learning_style, list_of_les_classifications)
            path = aco.AntColonySolver()
            result = path.solve(list(coordinates.items()))
            le_path = ""
            for ele in result:
                le_path = le_path + ele[0] + ", "
            self.path = le_path[:-2]

        elif algorithm == "ga":
            genetic_alg = ga. GeneticAlgorithm(
                learning_elements=list_of_les
            )
            self.path = genetic_alg.get_learning_path(
                input_learning_style=learning_style, input_learning_element=list_of_les
            )

        else:
            raise err.NoValidAlgorithmError()

    def prepare_le_for_aco(self, list_of_les):
        lz_in_list = False
        list_of_les_classifications = []
        for le in list_of_les:
            if le["classification"] == cons.abbreviation_ct:
                list_of_les_classifications.insert(0, le["classification"])
            elif le["classification"] == cons.abbreviation_as:
                list_of_les_classifications.append(le["classification"])
                lz_in_list = True
            else:
                if lz_in_list:
                    list_of_les_classifications.insert(
                        len(list_of_les_classifications) - 1,
                        le["classification"],
                    )
                else:
                    list_of_les_classifications.append(le["classification"])
        return list_of_les_classifications


class LearningPathTopic:
    def __init__(self, topic_id, learning_path_id, recommended, position) -> None:
        self.topic_id = topic_id
        self.learning_path_id = learning_path_id
        self.recommended = recommended
        self.position = position

    def serialize(self):
        return {
            "id": self.id,
            "topic_id": self.topic_id,
            "learning_path_id": self.learning_path_id,
            "recommended": self.recommended,
            "position": self.position,
        }


class LearningPathLearningElement:
    def __init__(
        self,
        learning_element_id,
        learning_path_id,
        recommended,
        position,
        learning_element=None,
    ) -> None:
        self.learning_element_id = learning_element_id
        self.learning_path_id = learning_path_id
        self.recommended = recommended
        self.position = position
        self.learning_element = learning_element

    def serialize(self):
        return {
            "id": self.id,
            "learning_element_id": self.learning_element_id,
            "learning_path_id": self.learning_path_id,
            "recommended": self.recommended,
            "position": self.position,
            "learning_element": self.learning_element,
        }
