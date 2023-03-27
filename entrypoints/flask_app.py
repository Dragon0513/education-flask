import datetime
from functools import wraps
import json
import os
import urllib.parse
from errors import errors as err

from flask import Flask, abort, jsonify, request, session
from flask import redirect, make_response
from flask_cors import CORS, cross_origin
from flask_caching import Cache

from repositories import orm
from service_layer import services, unit_of_work
from service_layer.lti.OIDCLoginFlask import OIDCLoginFlask
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

def authorize(permission):
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
                if 'permissions' not in state:
                    raise err.UnauthorizedError()
                if permission not in state['permissions']:
                    raise err.UnauthorizedError()

                return f(state, *args, **kws)          
        return decorated_function
    return decorator

# ##### TEST ENDPOINT #####
@app.route("/user")
@authorize('read:user_info')
def get_user_info(state):
    user_info = services.get_user_info(unit_of_work.SqlAlchemyUnitOfWork(), state['user_id'])
    user_dict = {'user': user_info, 'id': state['user_id']}
    status_code = 200
    return jsonify(user_dict), status_code

@app.route("/learningPath/<student_id>/<course_id>/<order_depth>",
           methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def get_learning_path(student_id, course_id, order_depth):
    method = request.method
    match method:
        case 'GET':
            learning_path = services.get_learning_path(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id,
                course_id,
                order_depth
            )
            if learning_path == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(learning_path), status_code
        case 'POST':
            learning_style = {"AKT": 0, "INT": 0, "VIS": 0, "GLO": 0}
            algorithm = "Graf"
            if request.json is not None:
                if 'learningStyle' in request.json:
                    learning_style = request.json["learningStyle"]
                if 'algorithm' in request.json:
                    algorithm = request.json["algorithm"]
            learning_path = services.create_learning_path(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id,
                course_id,
                order_depth,
                learning_style=learning_style,
                algorithm=algorithm
            )
            status_code = 201
            return jsonify(learning_path), status_code


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
def loginstatus():
    return services.get_loginstatus(request, tool_conf, session=session)

# 5. Logout by deleting cookie
@app.route('/logout', methods=['GET'])
def logout():
    return services.get_logout(request, tool_conf, session=session)

# Login with username and password
@app.route('/login_credentials', methods=['POST'])
def login_credentials():
    return services.get_login_credentials(request, tool_conf, session=session)

# ##### LOGGING ENDPOINTS #####
@app.route("/logs/frontend", methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def logging_frontend():
    method = request.method
    return_message = {}
    status_code = 400
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
            return_message = {'message': 'Item successfully created'}
        case 'GET':
            return_message = mocked_frontend_log
            status_code = 200
    return jsonify(return_message), status_code

# ##### HASKI ENDPOINTS #####

@app.route("/learningElement", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_learning_elements():
    method = request.method
    match method:
        case 'GET':
            learning_elements = services.get_learning_elements(
                unit_of_work.SqlAlchemyUnitOfWork()
            )
            if learning_elements == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(learning_elements), status_code
        case 'POST':
            condition1 = request.json is None
            condition2 = 'name' not in request.json
            condition3 = 'classification' not in request.json
            condition4 = 'ancestor_id' not in request.json
            condition5 = 'order_depth' not in request.json
            condition6 = 'prerequisite_id' in request.json
            if (condition1 or
                condition2 or
                condition3 or
                condition4 or
                    condition5):
                raise err.MissingParameterError()
            else:
                learning_element = services.create_element(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    request.json['name'],
                    request.json['classification'],
                    request.json['ancestor_id'],
                    request.json['order_depth'],
                    request.json['prerequisite_id'] if condition6 else None
                )
            status_code = 200
            return jsonify(learning_element), status_code


@app.route("/learningElement/<element_id>", methods=['GET', 'PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def get_learning_element_by_id(element_id):
    method = request.method
    match method:
        case 'GET':
            learning_element = services.get_learning_element_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                element_id
            )
            status_code = 200
            return jsonify(learning_element), status_code
        case 'PUT':
            condition1 = request.json is None
            condition2 = 'name' not in request.json
            condition3 = 'classification' not in request.json
            condition4 = 'ancestor_id' not in request.json
            condition5 = 'order_depth' not in request.json
            condition6 = 'prerequisite_id' in request.json
            if condition1 or \
                    condition2 or \
                    condition3 or \
                    condition4 or condition5:
                raise err.MissingParameterError()
            else:
                learning_element = services.update_learning_element(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    element_id,
                    request.json['name'],
                    request.json['classification'],
                    request.json['ancestor_id'],
                    request.json['prerequisite_id'] if condition6 else None,
                    request.json['order_depth']
                )
                if learning_element == {}:
                    status_code = 404
                else:
                    status_code = 200
                return jsonify(learning_element), status_code
        case 'DELETE':
            services.delete_learning_element(
                unit_of_work.SqlAlchemyUnitOfWork(),
                element_id
            )
            status_code = 204
            return jsonify(None), status_code


@app.route('/course', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_courses():
    method = request.method
    match method:
        case 'GET':
            course = services.get_courses(
                unit_of_work.SqlAlchemyUnitOfWork()
            )
            if course == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(course), status_code
        case 'POST':
            if request.json is None or 'name' not in request.json:
                raise err.MissingParameterError()
            else:
                name = request.json['name']
                test = services.create_course(
                    unit_of_work.SqlAlchemyUnitOfWork(), name)
            return jsonify(test), 201


@app.route('/course/<course_id>', methods=['GET', 'PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def get_course_by_id(course_id):
    method = request.method
    match method:
        case 'GET':
            course = services.get_course_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                course_id
            )
            if course == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(course), status_code
        case 'PUT':
            condition1 = request.json is None
            condition2 = 'name' not in request.json
            if condition1 or condition2:
                raise err.MissingParameterError()
            else:
                course = services.update_course(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    course_id,
                    request.json['name']
                )
                if course == {}:
                    status_code = 404
                else:
                    status_code = 200
                return jsonify(course), status_code
        case 'DELETE':
            services.delete_course(
                unit_of_work.SqlAlchemyUnitOfWork(),
                course_id
            )
            status_code = 204
            return jsonify(None), status_code


@app.route('/student', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_students():
    method = request.method
    match method:
        case 'GET':
            student = services.get_students(
                unit_of_work.SqlAlchemyUnitOfWork()
            )
            if student == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(student), status_code
        case 'POST':
            condition1 = 'name' not in request.json
            condition2 = "learning_style" in request.json
            if request.json is None or condition1:
                raise err.MissingParameterError()
            else:
                student = services.create_student(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    request.json['name'],
                    request.json['learning_style'] if condition2 else None
                )
            if student == {}:
                status_code = 404
            else:
                status_code = 201
            return jsonify(student), status_code


@app.route('/student/<student_id>', methods=['GET', 'PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def get_student_by_id(student_id):
    method = request.method
    match method:
        case 'GET':
            student = services.get_student_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id
            )
            if student == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(student), status_code
        case 'PUT':
            condition1 = request.json is None
            condition2 = 'name' not in request.json
            condition3 = 'learning_style' in request.json
            if condition1 or condition2:
                raise err.MissingParameterError()
            else:
                student = services.update_student(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    student_id,
                    request.json['name'],
                    request.json['learning_style'] if condition3 else None
                )
            if student == {}:
                status_code = 404
            else:
                status_code = 201
            return jsonify(student), status_code
        case 'DELETE':
            services.delete_student(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id
            )
            status_code = 204
            return jsonify(None), status_code


@app.route('/topic', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_topics():
    method = request.method
    match method:
        case 'GET':
            topic = services.get_topics(
                unit_of_work.SqlAlchemyUnitOfWork()
            )
            if topic == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(topic), status_code
        case 'POST':
            condition1 = request.json is None
            condition2 = 'name' not in request.json
            condition3 = 'course_id' not in request.json
            condition4 = 'order_depth' not in request.json
            condition5 = 'ancestor_id' in request.json
            condition6 = 'prerequisite_id' in request.json
            if condition1 or condition2 or condition3 or condition4:
                raise err.MissingParameterError()
            topic = services.create_topic(
                unit_of_work.SqlAlchemyUnitOfWork(),
                request.json['name'],
                request.json['course_id'],
                request.json['order_depth'],
                request.json['ancestor_id'] if condition5 else None,
                request.json['prerequisite_id'] if condition6 else None
            )
            if topic == {}:
                status_code = 404
            elif 'error' in topic:
                status_code = 400
            else:
                status_code = 201
            return jsonify(topic), status_code


@app.route('/topic/<course_id>/<order_depth>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_topics_for_course(course_id, order_depth):
    topics = services.get_topics_for_course(
        unit_of_work.SqlAlchemyUnitOfWork(),
        course_id,
        order_depth
    )
    if topics == {}:
        status_code = 404
    else:
        status_code = 200
    return jsonify(topics), status_code


@app.route('/topic/<course_id>/<order_depth>/<ancestor_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_topics_for_course_and_ancestor(course_id, order_depth, ancestor_id):
    topics = services.get_topics_for_course_and_ancestor(
        unit_of_work.SqlAlchemyUnitOfWork(),
        course_id,
        order_depth,
        ancestor_id
    )
    if topics == {}:
        status_code = 404
    else:
        status_code = 200
    return jsonify(topics), status_code


@app.route('/topic/<topic_id>', methods=['GET', 'PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def get_topic_by_id(topic_id):
    method = request.method
    match method:
        case 'GET':
            topic = services.get_topic_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                topic_id
            )
            if topic == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(topic), status_code
        case 'PUT':
            condition1 = request.json is None
            condition2 = 'name' not in request.json
            condition3 = 'course_id' not in request.json
            condition4 = 'order_depth' not in request.json
            condition5 = 'ancestor_id' in request.json
            condition6 = 'prerequisite_id' in request.json
            if condition1 or condition2 or condition3 or condition4:
                raise err.MissingParameterError()
            topic = services.update_topic(
                unit_of_work.SqlAlchemyUnitOfWork(),
                topic_id,
                request.json['name'],
                request.json['course_id'],
                request.json['order_depth'],
                request.json['ancestor_id'] if condition5 else None,
                request.json['prerequisite_id'] if condition6 else None
            )
            if topic == {}:
                status_code = 404
            else:
                status_code = 201
            return jsonify(topic), status_code
        case 'DELETE':
            services.delete_topic(
                unit_of_work.SqlAlchemyUnitOfWork(),
                topic_id
            )
            status_code = 204
            return jsonify(None), status_code

if __name__ == '__main__':
    app.run(port=5000, debug=True)