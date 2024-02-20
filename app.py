from flask import Flask, jsonify, request

from .business_logic import Logic

app = Flask(__name__)
logic = Logic()


@app.errorhandler(404)
def page_not_found():
    return jsonify({'message': 'Endpoint not found'}), 404


@app.route("/users", methods=["GET"])
def get_users():
    return logic.users_list_controller()


@app.route("/users/<str:user_id>", methods=["GET"])
def get_user(user_id):
    return logic.user_controller(user_id)


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    return logic.create_user_controller(data)


@app.route("/users/<str:user_id>", methods=["PATCH"])
def update_user(user_id: str):
    data = request.get_json()
    return logic.update_user_controller(user_id, data)


@app.route("/users/<str:user_id>", methods=["DELETE"])
def delete_user(user_id: str):
    return logic.delete_user_controller(user_id)
