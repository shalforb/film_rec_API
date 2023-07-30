from flask import Blueprint, request  
from init import db  
from models.user import User  
from schemas.user_schema import user_schema, users_schema  
from controllers.auth_controller import admin_required  
from flask_jwt_extended import jwt_required, get_jwt_identity  

# Creating a Blueprint for the user routes
user_bp = Blueprint('users', __name__, url_prefix='/users')

# Define a route for getting all users. It's only accessible to admins.
@user_bp.route('/', methods=['GET'])
@jwt_required()  # The request must include a valid JWT token
@admin_required  # The JWT token's user must be an admin
def get_users():
    users = User.query.all()  # Get all User objects from the database
    return users_schema.dump(users), 200  # Serialize the users to JSON format and return them

# Define a route for getting a specific user by their id.
@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)  # Get the User object with the given id
    if not user:  # If there's no user with this id
        return {"message": "User not found"}, 404
    return user_schema.dump(user), 200  # Serialize the user to JSON format and return it

# Define a route for creating a new user.
@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()  # Get the JSON payload of the request
    user = User(**data)  # Create a new User object using the data
    db.session.add(user)  # Add the user to the database session
    db.session.commit()  # Commit the changes to the database
    return user_schema.dump(user), 201  # Serialize the user to JSON format and return it

# Define a route for updating a specific user. The user can only update their own data.
@user_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()  # The request must include a valid JWT token
def update_user(id):
    user_id = get_jwt_identity()  # Get the id of the user from the JWT token
    user = User.query.get(id)  # Get the User object with the given id

    # If there's no user with this id or the token's user id doesn't match the user's id
    if not user or user.user_id != user_id:
        return {"message": "User not found or not authorized"}, 404

    data = request.get_json()  # Get the JSON payload of the request
    # For each key-value pair in the data, set the user's attribute with that name to that value
    for key, value in data.items():
        setattr(user, key, value)

    db.session.commit()  # Commit the changes to the database
    return user_schema.dump(user), 200  # Serialize the user to JSON format and return it

# Define a route for deleting a user. Only admins can delete users.
@user_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()  # The request must include a valid JWT token
@admin_required  # The JWT token's user must be an admin
def delete_user(id):
    user = User.query.get(id)  # Get the User object with the given id
    if not user:  # If there's no user with this id
        return {"message": "User not found"}, 404
    db.session.delete(user)  # Delete the user from the database session
    db.session.commit()  # Commit the changes to the database
    return '', 204  # Return no content

# Define a route for getting the data of the currently logged-in user.
@user_bp.route('/me', methods=['GET'])
@jwt_required()  # The request must include a valid JWT token
def get_current_user():
    user_id = get_jwt_identity()  # Get the id of the user from the JWT token
    user = User.query.get(user_id)  # Get the User object with this id
    if not user:  # If there's no user with this id
        return {"message": "User not found"}, 404
    return user_schema.dump(user), 200  # Serialize the user to JSON format and return it
