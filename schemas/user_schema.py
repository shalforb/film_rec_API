from init import db, ma
from marshmallow import fields
from models.user import User
from marshmallow.validate import Length, Email
from marshmallow import fields, pre_load
from marshmallow.validate import Regexp

# Define the UserSchema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True  # Keep the order of the fields as defined
        model = User  # Specify the User model
        fields = ('user_id', 'username', 'email', 'password', 'is_admin')  # Fields to include in the schema
        load_instance = True  # Deserialize to model instances

    # Define validation for fields
    username = fields.String(required=True, validate=[Length(min=1, max=25), Regexp(r'^[\w.]+$')])
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=Length(min=8, max=25))
    is_admin = fields.Boolean(required=True)

# Create instances of the UserSchema, excluding password field for security reasons
user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])