from flask import Flask
from src.routes.GetRoutes import server_test, get_all_todos_route, get_todo_by_id_route
from src.routes.PostRoutes import create_todo_route, finish_todo_route
from src.routes.PutRoutes import update_todo_route
from src.routes.DeleteRoutes import delete_todo_route

app = Flask(__name__)

# Setup routes
app.route('/', methods=['GET'])(server_test)
app.route('/todo', methods=['GET'])(get_all_todos_route)
app.route('/todo/<int:id>', methods=['GET'])(get_todo_by_id_route)

app.route('/todo', methods=['POST'])(create_todo_route)
app.route('/todo/<int:id>/finish', methods=['POST'])(finish_todo_route)

app.route('/todo/<int:id>', methods=['PUT'])(update_todo_route)

app.route('/todo/<int:id>', methods=['DELETE'])(delete_todo_route)

if __name__ == '__main__':
  app.run(debug=True, port=5000)