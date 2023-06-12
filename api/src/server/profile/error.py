class DuplicateUsernameException(Exception):
    def __init__(self, message="Username already exists!"):
        self.message = message
        super().__init__(message)


class DuplicateAccountException(Exception):
    def __init__(self, message="Profile already exists!"):
        self.message = message
        super().__init__(message)


class ProfileNotFoundException(Exception):
    def __init__(self, message="Profile not found!"):
        self.message = message
        super().__init__(message)
