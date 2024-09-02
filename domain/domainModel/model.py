from datetime import datetime
from domain.domainModel import learning_element_rating
from EducRating import mv_glicko, attempt

class LearningElement:
    def __init__(
        self,
        lms_id,
        activity_type,
        classification,
        name,
        university,
        created_by,
        created_at,
        last_updated=None,
        student_learning_element=None,
    ) -> None:
        self.id = None
        self.lms_id = lms_id
        self.activity_type = activity_type
        self.classification = classification
        self.name = name
        self.university = university
        self.created_by = created_by
        self.created_at = created_at
        self.last_updated = last_updated
        self.student_learning_element = student_learning_element

    def serialize(self):
        return {
            "id": self.id,
            "lms_id": self.lms_id,
            "activity_type": self.activity_type,
            "classification": self.classification,
            "name": self.name,
            "university": self.university,
            "created_by": self.created_by,
            "created_at": self.created_at,
            "last_updated": self.last_updated,
            "student_learning_element": self.student_learning_element,
        }


class Course:
    def __init__(
        self,
        lms_id,
        name,
        university,
        created_at=None,
        created_by=None,
        last_updated=None,
    ) -> None:
        self.id = None
        self.lms_id = lms_id
        self.name = name
        self.university = university
        self.created_at = created_at
        self.created_by = created_by
        self.last_updated = last_updated

    def serialize(self):
        return {
            "id": self.id,
            "lms_id": self.lms_id,
            "name": self.name,
            "university": self.university,
            "created_at": self.created_at,
            "created_by": self.created_by,
            "last_updated": self.last_updated,
        }


class Topic:
    def __init__(
        self,
        lms_id,
        is_topic,
        parent_id,
        contains_le,
        name,
        university,
        created_by,
        created_at,
        last_updated=None,
        student_topic=None,
    ) -> None:
        self.id = None
        self.lms_id = lms_id
        self.is_topic = is_topic
        self.parent_id = parent_id
        self.contains_le = contains_le
        self.name = name
        self.university = university
        self.created_by = created_by
        self.created_at = created_at
        self.last_updated = last_updated
        self.student_topic = student_topic

    def serialize(self):
        return {
            "id": self.id,
            "lms_id": self.lms_id,
            "is_topic": self.is_topic,
            "parent_id": self.parent_id,
            "contains_le": self.contains_le,
            "name": self.name,
            "university": self.university,
            "created_by": self.created_by,
            "created_at": self.created_at,
            "last_updated": self.last_updated,
            "student_topic": self.student_topic,
        }


class CourseTopic:
    def __init__(self, course_id, topic_id) -> None:
        self.id = None
        self.course_id = course_id
        self.topic_id = topic_id

    def serialize(self):
        return {"id": self.id, "course_id": self.course_id, "topic_id": self.topic_id}


class TopicLearningElement:
    def __init__(self, topic_id, learning_element_id) -> None:
        self.id = None
        self.topic_id = topic_id
        self.learning_element_id = learning_element_id

    def serialize(self):
        return {
            "id": self.id,
            "topic_id": self.topic_id,
            "learning_element_id": self.learning_element_id,
        }


class CourseCreatorCourse:
    def __init__(
        self, course_creator_id, course_id, created_at, last_updated=None
    ) -> None:
        self.id = None
        self.course_creator_id = course_creator_id
        self.course_id = course_id
        self.created_at = created_at
        self.last_updated = last_updated

    def serialize(self):
        return {
            "id": self.id,
            "course_creator_id": self.course_creator_id,
            "course_id": self.course_id,
            "created_at": self.created_at,
            "last_updated": self.last_updated,
        }


class TeacherCourse:
    def __init__(self, teacher_id, course_id) -> None:
        self.id = None
        self.teacher_id = teacher_id
        self.course_id = course_id

    def serialize(self):
        return {
            "id": self.id,
            "teacher_id": self.teacher_id,
            "course_id": self.course_id,
        }


class StudentCourse:
    def __init__(
        self,
        student_id,
        course_id,
        perception_dimension,
        perception_value,
        input_dimension,
        input_value,
        processing_dimension,
        processing_value,
        understanding_dimension,
        understanding_value,
    ) -> None:
        self.id = None
        self.student_id = student_id
        self.course_id = course_id
        self.perception_dimension = perception_dimension
        self.perception_value = perception_value
        self.input_dimension = input_dimension
        self.input_value = input_value
        self.processing_dimension = processing_dimension
        self.processing_value = processing_value
        self.understanding_dimension = understanding_dimension
        self.understanding_value = understanding_value

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "perception_dimension": self.perception_dimension,
            "perception_value": self.perception_value,
            "input_dimension": self.input_dimension,
            "input_value": self.input_value,
            "processing_dimension": self.processing_dimension,
            "processing_value": self.processing_value,
            "understanding_dimension": self.understanding_dimension,
            "understanding_value": self.understanding_value,
        }


class StudentTopic:
    def __init__(
        self, student_id, topic_id, done=False, done_at=None, visits=None
    ) -> None:
        self.id = None
        self.student_id = student_id
        self.topic_id = topic_id
        self.done = done
        self.done_at = done_at
        self.visits = visits

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "topic_id": self.topic_id,
            "done": self.done,
            "done_at": self.done_at,
            "visits": self.visits,
        }


class StudentTopicVisit:
    def __init__(self, student_id, topic_id, visit_start, visit_end=None) -> None:
        self.id = None
        self.student_id = student_id
        self.topic_id = topic_id
        self.visit_start = visit_start
        self.visit_end = visit_end

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "topic_id": self.topic_id,
            "visit_start": self.visit_start,
            "visit_end": self.visit_end,
        }


class StudentLearningElement:
    def __init__(
        self, student_id, learning_element_id, done=False, done_at=None
    ) -> None:
        self.id = None
        self.student_id = student_id
        self.learning_element_id = learning_element_id
        self.done = done
        self.done_at = done_at

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "learning_element_id": self.learning_element_id,
            "done": self.done,
            "done_at": self.done_at,
        }


class StudentLearningElementVisit:
    def __init__(
        self, student_id, learning_element_id, visit_start, visit_end=None
    ) -> None:
        self.id = None
        self.student_id = student_id
        self.learning_element_id = learning_element_id
        self.visit_start = visit_start
        self.visit_end = visit_end

    def serialize(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "learning_element_id": self.learning_element_id,
            "visit_start": self.visit_start,
            "visit_end": self.visit_end,
        }


class StudentLearningPathLearningElementAlgorithm:
    def __init__(self, student_id, topic_id, algorithm_id) -> None:
        self.id = None
        self.student_id = student_id
        self.topic_id = topic_id
        self.algorithm_id = algorithm_id

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "student_id": self.student_id,
            "topic_id": self.topic_id,
            "algorithm_id": self.algorithm_id,
        }


class LearningElementRating:
    # Get algorithm for learning element rating calculation.
    learning_element_rating_algorithm = learning_element_rating.LearningElementRatingAlgorithm()

    def __init__(self, learning_element_id: int, topic_id: int, timestamp: datetime, rating_value: float | None, rating_deviation: float | None) -> None:
        self.id = None
        self.learning_element_id = learning_element_id
        self.topic_id = topic_id
        self.timestamp = timestamp
        self.rating_value = rating_value if rating_value is not None else self.learning_element_rating_algorithm.inital_rating_value
        self.rating_deviation = rating_deviation if rating_deviation is not None else self.learning_element_rating_algorithm.inital_rating_deviation

    def serialize(self):
        return {
            "id": self.id,
            "learning_element_id": self.learning_element_id,
            "topic_id": self.topic_id,
            "rating_value": self.rating_value,
            "rating_deviation": self.rating_deviation,
            "timestamp": self.timestamp,
        }

    def calculate_updated_rating(self,
            attempt_timestamp: datetime,
            is_attempt_correct: bool,
            student_id: str,
            student_rating_value: float,
            student_rating_deviation: float,
            student_rating_timestamp: datetime,
            ) -> dict:

        # Calculate the updated rating for a learning element.
        updated_rating = self.learning_element_rating_algorithm.calculate_updated_rating(
            attempt=attempt.Attempt(
                attempt_id='',
                user_id=student_id,
                resource_id=str(self.learning_element_id),
                concept_id=str(self.topic_id),
                timestamp=attempt_timestamp,
                is_attempt_correct=is_attempt_correct,
            ),
            student_rating=mv_glicko.MVGlickoRating(
                value=student_rating_value,
                deviation=student_rating_deviation,
                timestamp=student_rating_timestamp
            ),
            learning_element_rating=mv_glicko.MVGlickoRating(
                value=self.rating_value,
                deviation=self.rating_deviation,
                timestamp=self.timestamp,
            ),
        )

        # Return the updated rating.
        return {
            "value": updated_rating.value,
            "deviation": updated_rating.deviation, 
            "timestamp": updated_rating.timestamp
        }