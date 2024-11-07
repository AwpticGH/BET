from flask import request, jsonify
from src.controller.DeleteController import DeleteController
from src.controller.GetController import GetController
from src.config.DataConfig import DataConfig
from src.helper.ResponseHelper import action_success, action_failed

get_controller = GetController(DataConfig.todo_list)
delete_controller = DeleteController(DataConfig.todo_list)

def delete_todo_route(id):
  todo = get_controller.get_by_id(id)
  new_todo = delete_controller.delete_todo(todo)
  
  return (jsonify(action_success(new_todo)), 200) if new_todo.deleted_at is not None else (jsonify(action_failed(todo)), 404)