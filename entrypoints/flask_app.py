from flask import Flask, jsonify

from repositories import orm

app = Flask(__name__)
orm.start_mappers()

@app.route("/")
def func():
    return jsonify(),200