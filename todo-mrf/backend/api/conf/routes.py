from flask_restful import Api

from api.handlers.TodoHandlers import TodoGetData, TodoMidifyItem


def generate_routes(app):
    api = Api(app)

    api.add_resource(TodoGetData, '/api/todo')
    api.add_resource(TodoMidifyItem, '/api/todo/<int:id>')
