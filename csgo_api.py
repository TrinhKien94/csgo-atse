from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class Employees(Resource):
    def get(self):
        return {'employees': request.args.get('username')} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        result = {'data': ['test']}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        result = {'data': ['test']}
        return jsonify(result)


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port=5002)
