import unittest

from src.tests.IntegrationTest import IntegrationTest
from src.tests.UnitTest import UnitTests

if __name__ == '__main__':
    loader = unittest.TestLoader()
    
    suite = loader.loadTestsFromTestCase(IntegrationTest)
    suite.addTests(loader.loadTestsFromTestCase(UnitTests))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
     