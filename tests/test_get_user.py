from unittest.mock import patch, Mock

import aiounittest

from src.logic import Logic


class GetUser(aiounittest.AsyncTestCase):    
    @patch('src.db.Database.get_user')
    async def test_user_controller_ok(self, mock_get_user):
        mock_get_user.return_value = {"status": "OK", "result": {"id": "example_id", "firstName": "John", "lastName": "Doe", "age": 19, "group": "admin"}}
        
        logic = Logic(logger=Mock())
        response = await logic.user_controller(user_id="example_id")
        
        self.assertEqual(response["status"], "OK")
        self.assertEqual(response["response"], {"id": "example_id", "firstName": "John", "lastName": "Doe", "age": 19, "group": "admin"})
    

    
    @patch('src.db.Database.get_user')
    async def test_user_controller_err(self, mock_get_user):
        mock_get_user.return_value = {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"}
        
        logic = Logic(logger=Mock())
        response = await logic.user_controller(user_id="example_id")

        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"})
        self.assertEqual(response["error"], "There was a problem while getting the user")


    @patch('src.db.Database.get_user')
    async def test_user_controller_no_data(self, mock_get_user):
        mock_get_user.return_value = {"status": "OK", "result": []}
        
        logic = Logic(logger=Mock())
        response = await logic.user_controller(user_id="example_id")
               
        self.assertEqual(response["response"], "The user with provided id does not exist")
        self.assertEqual(response["status"], "No_DATA")

    
    @patch('src.db.Database.get_user')
    async def test_user_controller_no_status(self, mock_get_user):
        mock_get_user.return_value = {"example": "Example response"}

        logic = Logic(logger=Mock())
        response = await logic.user_controller(user_id="example_id")

        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"example": "Example response"})
        self.assertEqual(response["error"], "There was a problem while getting the user")

  
