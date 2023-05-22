from flask_restx import fields, Model

UserModel = Model('UserModel', {
    'id': fields.Integer(readOnly=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'created_date': fields.DateTime
})