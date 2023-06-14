import jwt

from server.account.auth import AccountAuth
from server.account.dao import AccountDao
from server.account.error import AccountNotFoundException, DuplicateEmailException, InvalidCredentialsException
from server.account.model import AccountModel


class AccountService(object):
    @staticmethod
    def register(data):
        # Init Account instance with username, email, and hashed password
        account = AccountModel(email=data["email"], password=AccountAuth.hash_password(data["password"]))

        # Check for duplicate username & email
        # TODO: Replace with guards
        if AccountDao.find_by_email(account.email):
            raise DuplicateEmailException

        # Save & return Account instance to database
        AccountDao.save(account)
        return account

    @staticmethod
    def login(data):
        # Find account by email
        account = AccountDao.find_by_email(data["email"])
        if account is None:
            raise AccountNotFoundException

        # Check password match
        if not AccountAuth.is_matching_password(account.password, data["password"]):
            raise InvalidCredentialsException

        # Generate & return JWT access & refresh tokens
        tokens = {
            "access_token": AccountAuth.encode_token(account.id, "access"),
            "refresh_token": AccountAuth.encode_token(account.id, "refresh"),
        }

        return tokens

    @staticmethod
    def get_account_by_token(data):
        try:
            # Use token from data & extract accountId
            accountId = AccountAuth.decode_token(data["token"])

            # Find account by accountId
            account = AccountDao.find_by_id(accountId)

            # Token is invalid or account is not found
            if account is None:
                raise InvalidCredentialsException

            return account

        # Catch jwt.ExpiredSignatureError & jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            raise InvalidCredentialsException
        except jwt.InvalidTokenError:
            raise InvalidCredentialsException

    @staticmethod
    def refresh(data):
        account = AccountService.get_account_by_token(data=data)
        # Generate & return JWT access & refresh tokens
        return {"access_token": AccountAuth.encode_token(account.id, "access")}


# Auth
# Access tokens can be stored in memory and have short TTL
#   - Access token can be sent with HTTP header
#   - If user refreshes page or time expires, than they will need to re-login again
#   - When access_token is invalid, client can request a new access token via /refresh
# Refresh tokens can be stored in cookie and its paths can be limited to /refresh & /logout
#   - When client makes request to /refresh,
#     a new access_token is sent and client will store in memory & make request again
# If client makes request to secure endpoint that requires login,
# then return LoginRequiredMessage, regardless of refresh token
#   - redirect to login page?
