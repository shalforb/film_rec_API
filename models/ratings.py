# class Rating(db.Model):
#     __tablename = 'ratings'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     film_id = db.Column(db.Integer, db.ForeignKey('films.id'), nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#     review = db.Column(db.String)

#     user = db.relationship('User', back_pop='ratings')
#     film = db.relationship('Film', back_pop='ratings')

# class RatingSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Rating
#         load_instance = True