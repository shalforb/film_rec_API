from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Range
from models.film import Film

# Define the FilmSchema
class FilmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True  # Keep the order of the fields as defined
        model = Film  # Specify the Film model
        load_instance = True  # Deserialize to model instances
        fields = ('film_id', 'title', 'director', 'year')  # Fields to include in the schema

    # Define validation for fields
    title = fields.String(required=True, validate=Length(min=1, max=100))
    director = fields.String(required=True, validate=Length(min=1, max=100))
    year = fields.Integer(required=True, validate=Range(min=1800, max=2100))

# Create instances of the FilmSchema
film_schema = FilmSchema()
films_schema = FilmSchema(many=True)