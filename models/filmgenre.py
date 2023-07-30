from init import db, ma
from marshmallow import fields


# Define the FilmGenre model
class FilmGenre(db.Model):
    __tablename__ = 'film_genres'

    # Define the fields, specifying data types and constraints
    filmgenre_id = db.Column(db.Integer, primary_key=True)  # Primary key for the film genre
    film_id = db.Column(db.Integer, db.ForeignKey('films.film_id'), nullable=False)  # Foreign key pointing to the Film model
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)  # Foreign key pointing to the Genre model