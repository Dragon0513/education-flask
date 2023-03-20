class LearningCharacteristic:
    def __init__(self,
                 user_id) -> None:
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }


class LearningStyle:
    def __init__(self,
                 characteristic_id,
                 perception_dimension,
                 perception_value,
                 input_dimension,
                 input_value,
                 processing_dimension,
                 processing_value,
                 understanding_dimension,
                 understanding_value) -> None:
        self.characteristic_id = characteristic_id
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
            'id': self.id,
            'characteristic_id': self.characteristic_id,
            'perception_dimension': self.perception_dimension,
            'perception_value': self.perception_value,
            'input_dimension': self.input_dimension,
            'input_value': self.input_value,
            'processing_dimension': self.processing_dimension,
            'processing_value': self.processing_value,
            'understanding_dimension': self.understanding_dimension,
            'understanding_value': self.understanding_value
        }


class LearningStrategy:
    def __init__(self,
                 characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {
            'id': self.id,
            'characteristic_id': self.characteristic_id
        }


class Knowledge:
    def __init__(self,
                 characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {
            'id': self.id,
            'characteristic_id': self.characteristic_id
        }


class LearningAnalytics:
    def __init__(self,
                 characteristic_id) -> None:
        self.characteristic_id = characteristic_id

    def serialize(self):
        return {
            'id': self.id,
            'characteristic_id': self.characteristic_id
        }
