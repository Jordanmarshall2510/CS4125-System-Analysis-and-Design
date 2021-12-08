import unittest

from client.grapher import Grapher
import client.database
from client import app

class test_methods(unittest.TestCase):

    '''
    database.py (Client) Unit Tests
    '''
    # Tests database creation on clientside.
    def test_database(self):
        db = client.database.Database()
        self.assertTrue(db)
        del db

# Main function
if __name__ == '__main__':
    unittest.main()