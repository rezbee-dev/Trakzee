from sqlalchemy.sql import func

from server.app import db

class ProfileModel(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), unique=True, nullable=False)
    account = db.relationship("AccountModel", back_populates="profile")

    def __init__(self, username, account_id):
        self.username = username
        self.account_id = account_id
