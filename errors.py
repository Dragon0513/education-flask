class MissingParameterError(Exception):
    code = 400
    description = "Missing parameters in request."


class WrongLearningStyleDimensionError(Exception):
    code = 400
    description = "The Input Learning Style is out the range [0-11]."


class WrongLearningStyleNumberError(Exception):
    code = 400
    description = "There need to be 4 dimensions for the Learning Style."


class WrongParameterValueError(Exception):
    code = 400
    description = "The passed parameter values are invalid."


class ForeignKeyViolation(Exception):
    code = 400
    description = "There is a foreign key violation for a parameter. \
    Please check again!"


class NoValidAlgorithmError(Exception):
    code = 400
    description = "Please choose an existing Algorithm!"


class NoValidIdError(Exception):
    code = 404
    description = "This ID does not exist!"


class NoContentWarning(Exception):
    code = 204
    description = "No entries were found"


class CreationError(Exception):
    code = 409
    description = "Could not create the ressource due to an error!"


class DatabaseQueryError(Exception):
    code = 500
    description = "Something went wrong while querying the Database!"


class NoValidRoleError(Exception):
    code = 400
    description = "The provided role does not exist!"


class AlreadyExisting(Exception):
    code = 400
    description = "The entered values already exist in the database!"


class NoValidParameterValueError(Exception):
    code = 400
    description = "The send parameters have a wrong value!"


class NoLearningElementsError(Exception):
    code = 400
    description = "There are no learning elements for this topic!"
