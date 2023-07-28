from flask import Flask
import os
from init import db, ma, bcrypt, jwt
from flask import Blueprint
# from controllers.user_controller import user_bp
# from controllers.film_controller import film_bp
from controllers import cli_controller
# from controllers.genre_controller import genre_bp
# from controllers.filmgenre_controller import filmgenre_bp
from flask import current_app


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cli_controller.init_app(app)

    # app.register_blueprint(user_bp)
    # app.register_blueprint(film_bp)
    # app.register_blueprint(genre_bp)
    # app.register_blueprint(filmgenre_bp)

    return app