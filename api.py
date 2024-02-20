from flask import Flask, jsonify, Response, request

CREATED = 201
BAD_REQUEST = 400
SUCCESS = 200

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    """
    Zwraca listę zarejestrowanych użytkowników
    """
    # return get_all_users()
    return jsonify({"users": []}), SUCCESS


@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    """
    Zwraca dane użytkownika
    """
    # return get_user(id)
    return jsonify({}), SUCCESS


@app.route("/users", methods=["POST"])
def create_user():
    """
    Tworzy nowego użytkownika
    """
    # return create_user()
    return Response(status=CREATED)


@app.route("/users/<id>", methods=["PATCH"])
def update_user(id):
    """
    Aktualizuje dane użytkownika
    """
    # status_code = update_user(id)
    return Response(status=SUCCESS)


@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    """
    Usuwa użytkownika
    """
    # status_code = delete_user(id)
    return Response(status=SUCCESS)
