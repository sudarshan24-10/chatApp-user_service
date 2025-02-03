from marshmallow import Schema, fields, validate

class SignupRequestSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True)
    mobile_number = fields.String(
        required=True,
        validate=[
            validate.Length(equal=10),  # Ensures exactly 10 digits
            validate.Regexp(r"^\d{10}$", error="Mobile number must contain only digits (0-9).")
        ]
    )
    password = fields.String(required=True, validate=validate.Length(min=6, max=128))
    profile_pic = fields.String(required=False)

signup_schema = SignupRequestSchema()
