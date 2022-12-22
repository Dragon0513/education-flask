class AException(Exception):
    """
    Base class for all custom exceptions. Used for returning a web response with a custom ``message`` and status ``code``.
    """
    def __init__(self, exception : Exception | None = None, message=None, status_code=500):
        super().__init__(exception, message, status_code)
        conditional_message = (message + " Inner Exception: ") if message else "" + str(exception)
        self.message = conditional_message if exception is not None else message
        self.code = status_code

class MissingParameterError(AException):
    def __init__(self, exception : Exception | None = None, message = "Missing parameters in request.", status_code=404):
        super().__init__(exception, message, status_code)

class WrongLearningStyleDimensionError(AException):
    def __init__(self, exception : Exception | None = None, message = "The Input Learning Style is out the range [0-11].", status_code=400):
        super().__init__(exception, message, status_code)

class WrongLearningStyleNumberError(AException):
    def __init__(self, exception : Exception | None = None, message = "There need to be 4 dimensions for the Learning Style.", status_code=400):
        super().__init__(exception, message, status_code)

class WrongParameterValueError(AException):
    def __init__(self, exception : Exception | None = None, message = "The passed parameter values are invalid.", status_code=404):
        super().__init__(exception, message, status_code)
class StateNotMatchingError(AException):
    def __init__(self, exception : Exception | None = None, message = "The passed state is not matching.", status_code=400):
        super().__init__(exception, message, status_code)

class InvalidJWTError(AException):
    def __init__(self, exception : Exception | None = None, message = "The passed JWT is invalid.", status_code=400):
        super().__init__(exception, message, status_code)

class UnauthorizedError(AException):
    def __init__(self, exception : Exception | None = None, message = "The request is unauthorized.", status_code=401):
        super().__init__(exception, message, status_code)