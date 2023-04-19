import hmac
from models.user import UserModel


def authenticate(username, password):
    """
    Function that gets called when user calls the /auth endpoint with their username and password
    :param username: User's username in string format
    :param password: User's un-encrypted password in string format
    :return: A UserModel object  if authentication was successful, None otherwise
    """
    user = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payLoad):
    """
    Function that gets called when user has already authenticated,
    and Flask-JWT verified their authorisation header is correct
    :param payLoad: a dictionary with 'identity' key, which is the user id
    :return: a UserModel object
    """
    user_id = payLoad['identity']
    return UserModel.find_by_id(user_id)


