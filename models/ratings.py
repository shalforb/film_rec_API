from init import db, ma
from marshmallow import fields

# Define the Rating model
class Rating(db.Model):
    __tablename__ = 'ratings'

    # Define the fields, specifying data types and constraints
    rating_id = db.Column(db.Integer, primary_key=True)  # Primary key for the rating
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)  # Foreign key pointing to the User model
    film_id = db.Column(db.Integer, db.ForeignKey('films.film_id'), nullable=False)  # Foreign key pointing to the Film model
    rating = db.Column(db.Float, nullable=False)  # The rating value, represented as a floating point number