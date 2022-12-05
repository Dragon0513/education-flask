from urllib.request import Request
from service_layer import unit_of_work
from domain.tutoringModel import learning_path
from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask
from flask.wrappers import Request

def get_learning_path(
    uow: unit_of_work.AbstractUnitOfWork,
    student_id,
    learning_style: dict = {"AKT": 0, "INT": 0, "VIS": 0, "GLO": 0}
) -> str:
    with uow:
        path = learning_path.LearningPath(
            student_id=student_id, learning_style=learning_style)
        result = ', '.join(path.learning_path)
        if type(result) is not "":
            uow.learning_path.add(path)
            uow.commit()
    return result

def get_oidc_login(request : Request, tool_conf):
    ''' Return OIDC login url or error response in case of wrong parameters, unsecure or request'''     
    oidc_login = OIDCLoginFlask(request, tool_conf)
    return oidc_login.check_auth().login()
