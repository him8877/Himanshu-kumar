from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (initially empty)
data = []

# Create operation
@app.route('/create', methods=['POST'])
def create():
    req_data = request.get_json()
    data.append(req_data)
    return jsonify({'message': 'Data created successfully'}), 201

# Read operation
@app.route('/retrieve', methods=['GET'])
def retrieve():
    return jsonify(data)

# Update operation
@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    req_data = request.get_json()
    for item in data:
        if item['id'] == id:
            item.update(req_data)
            return jsonify({'message': 'Data updated successfully'})
    return jsonify({'error': 'Data not found'}), 404

# Delete operation
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    for item in data:
        if item['id'] == id:
            data.remove(item)
            return jsonify({'message': 'Data deleted successfully'})
    return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
