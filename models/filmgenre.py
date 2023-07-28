# from init import db, ma
# from marshmallow import fields

# class FilmGenre(db.Model):
#     __tablename = 'film_genres'

#     id = db.Column(db.Integer, primary_key=True)
#     film_id = db.ForeignKey('films.id')
#     genre_id = db.ForeignKey('genres.id')

#     film = db.relationship('Film', back_pop='film_genres')
#     genre = db.relationship('Genre', back_pop='film_genations')

# class FilmGenreSchema(ma.SQLineAutoSchema):
#     class Meta:
#         model = FilmGenre
#         load_instance = True