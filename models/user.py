from init import db, ma
from marshmallow import fields

# Define the User model
class User(db.Model):
    __tablename__ = 'users'

    # Define the fields, specifying data types and constraints
    user_id = db.Column(db.Integer, primary_key=True)  # Primary key for the user
    username = db.Column(db.String(64), unique=True, nullable=False)  # The username, must be unique
    password = db.Column(db.String(128), nullable=False)  # The user's password
    email = db.Column(db.String(120), unique=True, nullable=False)  # The user's email, must be unique
    is_admin = db.Column(db.Boolean, default=False)  # Boolean indicating whether the user is an admin or not, not an admin by default

    # Relationship to the Rating model
    ratings = db.relationship('Rating', backref='user', lazy=True)  # One to many relationship with Rating