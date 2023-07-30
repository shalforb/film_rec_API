from flask import Blueprint, request
from init import db
from models.genre import Genre
from schemas.genre_schema import genre_schema, genres_schema
from controllers.auth_controller import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity

# Define a blueprint for genre routes
genre_bp = Blueprint('genre', __name__, url_prefix='/genres')

# Define a route to get all genres
@genre_bp.route('', methods=['GET'])
def get_genres():
    # Query all genres from the Genre table
    genres = Genre.query.all()
    # Return all genres as a serialized list
    return genres_schema.dump(genres)

# Define a route to get a specific genre by ID
@genre_bp.route('/<int:id>', methods=['GET'])
def get_genre(id):
    # Get the genre by ID
    genre = Genre.query.get(id)
    # If no genre found with the given ID, return an error message
    if not genre:
        return {"message": "Genre not found"}, 404
    # Return the genre as a serialized object
    return genre_schema.dump(genre)

# Define a route to create a new genre
@genre_bp.route('', methods=['POST'])
# Only allow access to this route if the user is logged in and is an admin
@jwt_required()
@admin_required
def create_genre():
    # Get the request data
    body_data = request.get_json()
    # Create a new Genre object
    genre = Genre()
    # Set the name of the genre
    genre.name = body_data.get('name')
    # Add the new genre to the database and commit changes
    db.session.add(genre)
    db.session.commit()
    # Return the new genre as a serialized object
    return genre_schema.dump(genre), 201

# Define a route to update a genre
@genre_bp.route('/<int:id>', methods=['PUT'])
# Only allow access to this route if the user is logged in and is an admin
@jwt_required()
@admin_required
def update_genre(id):
    # Get the request data
    body_data = request.get_json()
    # Get the genre to be updated
    genre = Genre.query.get(id)
    # If no genre found with the given ID, return an error message
    if not genre:
        return {"message": "Genre not found"}, 404
    # Update the name of the genre
    genre.name = body_data.get('name', genre.name)
    # Commit changes to the database
    db.session.commit()
    # Return the updated genre as a serialized object
    return genre_schema.dump(genre)

# Define a route to delete a genre
@genre_bp.route('/<int:id>', methods=['DELETE'])
# Only allow access to this route if the user is logged in and is an admin
@jwt_required()
@admin_required
def delete_genre(id):
    # Get the genre to be deleted
    genre = Genre.query.get(id)
    # If no genre found with the given ID, return an error message
    if not genre:
        return {"message": "Genre not found"}, 404
    # Delete the genre from the database and commit changes
    db.session.delete(genre)
    db.session.commit()
    # Return an empty response
    return {}, 204