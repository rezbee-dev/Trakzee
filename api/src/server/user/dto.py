from flask_restx import Model, fields

UserDTO = Model(
    "UserDTO",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "active": fields.Boolean(default=True),
        "created_date": fields.DateTime,
    },
)

UserAuthDTO = Model.inherit("UserAuthDTO", UserDTO, {"password": fields.String(required=True)})