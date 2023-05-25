from sqlalchemy.sql import func

from server.app import db


class UserSchema(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "{0} - {1} - {2} - {3} - {4}".format(self.id, self.username, self.email, self.active, self.created_date)
