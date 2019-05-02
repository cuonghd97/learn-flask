from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

# class TodoExample(Resource):
#     def get(self, todo_id):
#         return {'todo_id': todos[todo_id]}
#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {'todo_id': todos[todo_id]}

class HttpCode201(Resource):
    def get(self):
        return {'response': '201'}, 201

class HttpCode2012(Resource):
    def get(self):
        return {'task': 'hello world'}, 201, {'another': 'another'}

# api.add_resource(TodoExample, '/<string:todo_id>')
api.add_resource(HttpCode201, '/code201/')
api.add_resource(HttpCode2012, '/another-201/')

if __name__ == '__main__':
    app.run(debug=True)