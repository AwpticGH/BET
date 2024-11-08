from src.controller.BaseController import BaseController
from src.model.TodoModel import TodoModel
from typing import List

class GetController(BaseController):
  
  def __init__(self, todo_list: List[TodoModel]):
    super().__init__(todo_list)
  
  def get_all(self):
    my_list: List[TodoModel] = []
    for todo in self.todo_list:
      if todo.deleted_at is None:
        my_list.append(todo)

    return my_list
  
  def get_by_id(self, id: int):
    for todo in self.todo_list:
      if todo.id == id:
        return todo
      
    return None