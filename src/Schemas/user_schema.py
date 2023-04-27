from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    password_hash = fields.String(load_only=True)
    type_token= fields.String()
    token= fields.String()