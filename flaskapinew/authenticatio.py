from flask import request, jsonify
from functools import wraps

class Authenticator:
    def __init__(self, users):
        self.users = users

    def check_credentials(self, auth):
        if not auth or not (auth.username in self.users and self.users[auth.username] == auth.password):
            return False
        return True

    def authenticate(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth = request.authorization
            if not self.check_credentials(auth):
                return jsonify({'message': 'Authentication failed'}), 401
            return f(*args, **kwargs)
        return decorated_function
