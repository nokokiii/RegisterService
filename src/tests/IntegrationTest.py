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

        self.assertEqual(response.json["firstName"], "John")
        self.assertEqual(response.json["lastName"], "Doe")
        self.assertEqual(response.json["age"], 2024-1990)
        self.assertEqual(response.json["group"], "user")


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

        self.assertEqual(response.json["firstName"], "John")
        self.assertEqual(response.json["lastName"], "Doe")
        self.assertEqual(response.json["age"], 2024-1990)
        self.assertEqual(response.json["group"], "user")

        data = {
            "firstName": "John",
            "lastName": "Luke"
        }

        response = self.app.patch(f"/users/{user_id}", json=data)

        response = self.app.get(f"/users/{user_id}")

        self.assertEqual(response.json["firstName"], "John")
        self.assertEqual(response.json["lastName"], "Luke")
        self.assertEqual(response.json["age"], 2024-1990)
        self.assertEqual(response.json["group"], "user")


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

        print(response.json)
        self.assertEqual(response.status_code, 404)
        

    def test(self):
        pass
    