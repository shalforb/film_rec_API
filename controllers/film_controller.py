from flask import Blueprint, request
from init import db
from models.film import Film
from models.filmgenre import FilmGenre
from schemas.film_schema import film_schema, films_schema
from controllers.auth_controller import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity

# create a Blueprint for film related routes
film_bp = Blueprint('film', __name__, url_prefix='/films')

# route to get all films
@film_bp.route('', methods=['GET'])
def get_films():
    # query the database for all films
    films = Film.query.all()
    # return all films in JSON format
    return films_schema.dump(films)

# route to get a film by id
@film_bp.route('/<int:id>', methods=['GET'])
def get_film(id):
    # query the database for a film with the given id
    film = Film.query.get(id)
    # return an error if no film was found
    if not film:
        return {"message": "Film not found"}, 404
    # return the film in JSON format
    return film_schema.dump(film)

# route to search for films by title
@film_bp.route('/search/<string:title>', methods=['GET'])
def search_film(title):
    # query the database for films with the given title (case insensitive)
    films = Film.query.filter(Film.title.ilike(f'%{title}%')).all()
    # return an error if no films were found
    if not films:
        return {"message": "No films found with the given title"}, 404
    # return the films in JSON format
    return films_schema.dump(films)

# route to get films by release year
@film_bp.route('/year/<int:year>', methods=['GET'])
def get_films_by_year(year):
    # query the database for films released in the given year
    films = Film.query.filter_by(year=year).all()
    # return an error if no films were found
    if not films:
        return {"message": "No films found from the given year"}, 404
    # return the films in JSON format
    return films_schema.dump(films)

# route to get films by director
@film_bp.route('/director/<string:director>', methods=['GET'])
def get_films_by_director(director):
    # query the database for films directed by the given director
    films = Film.query.filter_by(director=director).all()
    # return an error if no films were found
    if not films:
        return {"message": "No films found from the given director"}, 404
    # return the films in JSON format
    return films_schema.dump(films)

# route to get films by genre
@film_bp.route('/genre/<int:genre_id>', methods=['GET'])
def get_films_by_genre(genre_id):
    # query the database for films in the given genre
    genre_films = FilmGenre.query.filter_by(genre_id=genre_id).all()
    # return an error if no films were found
    if not genre_films:
        return {"message": "No films found for this genre"}, 404
    # return the films in JSON format
    films = [film_genre.film for film_genre in genre_films]
    return films_schema.dump(films)

# route to create a film, requires admin privileges
@film_bp.route('', methods=['POST'])
@jwt_required()
@admin_required
def create_film():
    # get the data from the request
    body_data = request.get_json()
    # create a new film
    film = Film()
    film.title = body_data.get('title')
    film.director = body_data.get('director')
    film.year = body_data.get('year')
    # add the film to the session and commit the session to the database
    db.session.add(film)
    db.session.commit()
    # return the film in JSON format
    return film_schema.dump(film), 201

# route to update a film, requires admin privileges
@film_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_film(id):
    # get the data from the request
    body_data = request.get_json()
    # query the database for the film to be updated
    film = Film.query.get(id)
    # return an error if no film was found
    if not film:
        return {"message": "Film not found"}, 404
    # update the film's information
    film.title = body_data.get('title', film.title)
    film.director = body_data.get('director', film.director)
    film.year = body_data.get('year', film.year)
    # commit the session to the database
    db.session.commit()
    # return the updated film in JSON format
    return film_schema.dump(film)

# route to delete a film, requires admin privileges
@film_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_film(id):
    # query the database for the film to be deleted
    film = Film.query.get(id)
    # return an error if no film was found
    if not film:
        return {"message": "Film not found"}, 404
    # delete the film from the session and commit the session to the database
    db.session.delete(film)
    db.session.commit()
    # return an empty response with a success status code
    return {}, 204