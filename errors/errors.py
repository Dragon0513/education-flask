class AException(Exception):
    """
    Base class for all custom exceptions. Used for returning a web
    response with a custom ``message`` and status ``code``.
    """

    status_code: int = 500

    def __init__(
        self,
        exception: Exception | None = None,
        message: str = "An unexpected error occurred.",
        status_code=500,
    ):
        super().__init__(exception, message, status_code)
        self.message = (
            message + (" Inner Exception: " + str(exception))
            if exception is not None
            else message
        )
        self.status_code = status_code


class ErrorException(AException):
    """General exception for on the fly errors."""

    def __init__(
        self,
        exception: Exception | None = None,
        message="An unexpected error occurred.",
        status_code=500,
    ):
        super().__init__(exception, message, status_code)


class TypeException(AException):
    """Exception for wrong type errors."""

    def __init__(
        self,
        exception: Exception | None = None,
        message="An unexpected type error occurred.",
        status_code=500,
    ):
        super().__init__(exception, message, status_code)


class MissingParameterError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="Missing parameters in request.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class WrongLearningStyleDimensionError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The Input Learning Style is out the range [0-11].",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class WrongLearningStyleNumberError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="There need to be 4 dimensions for the Learning Style.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class WrongParameterValueError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The passed parameter values are invalid.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class StateNotMatchingError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The passed state is not matching.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class InvalidJWTError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The passed JWT is invalid.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class KeyAlreadyExistsError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The passed key already exists.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class UnauthorizedError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The request is unauthorized.",
        status_code=401,
    ):
        super().__init__(exception, message, status_code)


class ForeignKeyViolation(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="There is a foreign key violation for a parameter. \
    Please check again!",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class NoValidAlgorithmError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="Please choose an existing Algorithm!",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class NoValidIdError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="This ID does not exist!",
        status_code=404,
    ):
        super().__init__(exception, message, status_code)


class NoContentWarning(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="No entries were found!",
        status_code=204,
    ):
        super().__init__(exception, message, status_code)


class CreationError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="Could not create the ressource due to an error!",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class DatabaseQueryError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="Something went wrong while querying the Database!",
        status_code=500,
    ):
        super().__init__(exception, message, status_code)


class NoValidRoleError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The provided role does not exist!",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class AlreadyExisting(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The entered values already exist in the database!",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class NoValidParameterValueError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The send parameters have a wrong value!",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class NoLearningElementsError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="There are no learning elements for this topic!",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class KeyNotFoundError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="Key not found. Please generate a \
            key pair as described in the README.md.",
        status_code=404,
    ):
        super().__init__(exception, message, status_code)


class ContactFormError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The contact form could not be sent.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class MissingUserError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The user does not exist.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)


class NoJsonError(AException):
    def __init__(
        self,
        exception: Exception | None = None,
        message="The request body is not a valid json.",
        status_code=400,
    ):
        super().__init__(exception, message, status_code)
