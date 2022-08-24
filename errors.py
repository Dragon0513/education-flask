class MissingParameterError(Exception):
    code = 404
    description = "Missing parameters in request."


class WrongLearningStyleDimensionError(Exception):
    code = 400
    description = "The Input Learning Style is out the range [0-11]."


class WrongLearningStyleNumberError(Exception):
    code = 400
    description = "There need to be 4 dimensions for the Learning Style."
