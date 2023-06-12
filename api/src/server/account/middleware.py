from functools import wraps
from flask import request

from server.account.error import *
from server.account.service import AccountService

class AuthMiddleware(object):
    current_account = None
    
    # src: https://circleci.com/blog/authentication-decorators-flask/
    @staticmethod
    def jwt_required(func):
        @wraps(func)
        def wrapper_jwt_required(*args, **kwargs):
            auth_headers = request.headers.get("Authorization")
            if auth_headers:
                try:
                    access_token = auth_headers.split(" ")[1]
                    AuthMiddleware.current_account = AccountService.get_account_by_token({"token": access_token})
                    return func(*args, **kwargs)
                except InvalidCredentialsException:
                    return {"message": "Invalid credentials. Please log in again"}, 401
                except Exception as err:
                    print("error message", err)
                    return {"message": "Unexcepted error, server cannot handle request"}, 500
            else:
                return {"message": "Invalid credentials. Please log in again"}, 401
            
        return wrapper_jwt_required