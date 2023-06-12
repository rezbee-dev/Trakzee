from flask import request
from flask_restx import Namespace, Resource

from server.account.dto import AccountFull, AccountPartial, AuthRefresh, AuthRequest, AuthResponse, AuthTokens
from server.account.error import AccountNotFoundException, DuplicateEmailException, InvalidCredentialsException
from server.account.middleware import AuthMiddleware
from server.account.service import AccountService

AccountRouter = Namespace("account", validate=True)

# Swagger Doc & Marshalling
AccountRouter.add_model(AuthResponse.name, AuthResponse)
AccountRouter.add_model(AuthRequest.name, AuthRequest)
AccountRouter.add_model(AuthRefresh.name, AuthRefresh)
AccountRouter.add_model(AuthTokens.name, AuthTokens)
AccountRouter.add_model(AccountPartial.name, AccountPartial)
AccountRouter.add_model(AccountFull.name, AccountFull)

# Request parsing & validation (ex: type errors)
auth_parser = AccountRouter.parser()
auth_parser.add_argument("Authorization", required=True, location="headers")

refresh_parser = AccountRouter.parser()
refresh_parser.add_argument("refresh_token", location="cookies")


@AccountRouter.route("/register")
class Register(Resource):
    @AccountRouter.marshal_with(AccountPartial)
    @AccountRouter.expect(AuthRequest)
    @AccountRouter.response(201, "Success")
    @AccountRouter.response(409, "Email already taken!")
    def post(self):
        req = request.get_json()

        try:
            account = AccountService.register(req)
            payload = {"id": account.id, "email": account.email, "verified": account.verified}
            return payload, 201
        except DuplicateEmailException:
            AccountRouter.abort(409, "Email already taken!")
        except Exception:
            AccountRouter.abort(500, "Unexcepted error, server cannot handle request")


@AccountRouter.route("/login")
class Login(Resource):
    @AccountRouter.marshal_with(AuthTokens)
    @AccountRouter.expect(AuthRequest)
    @AccountRouter.response(200, "Success")
    @AccountRouter.response(404, "Account not found. Please register or login again")
    def post(self):
        req = request.get_json()

        try:
            tokens = AccountService.login(req)
            headers = [
                ("Set-Cookie", f'refresh_token={tokens["refresh_token"]}; Path=/api/account/refresh; HttpOnly'),
                ("Set-Cookie", f'refresh_token={tokens["refresh_token"]}; Path=/api/account/logout; HttpOnly'),
            ]

            return {"access_token": tokens["access_token"]}, 200, headers
        except AccountNotFoundException:
            AccountRouter.abort(404, "Account not found. Please register or login again")
        except Exception:
            AccountRouter.abort(500, "Unexcepted error, server cannot handle request")


@AccountRouter.route("/")
class Account(Resource):
    @AccountRouter.marshal_with(AccountPartial)
    @AccountRouter.expect(auth_parser)
    @AccountRouter.response(200, "Success")
    @AccountRouter.response(401, "Invalid credentials. Please log in again")
    @AuthMiddleware.jwt_required
    def get(self):
        return AuthMiddleware.current_account, 200


@AccountRouter.route("/refresh")
class Refresh(Resource):
    @AccountRouter.marshal_with(AuthTokens)
    @AccountRouter.expect(refresh_parser)
    @AccountRouter.response(200, "Success")
    @AccountRouter.response(401, "Invalid credentials. Please log in again")
    def post(self):
        req = request.cookies.get("refresh_token")

        try:
            access_tokens = AccountService.refresh({"token": req})
            return access_tokens, 200
        except InvalidCredentialsException:
            AccountRouter.abort(401, "Invalid credentials. Please log in again")
        except Exception:
            AccountRouter.abort(500, "Unexcepted error, server cannot handle request")
