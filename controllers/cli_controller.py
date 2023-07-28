from flask import Blueprint
from init import db, bcrypt
from models.film import Film

def init_app(app):
    @app.cli.command('create')
    def create_db():
        db.create_all()
        print("Tables Created")

    @app.cli.command('drop')
    def drop_db():
        db.drop_all()
        print("Tables dropped")

    @app.cli.command("seed")
    def seed_db():
        from datetime import date
        # create the first card object
        film1 = Film(
            # set the attributes, not the id, SQLAlchemy will manage that for us
            title = "Jurassic Park",
            year = "1993",
            director = "Stephen Speilberg",
        )
        # Add the object as a new row to the table
        db.session.add(film1)
        
        # create the second card object
        film2 = Film(
            # set the attributes, not the id, SQLAlchemy will manage that for us
            title = "Godather",
            year = "1971",
            director = "Francis Ford Coppolla",
        )
        # Add the object as a new row to the table
        db.session.add(film2)
        # commit the changes
        db.session.commit()
        print("Table seeded")