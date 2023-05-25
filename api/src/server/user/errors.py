class DuplicateEmailException(Exception):
    def __init__(self, message="Email already exists!"):
        self.message = message
        super().__init__(message)


class UserNotFoundException(Exception):
    def __init__(self, message="User not found!"):
        self.message = message
        super().__init__(message)
