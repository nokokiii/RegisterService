import unittest

from src.app import app
from src.db import db, init_db


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_create_get_user(self):
        data = {
            "firstName": "John",
            "lastName": "Doe",
            "birthYear": 1990,
            "group": "user"
        }

        response = self.app.post("/users", json=data)

        user_id = response.json["id"]

        response = self.app.get(f"/users/{user_id}")

        self.assertEqual(response.status_code, 200)

    def test_create_get_update_get_user(self):
        data = {
            "firstName": "John",
            "lastName": "Doe",
            "birthYear": 1990,
            "group": "user"
        }

        response = self.app.post("/users", json=data)

        user_id = response.json["id"]

        response = self.app.get(f"/users/{user_id}")

        data = {
            "firstName": "John",
            "lastName": "Luke"
        }

        response = self.app.patch(f"/users/{user_id}", json=data)

        response = self.app.get(f"/users/{user_id}")

        self.assertEqual(response.status_code, 200)

    def test_create_delete_get_user(self):
        data = {
            "firstName": "John",
            "lastName": "Doe",
            "birthYear": 1990,
            "group": "user"
        }

        response = self.app.post("/users", json=data)

        user_id = response.json["id"]

        response = self.app.delete(f"/users/{user_id}")

        response = self.app.get(f"/users/{user_id}")

        self.assertEqual(response.status_code, 404)
        