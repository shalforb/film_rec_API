from init import db, ma
from marshmallow import fields

# Define the Film model
class Film(db.Model):
    __tablename__ = 'films'

    # Define the fields, specifying data types and constraints
    film_id = db.Column(db.Integer, primary_key=True)  # Primary key for the film
    title = db.Column(db.String(200), unique=True, nullable=False)  # The title of the film, must be unique
    director = db.Column(db.String(200), nullable=False)  # Director of the film
    year = db.Column(db.Integer, nullable=False)  # Release year of the film

    # Relationships to the Rating and FilmGenre models
    ratings = db.relationship('Rating', backref='film', lazy=True)  # One to many relationship with Rating
    film_genres = db.relationship('FilmGenre', backref='film', lazy=True)  # One to many relationship with FilmGenre