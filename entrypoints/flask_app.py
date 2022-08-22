from flask import Flask, jsonify, request
from domain.tutoringModel import learning_path
from service_layer import services, unit_of_work
from repositories import orm

app = Flask(__name__)
orm.start_mappers()


@app.route("/learningPath")
def get_learning_path():
    if request.json is None or 'studentId' not in request.json:
        return jsonify(), 404
    else:
        if 'learningStyle' in request.json:
            learning_path = services.get_learning_path(
                unit_of_work.SqlAlchemyUnitOfWork(),
                request.json["learningStyle"]
            )
        else:
            learning_path = services.get_learning_path(
                unit_of_work.SqlAlchemyUnitOfWork()
            )
        dict = {'learningPath': learning_path}
        return jsonify(dict), 200
