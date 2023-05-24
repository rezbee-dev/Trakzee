from server.app import db
from server.user.schema import UserSchema


class UserDao(object):
    @staticmethod
    def find_by_id(id):
        return db.session.get(UserSchema, {"id": id})

    @staticmethod
    def find_by_email(email):
        return db.session.execute(db.select(UserSchema).where(UserSchema.email == email)).one_or_none()

    @staticmethod
    def find_all():
        return db.session.execute(db.select(UserSchema)).all()

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def delete_all():
        db.session.execute(db.delete(UserSchema))
        db.session.commit()

    @staticmethod
    def delete_by_id(id):
        user = UserDao.find_by_id(id)

        if user is None:
            return None

        db.session.delete(user)
        db.session.commit()

        return user

    @staticmethod
    def update_by_id(id, data):
        user = UserDao.find_by_id(id)

        if user is None:
            return None

        user.username = data["username"]
        user.email = data["email"]

        db.session.commit()

        return user
