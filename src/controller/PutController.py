from src.controller.BaseController import BaseController
from typing import List
from src.model.TodoModel import TodoModel
from datetime import datetime
from src.helper.DatetimeHelper import DatetimeHelper

class PutController(BaseController):
  
  def __init__(self, todo_list: List[TodoModel]):
    super().__init__(todo_list)
  
  def update_todo(self, todo: TodoModel, title, description):
    update = False
    if todo is not None:
      if title is not None or title != "":
        todo.title = title
        update = True
      
      if description is not None or description != "":
        todo.description = description
        update = True
        
      if update:
        dt = datetime.now()
        todo.updated_at = DatetimeHelper.get_datetime_format(dt)
        
    return todo