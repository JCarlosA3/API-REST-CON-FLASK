from flask import Flask, jsonify, request
from db import get, post, put, delete

app = Flask(__name__)

# ------------------------
# RUTA PRINCIPAL
# ------------------------
@app.route("/")
def main():
    return jsonify({"mensaje": "API REST con Flask"})


# ------------------------
# RUTA GET - OBTENER USUARIOS
# ------------------------
@app.route("/users", methods=["GET"])
def users():
    return jsonify(get())


# ------------------------
# RUTA POST - CREAR USUARIO
# ------------------------
@app.route("/users", methods=["POST"])
def postUser():
    data = request.json
    return jsonify(post(data)), 201


# ------------------------
# RUTA PUT - ACTUALIZAR USUARIO
# ------------------------
@app.route("/users/<id>", methods=["PUT"])
def putUser(id):
    data = request.json
    return jsonify(put(id, data))


# ------------------------
# RUTA DELETE - ELIMINAR USUARIO
# ------------------------
@app.route("/users/<id>", methods=["DELETE"])
def deleteUser(id):
    return jsonify(delete(id))


# ------------------------
# EJECUCIÓN DIRECTA
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
