from flask import Blueprint, request
from init import db, bcrypt, ma
from marshmallow import Schema, fields, validate
from models.user import User
from schemas.user_schema import user_schema, UserSchema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from functools import wraps
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from datetime import timedelta

# Create an authentication blueprint with the 'auth' prefix for routing
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register route for new users
@auth_bp.route('/register', methods=['POST'])
def auth_register():
    try:
        # Get JSON data from the request
        body_data = request.get_json()

        # Initialize the schema and validate the user input
        user_schema = UserSchema()
        user_data = user_schema.load(body_data)
        
        # Check if the password and confirmation password are matching
        if body_data.get('password') != body_data.get('confirm_password'):
            return { 'error': 'Password and confirm password do not match.' }, 400

        # Create a new User model instance from the validated user info
        user = User() 
        user.username = user_data.get('username')
        user.email = user_data.get('email')
        user.password = bcrypt.generate_password_hash(user_data.get('password')).decode('utf-8')

        # Add the user to the db session and commit it to the database
        db.session.add(user)
        db.session.commit()

        # Return the newly created user and a 201 status code
        return user_schema.dump(user), 201
    
    # Handle Integrity Errors from the database
    except IntegrityError as err:
        # Unique violation would mean the email is already in use
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return { 'error': 'Email address already in use' }, 409
        # Not null violation would mean a required field is missing
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return { 'error': f'The {err.orig.diag.column_name} is required' }, 409
        

# Define schema for login credentials
class LoginSchema(ma.SQLAlchemyAutoSchema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

## Login route for existing users
@auth_bp.route('/login', methods=['POST'])
def auth_login():
    # Get JSON data from the request
    body_data = request.get_json()

    # Initialize the schema and validate the user input
    login_schema = LoginSchema()
    user_data = login_schema.load(body_data)

    # Query the database for a User with the given email
    stmt = db.select(User).filter_by(email=user_data.get('email'))
    user = db.session.scalar(stmt)

    # Check if user exists
    if user:
        # Check if password is correct
        if bcrypt.check_password_hash(user.password, user_data.get('password')):
            # Check if account is locked due to too many failed login attempts
            if user.locked:
                return { 'error': 'Account is locked due to too many failed login attempts. Please reset your password.' }, 401

            # Generate a JWT token for the authenticated user
            token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
            return { 'email': user.email, 'token': token, 'is_admin': user.is_admin }

        else:
            # Increment the failed login attempts for the user
            user.failed_login_attempts += 1
            db.session.commit()

            # Lock the user account after 5 failed attempts
            if user.failed_login_attempts >= 5:
                user.locked = True
                db.session.commit()

            # Return error for invalid credentials
            return { 'error': 'Invalid email or password' }, 401

    else:
        # Return error if user not found
        return { 'error': 'Invalid email or password' }, 401
    
# Decorator for routes that require admin privileges
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        # Get the current user from the JWT token
        current_user_id = get_jwt_identity()
        stmt = db.select(User).filter_by(id=current_user_id)
        current_user = db.session.scalar(stmt)

        # Return an error if the user is not an admin
        if not current_user.is_admin:
            return { 'error': 'Admin privilege required' }, 403

        # Otherwise, proceed with the function
        else:
            return fn(*args, **kwargs)
    return wrapper

# Decorator for routes that require user authentication
def user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get the current user from the JWT token
        user_id = get_jwt_identity()

        # Compare the user_id from JWT token to the target_user_id in the function's arguments
        target_user_id = kwargs.get('user_id')
        if user_id != target_user_id:
            return {"message": "You do not have the necessary permissions to perform this operation"}, 403

        # Proceed with the function if the user_id matches the target_user_id
        return func(*args, **kwargs)
    return wrapper