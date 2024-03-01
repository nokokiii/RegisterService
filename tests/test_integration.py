import unittest

from src.app import app


class IntegrationTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    async def test_create_get_user(self):
        data = {
            "firstName": "John",
            "lastName": "Doe",
            "birthYear": 1990,
            "group": "user"
        }

        response = await self.app.post("/users", json=data)

        user_id = await response.json["id"]

        response = await self.app.get(f"/users/{user_id}")

        self.assertEqual(response.json["firstName"], "John")
        self.assertEqual(response.json["lastName"], "Doe")
        self.assertEqual(response.json["age"], 2024-1990)
        self.assertEqual(response.json["group"], "user")


    async def test_create_get_update_get_user(self):
        data = {
            "firstName": "John",
            "lastName": "Doe",
            "birthYear": 1990,
            "group": "user"
        }

        response = await self.app.post("/users", json=data)

        user_id = response.json["id"]

        response = await self.app.get(f"/users/{user_id}")

        self.assertEqual(response.json["firstName"], "John")
        self.assertEqual(response.json["lastName"], "Doe")
        self.assertEqual(response.json["age"], 2024-1990)
        self.assertEqual(response.json["group"], "user")

        data = {
            "firstName": "John",
            "lastName": "Luke"
        }

        response = await self.app.patch(f"/users/{user_id}", json=data)

        response = await self.app.get(f"/users/{user_id}")

        self.assertEqual(response.json["firstName"], "John")
        self.assertEqual(response.json["lastName"], "Luke")
        self.assertEqual(response.json["age"], 2024-1990)
        self.assertEqual(response.json["group"], "user")


    async def test_create_delete_get_user(self):
        data = {
            "firstName": "John",
            "lastName": "Doe",
            "birthYear": 1990,
            "group": "user"
        }

        response = await self.app.post("/users", json=data)

        user_id = response.json["id"]

        response = await self.app.delete(f"/users/{user_id}")

        response = await self.app.get(f"/users/{user_id}")

        self.assertEqual(response.status_code, 404)
