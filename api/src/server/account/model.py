from server.app import db


class AccountModel(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    verified = db.Column(db.Boolean(), default=True, nullable=False)
    profile = db.relationship("ProfileModel", uselist=False, back_populates="account")

    def __init__(self, email, password):
        self.email = email
        self.password = password
