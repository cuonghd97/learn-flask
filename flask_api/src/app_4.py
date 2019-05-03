from flask import Flask
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('data', help='This is data', action='append', dest='other',)

class Demo(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        return args

api.add_resource(Demo, '/')

if __name__ == "__main__":
    app.run(debug=True)