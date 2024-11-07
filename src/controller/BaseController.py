from typing import List
from src.model.TodoModel import TodoModel

class BaseController:
  todo_list: List[TodoModel]
  
  def __init__(self, todo_list: List[TodoModel]):
    self.todo_list = todo_list