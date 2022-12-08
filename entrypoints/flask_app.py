from flask import Flask, jsonify, request
from service_layer import services, unit_of_work
from repositories import orm
import errors as err
from flask_cors import CORS, cross_origin
from sqlalchemy.exc import IntegrityError

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


@app.route("/learningElement", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_learning_elements():
    method = request.method
    match method:
        case 'GET':
            try:
                learning_elements = services.get_learning_elements(
                    unit_of_work.SqlAlchemyUnitOfWork()
                )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if learning_elements == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(learning_elements), status_code
        case 'POST':
            try:
                condition1 = request.json is None
                condition2 = 'name' not in request.json
                condition3 = 'classification' not in request.json
                condition4 = 'ancestor_id' not in request.json
                condition5 = 'order_depth' not in request.json
                if condition1 or condition2 or condition3 or condition4 or condition5:
                    raise err.MissingParameterError()
                else:
                    learning_element = services.create_element(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        request.json['name'],
                        request.json['classification'],
                        request.json['ancestor_id'],
                        request.json['order_depth'],
                        request.json['prerequisite_id'] if 'prerequisite_id' in request.json else None
                    )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e
            if type(learning_element) is IntegrityError:
                raise err.ForeignKeyViolation()
            elif learning_element == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(learning_element), status_code


@app.route("/learningElement/<element_id>", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_learning_element_by_id(element_id):
    try:
        learning_elements = services.get_learning_element_by_id(
            unit_of_work.SqlAlchemyUnitOfWork(),
            element_id
        )
    except (err.WrongLearningStyleNumberError,
            err.WrongLearningStyleDimensionError) as e:
        raise e

    status_code = 200
    return jsonify(learning_elements), status_code


@app.route('/module', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_modules():
    method = request.method
    match method:
        case 'GET':
            try:
                module = services.get_modules(
                    unit_of_work.SqlAlchemyUnitOfWork()
                )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if module == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(module), status_code
        case 'POST':
            if request.json is None or 'name' not in request.json:
                raise err.MissingParameterError()
            else:
                name = request.json['name']
                test = services.create_course(
                    unit_of_work.SqlAlchemyUnitOfWork(), name)
            return jsonify(test), 201


@app.route('/module/<module_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_module_by_id(module_id):
    try:
        module = services.get_module_by_id(
            unit_of_work.SqlAlchemyUnitOfWork(),
            module_id
        )
    except (err.WrongLearningStyleNumberError,
            err.WrongLearningStyleDimensionError) as e:
        raise e

    if module == {}:
        status_code = 404
    else:
        status_code = 200
    return jsonify(module), status_code


@app.route('/student', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_students():
    method = request.method
    match method:
        case 'GET':
            try:
                student = services.get_students(
                    unit_of_work.SqlAlchemyUnitOfWork()
                )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if student == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(student), status_code
        case 'POST':
            try:
                if request.json is None or 'name' not in request.json:
                    raise err.MissingParameterError()
                else:
                    name = request.json['name']
                    student = services.create_student(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        name
                    )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if student == {}:
                status_code = 404
            else:
                status_code = 201
            return jsonify(student), status_code


@app.route('/student/<student_id>', methods=['GET', 'PUT'])
@cross_origin(supports_credentials=True)
def get_student_by_id(student_id):
    method = request.method
    match method:
        case 'GET':
            try:
                student = services.get_student_by_id(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    student_id
                )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if student == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(student), status_code
        case 'PUT':
            try:
                if request.json is None or 'name' not in request.json:
                    raise err.MissingParameterError()
                else:
                    student = services.update_student(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student_id,
                        request.json['name'],
                        request.json['learning_style'] if 'learning_style' in request.json else None
                    )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if student == {}:
                status_code = 404
            else:
                status_code = 201
            return jsonify(student), status_code


@app.route('/topic', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_topics():
    method = request.method
    match method:
        case 'GET':
            try:
                topic = services.get_topics(
                    unit_of_work.SqlAlchemyUnitOfWork()
                )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if topic == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(topic), status_code
        case 'POST':
            try:
                condition1 = request.json is None
                condition2 = 'name' not in request.json
                condition3 = 'module_id' not in request.json
                condition4 = 'order_depth' not in request.json
                if condition1 or condition2 or condition3 or condition4:
                    raise err.MissingParameterError()
                topic = services.create_topic(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    request.json['name'],
                    request.json['module_id'],
                    request.json['order_depth'],
                    request.json['ancestor_id'] if 'ancestor_id' in request.json else None,
                    request.json['prerequisite_id'] if 'prerequisite_id' in request.json else None
                )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if topic == {}:
                status_code = 404
            elif 'error' in topic:
                status_code = 400
            else:
                status_code = 201
            return jsonify(topic), status_code


@app.route('/topic/<module_id>/<order_depth>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_topics_for_module(module_id, order_depth):
    try:
        topics = services.get_topics_for_module(
            unit_of_work.SqlAlchemyUnitOfWork(),
            module_id,
            order_depth
        )
    except (err.WrongLearningStyleNumberError,
            err.WrongLearningStyleDimensionError) as e:
        raise e

    if topics == {}:
        status_code = 404
    else:
        status_code = 200
    return jsonify(topics), status_code


@app.route('/topic/<module_id>/<order_depth>/<ancestor_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_topics_for_module_and_ancestor(module_id, order_depth, ancestor_id):
    try:
        topics = services.get_topics_for_module_and_ancestor(
            unit_of_work.SqlAlchemyUnitOfWork(),
            module_id,
            order_depth,
            ancestor_id
        )
    except (err.WrongLearningStyleNumberError,
            err.WrongLearningStyleDimensionError) as e:
        raise e

    if topics == {}:
        status_code = 404
    else:
        status_code = 200
    return jsonify(topics), status_code


@app.route('/topic/<topic_id>', methods=['GET', 'PUT'])
@cross_origin(supports_credentials=True)
def get_topic_by_id(topic_id):
    method = request.method
    match method:
        case 'GET':
            try:
                topic = services.get_topic_by_id(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    topic_id
                )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if topic == {}:
                status_code = 404
            else:
                status_code = 200
            return jsonify(topic), status_code
        case 'PUT':
            try:
                condition1 = request.json is None
                condition2 = 'name' not in request.json
                condition3 = 'module_id' not in request.json
                condition4 = 'order_depth' not in request.json
                if condition1 or condition2 or  condition3 or condition4:
                    raise err.MissingParameterError()
                topic = services.update_topic(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    topic_id,
                    request.json['name'],
                    request.json['module_id'],
                    request.json['order_depth'],
                    request.json['ancestor_id'] if 'ancestor_id' in request.json else None,
                    request.json['prerequisite_id'] if 'prerequisite_id' in request.json else None
                )
            except (err.WrongLearningStyleNumberError,
                    err.WrongLearningStyleDimensionError) as e:
                raise e

            if topic == {}:
                status_code = 404
            else:
                status_code = 201
            return jsonify(topic), status_code
