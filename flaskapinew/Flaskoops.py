from flask import Flask, Blueprint, request, jsonify
from functools import wraps
from config import  users

# Flask initialization
app = Flask(__name__)



# Authentication decorator
def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        required_headers = ('user', 'password')
        missing_headers = [header for header in required_headers if header not in request.headers]
        if missing_headers:
            return jsonify({
                "message" : "Missing Headers",
                "MIssing headers" : missing_headers
            }), 401
        auth = request.headers
        username=auth.get('user')
        password=auth.get('passowrd')
        excepted_password = users.get(username)
        
        
        if password == excepted_password:
            return jsonify({'message': 'Authentication failed'}), 401
        return f(*args, **kwargs)
    return decorated_function

# Password verification
def verify_password(username, password):
    stored_password = users.get(username)
    if stored_password and stored_password == password:
        return True
    return False

# class for items
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Initial data for items
items = [
    Item('Apple', 210.0),
    Item('Banana', 100.0),
    Item('Grapes', 80.0),
    Item('Kiwi', 100.0),
    Item('Onion', 80.0),
    Item('Sweet Potato', 60.0), 
    Item('Kurkure', 70.0),
    Item('Chips', 80.0),
    Item('Curd', 90.0),
    Item('Headphone', 500.0),
    Item('Chocolate', 110.0),  
    Item('Dairy Milk', 180.0),  
    Item('Salt', 30.0),
    Item('Mango', 140.0),
]

# Blueprint for items API
item_blueprint = Blueprint('items', __name__)

# validate request data 
def validate_request_data(data, fields):
    return all(field in data for field in fields)

# Routes
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Himanshu Singh Flask API'}), 200

@item_blueprint.route('/items', methods=['POST'])
@authenticate
def create_item():
    data = request.get_json()
    if not data or not validate_request_data(data, ['name', 'price']):
        return jsonify({'message': 'Invalid data'}), 400

    item = Item(name=data['name'], price=data['price'])
    items.append(item)
    return jsonify({'message': 'Item created'}), 201

@item_blueprint.route('/items', methods=['GET'])
@authenticate
def get_items():
    return jsonify({'items': [{'name': item.name, 'price': item.price} for item in items]}), 200

@item_blueprint.route('/items/<string:name>', methods=['GET'])
@authenticate
def get_item(name):
    item = next((item for item in items if item.name == name), None)
    if item:
        return jsonify({'name': item.name, 'price': item.price}), 200
    return jsonify({'message': 'Item not found'}), 404

# Registering the blueprint for items API under /api prefix
app.register_blueprint(item_blueprint, url_prefix='/api')

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
