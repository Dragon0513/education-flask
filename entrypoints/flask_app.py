from flask import Flask, jsonify, request
from service_layer import services, unit_of_work
from repositories import orm

app = Flask(__name__)
orm.start_mappers()


@app.route("/learningPath")
def get_learning_path():
    if request.json is None or 'studentId' not in request.json:
        status_code = 404
        return jsonify(), status_code
    else:
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

        if learning_path is ValueError:
            status_code = 400
            return jsonify({"Error": "Something is wrong..."}), status_code
        else:
            dict = {'learningPath': learning_path}
            status_code = 200
            return jsonify(dict), status_code
