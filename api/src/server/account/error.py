class DuplicateEmailException(Exception):
    def __init__(self, message="Email already exists!"):
        self.message = message
        super().__init__(message)


class AccountNotFoundException(Exception):
    def __init__(self, message="Account not found!"):
        self.message = message
        super().__init__(message)


class InvalidCredentialsException(Exception):
    def __init__(self, message="Credentials are invalid!"):
        self.message = message
        super().__init__(message)
