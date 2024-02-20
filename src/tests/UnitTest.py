import unittest
import src.app as app
from src.db import db, init_db


class UnitTests(unittest.TestCase):

    def test_all_users(self):
        with app.app.test_request_context():
            response, status_code = app.get_users()
            self.assertEqual(type(response), list)
            self.assertEqual(status_code, 200)

    def test_user(self):
        with app.app.test_request_context():
            # ID is random so I cannot check id
            response, status_code = app.get_user()
            self.assertEqual(type(response), dict)
            self.assertEqual(status_code, 200)

    def test_create_user(self):
        with app.app.test_request_context():
            data = {'firstName': 'John', 'lastName': 'Doe', 'birthYear': '1995', 'group': 'admin'}
            response, status_code = app.create_user(data)
            self.assertEqual(type(response), dict)
            self.assertEqual(status_code, 201)

            response, status_code = app.get_user({})
            self.assertEqual(type(response), dict)
            self.assertEqual(status_code, 403)

    def test_update_user(self):
        with app.app.test_request_context():
            data = {'firstName': 'John', 'lastName': 'Luke'}
            response, status_code = app.update_user(user_id, data)
            self.assertEqual(type(response), dict)
            self.assertEqual(status_code, 204)

            response, status_code = app.update_user(user_id, {})
            self.assertEqual(type(response), dict)
            self.assertEqual(status_code, 403)

            response, status_code = app.update_user("not_existing_id", {"firstName": "John"})
            self.assertEqual(type(response), dict)
            self.assertEqual(status_code, 404)

    def test_delete_user(self):
        with app.app.test_request_context():
            response, status_code = app.delete_user(user_id)
            self.assertEqual(type(response), dict)
            self.assertEqual(status_code, 204)

            response, status_code = app.delete_user("not_existing_id")
            self.assertEqual(type(response), dict)
            self.assertEqual(status_code, 404)


unittest.main()
