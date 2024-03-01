from unittest.mock import patch, Mock

import aiounittest

from src.logic import Logic


class DeleteUser(aiounittest.AsyncTestCase):
    @patch('src.db.Database.delete_user')
    async def test_delete_user_controller_ok(self, mock_delete_user):
        mock_delete_user.return_value = {"status": "OK", "result": {}}
        
        logic = Logic(logger=Mock())
        response = await logic.delete_user_controller(user_id="example_id")
        
        self.assertEqual(response["status"], "OK")
        self.assertEqual(response["response"], "User deleted")

    
    @patch('src.db.Database.delete_user')
    async def test_delete_user_controller_err(self, mock_delete_user):
        mock_delete_user.return_value = {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"}
        
        logic = Logic(logger=Mock())
        response = await logic.delete_user_controller(user_id="example_id")
               
        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"status": "ERR", "time": "4ms289µs828ns", "error": "Failed to parse query"})
        self.assertEqual(response["error"], "There was a problem while deleting the user")


    @patch('src.db.Database.delete_user')
    async def test_delete_user_controller_no_status(self, mock_delete_user):
        mock_delete_user.return_value = {"example": "Example response"}

        logic = Logic(logger=Mock())
        response = await logic.delete_user_controller(user_id="example_id")

        self.assertEqual(response["status"], "ERR")
        self.assertEqual(response["response"], {"example": "Example response"})
        self.assertEqual(response["error"], "There was a problem while deleting the user")
