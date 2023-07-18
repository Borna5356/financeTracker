import db_utils as db
import unittest
import users
from importlib.resources import path

class TestChat(unittest.TestCase):

    def setUp(slef):
        path = "db/test_data.sql"
        db.exec_sql_file("db/drop_tables.sql")
        db.exec_sql_file(path)
    
    def test_get_user(self):
        #setup
        username = "Borneo"

        #invoke
        user = users.get_user(username)

        #analyze
        self.assertEqual(username, user[1], "get_user should have returned " + username + "but returned " + user[1])
    
    def test_create_user(self):
        #setup
        username = "Hon"
        email = "hon@gmail.com"
        password = "Honey"

        #invoke
        users.create_user(username, email, password)
        user = users.get_user(username)

        #analyze
        self.assertEqual(username, user[1], "create_user should have created a " + username + " as a user")
    
    def test_create_user_unique_username(self):
        #setup
        username = "Borneo"
        email = "borna@gmail.com"
        password = "three"
        
        #invoke
        result = users.create_user(username, email, password)

        #analyze
        self.assertEqual(result, False)