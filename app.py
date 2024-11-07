from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Initialize an empty array/list to store todos
todos = []

@app.route('/', methods=['GET'])
def api_test():
  return jsonify({
    "status": 200,
    "message": "Server is alive"
  }), 200

@app.route('/todo', methods=['POST'])
def create_todo():
  data = request.get_json()
  new_todo = {
    'id': len(todos) + 1,  # Simple ID generation, starts from 1
    'title': data['title'],
    'description': data['description'],
    'finished_at': None,
    'created_at': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
    'updated_at': None,
    'deleted_at': None
  }
  todos.append(new_todo)
  return jsonify(new_todo), 201

@app.route('/todo', methods=['GET'])
def get_all_todos():
  return jsonify(todos)

@app.route('/todo/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
  todo = next((t for t in todos if t['id'] == todo_id), None)
  if todo:
    return jsonify(todo)
  return jsonify({'message': 'Todo not found'}), 404

@app.route('/todo/<int:todo_id>', methods=['PUT', 'PATCH'])
def update_todo(todo_id):
  todo = next((t for t in todos if t['id'] == todo_id), None)
  if not todo:
    return jsonify({'message': 'Todo not found'}), 404
  data = request.get_json()
  todo['title'] = data.get('title', todo['title'])
  todo['description'] = data.get('description', todo['description'])
  todo['updated_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
  return jsonify(todo)

@app.route('/todo/<int:todo_id>/finish', methods=['POST'])
def finish_todo(todo_id):
  todo = next((t for t in todos if t['id'] == todo_id), None)
  if not todo:
    return jsonify({'message': 'Todo not found'}), 404
  todo['finished_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
  return jsonify(todo)

@app.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
  todo = next((t for t in todos if t['id'] == todo_id), None)
  if not todo:
    return jsonify({'message': 'Todo not found'}), 404
  todo['deleted_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
  return jsonify(todo)

if __name__ == '__main__':
  app.run(debug=True, port=5000)