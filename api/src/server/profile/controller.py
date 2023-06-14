from flask import request
from flask_restx import Namespace, Resource

from server.profile.dto import ProfileRequest, ProfileResponse

from server.profile.error import DuplicateUsernameException
from server.profile.service import ProfileService

ProfileRouter = Namespace("profile", validate=True)

# Swagger Doc & Marshalling
ProfileRouter.add_model(ProfileResponse.name, ProfileResponse)
ProfileRouter.add_model(ProfileRequest.name, ProfileRequest)


@ProfileRouter.route("")
class Profiles(Resource):
    # see https://flask-restx.readthedocs.io/en/stable/swagger.html#the-api-expect-decorator
    @ProfileRouter.expect(ProfileRequest)
    @ProfileRouter.response(201, "<profile_username>'s profile created!")
    @ProfileRouter.response(400, "Username already taken!")
    def post(self):
        """Creates a new profile."""
        req = request.get_json()

        try:
            profile = ProfileService.create(req)
            return {"message": f"{profile.username}'s profile created!"}, 201
        except DuplicateUsernameException:
            ProfileRouter.abort(409, "Username already taken!")
        except Exception:
            ProfileRouter.abort(500, "Unexcepted error, server cannot handle request")


# @ProfileRouter.route("/<int:profile_id>")
# class Profile(Resource):
#     @ProfileRouter.marshal_with(ProfileDTO)
#     @ProfileRouter.response(200, "Success")
#     @ProfileRouter.response(404, "Profile <profile_id> does not exist")
#     def get(self, profile_id):
#         """Returns a single profile"""
#         profile = ProfileService.find_by_id(profile_id)

#         if profile is None:
#             # data {message: "User <> does not exist"}
#             ProfileRouter.abort(404, f"Profile {profile_id} does not exist")

#         return profile, 200

#     @ProfileRouter.response(200, "<user_id> was removed!")
#     @ProfileRouter.response(404, "Profile <profile_id> does not exist")
#     def delete(self, profile_id):
#         """Deletes a profile"""
#         profile = ProfileService.delete_by_id(profile_id)

#         if profile is None:
#             ProfileRouter.abort(404, f"Profile {profile_id} does not exist")

#         return {"message": f"{profile.email} was removed!"}, 200

#     @ProfileRouter.expect(ProfileDTO)
#     @ProfileRouter.response(200, "<user_id> was updated!")
#     @ProfileRouter.response(400, "Sorry, that email already exists")
#     @ProfileRouter.response(404, "Profile <profile_id> does not exist")
#     def put(self, profile_id):
#         """Updates a profile"""
#         req = request.get_json()

#         try:
#             profile = ProfileService.update_by_id(profile_id, req)
#             return {"message": f"{profile.id} was updated!"}, 200
#         except ProfileNotFoundException:
#             ProfileRouter.abort(404, f"Profile {profile_id} does not exist")
#             return
#         except DuplicateEmailException:
#             ProfileRouter.abort(409, "Sorry, that email already exists")
#             return
#         except Exception:
#             ProfileRouter.abort(500, "Unexpected error, server cannot handle request")
#             return
