from datetime import datetime

from domain.domainModel import model as DM


def test_calculate_learning_element_rating():
    learning_element = DM.LearningElementRating(
        1, 1, datetime.fromisoformat("2023-01-01 16:00"), None, None
    )
    serialized_learning_element = learning_element.serialize()
    assert serialized_learning_element["rating_value"] == 1500
    assert serialized_learning_element["rating_deviation"] == 350

    learning_element_2 = DM.LearningElementRating(
        2, 1, datetime.fromisoformat("2023-01-01 16:00"), 1500, 350
    )
    result = learning_element_2.calculate_updated_rating(
        attempt_timestamp=datetime.fromisoformat("2023-01-01 16:00"),
        attempt_result=False,
        student_id=1,
        student_rating_value=1500,
        student_rating_deviation=350,
        student_rating_timestamp=datetime.fromisoformat("2023-01-01 16:00"),
    )

    assert result == {
        "value": 1662.2120026057648,
        "deviation": 290.2305060910912,
        "timestamp": datetime.fromisoformat("2023-01-01 16:00"),
    }
