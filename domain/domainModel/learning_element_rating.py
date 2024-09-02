from EducRating.mv_glicko import MVGlicko, MVGlickoRating
from EducRating.attempt import Attempt

class LearningElementRatingAlgorithm:
    # Rating algorithm.
    mv_glicko = MVGlicko()

    # Initial rating values.
    inital_rating_value=mv_glicko.default_rating_value
    inital_rating_deviation=mv_glicko.default_rating_deviation

    def calculate_updated_rating(self, attempt: Attempt, student_rating: MVGlickoRating, learning_element_rating: MVGlickoRating) -> MVGlickoRating:

        updated_rating = self.mv_glicko.calculate_updated_resource_rating(
            attempt=attempt,
            resource_rating=learning_element_rating,
            # Every learning element in HASKI belongs to exactly one topic.
            all_user_ratings_of_user_on_concepts_of_resource=[student_rating]
        )

        return updated_rating