from marshmallow import Schema, fields, validate

class SignupRequestSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True)
    mobile_number = fields.String(required=True, validate=validate.Length(min=10, max=10))
    password = fields.String(required=True, validate=validate.Length(min=6, max=128))
    profile_pic = fields.String(required=False)

# Create an instance of the schema for validation
signup_schema = SignupRequestSchema()
