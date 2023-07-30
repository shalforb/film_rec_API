from init import db, ma
from marshmallow import fields
from models.genre import Genre
from marshmallow.validate import Length

# Define the GenreSchema
class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre  # Specify the Genre model
        ordered = True  # Keep the order of the fields as defined
        fields = ('genre_id', 'genre')  # Fields to include in the schema
        load_instance = True  # Deserialize to model instances

    # Define validation for fields
    genre = fields.String(required=True, validate=Length(min=1, max=100))

# Create instances of the GenreSchema
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)