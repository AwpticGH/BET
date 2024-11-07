from src.controller.BaseController import BaseController
from src.model.TodoModel import TodoModel
from typing import List
from datetime import datetime
from src.helper.DatetimeHelper import DatetimeHelper

class DeleteController(BaseController):
  
  def __init__(self, todo_list: List[TodoModel]):
    super().__init__(todo_list)
    
  def delete_todo(self, todo: TodoModel):
    dt = datetime.now()
    todo.deleted_at = DatetimeHelper.get_datetime_format(dt)
      
    return todo