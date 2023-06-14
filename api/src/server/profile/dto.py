from flask_restx import Model, fields

from server.account.dto import AccountPartial

ProfileResponse = Model.clone(
    "Profile response",
    AccountPartial,
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)

ProfileRequest = Model(
    "Profile request",
    {
        "username": fields.String(required=True),
    },
)
