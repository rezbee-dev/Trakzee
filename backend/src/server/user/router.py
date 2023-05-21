from flask import Blueprint, request
from flask_restx import Resource, Api

from server.user.schema import User as UserSchema
from server.app import db

user_blueprint = Blueprint('user', __name__)
api = Api(user_blueprint)

class Users(Resource):
    def post(self):
        # raises 400 error if data is not valid JSON
        req = request.get_json()
        
        user = UserSchema(username=req['username'], email=req['email'])

        db.session.add(user)
        db.session.commit()
        
        return {'message': f'{user.email} was added'}, 201
    
api.add_resource(Users, '/users')