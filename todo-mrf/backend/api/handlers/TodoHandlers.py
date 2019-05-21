from flask_restful import Resource, reqparse

from api.models import Todo
import api.error as error

parser = reqparse.RequestParser()

class TodoGetData(Resource):
    def post(self):
        parser.add_argument('work', help='Work can not be none', required=True)

        todo_item = parser.parse_args()

        new_todo_item = Todo(work=todo_item['work'])
        print(todo_item)
        try:
            new_todo_item.save_to_db()

            return {'message': 'Add success'}
        except Exception as e:
            return error.SERVER_ERROR_500

    def get(self):
        return Todo.get_all()

    def delete(self):
        return Todo.delete_done()

class TodoMidifyItem(Resource):
    def put(self, id):
        return Todo.change_done(id)

    def delete(self, id):
        return Todo.delete_one(id)