# auth.py
from functools import wraps
from flask import request, jsonify
from config import users

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        required_headers = ('user', 'password')
        missing_headers = [header for header in required_headers if header not in request.headers]
        if missing_headers:
            return jsonify({
                "message": "Missing Headers",
                "Missing headers": missing_headers
            }), 401

        auth = request.headers
        username = auth.get('user')
        password = auth.get('password')
        expected_password = users.get(username)

        if not expected_password or password != expected_password:
            return jsonify({'message': 'Authentication failed'}), 401
        return f(*args, **kwargs)
    return decorated_function
