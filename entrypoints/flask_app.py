import os
from zoneinfo import available_timezones

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_caching import Cache

import errors as err
from flask import redirect
from repositories import orm
from service_layer import services, unit_of_work
from pylti1p3.contrib.flask import FlaskOIDCLogin, FlaskMessageLaunch, FlaskRequest, FlaskCacheDataStorage
from pylti1p3.deep_link_resource import DeepLinkResource
from pylti1p3.grade import Grade
from pylti1p3.lineitem import LineItem
from pylti1p3.tool_config import ToolConfJsonFile
from pylti1p3.registration import Registration

from service_layer.lti.config.ToolConfigJson import ToolConfigJson
from service_layer.lti.OIDCLogin import OIDCLogin


app = Flask(__name__)
CORS(app, supports_credentials=True)
orm.start_mappers()
cache = Cache(app)

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

def get_lti_config_path():
    return os.path.abspath(os.path.join(app.root_path, '../configs/lti_config.json'))

def get_launch_data_storage():
    return FlaskCacheDataStorage(cache)

@app.errorhandler(Exception)
def handle_exception(err):
    response = {"error": err.args[0]}
    return jsonify(response), err.code


@app.route("/learningPath")
@cross_origin(supports_credentials=True)
def get_learning_path():
    if request.json is None or 'studentId' not in request.json:
        raise err.MissingParameterError()
    else:
        try:
            if 'learningStyle' in request.json:
                learning_path = services.get_learning_path(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    request.json["studentId"],
                    request.json["learningStyle"]
                )
            else:
                learning_path = services.get_learning_path(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    request.json["studentId"]
                )
        except (err.WrongLearningStyleNumberError,
                err.WrongLearningStyleDimensionError) as e:
            raise e

        dict = {'learningPath': learning_path}
        status_code = 200
        return jsonify(dict), status_code
@app.route('/lti_launch/', methods=['POST'])
def lti_launch():
    return redirect('http://localhost:8080')

@app.route('/lti_login/', methods=['GET', 'POST'])
def lti_login():
    tool_conf = ToolConfigJson(get_lti_config_path())
    launch_data_storage = get_launch_data_storage()

    target_link_uri = request.form['target_link_uri']
    if not target_link_uri:
        raise Exception('Missing "target_link_uri" param')


    # oidc_login = FlaskOIDCLogin(request, tool_conf, launch_data_storage=launch_data_storage)
    oidc_login = OIDCLogin(request, tool_conf, launch_data_storage=launch_data_storage)
    return oidc_login\
        .check_auth()\
        .login()

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
            print(type(request.json))
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
