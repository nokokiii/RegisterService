import aiounittest
import json
import src.app as app

class TestUserEndpoints(aiounittest.AsyncTestCase):
    async def test_get_users(self):
        test_app = app.app
        test_client = test_app.test_client()
        response = await test_client.get('/users')
        self.assertEqual(response.status_code, 200)
        json_data = await response.get_json()
        self.assertIsInstance(json_data, list)
    
    
    async def test_get_user(self):
        test_app = app.app
        test_client = test_app.test_client()
        user_id = "some_user_id"
        response = await test_client.get(f'/users/{user_id}')
        self.assertIn(response.status_code, [200, 404])
        json_data = await response.get_json()
        self.assertIsInstance(json_data, dict)


    async def test_create_user(self):
        test_app = app.app
        test_client = test_app.test_client()
        example_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "Admin"}
        response = await test_client.post('/users', json=example_data)
        self.assertEqual(response.status_code, 201)


    async def test_update_user(self):
        test_app = app.app
        test_client = test_app.test_client()
        user_id = "some_user_id"
        example_data = {"firstName": "John", "lastName": "Doe"}
        response = await test_client.patch(f'/users/{user_id}', json=example_data)
        self.assertIn(response.status_code, [202, 400])

    
    async def test_delete_user(self):
        test_app = app.app
        test_client = test_app.test_client()
        user_id = "some_user_id"
        response = await test_client.delete(f'/users/{user_id}')
        self.assertIn(response.status_code, 200)
