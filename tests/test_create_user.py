from unittest.mock import patch, Mock

import aiounittest

from src.logic import Logic


class CreateUser(aiounittest.AsyncTestCase):    
    @patch('src.db.Database.create_user')
    async def test_create_user_controller_ok(self, mock_create_user):
        mock_create_user.return_value = {"status": "OK", "result": {}}
        
        logic = Logic(logger=Mock())
        example_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1999, "group": "admin"}
        response = await logic.create_user_controller(data=example_data)
        
        self.assertEqual(response["status"], "OK")
        self.assertEqual(response["response"], "User created")
    

    @patch('src.db.Database.create_user')
    async def test_create_user_controller_bad_request(self, mock_create_user):        
        logic = Logic(logger=Mock())
        example_bad_data = {"lastName": "Doe", "birthYear": 1999, "group": "admin"}
        response = await logic.create_user_controller(data=example_bad_data)

        self.assertEqual(response["status"], "BAD_REQUEST")
        self.assertEqual(response["response"], "The provided data is missing values")


    @patch('src.db.Database.create_user')
    async def test_create_user_controller_err(self, mock_create_user):
        mock_create_user.return_value = {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"}
        
        logic = Logic(logger=Mock())
        example_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1999, "group": "admin"}
        response = await logic.create_user_controller(data=example_data)
               
        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"})
        self.assertEqual(response["error"], "There was a problem while creating the user")

    
    @patch('src.db.Database.create_user')
    async def test_create_user_controller_no_status(self, mock_create_user):
        mock_create_user.return_value = {"example": "Example response"}

        logic = Logic(logger=Mock())
        example_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1999, "group": "admin"}
        response = await logic.create_user_controller(data=example_data)

        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"example": "Example response"})
        self.assertEqual(response["error"], "There was a problem while creating the user")
