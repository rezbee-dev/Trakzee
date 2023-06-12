from server.profile.dao import ProfileDao
from server.profile.error import DuplicateAccountException, DuplicateUsernameException
from server.profile.model import ProfileModel


class ProfileService(object):
    @staticmethod
    def create(data):
        # extract username & account_id and init Profile instance
        profile = ProfileModel(username=data["username"], account_id=data["account_id"])

        # check for existing profile with same account_id
        if ProfileDao.find_by_account_id(profile.account_id):
            raise DuplicateAccountException

        # Check for duplicate username
        if ProfileDao.find_by_username(profile.username):
            raise DuplicateUsernameException

        # save Profile instance and return saved model
        return ProfileModel.save(profile)
