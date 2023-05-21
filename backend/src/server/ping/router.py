from flask import Blueprint
from flask_restx import Resource, Api

# Blueprints are like express router; they represent collection of routes for some model that can be registered with flask app
ping_blueprint = Blueprint('ping', __name__)
# Registering blueprints with flask_restx api allows for more routing functionalities (url prefixes) and other uses
# see: https://flask-restx.readthedocs.io/en/latest/scaling.html?highlight=blueprint#use-with-blueprints
api = Api(ping_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')