# from flask import Blueprint, request
# from init import db
# from models.user import User, user_schema, users_schema
# user_bp = Blueprint('users', __name__, url_prefix='/users')

# @user_bp.route('/', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return users_schema.dump(users), 200

# @user_bp.route('/<int:id>', methods=['GET'])
# def get_user(id):
#     user = User.query.get(id)
#     return user_schema.dump(user), 200

# @user_bp.route('/', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     user = User(**data)
#     db.session.add(user)
#     db.session.commit()
#     return user_schema.dump(user), 201

# @user_bp.route('/<int:id>', methods=['PUT'])
# def update_user(id):
#     data = request.get_json()
#     user = User.query.get(id)
#     for key, value in data.items():
#         setattr(user, key, value)
#     db.session.commit()
#     return user_schema.dump(user), 200

# @user_bp.route('/<int:id>', methods=['DELETE'])
# def delete_user(id):
#     user = User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()
#     return '', 204