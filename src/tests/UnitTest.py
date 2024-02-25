import unittest
import src.app as app
from src.db import db, init_db


class UnitTests(unittest.TestCase):

    def test_all_users_status(self):
        with app.app.test_request_context():
            _, status_code = app.get_users()
            self.assertEqual(status_code, 200)

    def test_user_no_id_res_type(self):
        with app.app.test_request_context():
            response, _ = app.get_user()
            self.assertEqual(type(response), dict)
    
    def test_user_no_id_status(self):
        with app.app.test_request_context():
            _, status_code = app.get_user()
            self.assertEqual(status_code, 403)

    def test_create_user_res_type(self):
        with app.app.test_request_context():
            data = {'firstName': 'John', 'lastName': 'Doe', 'birthYear': '1995', 'group': 'admin'}
            response, _ = app.create_user()
            self.assertEqual(type(response), dict)

    def test_create_user_status(self):
        with app.app.test_request_context():
            data = {'firstName': 'John', 'lastName': 'Doe', 'birthYear': '1995', 'group': 'admin'}
            _, status_code = app.create_user(data)
            self.assertEqual(status_code, 201)

    def test_empty_create_user_res_type(self):
        with app.app.test_request_context():
            response, _ = app.get_user({})
            self.assertEqual(type(response), dict)

    def test_empty_create_user_status(self):
        with app.app.test_request_context():
            _, status_code = app.get_user({})
            self.assertEqual(status_code, 403)

    def test_missing_id_update_user_res_type(self):
        with app.app.test_request_context():
            response, _ = app.update_user("not_existing_id", {"firstName": "John"})
            self.assertEqual(type(response), dict)

    def test_wonrg_id_update_user_status(self):
        with app.app.test_request_context():
            _, status_code = app.update_user("not_existing_id", {"firstName": "John"})
            self.assertEqual(status_code, 404)

    def test_empty_update_user_res_type(self):
        with app.app.test_request_context():
            response, _ = app.update_user("some_id", {})
            self.assertEqual(type(response), dict)

    def test_empty_update_user_status(self):
        with app.app.test_request_context():
            _, status_code = app.update_user("some_id", {})
            self.assertEqual(status_code, 403)

    # def test_update_user(self):
    #     with app.app.test_request_context():
    #         data = {'firstName': 'John', 'lastName': 'Luke'}
    #         response, status_code = app.update_user(user_id, data)
    #         self.assertEqual(type(response), dict)
    #         self.assertEqual(status_code, 204)

    #         response, status_code = app.update_user(user_id, {})
    #         self.assertEqual(type(response), dict)
    #         self.assertEqual(status_code, 403)

    #         response, status_code = app.update_user("not_existing_id", {"firstName": "John"})
    #         self.assertEqual(type(response), dict)
    #         self.assertEqual(status_code, 404)

    # def test_delete_user(self):
    #     with app.app.test_request_context():
    #         response, status_code = app.delete_user(user_id)
    #         self.assertEqual(type(response), dict)
    #         self.assertEqual(status_code, 204)

    #         response, status_code = app.delete_user("not_existing_id")
    #         self.assertEqual(type(response), dict)
    #         self.assertEqual(status_code, 404)
