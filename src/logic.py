from src.db import Database


class Logic:
    def __init__(self, logger):
        self.db = Database()
        self.logger = logger

    async def users_list_controller(self) -> dict:
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
            db_res = await self.db.get_users()
        except Exception as e:
            self.logger.error("There was problem while getting data from database: ", str(e))
            return {"status": "ERR", "response": "There was a problem while getting users", "error": str(e)}        
        try:
            if db_res and "status" in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": db_res["result"]}
                elif db_res["status"] == "ERR":
                    self.logger.error("There was a problem while getting users (prob db side problem): ", db_res)
                    return {"status": "ERR", "response": db_res, "error": "There was a problem while getting users"}
            self.logger.error("There was a problem while getting users (missing status in db_res): ", db_res)
            return {"status": "ERR", "response": db_res, "error": "There was a problem while getting users"}
        except Exception as e:
            self.logger.error("There was problem while parasing db response: ", str(e))
            return {"status": "ERR", "response": "There was a problem while getting users", "error": str(e)}
              

    async def user_controller(self, user_id: str) -> dict:
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
            db_res = await self.db.get_user(user_id)
        except Exception as e:
            self.logger.error("There was problem while getting data from database: ", str(e))
            return {"status": "ERR", "response": "There was a problem while getting the user", "error": str(e)}
        
        try:
            if db_res and "status" in db_res:
                if "result" in db_res and len(db_res["result"]) > 0 and db_res["status"] == "OK":
                    return {"status": "OK", "response": db_res["result"]}
                elif "result" in db_res and db_res["status"] != "ERR" and len(db_res["result"]) == 0:
                    return {"status": "No_DATA", "response": "The user with provided id does not exist"}
                elif db_res["status"] == "ERR":
                    self.logger.error("There was a problem while getting the user (prob db side problem): ", db_res)
                    return {"status": "ERR", "response": db_res, "error": "There was a problem while getting the user"}
            self.logger.error("There was a problem while getting the user (missing status in db_res): ", db_res)
            return {"status": "ERR", "response": db_res, "error": "There was a problem while getting the user"}
        except Exception as e:
            self.logger.error("There was problem while parasing db response: ", str(e))
            return {"status": "ERR", "response": "There was a problem while getting the user", "error": str(e)}


    async def create_user_controller(self, data: dict) -> dict:
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
        if any(key not in data for key in required_keys):
            return {"status": "BAD_REQUEST", "response": "The provided data is missing values"}

        try:
            db_res = await self.db.create_user(data)
        except Exception as e:
            self.logger.error("There was problem while getting data from database: ", str(e))
            return {"status": "ERR", "response": "There was a problem while creating the user", "error": str(e)}
        
        try:
            if db_res and "status" in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": "User created"}
                elif db_res["status"] == "ERR":
                    self.logger.error("There was a problem while creating the user (prob db side problem): ", db_res)
                    return {"status": "ERR", "response": db_res, "error": "There was a problem while creating the user"}
            self.logger.error("There was a problem while creating the user (missing status in db_res): ", db_res)
            return {"status": "ERR", "response": db_res, "error": "There was a problem while creating the user"}
        except Exception as e:
            self.logger.error("There was problem while parasing db response: ", str(e))
            return {"status": "ERR", "response": "There was a problem while creating the user", "error": str(e)}



    async def update_user_controller(self, user_id: str, data: dict) -> dict:
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
        is_firstname = "firstName" in data
        is_lastname = "lastName" in data
        is_birthyear = "birthYear" in data
        is_group = "group" in data


        if not any([is_firstname, is_lastname, is_birthyear, is_group]):
            return {"status": "BAD_REQUEST", "response": "The provided data is missing values"}

        try:
            db_res = await self.db.update_user(user_id, is_firstname, is_lastname, is_birthyear, is_group, data)
        except Exception as e:
            self.logger.error("There was problem while getting data from database: ", str(e))
            return {"status": "ERR", "response": "There was a problem while updating the user", "error": str(e)}

        try:
            if db_res and "status" in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": "User updated"}
                elif db_res["status"] == "ERR":
                    self.logger.error("There was a problem while updating the user (prob db side problem): ", db_res)
                    return {"status": "ERR", "response": db_res, "error": "There was a problem while updating the user"}
            self.logger.error("There was a problem while updating the user (missing status in db_res): ", db_res)
            return {"status": "ERR", "response": db_res, "error": "There was a problem while updating the user"}
        except Exception as e:
            self.logger.error("There was problem while parasing db response: ", str(e))
            return {"status": "ERR", "response": "There was a problem while updating the user", "error": str(e)}


    async def delete_user_controller(self, user_id: str) -> dict:
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
            db_res = await self.db.delete_user(user_id)
        except Exception as e:
            self.logger.error("There was problem while getting data from database: ", str(e))
            return {"status": "ERR", "response": "There was a problem while deleting the user", "error": str(e)}
        try:
            if db_res and "status" in db_res:
                if db_res["status"] == "OK":
                    return {"status": "OK", "response": "User deleted"}
                elif db_res["status"] == "ERR":
                    self.logger.error("There was a problem while deleting the user (prob db side problem): ", db_res)
                    return {"status": "ERR", "response": db_res, "error": "There was a problem while deleting the user"}
            self.logger.error("There was a problem while deleting the user (missing status in db_res): ", db_res)
            return {"status": "ERR", "response": db_res, "error": "There was a problem while deleting the user"}
        except Exception as e:
            self.logger.error("There was problem while parasing db response: ", str(e))
            return {"status": "ERR", "response": db_res, "error": "There was a problem while deleting the user"}
    