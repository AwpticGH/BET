from src.controller.BaseController import BaseController
from typing import List
from src.model.TodoModel import TodoModel
from src.helper.DatetimeHelper import DatetimeHelper
from datetime import datetime

class PostController(BaseController):

  def __init__(self, todo_list: List[TodoModel]):
    super().__init__(todo_list)
  
  def create_todo(self, id: int, title, description):
    todo = TodoModel(id, title, description)
    self.todo_list.append(todo)
    return todo
  
  def finish_todo(self, todo: TodoModel):
    dt = datetime.now()
    todo.finished_at = DatetimeHelper.get_datetime_format(dt)
      
    return todo