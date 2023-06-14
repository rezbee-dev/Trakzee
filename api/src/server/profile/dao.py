from server.app import db
from server.profile.model import ProfileModel


class ProfileDao(object):
    @staticmethod
    def find_by_account_id(id):
        # check for existing profile with same account_id
        return db.session.execute(db.select(ProfileModel).where(ProfileModel.account_id == id)).one_or_none()

    @staticmethod
    def find_by_username(username):
        return db.session.execute(db.select(ProfileModel).where(ProfileModel.username == username)).one_or_none()

    # @staticmethod
    # def find_by_id(id):
    #     return db.session.get(ProfileSchema, {"id": id})

    # @staticmethod
    # def find_all():
    #     return db.session.execute(db.select(ProfileSchema)).all()

    # @staticmethod
    # def save(profile):
    #     db.session.add(profile)
    #     db.session.commit()

    # @staticmethod
    # def delete_all():
    #     db.session.execute(db.delete(ProfileSchema))
    #     db.session.commit()

    # @staticmethod
    # def delete_by_id(id):
    #     profile = ProfileDao.find_by_id(id)

    #     if profile is None:
    #         return None

    #     db.session.delete(profile)
    #     db.session.commit()

    #     return profile

    # @staticmethod
    # def update_by_id(id, data):
    #     profile = ProfileDao.find_by_id(id)

    #     if profile is None:
    #         return None

    #     profile.profilename = data["profilename"]
    #     profile.email = data["email"]

    #     db.session.commit()

    #     return profile
