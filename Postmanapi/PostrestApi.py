from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

# Sample data
items = [
    { 'id': 1, 'name': 'Himanshu' },
    { 'id': 2, 'name': 'Shubham' },
    { 'id': 3, 'name': 'Rahul' },
    { 'id': 4, 'name': 'Rohit' },
    { 'id': 5, 'name': 'Sidhu' },
    { 'id': 6, 'name': 'Ravi' },
    { 'id': 7, 'name': 'Kalash' },
    { 'id': 8, 'name': 'Sumit' },
    { 'id': 9, 'name': 'Albert' },
    { 'id': 10, 'name': 'Anshu' },
    { 'id': 11, 'name': 'Vikalp' },
    { 'id': 12, 'name': 'Gudiya' },
    { 'id': 13, 'name': 'Nida' },
    { 'id': 14, 'name': 'Ajay' },
    { 'id': 15, 'name': 'Smita' },
    { 'id': 16, 'name': 'Varun' },
    { 'id': 17, 'name': 'Aparna' },
    { 'id': 18, 'name': 'Arpita' },
    { 'id': 19, 'name': 'Siddharth' },
    { 'id': 20, 'name': 'Aditya' }
]

# GET all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET a single item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    return jsonify(item)

# POST a new item
@app.route('/api/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        abort(400)
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name']
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT update an existing item
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    if not request.json or 'name' not in request.json:
        abort(400)
    item['name'] = request.json['name']
    return jsonify(item)

# DELETE an item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    items.remove(item)
    return jsonify({ 'result': True })

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({ 'error': 'Bad request', 'message': str(error)}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({ 'error': 'Not found', 'message': 'Invalid Data.' }), 404)

@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': 'Method Not Allowed'}), 405)

@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'error': 'Forbidden'}), 403)

if __name__ == '__main__':
    app.run(debug=True)
