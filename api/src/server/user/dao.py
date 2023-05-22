from server.app import db
from server.user.schema import UserSchema


class UserDao(object):
    @staticmethod
    def find_by_id(id):
        return db.session.get(UserSchema, {"id": id})

    @staticmethod
    def find_by_email(email):
        return db.session.execute(
            db.select(UserSchema).where(UserSchema.email == email)
        ).one_or_none()

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
