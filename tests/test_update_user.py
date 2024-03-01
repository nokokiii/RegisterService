from unittest.mock import patch, Mock

import aiounittest

from src.logic import Logic


class UpdateUser(aiounittest.AsyncTestCase):    
    @patch('src.db.Database.update_user')
    async def test_update_user_controller_ok(self, mock_update_user):
        mock_update_user.return_value = {"status": "OK", "result": {}}
        
        logic = Logic(logger=Mock())
        example_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1999, "group": "admin"}
        response = await logic.update_user_controller(user_id="example_id", data=example_data)
        
        self.assertEqual(response["status"], "OK")
        self.assertEqual(response["response"], "User updated")
    

    @patch('src.db.Database.update_user')
    async def test_user_list_controller_bad_request(self, mock_update_user):
        logic = Logic(logger=Mock())
        example_bad_data = {}
        response = await logic.update_user_controller(user_id="example_id", data=example_bad_data)

        self.assertEqual(response["status"], "BAD_REQUEST")
        self.assertEqual(response["response"], "The provided data is missing values")


    @patch('src.db.Database.update_user')
    async def test_user_list_controller_err(self, mock_update_user):
        mock_update_user.return_value = {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"}
        
        logic = Logic(logger=Mock())
        example_data = {"birthYear": 2000}
        response = await logic.update_user_controller(user_id="example_id", data=example_data)
               
        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"})
        self.assertEqual(response["error"], "There was a problem while updating the user")

    
    @patch('src.db.Database.update_user')
    async def test_user_list_controller_no_status(self, mock_update_user):
        mock_update_user.return_value = {"example": "Example response"}

        logic = Logic(logger=Mock())
        example_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1999, "group": "admin"}
        response = await logic.update_user_controller(user_id="example_id", data=example_data)

        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"example": "Example response"})
        self.assertEqual(response["error"], "There was a problem while updating the user")
