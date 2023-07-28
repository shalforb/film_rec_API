# from flask import Blueprint, request
# from init import db
# from models.film import Film, film_schema, films_schema

# film_bp = Blueprint('film', __name__, url_prefix='/films')

# @film_bp.route('', methods=['POST'])
# def create_film():
#     body_data = request.get_json()
#     film = Film()
#     film.title = body_data.get('title')
#     film.director = body_data.get('director')
#     db.session.add(film)
#     db.session.commit()
#     return film_schema.dump(film), 201

# @film_bp.route('', methods=['GET'])
# def get_films():
#     films = Film.query.all()
#     return films_schema.dump(films)

# @film_bp.route('/<int:id>', methods=['GET'])
# def get_film(id):
#     film = Film.query.get(id)
#     if not film:
#         return {"message": "Film not found"}, 404
#     return film_schema.dump(film)

# @film_bp.route('/<int:id>', methods=['PUT'])
# def update_film(id):
#     body_data = request.get_json()
#     film = Film.query.get(id)
#     if not film:
#         return {"message": "Film not found"}, 404
#     film.title = body_data.get('title', film.title)
#     film.director = body_data.get('director', film.director)
#     db.session.commit()
#     return film_schema.dump(film)

# @film_bp.route('/<int:id>', methods=['DELETE'])
# def delete_film(id):
#     film = Film.query.get(id)
#     if not film:
#         return {"message": "Film not found"}, 404
#     db.session.delete(film)
#     db.session.commit()
#     return {}, 204