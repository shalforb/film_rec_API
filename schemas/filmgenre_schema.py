from init import db, ma
from marshmallow import fields
from models.filmgenre import FilmGenre

# Define the FilmGenreSchema
class FilmGenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FilmGenre  # Specify the FilmGenre model
        ordered = True  # Keep the order of the fields as defined
        load_instance = True  # Deserialize to model instances
        fields = ('filmgenre_id', 'film_id', 'genre_id')  # Fields to include in the schema

    # Specify required fields
    film_id = fields.Integer(required=True)
    genre_id = fields.Integer(required=True)

# Create instances of the FilmGenreSchema
filmgenre_schema = FilmGenreSchema()
filmgenres_schema = FilmGenreSchema(many=True)