from server.user.dao import UserDao
from server.user.errors import DuplicateEmailException, UserNotFoundException
from server.user.schema import UserSchema


# See: https://stackoverflow.com/questions/332255/difference-between-class-foo-and-class-fooobject-in-python
class UserService(object):
    @staticmethod
    def create(data):
        user = UserSchema(username=data["username"], email=data["email"])

        if UserDao.find_by_email(user.email):
            raise DuplicateEmailException

        UserDao.save(user)

        return user

    @staticmethod
    def find_by_id(id):
        return UserDao.find_by_id(id)

    @staticmethod
    def find_all():
        rows = UserDao.find_all()
        users = [user[0] for user in rows]
        return users

    @staticmethod
    def delete_all():
        return UserDao.delete_all()

    @staticmethod
    def delete_by_id(id):
        return UserDao.delete_by_id(id)

    # todo: implement guards
    @staticmethod
    def update_by_id(id, data):
        user = UserDao.find_by_id(id)

        if user is None:
            raise UserNotFoundException

        if user.email != data["email"] and UserDao.find_by_email(data["email"]):
            raise DuplicateEmailException

        return UserDao.update_by_id(id, data)
