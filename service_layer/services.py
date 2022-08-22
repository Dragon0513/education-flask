from service_layer import unit_of_work
from domain.tutoringModel import learning_path


def get_learning_path(
    uow: unit_of_work.AbstractUnitOfWork,
    learning_style: dict = {"AKT": 0, "INT": 0, "VIS": 0, "GLO": 0}
) -> str:
    with uow:
        path = learning_path.LearningPath()
        result = path.get_learning_path(learning_style)
    return result
