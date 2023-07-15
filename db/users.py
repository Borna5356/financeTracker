import db_utils as db


def get_user(username):
    """
    Gets a user from the table using a username
    """
    command = "SELECT * FROM users WHERE username=%s"
    values = [username]
    return db.exec_get_one(command, values)

def create_user(username, email, password):
    """
    Creates a new user in the users table
    """
    command = "INSERT INTO users(username, email, password) VALUES (%s, %s, %s)"
    values = [username, email, password]
    db.exec_commit(command, values)