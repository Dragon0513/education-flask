from zoneinfo import available_timezones
from flask import Flask, jsonify, request
from service_layer import services, unit_of_work
from repositories import orm
import errors as err

app = Flask(__name__)
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


@app.route("/learningPath")
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


@app.route("/logs/frontend", methods=['POST', 'GET'])
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
