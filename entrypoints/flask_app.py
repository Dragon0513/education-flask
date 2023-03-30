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
                        'admin', 'course_creator', 'student', 'teacher']
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
            condition3 = type(request.json['name']) is str
            condition4 = type(request.json['university']) is str
            if condition1 and condition2:
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
            result = {'message': 'Deletion was successful'}
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


@app.route("/user/<user_id>/<lms_user_id>/settings",
           methods=['GET', 'PUT', 'DELETE'])
@cross_origin(supports_credentials=True)
def settings_by_user_id(user_id, lms_user_id):
    method = request.method
    match method:
        case 'GET':
            settings = services.get_settings_for_user(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id
            )
            status_code = 200
            return jsonify(settings), status_code
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

@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>" +
           "/learningCharacteristics",
           methods=['GET', 'DELETE'])
@cross_origin(supports_credentials=True)
def learning_characteristics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case 'GET':
            characteristic = services.get_learning_characteristics(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id
            )
            status_code = 200
            return jsonify(characteristic), status_code
        case 'DELETE':
            characteristic = services.reset_learning_characteristics(
                unit_of_work.SqlAlchemyUnitOfWork(),
                student_id
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
                    if answer != "a":
                        if answer != "b":
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
                    vv_2_f7=ils['vv_2_f7'],
                    vv_5_f19=ils['vv_5_f19'],
                    vv_7_f27=ils['vv_7_f27'],
                    vv_10_f39=ils['vv_10_f39'],
                    vv_11_f43=ils['vv_11_f43'],
                    si_1_f2=ils['si_1_f2'],
                    si_4_f14=ils['si_4_f14'],
                    si_7_f26=ils['si_7_f26'],
                    si_10_f38=ils['si_10_f38'],
                    si_11_f42=ils['si_11_f42'],
                    ar_3_f9=ils['ar_3_f9'],
                    ar_4_f13=ils['ar_4_f13'],
                    ar_6_f21=ils['ar_6_f21'],
                    ar_7_f25=ils['ar_7_f25'],
                    ar_8_f29=ils['ar_8_f29'],
                    sg_1_f4=ils['sg_1_f4'],
                    sg_2_f8=ils['sg_2_f8'],
                    sg_4_f16=ils['sg_4_f16'],
                    sg_10_f40=ils['sg_10_f40'],
                    sg_11_f44=ils['sg_11_f44'],
                    vv_1_f3=ils['vv_1_f3']
                    if 'vv_1_f3' in ils.keys() else None,
                    vv_3_f11=ils['vv_3_f11']
                    if 'vv_3_f11' in ils.keys() else None,
                    vv_4_f15=ils['vv_4_f15']
                    if 'vv_4_f15' in ils.keys() else None,
                    vv_6_f23=ils['vv_6_f23']
                    if 'vv_6_f23' in ils.keys() else None,
                    vv_8_f31=ils['vv_8_f31']
                    if 'vv_8_f31' in ils.keys() else None,
                    vv_9_f35=ils['vv_9_f35']
                    if 'vv_9_f35' in ils.keys() else None,
                    si_2_f6=ils['si_2_f6']
                    if 'si_2_f6' in ils.keys() else None,
                    si_3_f10=ils['si_3_f10']
                    if 'si_3_f10' in ils.keys() else None,
                    si_5_f18=ils['si_5_f18']
                    if 'si_5_f18' in ils.keys() else None,
                    si_6_f22=ils['si_6_f22']
                    if 'si_6_f22' in ils.keys() else None,
                    si_8_f30=ils['si_8_f30']
                    if 'si_8_f30' in ils.keys() else None,
                    si_9_f34=ils['si_9_f34']
                    if 'si_9_f34' in ils.keys() else None,
                    ar_1_f1=ils['ar_1_f1']
                    if 'ar_1_f1' in ils.keys() else None,
                    ar_2_f5=ils['ar_2_f5']
                    if 'ar_2_f5' in ils.keys() else None,
                    ar_5_f17=ils['ar_5_f17']
                    if 'ar_5_f17' in ils.keys() else None,
                    ar_9_f33=ils['ar_9_f33']
                    if 'ar_9_f33' in ils.keys() else None,
                    ar_10_f37=ils['ar_10_f37']
                    if 'ar_10_f37' in ils.keys() else None,
                    ar_11_f41=ils['ar_11_f41']
                    if 'ar_11_f41' in ils.keys() else None,
                    sg_3_f12=ils['sg_3_f12']
                    if 'sg_3_f12' in ils.keys() else None,
                    sg_5_f20=ils['sg_5_f20']
                    if 'sg_5_f20' in ils.keys() else None,
                    sg_6_f24=ils['sg_6_f24']
                    if 'sg_6_f24' in ils.keys() else None,
                    sg_7_f28=ils['sg_7_f28']
                    if 'sg_7_f28' in ils.keys() else None,
                    sg_8_f32=ils['sg_8_f32']
                    if 'sg_8_f32' in ils.keys() else None,
                    sg_9_f36=ils['sg_9_f36']
                    if 'sg_9_f36' in ils.keys() else None,
                    org1_f1=list_k['org1_f1'],
                    org2_f2=list_k['org2_f2'],
                    org3_f3=list_k['org3_f3'],
                    ela1_f4=list_k['ela1_f4'],
                    ela2_f5=list_k['ela2_f5'],
                    ela3_f6=list_k['ela3_f6'],
                    krp1_f7=list_k['krp1_f7'],
                    krp2_f8=list_k['krp2_f8'],
                    krp3_f9=list_k['krp3_f9'],
                    wie1_f10=list_k['wie1_f10'],
                    wie2_f11=list_k['wie2_f11'],
                    wie3_f12=list_k['wie3_f12'],
                    zp1_f13=list_k['zp1_f13'],
                    zp2_f14=list_k['zp2_f14'],
                    zp3_f15=list_k['zp3_f15'],
                    kon1_f16=list_k['kon1_f16'],
                    kon2_f17=list_k['kon2_f17'],
                    kon3_f18=list_k['kon3_f18'],
                    reg1_f19=list_k['reg1_f19'],
                    reg2_f20=list_k['reg2_f20'],
                    reg3_f21=list_k['reg3_f21'],
                    auf1_f22=list_k['auf1_f22'],
                    auf2_f23=list_k['auf2_f23'],
                    auf3_f24=list_k['auf3_f24'],
                    ans1_f25=list_k['ans1_f25'],
                    ans2_f26=list_k['ans2_f26'],
                    ans3_f27=list_k['ans3_f27'],
                    zei1_f28=list_k['zei1_f28'],
                    zei2_f29=list_k['zei2_f29'],
                    zei3_f30=list_k['zei3_f30'],
                    lms1_f31=list_k['lms1_f31'],
                    lms2_f32=list_k['lms2_f32'],
                    lms3_f33=list_k['lms3_f33'],
                    lit1_f34=list_k['lit1_f34'],
                    lit2_f35=list_k['lit2_f35'],
                    lit3_f36=list_k['lit3_f36'],
                    lu1_f37=list_k['lu1_f37'],
                    lu2_f38=list_k['lu2_f38'],
                    lu3_f39=list_k['lu3_f39']
                )
                status_code = 201
                return jsonify(result), status_code
            else:
                raise err.MissingParameterError()

if __name__ == '__main__':
    app.run(port=5000, debug=True)