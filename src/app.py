import asyncio

from quart import Quart, jsonify, request

import src.status_code as sc
from src.logic import Logic
from src.db_driver import init_db


app = Quart(__name__)
logic = Logic(app.logger)
asyncio.run(init_db())


@app.before_serving
async def startup():
    await init_db()


@app.errorhandler(404)
async def page_not_found(e):
    app.loggin.error(e)
    return jsonify({'message': 'Endpoint not found'}), sc.NOT_FOUND


@app.get("/users")
async def get_users():
    """
    Handle the GET request to get the list of users.
    """
    response = await logic.users_list_controller()

    if "status" not in response:
        app.logger.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR

    if response["status"] == "OK":
        return jsonify(response["response"]), sc.OK
    elif response["status"] == "ERR":
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    app.logger.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR


@app.get("/users/<user_id>")
async def get_user(user_id: str):
    """
    Handle the GET request to get the user by ID.
    """
    response = await logic.user_controller(user_id)

    if "status" not in response:
        app.logger.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    
    if response["status"] == "OK":
        return jsonify(response), sc.OK
    elif response["status"] == "ERR":
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    elif response["status"] == "No_DATA":
        return jsonify(response), sc.NOT_FOUND
    app.logger.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR


@app.post("/users")
async def create_user():
    data = request.get_json()
    response = await logic.create_user_controller(data)

    if "status" not in response:
        app.logger.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    
    
    if response["status"] == "OK":
        return jsonify(response), sc.CREATED
    elif response["status"] == "BAD_REQUEST":
        return jsonify(response), sc.BAD_REQUEST
    elif response["status"] == "ERR":
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    app.logger.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR



@app.patch("/users/<user_id>")
async def update_user(user_id: str):
    data = request.get_json()
    response = await logic.update_user_controller(user_id, data)

    if "status" not in response:
        app.logger.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    
    if response["status"] == "OK":
        return jsonify(response), sc.ACCEPTED
    elif response["status"] == "BAD_REQUEST":
        return jsonify(response), sc.BAD_REQUEST
    elif response["status"] == "ERR":
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    app.logger.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR


@app.delete("/users/<user_id>")
async def delete_user(user_id: str):
    response = await logic.delete_user_controller(user_id)

    if "status" not in response:
        app.logger.error(response)
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR

    if response["status"] == "OK":
        return jsonify({"message": "User Deleted"}), sc.OK
    elif response["status"] == "ERR":
        return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR
    app.logger.error(response)
    return jsonify({"message": "Internal Server Error"}), sc.INTERNAL_SERVER_ERROR


if __name__ == "__main__":
    app.run(debug=True)
