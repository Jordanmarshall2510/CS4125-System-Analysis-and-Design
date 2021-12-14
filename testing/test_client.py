import unittest
from client import database

from client.database import Database


class test_methods(unittest.TestCase):

    '''
    database.py (Client) Unit Tests
    '''
    # Tests database creation on clientside.

    def test_database(self):
        db = Database(None, None, None, None, True)
        self.assertTrue(db)


# Main function
if __name__ == '__main__':
    unittest.main()
