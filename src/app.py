import asyncio

from flask import Flask, jsonify, request

from .logic import Logic
from .db import init_db

app = Flask(__name__)
logic = Logic()
asyncio.run(init_db())


@app.errorhandler(404)
def page_not_found():
    return jsonify({'message': 'Endpoint not found'}), 404


@app.get("/users")
def get_users():
    return logic.users_list_controller()


@app.get("/users/<user_id>")
def get_user(user_id):
    return logic.user_controller(user_id)


@app.post("/users")
def create_user():
    data = request.get_json()
    return logic.create_user_controller(data)


@app.patch("/users/<user_id>")
def update_user(user_id: str):
    data = request.get_json()
    return logic.update_user_controller(user_id, data)


@app.delete("/users/<user_id>")
def delete_user(user_id: str):
    return logic.delete_user_controller(user_id)


if __name__ == "__main__":
    app.run(debug=True)
