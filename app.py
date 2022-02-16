from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


app = Flask(__name__)
api = Api(app)

data = {
    'name': {0: 'haider', 1: 'ali', 2: 'raza'},
    'age': {0: '18', 1: '22', 2: '35'},
    'branch': {0: 'api', 1: 'mvc', 2: 'csr'}
}


class Users(Resource):

    def get(self):
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('branch', required=True)
        args = parser.parse_args()

        if args['name'] in list(data['name'].values()):
            return {
                'message': f"'{args['name']}' already exists."
            }, 401
        else:
            data['name'][len(data['name'])] = args['name']
            data['age'][len(data['age'])] = args['age']
            data['branch'][len(data['branch'])] = args['branch']
            return {'data': data}, 200


class Locations(Resource):
    # methods go here
    pass


api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
