# Import the necessary packages
from flask_sqlalchemy import SQLAlchemy  # For ORM-based database interactions
from flask_marshmallow import Marshmallow  # For object serialization/deserialization
from flask_bcrypt import Bcrypt  # For password hashing
from flask_jwt_extended import JWTManager  # For handling JSON Web Tokens (JWTs)

# Initialize instances of the imported packages
db = SQLAlchemy()  # This object links with our Flask application to various database operations
ma = Marshmallow()  # Object for serialization of SQLAlchemy objects to JSON and vice versa
bcrypt = Bcrypt()  # Object to handle hashing of sensitive data like passwords
jwt = JWTManager()  # Object to handle operations related to JWT such as creation, expiration, and verification
