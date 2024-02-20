from flask import Flask
from .business_logic import Logic

app = Flask(__name__)
logic = Logic()


@app.route("/users", methods=["GET"])
def get_users():
    return logic.users_list_controller()


@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    return logic.user_controller(user_id)


@app.route("/users", methods=["POST"])
def create_user():
    return logic.create_user_controller()


@app.route("/users/<user_id>", methods=["PATCH"])
def update_user(user_id):
    return logic.update_user_controller(user_id)


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return logic.delete_user_controller(user_id)
