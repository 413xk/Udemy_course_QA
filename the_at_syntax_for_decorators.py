import functools

user = {'username': 'Jose', 'access_level': 'admin'}


def make_secure(func):
    @functools.wraps(func) # it makes 'make_secure' the wrapper of 'secure_function'
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permission for {user["username"]}.'

    return secure_function


@make_secure
def get_admin_password():
    return '1234'


print(get_admin_password())
