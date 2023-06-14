from functools import wraps

from flask import abort, request

from server.account.error import InvalidCredentialsException
from server.account.service import AccountService


class AuthMiddleware(object):
    current_account = None

    # src: https://circleci.com/blog/authentication-decorators-flask/
    @staticmethod
    def jwt_required(f):
        @wraps(f)
        def _jwt_required(*args, **kwargs):
            auth_headers = request.headers.get("Authorization")
            try:
                if auth_headers:
                    access_token = auth_headers.split(" ")[1]
                    AuthMiddleware.current_account = AccountService.get_account_by_token({"token": access_token})
                    return f(*args, **kwargs)
                else:
                    raise InvalidCredentialsException
            except InvalidCredentialsException:
                abort(401, {"message": "Invalid credentials. Please log in again"})
            except Exception:
                abort(500, {"message": "Unexcepted error, server cannot handle request"})

        return _jwt_required
