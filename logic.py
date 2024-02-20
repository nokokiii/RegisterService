import asyncio

from flask import jsonify

from .db import db


class Logic:
    def users_list_controller(self) -> tuple[[], int]:
        """
        Return list of all users
        """
        query = "SELECT * FROM Users"
        users = asyncio.run(db(query))
        return jsonify(users), 200

    def user_controller(self, user_id: str) -> tuple[[], int]:
        """
        Return user by id
        """
        try:
            query = f"SELECT * FROM ONLY Users:{user_id}"
            if user_info := asyncio.run(db(query)):
                return jsonify(user_info), 200
            else:
                return jsonify({"message": "User with provided id doesn't exist"}), 404
        except:
            return jsonify({"message": "There was a problem while getting user"}), 500

    def create_user_controller(self, data: dict) -> tuple[[], int]:
        """
        Create new user
        """
        required_keys = ['firstName', 'lastName', 'birthYear', 'group']
        if not all(key in data for key in required_keys):
            return jsonify({"message": "The provided data is not correct"}), 403

        try:
            query = f'CREATE Users SET firstName = "{data["firstName"]}", lastName = "{data["lastName"]}", birthYear = "{data["birthYear"]}", group = "{data["group"]};'
            asyncio.run(db(query))
            return jsonify({"message": "User created"}), 201
        except:
            return jsonify({"message": "There was a problem while updating the user"}), 500

    def update_user_controller(self, user_id: str, data: dict) -> tuple[[], int]:
        """
        Update user
        """
        query = f"UPDATE Users:{user_id} SET "
        is_correct = False

        if "firstName" in data.keys():
            query += f'firstName = "{data["firstName"]}"'
            is_correct = True
        if "lastName" in data.keys():
            query += f'lastName = "{data["lastName"]}"'
            is_correct = True
        if "birthYear" in data.keys():
            query += f'birthYear = "{data["birthYear"]}"'
            is_correct = True
        if "group" in data.keys():
            query += f'group = "{data["group"]}"'
            is_correct = True

        if not is_correct:
            return jsonify({"message": "The provided data is invalid"}), 403

        query = query[:-1] + f" WHERE id = Users:{user_id};"

        try:
            res = asyncio.run(db(query))
        except:
            return jsonify({"message": "There was problem updating the user"}), 500

        if not res:
            return jsonify({"message": "The user with provided id does not exist"}), 404
        return jsonify({"message": "User updated"}), 200

    def delete_user_controller(self, user_id: str) -> tuple[[], int]:
        """
        Delete user
        """
        try:
            query = f"DELETE ONLY Users:{user_id};"
            asyncio.run(db(query))
            return jsonify({"message": "User deleted"}), 200
        except:
            return jsonify({"message": "There was a problem while deleting user"}), 500
