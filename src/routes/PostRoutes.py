from flask import request, jsonify
from src.controller.PostController import PostController
from src.controller.GetController import GetController
from src.config.DataConfig import DataConfig
from src.helper.ResponseHelper import create_failed, action_success, action_failed

get_controller = GetController(DataConfig.todo_list)
post_controller = PostController(DataConfig.todo_list)

def create_todo_route():
  data = request.get_json()
  todo = post_controller.create_todo(DataConfig.id, data["title"], data["description"])
  if todo:
    DataConfig.id += 1
  return (jsonify(action_success(todo)), 200) if todo else (jsonify(create_failed()), 400)

def finish_todo_route(id):
  todo = get_controller.get_by_id(id)
  new_todo = post_controller.finish_todo(todo)
  
  return (jsonify(action_success(new_todo)), 200) if new_todo.finished_at is not None else (jsonify(action_failed(todo)), 404)