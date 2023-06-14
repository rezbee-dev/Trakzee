from flask_restx import Model, fields

AuthResponse = Model(
    "Auth response",
    {
        "id": fields.Integer(readOnly=True),
        "email": fields.String(required=True),
    },
)

AuthRequest = Model(
    "Auth request",
    {
        "email": fields.String(required=True),
        "password": fields.String(required=True),
    },
)

AuthRefresh = Model("Refresh token", {"refresh_token": fields.String(required=True)})

AuthTokens = Model("Access token", {"access_token": fields.String(required=True)})

# AuthTokens = Model.clone(
#     "Auth tokens",
#     AuthRefresh,
#     {
#         "access_token": fields.String(required=True)
#     }
# )

AccountPartial = Model(
    "Account Partial",
    {
        "id": fields.Integer(readOnly=True),
        "email": fields.String(required=True),
        "verified": fields.Boolean(required=True),
    },
)

AccountFull = Model.inherit(
    "Account Full",
    AccountPartial,
    {
        "password": fields.String(required=True),
    },
)
