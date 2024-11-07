from src.model.TodoModel import TodoModel

def empty_list():
  return {"status": 200, "message": "List is empty"}

def todo_not_found():
  return {"status": 200, "message": "Todo not found"}

def create_failed():
  return {"status": 400, "error": "Failed to create todo"}

def action_success(todo: TodoModel):
  return {
    "message": "Success",
    "todo": todo.__dict__
  }
  
def action_failed(todo: TodoModel):
  return {
    "error": "Failed to perform action",
    "todo": todo.__dict__
  }