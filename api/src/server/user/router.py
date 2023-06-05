from flask import request
from flask_restx import Namespace, Resource

from server.user.errors import DuplicateEmailException, UserNotFoundException
from server.user.dto import UserDTO, UserAuthDTO
from server.user.service import UserService

# user_blueprint = Blueprint("user", __name__)
# api = Api(user_blueprint, validate=True)
# api.models[UserDTO.name] = UserDTO

user_ns = Namespace("users", validate=True)
user_ns.models[UserDTO.name] = UserDTO
user_ns.models[UserAuthDTO.name] = UserAuthDTO

@user_ns.route("")
class Users(Resource):
    # see https://flask-restx.readthedocs.io/en/stable/swagger.html#the-api-expect-decorator
    @user_ns.expect(UserAuthDTO)
    @user_ns.response(201, "<user_email> was added!")
    @user_ns.response(400, "Email already exists!")
    def post(self):
        """Creates a new user."""
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

    @user_ns.marshal_with(UserDTO, as_list=True)
    def get(self):
        """Returns all users."""
        return UserService.find_all(), 200

    # def delete(self):
    #     UserService.delete_all()
    #     return {"message": "All users deleted"}, 204


@user_ns.route("/<int:user_id>")
class User(Resource):
    @user_ns.marshal_with(UserDTO)
    @user_ns.response(200, "Success")
    @user_ns.response(404, "User <user_id> does not exist")
    def get(self, user_id):
        """Returns a single user"""
        user = UserService.find_by_id(user_id)

        if user is None:
            # data {message: "User <> does not exist"}
            user_ns.abort(404, f"User {user_id} does not exist")

        return user, 200

    @user_ns.response(200, "<user_id> was removed!")
    @user_ns.response(404, "User <user_id> does not exist")
    def delete(self, user_id):
        """Deletes a user"""
        user = UserService.delete_by_id(user_id)

        if user is None:
            user_ns.abort(404, f"User {user_id} does not exist")

        return {"message": f"{user.email} was removed!"}, 200

    @user_ns.expect(UserDTO)
    @user_ns.response(200, "<user_id> was updated!")
    @user_ns.response(400, "Sorry, that email already exists")
    @user_ns.response(404, "User <user_id> does not exist")
    def put(self, user_id):
        """Updates a user"""
        req = request.get_json()

        try:
            user = UserService.update_by_id(user_id, req)
            return {"message": f"{user.id} was updated!"}, 200
        except UserNotFoundException:
            user_ns.abort(404, f"User {user_id} does not exist")
            return
        except DuplicateEmailException:
            user_ns.abort(409, "Sorry, that email already exists")
            return
        except Exception:
            user_ns.abort(500, "Unexpected error, server cannot handle request")
            return
