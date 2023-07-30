from flask import Flask
from init import db, ma, bcrypt, jwt
import os
from flask import Blueprint
from flask import current_app

def create_app():
    # Initialize a new Flask application
    app = Flask(__name__)

    # Set the configuration parameters for the Flask application
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")  # Sets the database URL from the environment variable
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")  # Sets the JWT secret key from the environment variable

    # Initialize packages with the Flask application instance
    db.init_app(app)  # Initialize SQLAlchemy with this Flask application
    ma.init_app(app)  # Initialize Marshmallow with this Flask application
    bcrypt.init_app(app)  # Initialize Bcrypt with this Flask application
    jwt.init_app(app)  # Initialize JWTManager with this Flask application

    # Import commands and initialize with app
    import commands
    commands.init_app(app)

    # Import all registerable controllers from the controllers module
    from controllers import registerable_controllers
    # Loop over each controller, and register it as a Blueprint with the Flask application
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    # Finally, return the configured Flask application instance
    return app