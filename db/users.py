import db_utils as db


def get_user(username):
    """
    Gets a user from the table using a username
    """
    command = "SELECT * FROM users WHERE username=%s"
    values = [username]
    return db.exec_get_one(command, values)