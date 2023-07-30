from flask import Blueprint, request
from init import db
from models.film import Film
from models.genre import Genre
from models.filmgenre import FilmGenre
from schemas.filmgenre_schema import filmgenre_schema, filmgenres_schema
from controllers.auth_controller import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create a new blueprint for filmgenre routes
filmgenre_bp = Blueprint('filmgenre', __name__, url_prefix='/filmgenres')

# Define route to get all genres for a given film
@filmgenre_bp.route('/<int:film_id>', methods=['GET'])
def get_genres_for_film(film_id):
    # Query FilmGenre table for all entries with given film_id
    filmgenres = FilmGenre.query.filter_by(film_id=film_id).all()
    # Return all genres as a serialized list
    return filmgenres_schema.dump(filmgenres)

# Define route to add a genre to a film
@filmgenre_bp.route('/<int:film_id>/<int:genre_id>', methods=['POST'])
# Only allow access to this route if user is logged in and is an admin
@jwt_required()
@admin_required
def add_genre_to_film(film_id, genre_id):
    # Get the film and genre from the database
    film = Film.query.get(film_id)
    genre = Genre.query.get(genre_id)
    # If either the film or genre doesn't exist, return an error message
    if not film or not genre:
        return {"message": "Film or genre not found"}, 404
    # Create a new FilmGenre entry linking the film and genre
    filmgenre = FilmGenre(film_id=film.id, genre_id=genre.id)
    # Add the new FilmGenre entry to the database and commit changes
    db.session.add(filmgenre)
    db.session.commit()
    # Return the new FilmGenre entry as a serialized object
    return filmgenre_schema.dump(filmgenre), 201

# Define route to remove a genre from a film
@filmgenre_bp.route('/<int:film_id>/<int:genre_id>', methods=['DELETE'])
# Only allow access to this route if user is logged in and is an admin
@jwt_required()
@admin_required
def remove_genre_from_film(film_id, genre_id):
    # Query FilmGenre table for an entry with the given film_id and genre_id
    filmgenre = FilmGenre.query.filter_by(film_id=film_id, genre_id=genre_id).first()
    # If such a FilmGenre entry doesn't exist, return an error message
    if not filmgenre:
        return {"message": "Film or genre not found"}, 404
    # Remove the FilmGenre entry from the database and commit changes
    db.session.delete(filmgenre)
    db.session.commit()
    # Return an empty response
    return {}, 204