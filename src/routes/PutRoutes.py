from flask import request, jsonify
from src.controller.PutController import PutController
from src.controller.GetController import GetController
from src.config.DataConfig import DataConfig
from src.helper.ResponseHelper import action_success, action_failed

get_controller = GetController(DataConfig.todo_list)
put_controller = PutController(DataConfig.todo_list)

def update_todo_route(id):
  data = request.get_json()
  todo = get_controller.get_by_id(id)
  updated_at = todo.updated_at
  
  new_todo = put_controller.update_todo(todo, data["title"], data["description"])
  new_updated_at = new_todo.updated_at
  
  return (jsonify(action_success(new_todo)), 200) if updated_at != new_updated_at else (jsonify(action_failed(todo)), 400)