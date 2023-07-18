from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = {
    '1': {'task': 'Read a book'},
    '2': {'task': 'Learn Python'},
}

# Read (GET Method)
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Create (POST Method)
@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or 'task' not in request.json:
        abort(400)
    task = {str(len(tasks) + 1): request.json['task']}
    tasks.update(task)
    return jsonify(task), 201

# Update (PUT Method)
@app.route('/api/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id not in tasks:
        abort(404)
    if not request.json or 'task' not in request.json:
        abort(400)
    tasks[task_id] = request.json['task']
    return jsonify(tasks[task_id]), 200

# Delete (DELETE Method)
@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        abort(404)
    task = tasks.pop(task_id)
    return jsonify(task), 200

if __name__ == '__main__':
    app.run(debug=True)
