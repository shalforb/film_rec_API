# from init import db, ma
# from marshmallow import fields

# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False, unique=True)
#     password = db.Column(db.String, nullable=False)
#     is_admin = db.Column(db.Boolean, default=False)

#     ratings = db.relationship('Rating', back_populates='user', cascade='all, delete')

# class UserSchema(ma.SQLAlchemySchema):
#     ratings = fields.List(fields.Nested('RatingSchema', exclude=['user']))

#     class Meta:
#         fields = ('id', 'name', 'email', 'password', 'is_admin', 'ratings')

# user_schema = UserSchema(exclude=['password'])
# users_schema = UserSchema(many=True, exclude=['password'])