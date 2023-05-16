from functools import wraps
import json
import os
from errors import errors as err

from flask import Flask, jsonify, request, session
from flask import make_response
from flask_cors import CORS, cross_origin
import re
from utils import constants as cons
from flask_caching import Cache

from repositories import orm
from service_layer import services, unit_of_work
from service_layer.lti.config.ToolConfigJson import ToolConfigJson
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement


app = Flask(__name__)
# import secret key from environment variable
app.secret_key = os.environ.get('SECRET_KEY')
CORS(app, supports_credentials=True)
orm.start_mappers()
cache = Cache(app)
tool_conf = ToolConfigJson(os.path.abspath(os.path.join(app.root_path, '../configs/lti_config.json')))
app.config["JWT_SECRET_KEY"] = app.secret_key
app.config["JWT_ALGORITHM"] = "RSA256"


mocked_frontend_log = {"logs": [{
    "name": "FID",
    "value": 1.900000000372529,
    "rating": "good",
    "delta": 1.900000000372529,
    "entries": [
            {
                "name": "pointerdown",
                "entryType": "first-input",
                "startTime": 1611.5,
                "duration": 8,
                "processingStart": 1613.4000000003725,
                "processingEnd": 1613.4000000003725,
                "cancelable": True
            }
    ],
    "id": "v3-1665130071366-6352791670096",
    "navigationType": "reload"
}]}
@app.errorhandler(Exception)
def handle_custom_exception(ex):
    response = json.dumps({'error': ex.__class__.__name__, 'message': str(ex)})
    return response

def authorize(role):
    '''🔑 Decorator for checking if user has the required permission to access the endpoint'''
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kws):
                state_jwt = request.cookies.get('haski_state')
                if state_jwt is None:
                    raise err.StateNotMatchingError()

                if not JWTKeyManagement.verify_jwt_payload(JWTKeyManagement.verify_jwt(state_jwt), verify_nonce=False):
                    raise err.UnauthorizedError()
                state = JWTKeyManagement.verify_jwt(state_jwt)
                if 'role' not in state:
                    raise err.UnauthorizedError()
                if role not in state['role']:
                    raise err.UnauthorizedError()

                return f(state, *args, **kws)          
        return decorated_function
    return decorator

# ##### TEST ENDPOINT #####
@app.route("/user")
@authorize('instructor')
def get_user_info(state):
    user_info = services.get_user_info(unit_of_work.SqlAlchemyUnitOfWork(), state['user_id'])
    user_dict = {'user': user_info, 'id': state['user_id']}
    status_code = 200
    return jsonify(user_dict), status_code

# User Administration via LMS
@app.route("/lms/user", methods=['POST'])
@cross_origin(supports_credentials=True)
def create_user():
    method = request.method
    match method:
        case 'POST':
            condition1 = 'name' in request.json
            condition2 = 'university' in request.json
            condition3 = 'lms_user_id' in request.json
            condition4 = 'role' in request.json
            if condition1 and condition2 and condition3 and condition4:
                condition5 = type(request.json['name']) is str
                condition6 = type(request.json['university']) is str
                condition7 = type(request.json['lms_user_id']) is int
                condition8 = type(request.json['role']) is str
                if condition5 and condition6 and condition7 and condition8:
                    role = request.json["role"].lower()
                    available_roles = [
                        'admin', 'course creator', 'student', 'teacher']
                    if role not in available_roles:
                        raise err.NoValidRoleError()
                    else:
                        user = services.create_user(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            request.json["name"],
                            request.json["university"],
                            request.json["lms_user_id"],
                            role
                        )
                        status_code = 201
                        return jsonify(user), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


@app.route("/lms/user/<user_id>/<lms_user_id>", methods=['PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def user_administration(user_id, lms_user_id):
    method = request.method
    match method:
        case 'PUT':
            condition1 = 'name' in request.json
            condition2 = 'university' in request.json
            if condition1 and condition2:
                condition3 = type(request.json['name']) is str
                condition4 = type(request.json['university']) is str
                if condition3 and condition4:
                    user = services.update_user(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        int(user_id),
                        int(lms_user_id),
                        request.json["name"],
                        request.json["university"]
                    )
                    status_code = 201
                    return jsonify(user), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()
        case 'DELETE':
            services.delete_user(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id
            )
            result = {'message': cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_user_by_id(user_id, lms_user_id):
    method = request.method
    match method:
        case 'GET':
            user = services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id
            )
            status_code = 200
            return jsonify(user), status_code


# Course Administration via LMS
@app.route("/lms/course", methods=['POST'])
@cross_origin(supports_credentials=True)
def post_course():
    method = request.method
    match method:
        case 'POST':
            condition1 = request.json is not None
            condition2 = 'name' in request.json
            condition3 = 'lms_id' in request.json
            condition4 = 'university' in request.json
            condition5 = 'created_by' in request.json
            condition6 = 'created_at' in request.json
            if condition1 and condition2 and condition3 and condition4\
                    and condition5 and condition6:
                condition7 = type(request.json['lms_id']) is int
                condition8 = type(request.json['name']) is str
                condition9 = type(request.json['university']) is str
                condition10 = type(request.json['created_by']) is int
                condition11 = type(request.json['created_at']) is str
                if condition7 and condition8 and condition9\
                        and condition10 and condition11:
                    course = services.create_course(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        request.json['lms_id'],
                        request.json['name'],
                        request.json['university'],
                        request.json['created_by'],
                        request.json['created_at']
                    )
                    status_code = 201
                    return jsonify(course), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


@app.route("/lms/course/<course_id>/<lms_course_id>",
           methods=['PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def course_management(course_id, lms_course_id):
    method = request.method
    match method:
        case 'PUT':
            condition1 = request.json is not None
            condition2 = 'name' in request.json
            condition3 = 'university' in request.json
            condition4 = 'last_updated' in request.json
            if condition1 and condition2 and condition3 and condition4:
                condition5 =\
                    re.search(cons.date_format,
                              request.json['last_updated'])
                if condition5:
                    course = services.update_course(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        course_id,
                        lms_course_id,
                        request.json['name'],
                        request.json['university']
                    )
                    status_code = 201
                    return jsonify(course), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()
        case 'DELETE':
            services.delete_course(
                unit_of_work.SqlAlchemyUnitOfWork(),
                course_id
            )
            result = {'message': cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code


# ##### LTI ENDPOINTS #####
# 1. LTI login is the first step of the OIDC Login workflow initiated by the platform
@app.route('/lti_login/', methods=['POST'])
def lti_login():
    return services.get_oidc_login(request, tool_conf, session=session)

# 2. After the platform has verified the LTI launch request, it uses this endpoint to which we redirected
@app.route('/lti_launch/', methods=['POST'])
def lti_launch():
    return services.get_lti_launch(request, tool_conf, session=session)

# 3. Get cookie for frontend if end of OIDC Login workflow by using a short living valid nonce
@app.route('/login', methods=['POST'])
def login():
    return services.get_login(request, tool_conf, session=session)

# 4. Get login status if user is already logged in by using a valid cookie
@app.route('/loginstatus', methods=['GET'])
@authorize('instructor')
def loginstatus():
    return services.get_loginstatus(request, tool_conf, session=session)

# 5. Logout by deleting cookie
@app.route('/logout', methods=['GET'])
def logout():
    return services.get_logout(request, tool_conf, session=session)

# Send the enpoint which launches the LTI tool to the frontend
@app.route('/lti_launch_view', methods=['GET'])
def lti_launch_view():
    response = make_response()
    response.data = json.dumps({'lti_launch_view': tool_conf.get_haski_activity_url(os.environ.get('LMS_URL', "http://fakedomain.com")) })
    return response

# Login with username and password
@app.route('/login_credentials', methods=['POST'])
def login_credentials():
    return services.get_login_credentials(request, tool_conf, session=session)

# ##### LOGGING ENDPOINTS #####
@app.route("/lms/course/<course_id>/<lms_course_id>/topic",
           methods=['POST'])
@cross_origin(supports_credentials=True)
def post_topic(course_id, lms_course_id):
    method = request.method
    match method:
        case 'POST':
            condition1 = request.json is not None
            condition2 = 'name' in request.json
            condition3 = 'lms_id' in request.json
            condition4 = 'is_topic' in request.json
            condition5 = 'contains_le' in request.json
            condition6 = 'created_by' in request.json
            condition7 = 'created_at' in request.json
            condition8 = 'university' in request.json
            if condition1 and condition2 and condition3 and condition4\
                    and condition5 and condition6 and condition7\
                    and condition8:
                condition9 = type(request.json['name']) is str
                condition10 = type(request.json['lms_id']) is int
                condition11 = type(request.json['is_topic']) is bool
                condition12 = type(request.json['contains_le']) is bool
                condition13 = type(request.json['created_by']) is str
                condition14 = type(request.json['created_at']) is str
                condition15 = type(request.json['university']) is str
                if condition9 and condition10 and condition11 and\
                        condition12 and condition13 and\
                        condition14 and condition15:
                    topic = services.create_topic(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        course_id,
                        request.json['lms_id'],
                        request.json['is_topic'],
                        request.json['parent_id']
                        if 'parent_id' in request.json else None,
                        request.json['contains_le'],
                        request.json['name'],
                        request.json['university'],
                        request.json['created_by'],
                        request.json['created_at']
                    )
                    status_code = 201
                    return jsonify(topic), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


@app.route("/lms/course/<course_id>/<lms_course_id>/topic/<topic_id>/" +
           "<lms_topic_id>", methods=['PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def topic_administration(course_id, lms_course_id, topic_id, lms_topic_id):
    method = request.method
    match method:
        case 'PUT':
            condition1 = request.json is not None
            condition2 = 'name' in request.json
            condition3 = 'is_topic' in request.json
            condition4 = 'contains_le' in request.json
            condition5 = 'created_by' in request.json
            condition6 = 'created_at' in request.json
            condition7 = 'university' in request.json
            condition8 = 'last_updated' in request.json
            if condition1 and condition2 and condition3\
                    and condition4 and condition5 and condition6\
                    and condition7 and condition8:
                condition9 =\
                    re.search(cons.date_format,
                              request.json['last_updated'])
                if condition9:
                    topic = services.update_topic(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        topic_id,
                        lms_topic_id,
                        request.json['is_topic'],
                        request.json['parent_id'],
                        request.json['contains_le'],
                        request.json['name'],
                        request.json['university'],
                        request.json['created_by'],
                        request.json['created_at'],
                        request.json['last_updated']
                    )
                    status_code = 201
                    return jsonify(topic), status_code
                else:
                    raise err.NoValidParameterValueError()
            else:
                raise err.MissingParameterError()
        case 'DELETE':
            services.delete_topic(
                unit_of_work.SqlAlchemyUnitOfWork(),
                topic_id
            )
            result = {'message': cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code


@app.route("/lms/course/<course_id>/<lms_course_id>/topic/<topic_id>/" +
           "<lms_topic_id>/learningElement", methods=['POST'])
@cross_origin(supports_credentials=True)
def create_learning_element(course_id,
                            lms_course_id,
                            topic_id,
                            lms_topic_id):
    method = request.method
    match method:
        case 'POST':
            condition1 = request.json is not None
            condition2 = 'lms_id' in request.json
            condition3 = 'activity_type' in request.json
            condition4 = 'classification' in request.json
            condition5 = 'name' in request.json
            condition6 = 'created_by' in request.json
            condition7 = 'created_at' in request.json
            condition8 = 'university' in request.json
            if condition1 and condition2 and condition3 and condition4\
                    and condition5 and condition6 and condition7 and\
                    condition8:
                condition9 = type(request.json['lms_id']) == int
                condition10 = type(request.json['activity_type']) == str
                condition11 = type(request.json['classification']) == str
                condition12 = type(request.json['name']) == str
                condition13 = type(request.json['created_by']) == str
                condition14 = type(request.json['created_at']) == str
                condition15 = type(request.json['university']) == str
                if condition9 and condition10 and condition11\
                        and condition12 and condition13\
                        and condition14 and condition15:
                    learning_element = services.create_learning_element(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        topic_id,
                        request.json['lms_id'],
                        request.json['activity_type'],
                        request.json['classification'],
                        request.json['name'],
                        request.json['created_by'],
                        request.json['created_at'],
                        request.json['university']
                    )
                    status_code = 201
                    return jsonify(learning_element), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


@app.route("/lms/course/<course_id>/<lms_course_id>/topic/<topic_id>/" +
           "<lms_topic_id>/learningElement/<learning_element_id>/" +
           "<lms_learning_element_id>", methods=['PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def learning_element_administration(course_id,
                                    lms_course_id,
                                    topic_id,
                                    lms_topic_id,
                                    learning_element_id,
                                    lms_learning_element_id):
    method = request.method
    match method:
        case 'PUT':
            condition1 = request.json is not None
            condition2 = 'activity_type' in request.json
            condition3 = 'classification' in request.json
            condition4 = 'name' in request.json
            condition5 = 'created_by' in request.json
            condition6 = 'created_at' in request.json
            condition7 = 'university' in request.json
            condition8 = 'last_updated' in request.json
            if condition1 and condition2 and condition3\
                    and condition4 and condition5 and condition6\
                    and condition7 and condition8:
                condition9 =\
                    re.search(cons.date_format,
                              request.json['last_updated'])
                condition10 = type(request.json['activity_type']) == str
                condition11 = type(request.json['classification']) == str
                condition12 = type(request.json['name']) == str
                condition13 = type(request.json['created_by']) == str
                condition14 = type(request.json['created_at']) == str
                condition15 = type(request.json['university']) == str
                condition16 = type(request.json['last_updated']) == str
                if condition9 and condition10 and condition11\
                        and condition12 and condition13 and condition14\
                        and condition15 and condition16:
                    learning_element = services.update_learning_element(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        learning_element_id,
                        lms_learning_element_id,
                        request.json['activity_type'],
                        request.json['classification'],
                        request.json['name'],
                        request.json['created_by'],
                        request.json['created_at'],
                        request.json['last_updated'],
                        request.json['university']
                    )
                    status_code = 201
                    return jsonify(learning_element), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()
        case 'DELETE':
            services.delete_learning_element(
                unit_of_work.SqlAlchemyUnitOfWork(),
                course_id,
                topic_id,
                learning_element_id
            )
            result = {'message': cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code

# ##### HASKI ENDPOINTS #####

@app.route("/lms/course/<course_id>/student/<student_id>",
           methods=['POST'])
@cross_origin(supports_credentials=True)
def post_student_course(course_id, student_id):
    method = request.method
    match method:
        case 'POST':
            student_course = services.add_student_to_course(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id,
                course_id
            )
            status_code = 201
            return jsonify(student_course), status_code


@app.route("/lms/course/<course_id>/teacher/<teacher_id>",
           methods=['POST'])
@cross_origin(supports_credentials=True)
def post_teacher_course(course_id, teacher_id):
    method = request.method
    match method:
        case 'POST':
            teacher_course = services.add_teacher_to_course(
                unit_of_work.SqlAlchemyUnitOfWork(),
                teacher_id,
                course_id
            )
            status_code = 201
            return jsonify(teacher_course), status_code


@app.route("/lms/student/<student_id>/<lms_user_id>/topic/<topic_id>",
           methods=['POST'])
@cross_origin(supports_credentials=True)
def post_student_topic_visit(student_id, lms_user_id, topic_id):
    method = request.method
    match method:
        case 'POST':
            condition1 = request.json is not None
            condition2 = 'visit_start' in request.json
            if condition1 and condition2:
                condition3 =\
                    re.search(cons.date_format,
                              request.json['visit_start'])
                condition4 = type(request.json['visit_start']) is str
                if condition3 and condition4:
                    result = services.add_student_topic_visit(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student_id,
                        topic_id,
                        request.json['visit_start'],
                        request.json['previous_topic_id']
                        if 'previous_topic_id' in request.json else None
                    )
                    status_code = 201
                    return jsonify(result), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


@app.route("/lms/student/<student_id>/<lms_user_id>/learningElement/" +
           "<learning_element_id>", methods=['POST'])
@cross_origin(supports_credentials=True)
def post_student_learning_element_id_visit(student_id,
                                           lms_user_id,
                                           learning_element_id):
    method = request.method
    match method:
        case 'POST':
            condition1 = request.json is not None
            condition2 = 'visit_start' in request.json
            if condition1 and condition2:
                condition3 = type(request.json['visit_start']) is str
                condition4 =\
                    re.search(cons.date_format,
                              request.json['visit_start'])
                if condition3 and condition4:
                    result = services.add_student_learning_element_visit(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student_id,
                        learning_element_id,
                        request.json['visit_start']
                    )
                    status_code = 201
                    return jsonify(result), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course/" +
           "<course_id>/learningElement", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_elements_for_course(user_id,
                                     lms_user_id,
                                     student_id,
                                     course_id):
    method = request.method
    match method:
        case 'GET':
            learning_elements =\
                services.get_learning_elements_for_course_id(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    user_id,
                    lms_user_id,
                    student_id,
                    course_id
                )
            status_code = 200
            return jsonify(learning_elements), status_code


# Student Endpoints
@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "learningCharacteristics", methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_learning_characteristics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'DELETE':
            characteristic = services.reset_learning_characteristics(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id
            )
            status_code = 200
            return jsonify(characteristic), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>" +
           "/learningCharacteristics",
           methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_characteristics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'GET':
            characteristic = services.get_learning_characteristics(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id,
                user_id,
                lms_user_id
            )
            status_code = 200
            return jsonify(characteristic), status_code


@app.route("/lms/student/<student_id>/<lms_user_id>/questionnaire",
           methods=['POST'])
@cross_origin(supports_credentials=True)
def questionnaire(student_id, lms_user_id):
    method = request.method
    match method:
        case 'POST':
            condition1 = 'ils' in request.json
            condition2 = "list_k" in request.json
            if condition1 and condition2:
                ils = {}
                for key in request.json['ils']:
                    ils[key['question_id']] = key['answer']
                required_answers_ils = [
                    'vv_2_f7', 'vv_5_f19', 'vv_7_f27', 'vv_10_f39',
                    'vv_11_f43', 'si_1_f2', 'si_4_f14', 'si_7_f26',
                    'si_10_f38', 'si_11_f42', 'ar_3_f9', 'ar_4_f13',
                    'ar_6_f21', 'ar_7_f25', 'ar_8_f29', 'sg_1_f4',
                    'sg_2_f8', 'sg_4_f16', 'sg_10_f40', 'sg_11_f44'
                ]
                for key in required_answers_ils:
                    if key not in ils.keys():
                        raise err.MissingParameterError()
                for answer in ils.values():
                    if type(answer) != str:
                        raise err.WrongParameterValueError()
                    if answer != "a" and answer != "b":
                        raise err.NoValidParameterValueError()
                list_k = {}
                for key in request.json['list_k']:
                    list_k[key['question_id']] = key['answer']
                required_answers_list_k = [
                    'org1_f1', 'org2_f2', 'org3_f3', 'ela1_f4', 'ela2_f5',
                    'ela3_f6', 'krp1_f7', 'krp2_f8', 'krp3_f9', 'wie1_f10',
                    'wie2_f11', 'wie3_f12', 'zp1_f13', 'zp2_f14', 'zp3_f15',
                    'kon1_f16', 'kon2_f17', 'kon3_f18', 'reg1_f19', 'reg2_f20',
                    'reg3_f21', 'auf1_f22', 'auf2_f23', 'auf3_f24', 'ans1_f25',
                    'ans2_f26', 'ans3_f27', 'zei1_f28', 'zei2_f29', 'zei3_f30',
                    'lms1_f31', 'lms2_f32', 'lms3_f33', 'lit1_f34', 'lit2_f35',
                    'lit3_f36', 'lu1_f37', 'lu2_f38', 'lu3_f39'
                ]
                for key in required_answers_list_k:
                    if key not in list_k.keys():
                        raise err.MissingParameterError()
                for answer in list_k.values():
                    if type(answer) != int:
                        raise err.WrongParameterValueError()
                    if answer > 5:
                        raise err.NoValidParameterValueError()
                    if answer < 0:
                        raise err.NoValidParameterValueError()
                result = services.create_questionnaire(
                    uow=unit_of_work.SqlAlchemyUnitOfWork(),
                    student_id=student_id,
                    ils_answers=ils,
                    list_k_answers=list_k
                )
                status_code = 201
                return jsonify(result), status_code
            else:
                raise err.MissingParameterError()


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "learningStyle", methods=['PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def learning_style_administration(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'PUT':
            condition1 = request.json is not None
            condition2 = 'perception_dimension' in request.json
            condition3 = 'perception_value' in request.json
            condition4 = 'input_dimension' in request.json
            condition5 = 'input_value' in request.json
            condition6 = 'processing_dimension' in request.json
            condition7 = 'processing_value' in request.json
            condition8 = 'understanding_dimension' in request.json
            condition9 = 'understanding_value' in request.json
            if condition1 and condition2 and condition3 and condition4\
                    and condition5 and condition6 and condition7\
                    and condition8 and condition9:
                condition10 = type(request.json['perception_dimension']) is str
                condition11 = type(request.json['perception_value']) is int
                condition12 = type(request.json['input_dimension']) is str
                condition13 = type(request.json['input_value']) is int
                condition14 = type(request.json['processing_dimension']) is str
                condition15 = type(request.json['processing_value']) is int
                condition16 = type(
                    request.json['understanding_dimension']) is str
                condition17 = type(request.json['understanding_value']) is int
                if condition10 and condition11 and condition12\
                        and condition13 and condition14 and condition15\
                        and condition16 and condition17:
                    condition18 = 0 < request.json['perception_value'] < 12
                    condition19 = 0 < request.json['input_value'] < 12
                    condition20 = 0 < request.json['processing_value'] < 12
                    condition21 = 0 < request.json['understanding_value'] < 12
                    if condition18 and condition19 and condition20\
                            and condition21:
                        result = services.update_learning_style_by_student_id(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            user_id,
                            lms_user_id,
                            student_id,
                            request.json['perception_dimension'],
                            request.json['perception_value'],
                            request.json['input_dimension'],
                            request.json['input_value'],
                            request.json['processing_dimension'],
                            request.json['processing_value'],
                            request.json['understanding_dimension'],
                            request.json['understanding_value'],
                        )
                        status_code = 201
                        return jsonify(result), status_code
                    else:
                        raise err.WrongLearningStyleDimensionError()
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()
        case 'DELETE':
            result = services.reset_learning_style_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "learningStyle", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_style(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_learning_style_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "learningStrategy", methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_learning_strategy(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'DELETE':
            result = services.reset_learning_strategy_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "learningStrategy", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_strategy(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_learning_strategy_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "learningAnalytics", methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_learning_analytics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'DELETE':
            result = services.reset_learning_analytics_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "learningAnalytics", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_analytics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_learning_analytics_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "knowledge", methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_knowledge(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'DELETE':
            result = services.reset_knowledge_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/" +
           "knowledge", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_knowledge(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_knowledge_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course",
           methods=['GET'])
@cross_origin(supports_credentials=True)
def get_courses_by_student_id(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_courses_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course" +
           "/<course_id>", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_course_by_course_id(user_id,
                            lms_user_id,
                            student_id,
                            course_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_course_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                course_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course" +
           "/<course_id>/topic", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_topics_by_student_and_course_id(user_id,
                                        lms_user_id,
                                        student_id,
                                        course_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_topics_by_student_and_course_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course" +
           "/<course_id>/topic/<topic_id>", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_topics_by_student_course_and_topic_id(user_id,
                                              lms_user_id,
                                              student_id,
                                              course_id,
                                              topic_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_topic_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                course_id,
                student_id,
                topic_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course" +
           "/<course_id>/topic/<topic_id>/subtopic", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_sub_topics_by_topic_id(user_id,
                               lms_user_id,
                               student_id,
                               course_id,
                               topic_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_sub_topic_by_topic_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course" +
           "/<course_id>/topic/<topic_id>/learningElement", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_element_by_student_course_and_topic_id(user_id,
                                                        lms_user_id,
                                                        student_id,
                                                        course_id,
                                                        topic_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_learning_elements_for_course_and_topic_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course" +
           "/<course_id>/topic/<topic_id>/learningElement/" +
           "<learning_element_id>", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_element_by_le_id(user_id,
                                  lms_user_id,
                                  student_id,
                                  course_id,
                                  topic_id,
                                  learning_element_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_learning_element_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id,
                learning_element_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course/" +
           "<course_id>/topic/<topic_id>/recommendation", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_element_recommendation(user_id,
                                        lms_user_id,
                                        student_id,
                                        course_id,
                                        topic_id):
    method = request.method
    match method:
        case 'GET':
            result = services.get_learning_element_recommendation(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id
            )
            status_code = 200
            return jsonify(result), status_code


# Learning Path Endpoints
@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course/" +
           "<course_id>/topic/<topic_id>/learningPath",
           methods=['POST'])
@cross_origin(supports_credentials=True)
def learning_path_administration(
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id
):
    method = request.method
    match method:
        case 'POST':
            condition1 = request.json is not None
            condition2 = 'algorithm' in request.json
            if condition1 and condition2:
                available_algorithms = ['graf', 'aco', 'ga']
                condition3 = type(request.json['algorithm']) is str
                condition4 = request.json['algorithm'].lower()\
                    in available_algorithms
                if condition3 and condition4:
                    result = services.create_learning_path(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        user_id,
                        lms_user_id,
                        student_id,
                        course_id,
                        topic_id,
                        request.json['algorithm'].lower()
                    )
                    status_code = 201
                    return jsonify(result), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course/" +
           "<course_id>/topic/<topic_id>/learningPath",
           methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_path(
    user_id,
    lms_user_id,
    student_id,
    course_id,
    topic_id
):
    method = request.method
    match method:
        case 'GET':
            result = services.get_learning_path(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id
            )
            status_code = 200
            return jsonify(result), status_code


# User Endpoints
@app.route("/user/<user_id>/<lms_user_id>", methods=['GET'])
@cross_origin(supports_credentials=True)
def user_by_user_id(user_id, lms_user_id):
    method = request.method
    match method:
        case 'GET':
            user = services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id
            )
            status_code = 200
            return jsonify(user), status_code


@app.route("/user/<user_id>/<lms_user_id>/settings",
           methods=['PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def settings_by_user_id_administration(user_id, lms_user_id):
    method = request.method
    match method:
        case 'PUT':
            condition1 = 'theme' in request.json
            condition2 = 'pswd' in request.json
            if condition1:
                settings = services.update_settings_for_user(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    user_id,
                    request.json['theme'],
                    request.json['pswd'] if condition2 else None
                )
                status_code = 201
                return jsonify(settings), status_code
            else:
                raise err.MissingParameterError()
        case 'DELETE':
            settings = services.reset_settings(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id
            )
            result = settings
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/settings",
           methods=['GET'])
@cross_origin(supports_credentials=True)
def get_settings_by_user_id(user_id, lms_user_id):
    method = request.method
    match method:
        case 'GET':
            settings = services.get_settings_for_user(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id
            )
            status_code = 200
            return jsonify(settings), status_code


# Log Endpoints
@app.route("/logs/frontend", methods=['POST'])
@cross_origin(supports_credentials=True)
def logging_frontend():
    method = request.method
    required_log_attributes = ['name',
                               'value',
                               'rating',
                               'delta',
                               'entries',
                               'id',
                               'navigationType']
    available_names = ['FCP',
                       'TTFB',
                       'CLS',
                       'LCP',
                       'FID',
                       'INP']
    available_ratings = ['good',
                         'needs-improvement',
                         'poor']
    available_navigation_type = ['navigate',
                                 'reload',
                                 'back-forward',
                                 'back-forward-cache',
                                 'prerender']
    missing_value = False
    match method:
        case 'POST':
            for key in required_log_attributes:
                if request.json is None or key not in request.json:
                    missing_value = True
            if missing_value:
                raise err.MissingParameterError()
            con1 = request.json['name'] in available_names
            con2 = request.json['rating'] in available_ratings
            con3 = request.json['navigationType'] in available_navigation_type
            if (not con1 and con2 and con3):
                raise err.WrongParameterValueError()
            mocked_frontend_log['logs'].append(request.json)
            status_code = 201
            return jsonify(request.json), status_code


# Admin Endpoints
@app.route("/user/<user_id>/<lms_user_id>/admin/<admin_id>/user",
           methods=['GET'])
@cross_origin(supports_credentials=True)
def get_users_by_admin(user_id, lms_user_id, admin_id):
    method = request.method
    match method:
        case 'GET':
            users = services.get_users_by_admin(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id
            )
            status_code = 200
            return jsonify(users), status_code


@app.route("/user/<user_id>/<lms_user_id>/admin/<admin_id>/logs",
           methods=['GET'])
@cross_origin(supports_credentials=True)
def get_admin_logs(user_id, lms_user_id, admin_id):
    method = request.method
    match method:
        case 'GET':
            services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id
            )
            return_message = mocked_frontend_log
            status_code = 200
            return jsonify(return_message), status_code


# Teacher Endpoints
@app.route("/user/<user_id>/<lms_user_id>/teacher/<teacher_id>/course",
           methods=['GET'])
@cross_origin(supports_credentials=True)
def get_teacher_courses(user_id, lms_user_id, teacher_id):
    method = request.method
    match method:
        case 'GET':
            courses = services.get_courses_for_teacher(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                teacher_id
            )
            status_code = 200
            return jsonify(courses), status_code
        

if __name__ == '__main__':
    app.run(port=5000, debug=True)