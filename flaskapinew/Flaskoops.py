from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from config import db_config
from auth import authenticate

# Flask initialization
app = Flask(__name__)

# MySQL connection setup
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Class for items
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Initial data for items
initial_items = [
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

# Insert initial data into the database
def insert_initial_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM items")
    item_count = cursor.fetchone()[0]
    
    if item_count == 0:  # Only insert if table is empty
        for item in initial_items:
            cursor.execute("INSERT INTO items (name, price) VALUES (%s, %s)", (item.name, item.price))
        conn.commit()
    cursor.close()
    conn.close()

# Blueprint items API
item_blueprint = Blueprint('items', __name__)

# Validate request data
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
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, price) VALUES (%s, %s)", (item.name, item.price))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Item created'}), 201

@item_blueprint.route('/items', methods=['GET'])
@authenticate
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify({'items': [{'name': item[0], 'price': item[1]} for item in items]}), 200

@item_blueprint.route('/items/<string:name>', methods=['GET'])
@authenticate
def get_item(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM items WHERE name = %s", (name,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()

    if item:
        return jsonify({'name': item[0], 'price': item[1]}), 200
    return jsonify({'message': 'Item not found'}), 404

# Registering the blueprint for items API under /api prefix
app.register_blueprint(item_blueprint, url_prefix='/api')

# Insert initial items when the application starts
insert_initial_items()

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
