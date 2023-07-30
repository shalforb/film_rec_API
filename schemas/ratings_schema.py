from init import db, ma
from marshmallow import fields
from marshmallow import validate
from models.ratings import Rating

# Define the RatingSchema
class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating  # Specify the Rating model
        ordered = True  # Keep the order of the fields as defined
        fields = ('rating_id', 'film_id', 'user_id', 'rating')  # Fields to include in the schema
        load_instance = True  # Deserialize to model instances

    # Specify required fields and validate rating
    film_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    rating = fields.Integer(required=True, validate=validate.Range(min=0, max=5))

# Create instances of the RatingSchema
rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)