from flask import Flask, jsonify, request
from db import get, post, put, delete

app = Flask(__name__)


@app.route("/")
def main():
    return jsonify({"mensaje": "API REST con Flask"})


@app.route("/users", methods=["GET"])
def users():
    return jsonify(get())


@app.route("/users", methods=["POST"])
def postUser():
    data = request.json
    return jsonify(post(data)), 201


@app.route("/users/<id>", methods=["PUT"])
def putUser(id):
    data = request.json
    return jsonify(put(id, data))


@app.route("/users/<id>", methods=["DELETE"])
def deleteUser(id):
    return jsonify(delete(id))


if __name__ == "__main__":
    app.run(debug=True)
