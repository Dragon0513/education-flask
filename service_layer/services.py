from urllib.request import Request

from flask import Response
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

# ##### TEST ENDPOINT #####
def get_user_info(uow: unit_of_work.AbstractUnitOfWork, user_id : str) -> str:
    with uow:
        return "Das wäre jetzt der User mit id: " + user_id
        # user_info = uow.user_info.get(user_id)
        # if user_info is None:
        #     raise err.UserNotFoundError()
        # return user_info

# ##### LTI #####
def get_oidc_login(request : Request, tool_conf, session) -> Response:
    ''' Return OIDC login url or error response in case of wrong parameters, unsecure or request'''     
    oidc_login = OIDCLoginFlask(request, tool_conf, session=session)
    return oidc_login.check_auth().auth_redirect() or Response("Error", status=500)

def get_lti_launch(request : Request, tool_conf, session) -> Response:
    ''' Return LTI launch data or error response in case of wrong parameters, unsecure or request'''     
    oidc_login = OIDCLoginFlask(request, tool_conf, session=session)
    return oidc_login.verify_state().verify_id_token().lti_launch_from_id_token() or Response("Error", status=500)

def get_login(request : Request, tool_conf, session):
    ''' Return cookie value or None'''
    # check if request has 
    oidc_login = OIDCLoginFlask(request, tool_conf, session=session)
    return oidc_login.get_login() or None