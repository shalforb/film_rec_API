from flask import Blueprint, request
from init import db
from models.ratings import Rating
from models.user import User
from schemas.ratings_schema import rating_schema, ratings_schema, RatingSchema
from controllers.auth_controller import user_required
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError


# Create a blueprint for ratings routes
rating_bp = Blueprint('rating', __name__, url_prefix='/ratings')

# Define a route to create a rating
@rating_bp.route('/', methods=['POST'])
# This route requires a valid JWT token
@jwt_required()
def create_rating():
    # Get the identity of the user (email)
    user_id = get_jwt_identity()
    # Get the User instance from the database
    user = User.query.get(user_id)
    # If the user is not found, return an error message
    if not user:
        return {'message': 'User not found'}, 404

    # Get the data from the request
    data = request.get_json()
    rating_schema = RatingSchema()
    # Validate the request data
    try:
        validated_data = rating_schema.load(data)
    except ValidationError as err:
        # If the data is not valid, return an error message
        return {'error': err.messages}, 400

    # Create a new Rating instance and add it to the database
    rating = Rating(**validated_data)
    db.session.add(rating)
    db.session.commit()
    # Return the created rating
    return rating_schema.dump(rating), 201

# Define a route to update a rating
@rating_bp.route('/<int:id>', methods=['PUT'])
# This route requires a valid JWT token
@jwt_required()
def update_rating(id):
    # Same process as in the create_rating function
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404

    # Get the data from the request and the Rating instance from the database
    data = request.get_json()
    rating = Rating.query.get(id)
    # If the rating is not found or not owned by the user, return an error message
    if not rating or rating.user_id != user_id:
        return {'message': 'Rating not found or not owned by the user'}, 404

    # Update the rating with the new data
    for key, value in data.items():
        setattr(rating, key, value)

    db.session.commit()
    # Return the updated rating
    return rating_schema.dump(rating), 200

# Define a route to delete a rating
@rating_bp.route('/<int:id>', methods=['DELETE'])
# This route requires a valid JWT token
@jwt_required()
def delete_rating(id):
    # Same process as in the update_rating function
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    rating = Rating.query.get(id)
    if not rating or rating.user_id != user_id:
        return {'message': 'Rating not found or not owned by the user'}, 404

    # Delete the rating from the database
    db.session.delete(rating)
    db.session.commit()
    # Return no content
    return '', 204

# Define a route to get all ratings by a specific user
@rating_bp.route('/user/<int:user_id>', methods=['GET'])
# This route requires a valid JWT token and the user to be a user
@jwt_required()
@user_required
def get_ratings_by_user(user_id):
    # Get the identity of the current user
    current_user = get_jwt_identity()
    # If the current user is not the user specified in the route, return an error message
    if current_user != user_id:
        return {"message": "You do not have the necessary permissions to perform this operation"}, 403
    # Get all ratings by the user
    ratings = Rating.query.filter_by(user_id=user_id).all()
    if not ratings:
        return {"message": "No ratings found for this user"}, 404
    # Return all ratings by the user
    return ratings_schema.dump(ratings), 200

# Define a route to get all ratings for a specific film
@rating_bp.route('/film/<int:film_id>', methods=['GET'])
def get_ratings_for_film(film_id):
    # Get all ratings for the film
    ratings = Rating.query.filter_by(film_id=film_id).all()
    if not ratings:
        return {"message": "No ratings found for this film"}, 404
    # Return all ratings for the film
    return ratings_schema.dump(ratings), 200

# Define a route to get the average rating for a specific film
@rating_bp.route('/film/<int:film_id>/average', methods=['GET'])
def get_average_rating_for_film(film_id):
    # Get all ratings for the film
    ratings = Rating.query.filter_by(film_id=film_id).all()
    if len(ratings) == 0:
        return {"message": "No ratings found for this film"}, 404
    # Calculate the average rating
    average_rating = sum([rating.rating for rating in ratings]) / len(ratings)
    # Return the average rating
    return {'average_rating': average_rating}, 200

# Define a route to delete all ratings by a specific user
@rating_bp.route('/user/<int:user_id>', methods=['DELETE'])
# This route requires a valid JWT token and the user to be a user
@jwt_required()
@user_required
def delete_ratings_by_user(user_id):
    # Same process as in the get_ratings_by_user function
    current_user = get_jwt_identity()
    if current_user != user_id:
        return {"message": "You do not have the necessary permissions to perform this operation"}, 403
    ratings = Rating.query.filter_by(user_id=user_id).all()
    if not ratings:
        return {"message": "No ratings found for this user"}, 404
    # Delete all ratings by the user
    for rating in ratings:
        db.session.delete(rating)
    db.session.commit()
    # Return no content
    return '', 204