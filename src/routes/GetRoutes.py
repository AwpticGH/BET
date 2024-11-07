from flask import jsonify
from src.controller.GetController import GetController
from src.config.DataConfig import DataConfig
from src.helper.ResponseHelper import empty_list, todo_not_found

get_controller = GetController(DataConfig.todo_list)

def server_test():
  return jsonify({
    "status": 200,
    "message": "Server is alive"
  }), 200

def get_all_todos_route():
  todo_list = get_controller.get_all()
  return jsonify([todo.__dict__ for todo in todo_list]) if len(todo_list) != 0 else jsonify(empty_list()), 200

def get_todo_by_id_route(id):
  todo = get_controller.get_by_id(id)
  return jsonify(todo.__dict__) if todo else jsonify(todo_not_found()), 200