from unittest.mock import patch, Mock

import aiounittest

from src.logic import Logic


class GetUsers(aiounittest.AsyncTestCase):    
    @patch('src.db.Database.get_users')
    async def test_users_list_controller_ok(self, mock_get_users):
        mock_get_users.return_value = {"status": "OK", "result": [{"user_id": 1, "username": "testuser"}]}
        
        logic = Logic(logger=Mock())
        response = await logic.users_list_controller()
        
        self.assertEqual(response["status"], "OK")
        self.assertEqual(len(response["response"]), 1)
        self.assertEqual(response["response"][0]["username"], "testuser")
    

    @patch('src.db.Database.get_users')
    async def test_users_list_controller_err(self, mock_get_users):
        mock_get_users.return_value = {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"}
        
        logic = Logic(logger=Mock())
        response = await logic.users_list_controller()

        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"})
        self.assertEqual(response["error"], "There was a problem while getting users")

    
    @patch('src.db.Database.get_users')
    async def test_users_list_controller_no_status(self, mock_get_users):
        mock_get_users.return_value = {"example": "Example response"}

        logic = Logic(logger=Mock())
        response = await logic.users_list_controller()

        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"example": "Example response"})
        self.assertEqual(response["error"], "There was a problem while getting users")
