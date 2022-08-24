from flask import Flask, jsonify, request
from service_layer import services, unit_of_work
from repositories import orm
import errors as err

app = Flask(__name__)
orm.start_mappers()


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
