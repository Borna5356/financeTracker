import db_utils as db
import unittest
import users
from importlib.resources import path

class TestChat(unittest.TestCase):

    def setUp(slef):
        path = "db/test_data.sql"
        db.exec_sql_file(path)
    
    def tearDown(self):
        path = "db/drop_tables.sql"
        db.exec_sql_file(path)
    
    def test_get_user(self):
        #setup
        username = "Borneo"

        #invoke
        user = users.get_user(username)

        #analyze
        self.assertEqual(username, user[1], "get_user should have returned " + username + "but returned " + user[1])