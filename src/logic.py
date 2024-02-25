from src.db import Database


class Logic:
    def __init__(self):
        self.db = Database()

    def users_list_controller(self) -> dict:
        """
        Return the list of users from the database.

        Returns:
            dict: A dictionary containing the status and response of the operation.
                - If the operation is successful, the status will be "OK" and the response will contain the user list.
                - If there is an error, the status will be "ERR" and the response will contain an error message.
        
        Raises:
            Exception: If there is a problem while getting users from the database.
        """
        try:
            if db_res := self.db.get_users()[0] and db_res and "status" not in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": db_res["response"]}
                elif db_res["status"] == "ERR":
                    return {"status": "ERR", "response": db_res["response"], "error": "There was a problem while getting users"}
        except Exception as e:
            return {"status": "ERR", "response": "There was a problem while getting users", "error": str(e)}
        return {"status": "ERR", "response": db_res, "error": "There was a problem while getting users"}
              

    def user_controller(self, user_id: str) -> dict:
        """
        Return the user information by ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A dictionary containing the status and response of the operation.
                - If the operation is successful, the status will be "OK" and the response will contain the user information.
                - If there is an error, the status will be "ERR" and the response will contain an error message.

        Raises:
            Exception: If there is a problem while getting the user from the database.
        """
        try:
            if db_res := self.db.get_user(user_id)[0] and db_res and "status" not in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": db_res["response"]}
                elif db_res["status"] == "ERR":
                    return {"status": "ERR", "response": db_res["response"], "error": "There was a problem while getting the user"}
                elif len(db_res["results"]) == 0:
                    return {"status": "No_DATA", "response": "The user with provided id does not exist"}
        except Exception as e:
            return {"status": "ERR", "response": "There was a problem while getting the user", "error": str(e)}
        return {"status": "ERR", "response": db_res, "error": "There was a problem while getting the user"}


    def create_user_controller(self, data: dict) -> dict:
        """
        Create user in the database.

        Args:
            data (dict): The user data.

        Returns:
            dict: A dictionary containing the status and response of the operation.
                - If the operation is successful, the status will be "OK" and the response will contain a success message.
                - If there is an error, the status will be "ERR" and the response will contain an error message.

        Raises:
            Exception: If there is a problem while creating the user in the database.
        """
        required_keys = ['firstName', 'lastName', 'birthYear', 'group']
        if not all(key in data for key in required_keys):
            return {"status": "BAD_REQUEST", "response": "The provided data is missing values"}

        try:
            if db_res := self.db.create_user(data)[0] and db_res and "status" not in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": "User created"}
                elif db_res["status"] == "ERR":
                    return {"status": "ERR", "response": db_res["response"], "error": "There was a problem while creating the user"}
        except Exception as e:
            return {"status": "ERR", "response": "There was a problem while creating the user", "error": str(e)}
        return {"status": "ERR", "response": db_res, "error": "There was a problem while creating the user"}


    def update_user_controller(self, user_id: str, data: dict) -> dict:
        """
        Update user in the database.

        Args:
            user_id (str): The ID of the user.
            data (dict): The user data.

        Returns:
            dict: A dictionary containing the status and response of the operation.
                - If the operation is successful, the status will be "OK" and the response will contain a success message.
                - If there is an error, the status will be "ERR" and the response will contain an error message.

        Raises:
            Exception: If there is a problem while updating the user in the database.
        """
        query = f"UPDATE Users:{user_id} SET "

        is_firstname = True if "firstName" in data else "False"
        is_lastname = True if "lastName" in data else "False"
        is_birthyear = True if "birthYear" in data else "False"
        is_group = True if "group" in data else "False"


        if not any([is_firstname, is_lastname, is_birthyear, is_group]):
            return {"status": "BAD_REQUEST", "response": "The provided data is missing values", "error": "The provided data is missing values"}

        try:
            if db_res := self.db.update_user(query, is_firstname, is_lastname, is_birthyear, is_group)[0] and db_res and "status" not in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": "User updated"}
                elif db_res["status"] == "ERR":
                    return {"status": "ERR", "response": db_res["response"], "error": "There was a problem while updating the user"}
        except Exception as e:
            return {"status": "ERR", "response": "There was a problem while updating the user", "error": str(e)}
        return {"status": "ERR", "response": db_res, "error": "There was a problem while updating the user"}


    def delete_user_controller(self, user_id: str) -> dict:
        """
        Delete user from the database.

        Args:
            user_id (str): The ID of the user.
            
        Returns:
            tuple: A tuple containing the status and response of the operation.
                - If the operation is successful, the status will be "OK" and the response will contain a success message.
                - If there is an error, the status will be "ERR" and the response will contain an error message.

        Raises:
            Exception: If there is a problem while deleting the user from the database.
        """
        try:
            if db_res := self.db.delete_user(user_id)[0] and db_res and "status" not in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": "User deleted"}
                elif db_res["status"] == "ERR":
                    return {"status": "ERR", "response": db_res["response"], "error": "There was a problem while deleting the user"}
        except Exception as e:
            return {"status": "ERR", "response": "There was a problem while deleting the user", "error": str(e)}
        return {"status": "ERR", "response": db_res, "error": "There was a problem while deleting the user"}
    