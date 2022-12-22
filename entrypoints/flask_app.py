from functools import wraps
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
# app.config["SESSION_USE_SIGNER"] = True
# if os.environ.get('FLASK_ENV') == 'production': # only set secure cookie in production: will only allow cookie transmission in https
#     app.config["SESSION_COOKIE_SECURE"] = True
# else:
#     app.config["SESSION_COOKIE_SECURE"] = False

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
    if isinstance(ex, err.AException):
        response = make_response(ex.message, ex.code)
        return response
    else:
        response = make_response(str(err),500)
    return response

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
            state_jwt = request.cookies.get('state')
            if state_jwt is None:
                raise err.StateNotMatchingError()

            if not JWTKeyManagement.verify_jwt_payload(JWTKeyManagement.verify_jwt(state_jwt), verify_nonce=False):
                raise err.UnauthorizedError()
            state = JWTKeyManagement.verify_jwt(state_jwt)


            return f(state, *args, **kws)            
    return decorated_function

@app.route("/learningPath")
@authorize
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


# loginmask or get cookie for frontend if end of OIDC Login workflow
@app.route('/login', methods=['POST'])
def login():
    return services.get_login(request, tool_conf, session=session)

@app.route('/lti_launch/', methods=['POST'])
def lti_launch():
    return services.get_lti_launch(request, tool_conf, session=session)

@app.route('/lti_login/', methods=['POST'])
def lti_login():
    return services.get_oidc_login(request, tool_conf, session=session)

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

if __name__ == '__main__':
    app.run(port=5000, debug=True)