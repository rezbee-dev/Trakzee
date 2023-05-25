from flask import Blueprint, request
from flask_restx import Api, Resource

from server.user.errors import DuplicateEmailException, UserNotFoundException
from server.user.model import UserModel
from server.user.service import UserService

user_blueprint = Blueprint("user", __name__)
api = Api(user_blueprint, validate=True)
api.models[UserModel.name] = UserModel


@api.route("/users")
class Users(Resource):
    # see https://flask-restx.readthedocs.io/en/stable/swagger.html#the-api-expect-decorator
    @api.expect(UserModel)
    def post(self):
        # See default error handling:
        # https://flask.palletsprojects.com/en/2.3.x/api/#flask.Request.on_json_loading_failed
        req = request.get_json()

        try:
            user = UserService.create(req)
            return {"message": f"{user.email} was added"}, 201
        except DuplicateEmailException as dupErr:
            print("ERROR!\n", dupErr.message)
            return {"message": "Email already exists!"}, 409
        except Exception as err:
            print("ERROR!\n", err)
            return {"message": "Unexcepted error, server cannot handle request"}, 500

    @api.marshal_with(UserModel, as_list=True)
    def get(self):
        return UserService.find_all(), 200

    def delete(self):
        UserService.delete_all()
        return {"message": "All users deleted"}, 204


@api.route("/users/<int:user_id>")
class User(Resource):
    @api.marshal_with(UserModel)
    def get(self, user_id):
        user = UserService.find_by_id(user_id)

        if user is None:
            # data {message: "User <> does not exist"}
            api.abort(404, f"User {user_id} does not exist")

        return user, 200

    def delete(self, user_id):
        user = UserService.delete_by_id(user_id)

        if user is None:
            api.abort(404, f"User {user_id} does not exist")

        return {"message": f"{user.email} was removed!"}, 200

    @api.expect(UserModel)
    def put(self, user_id):
        req = request.get_json()

        try:
            user = UserService.update_by_id(user_id, req)
            return {"message": f"{user.id} was updated!"}, 200
        except UserNotFoundException:
            api.abort(404, f"User {user_id} does not exist")
            return
        except DuplicateEmailException:
            api.abort(409, "Sorry, that email already exists")
            return
        except Exception:
            api.abort(500, "Unexpected error, server cannot handle request")
            return
