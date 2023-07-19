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
    Creates a new user with a unique username in the users table
    """
    user = get_user(username)
    if (user != None):
        return False
    command = "INSERT INTO users(username, email, password) VALUES (%s, %s, %s)"
    values = [username, email, password]
    db.exec_commit(command, values)
    return True

def verify_password(username, password):
    """
    Verifies that the password that the user used is correct
    """
    user = get_user(username)
    return user[3] == password