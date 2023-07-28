from init import db, ma
from marshmallow import fields

class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String, nullable=False)

    # film_genres = db.relationship('FilmGenre', back_populates = 'film', cascade='all, delete')
    # ratings = db.relationship('Rating', back_populates = 'film', cascade='all, delete')

# class FilmSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Film
#         load_instance = True