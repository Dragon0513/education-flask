from flask import Flask, jsonify, request
from service_layer import services, unit_of_work
from repositories import orm
import errors as err
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)
orm.start_mappers()

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
def handle_exception(err):
    response = {"error": err.description}
    return jsonify(response), err.code


@app.route("/lms/user", methods=['POST'])
@cross_origin(supports_credentials=True)
def create_user():
    method = request.method
    match method:
        case 'POST':
            name = request.json["name"],
            university = request.json["university"],
            lms_user_id = request.json["lms_user_id"],
            role = request.json["role"].lower()
            available_roles = ['admin', 'course_creator', 'student', 'teacher']
            if role not in available_roles:
                raise err.NoValidRoleError()
            else:
                user = services.create_user(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    name,
                    university,
                    lms_user_id,
                    role
                )
                status_code = 201
                return jsonify(user), status_code


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
