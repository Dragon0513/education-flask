from service_layer import unit_of_work
from domain.tutoringModel import learning_path


def get_learning_path(
    uow: unit_of_work.AbstractUnitOfWork,
    student_id,
    learning_style: dict = {"AKT": 0, "INT": 0, "VIS": 0, "GLO": 0}
) -> str:
    with uow:
        path = learning_path.LearningPath(
            student_id=student_id, learning_style=learning_style)
        condition = type(path.learning_path) is ValueError
        if condition:
            return ValueError
        result = ', '.join(path.learning_path)
        if type(result) is not "":
            uow.learning_path.add(path)
            uow.commit()
    return result
