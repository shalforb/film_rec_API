from controllers.user_controller import user_bp
from controllers.film_controller import film_bp
from controllers.ratings_controller import rating_bp
from controllers.auth_controller import auth_bp
from controllers.genre_controller import genre_bp
from controllers.filmgenre_controller import filmgenre_bp

# An array of blueprints is created, which will later be registered in the application factory
# The order of registration can be important because route handlers for common path prefixes 
# are defined on a first-registered-first-served basis. 
registerable_controllers = [
    user_bp,
    film_bp,
    rating_bp,
    auth_bp,
    genre_bp,
    filmgenre_bp
]


