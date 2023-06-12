import datetime
import jwt
from flask import current_app

from server.app import bcrypt

class AccountAuth(object):
    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password, current_app.config.get('BCRYPT_LOG_ROUNDS')).decode('utf-8')
    
    @staticmethod
    def is_matching_password(passwordOriginal, password):
        return bcrypt.check_password_hash(passwordOriginal, password)

    @staticmethod
    def encode_token(user_id, token_type):
        
        seconds = current_app.config.get('ACCESS_TOKEN_EXPIRATION') if token_type == 'access' else current_app.config.get('REFRESH_TOKEN_EXPIRATION')
        
        jwt_payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=seconds),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id
        }
        
        return jwt.encode(
            payload=jwt_payload,
            key=current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
        
    @staticmethod
    def decode_token(token):
        payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms='HS256')
        return payload["sub"]
    
    