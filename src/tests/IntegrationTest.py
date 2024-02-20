import unittest

from src.app import app
from src.db import db, init_db


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_user(self):
        pass

    def test_create_update_delete_user(self):
        pass
