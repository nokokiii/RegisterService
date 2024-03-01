import unittest

from tests.test_integration import IntegrationTest
from tests.test_get_users import GetUsers
from tests.test_get_user import GetUser
from tests.test_create_user import CreateUser
from tests.test_update_user import UpdateUser
from tests.test_delete_user import DeleteUser


if __name__ == '__main__':
    loader = unittest.TestLoader()
    
    suite = loader.loadTestsFromTestCase(GetUsers)
    suite.addTests(loader.loadTestsFromTestCase(GetUser))
    suite.addTests(loader.loadTestsFromTestCase(CreateUser))
    suite.addTests(loader.loadTestsFromTestCase(UpdateUser))
    suite.addTests(loader.loadTestsFromTestCase(DeleteUser))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
     