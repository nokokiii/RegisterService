import asyncio
import logging as log

from flask import Flask, jsonify, request

import src.status_code as sc
from src.logic import Logic
from src.db_driver import init_db


app = Flask(__name__)
logic = Logic()
asyncio.run(init_db())


@app.errorhandler(404)
def page_not_found():
    return jsonify({'message': 'Endpoint not found'}), sc.NOT_FOUND


@app.get("/users")
def get_users():
    response = logic.users_list_controller()

    if "status" not in response:
        log.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR

    if response["status"] == "OK":
        return jsonify(response), sc.OK
    elif response["status"] == "ERR":
        log.error(response["response"], response["error"])
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    log.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR


@app.get("/users/<user_id>")
def get_user(user_id: str):
    response = logic.user_controller(user_id)

    if "status" not in response:
        log.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    
    if response["status"] == "OK":
        return jsonify(response), sc.OK
    elif response["status"] == "ERR":
        log.error(response["response"], response["error"])
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    elif response["status"] == "No_DATA":
        return jsonify(response), sc.NOT_FOUND
    log.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR


@app.post("/users")
def create_user():
    data = request.get_json()
    response = logic.create_user_controller(data)

    if "status" not in response:
        log.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    
    if response["status"] == "OK":
        return jsonify(response), sc.CREATED
    elif response["status"] == "ERR":
        log.error(response["response"], response["error"])
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    log.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR



@app.patch("/users/<user_id>")
def update_user(user_id: str):
    data = request.get_json()
    response = logic.update_user_controller(user_id, data)

    if "status" not in response:
        log.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    
    if response["status"] == "OK":
        return jsonify(response), sc.ACCEPTED
    elif response["status"] == "ERR":
        log.error(response["response"], response["error"])
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    log.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR


@app.delete("/users/<user_id>")
def delete_user(user_id: str):
    response = logic.delete_user_controller(user_id)

    if "status" not in response:
        log.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR

    if response["status"] == "OK":
        return jsonify({"message": "User Deleted"}), sc.OK
    elif response["status"] == "ERR":
        log.error(response["response"], response["error"])
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    log.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR


if __name__ == "__main__":
    app.run(debug=True)
