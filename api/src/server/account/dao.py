from server.app import db
from server.account.model import AccountModel

class AccountDao(object):
    @staticmethod
    def find_by_id(id):
        return db.session.get(AccountModel, {"id": id})
    
    @staticmethod
    def find_by_email(email):
        return db.session.scalar(db.select(AccountModel).where(AccountModel.email == email))
    
    @staticmethod
    def save(account):
        db.session.add(account)
        db.session.commit()