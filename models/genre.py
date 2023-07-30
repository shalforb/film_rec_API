from init import db, ma
from marshmallow import fields

# Define the Genre model
class Genre(db.Model):
    __tablename__ = 'genres'

    # Define the fields, specifying data types and constraints
    genre_id = db.Column(db.Integer, primary_key=True)  # Primary key for the genre
    genre_name = db.Column(db.String(64), unique=True, nullable=False)  # The name of the genre, must be unique

    # Relationship to the FilmGenre model
    film_genres = db.relationship('FilmGenre', backref='genre', lazy=True)  # One to many relationship with FilmGenre