from flask import Blueprint
from init import db, bcrypt 
from models.user import User
from models.ratings import Rating 
from models.film import Film
from models.filmgenre import FilmGenre
from models.genre import Genre



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
        
        film1 = Film(title="The Godfather", year=1972, director="Francis Ford Coppola")
        db.session.add(film1)

        film2 = Film(title="The Shawshank Redemption", year=1994, director="Frank Darabont")
        db.session.add(film2)

        film3 = Film(title="Pulp Fiction", year=1994, director="Quentin Tarantino")
        db.session.add(film3)

        film4 = Film(title="Fight Club", year=1999, director="David Fincher")
        db.session.add(film4)

        film5 = Film(title="Forrest Gump", year=1994, director="Robert Zemeckis")
        db.session.add(film5)

        film6 = Film(title="Inception", year=2010, director="Christopher Nollan")
        db.session.add(film6)

        film7 = Film(title="The Matrix", year=1999, director="Lana and Lilly Wachowski")
        db.session.add(film7)

        film8 = Film(title="Goodfellas", year=1990, director="Martin Scorsese")
        db.session.add(film8)

        film9 = Film(title="Se7en", year=1995, director="David Fincher")
        db.session.add(film9)

        film10 = Film(title="Gladiator", year=2000, director="Ridley Scott")
        db.session.add(film10)

        film11 = Film(title="The Dark Knight", year=2008, director="Christopher Nollan")
        db.session.add(film11)

        film12 = Film(title="Schindler's List", year=1993, director="Steven Spielberg")
        db.session.add(film12)

        film13 = Film(title="Interstellar", year=2014, director="Christopher Nolan")
        db.session.add(film13)

        film14 = Film(title="Django Unchained", year=2012, director="Quentin Tarantino")
        db.session.add(film14)

        film15 = Film(title="The Lord of the Rings: The Fellowship of the Ring", year=2001, director="Peter Jackson")
        db.session.add(film15)

        film16 = Film(title="The Lord of the Rings: The Two Towers", year=2002, director="Peter Jackson")
        db.session.add(film16)

        film17 = Film(title="The Lord of the Rings: The Return of the King", year=2003, director="Peter Jackson")
        db.session.add(film17)

        film18 = Film(title="Avengers: Endgame", year=2019, director="Anthony Russo, Joe Russo")
        db.session.add(film18)

        film19 = Film(title="Titanic", year=1997, director="James Cameron")
        db.session.add(film19)

        film20 = Film(title="Inglourious Basterds", year=2009, director="Quentin Tarantino")
        db.session.add(film20)

        admin_user = User(
            username = "admin",
            email = "admin@admin.com",
            password = bcrypt.generate_password_hash("admin").decode('utf-8'),
            is_admin = True
        )
        db.session.add(admin_user)  

        user1 = User(
            username = "user1",
            email = "user1@user1.com",
            password = bcrypt.generate_password_hash("user1").decode('utf-8'),
            is_admin = False
        )
        db.session.add(user1)

        user2 = User(
            username = "user2",
            email = "user2@user2.com",
            password = bcrypt.generate_password_hash("user2").decode('utf-8'),
            is_admin = False
        )
        db.session.add(user2)

        genre1 = Genre(genre_name="Action")
        db.session.add(genre1)

        genre2 = Genre(genre_name="Adventure")
        db.session.add(genre2)

        genre3 = Genre(genre_name="Comedy")
        db.session.add(genre3)

        genre4 = Genre(genre_name="Crime")
        db.session.add(genre4)

        genre5 = Genre(genre_name="Drama")
        db.session.add(genre5)

        genre6 = Genre(genre_name="Fantasy")
        db.session.add(genre6)

        genre7 = Genre(genre_name="Historical")
        db.session.add(genre7)

        genre8 = Genre(genre_name="Horror")
        db.session.add(genre8)

        genre9 = Genre(genre_name="Mystery")
        db.session.add(genre9)

        genre10 = Genre(genre_name="Romance")
        db.session.add(genre10)

        genre11 = Genre(genre_name="Science Fiction")
        db.session.add(genre11)

        genre12 = Genre(genre_name="Thriller")
        db.session.add(genre12)

        genre13 = Genre(genre_name="Western")
        db.session.add(genre13)

        genre14 = Genre(genre_name="War")
        db.session.add(genre14)

        genre15 = Genre(genre_name="Animation")
        db.session.add(genre15)

        genre16 = Genre(genre_name="Musical")
        db.session.add(genre16)

        genre17 = Genre(genre_name="Family")
        db.session.add(genre17)

        genre18 = Genre(genre_name="Documentary")
        db.session.add(genre18)

        genre19 = Genre(genre_name="Biography")
        db.session.add(genre19)

        genre20 = Genre(genre_name="Sport")
        db.session.add(genre20)

        filmgenre1 = FilmGenre(film_id=1, genre_id=4)
        db.session.add(filmgenre1)

        filmgenre2 = FilmGenre(film_id=1, genre_id=5)
        db.session.add(filmgenre2)

        filmgenre3 = FilmGenre(film_id=1, genre_id=12)
        db.session.add(filmgenre3)

        filmgenre4 = FilmGenre(film_id=2, genre_id=5)
        db.session.add(filmgenre4)

        filmgenre5 = FilmGenre(film_id=2, genre_id=12)  
        db.session.add(filmgenre5)

        filmgenre6 = FilmGenre(film_id=3, genre_id=5)
        db.session.add(filmgenre6)

        filmgenre7 = FilmGenre(film_id=3, genre_id=12)
        db.session.add(filmgenre7)

        filmgenre8 = FilmGenre(film_id=4, genre_id=1)
        db.session.add(filmgenre8)

        filmgenre9 = FilmGenre(film_id=4, genre_id=5)
        db.session.add(filmgenre9)

        filmgenre10 = FilmGenre(film_id=4, genre_id=12)
        db.session.add(filmgenre10)

        filmgenre11 = FilmGenre(film_id=5, genre_id=5)
        db.session.add(filmgenre11)

        filmgenre12 = FilmGenre(film_id=5, genre_id=10)
        db.session.add(filmgenre12)

        filmgenre13 = FilmGenre(film_id=6, genre_id=1)
        db.session.add(filmgenre13)

        filmgenre14 = FilmGenre(film_id=6, genre_id=5)
        db.session.add(filmgenre14)

        filmgenre15 = FilmGenre(film_id=6, genre_id=11)
        db.session.add(filmgenre15)

        filmgenre16 = FilmGenre(film_id=7, genre_id=1)
        db.session.add(filmgenre16)

        filmgenre17 = FilmGenre(film_id=7, genre_id=5)
        db.session.add(filmgenre17)

        filmgenre18 = FilmGenre(film_id=7, genre_id=11)
        db.session.add(filmgenre18)

        filmgenre19 = FilmGenre(film_id=8, genre_id=4)
        db.session.add(filmgenre19)

        filmgenre20 = FilmGenre(film_id=8, genre_id=5)
        db.session.add(filmgenre20)

        filmgenre21 = FilmGenre(film_id=8, genre_id=12)
        db.session.add(filmgenre21)

        filmgenre22 = FilmGenre(film_id=9, genre_id=5)
        db.session.add(filmgenre22)

        filmgenre23 = FilmGenre(film_id=9, genre_id=9)
        db.session.add(filmgenre23)

        filmgenre24 = FilmGenre(film_id=9, genre_id=12)
        db.session.add(filmgenre24)

        filmgenre25 = FilmGenre(film_id=10, genre_id=1)
        db.session.add(filmgenre25)

        filmgenre26 = FilmGenre(film_id=10, genre_id=5)
        db.session.add(filmgenre26)

        filmgenre27 = FilmGenre(film_id=10, genre_id=12)
        db.session.add(filmgenre27)

        filmgenre28 = FilmGenre(film_id=11, genre_id=1)
        db.session.add(filmgenre28)

        filmgenre29 = FilmGenre(film_id=11, genre_id=5)
        db.session.add(filmgenre29)

        filmgenre30 = FilmGenre(film_id=11, genre_id=11)
        db.session.add(filmgenre30)

        filmgenre31 = FilmGenre(film_id=12, genre_id=5)
        db.session.add(filmgenre31)

        filmgenre32 = FilmGenre(film_id=12, genre_id=7)
        db.session.add(filmgenre32)

        filmgenre33 = FilmGenre(film_id=12, genre_id=12)
        db.session.add(filmgenre33)

        filmgenre34 = FilmGenre(film_id=13, genre_id=1)
        db.session.add(filmgenre34)

        filmgenre35 = FilmGenre(film_id=13, genre_id=5)
        db.session.add(filmgenre35)

        filmgenre36 = FilmGenre(film_id=13, genre_id=11)
        db.session.add(filmgenre36)

        filmgenre37 = FilmGenre(film_id=14, genre_id=4)
        db.session.add(filmgenre37)

        filmgenre38 = FilmGenre(film_id=14, genre_id=5)
        db.session.add(filmgenre38)

        filmgenre39 = FilmGenre(film_id=14, genre_id=12)
        db.session.add(filmgenre39)

        filmgenre40 = FilmGenre(film_id=15, genre_id=1)
        db.session.add(filmgenre40)

        filmgenre41 = FilmGenre(film_id=15, genre_id=5)
        db.session.add(filmgenre41)

        filmgenre42 = FilmGenre(film_id=15, genre_id=6)
        db.session.add(filmgenre42)

        filmgenre43 = FilmGenre(film_id=16, genre_id=1)
        db.session.add(filmgenre43)

        filmgenre44 = FilmGenre(film_id=16, genre_id=5)
        db.session.add(filmgenre44)

        filmgenre45 = FilmGenre(film_id=16, genre_id=6)
        db.session.add(filmgenre45)

        filmgenre46 = FilmGenre(film_id=17, genre_id=1)
        db.session.add(filmgenre46)

        filmgenre47 = FilmGenre(film_id=17, genre_id=5)
        db.session.add(filmgenre47)

        filmgenre48 = FilmGenre(film_id=17, genre_id=6)
        db.session.add(filmgenre48)

        filmgenre49 = FilmGenre(film_id=18, genre_id=1)
        db.session.add(filmgenre49)

        filmgenre50 = FilmGenre(film_id=18, genre_id=5)
        db.session.add(filmgenre50)

        filmgenre51 = FilmGenre(film_id=18, genre_id=11)
        db.session.add(filmgenre51)

        filmgenre52 = FilmGenre(film_id=19, genre_id=5)
        db.session.add(filmgenre52)

        filmgenre53 = FilmGenre(film_id=19, genre_id=10)
        db.session.add(filmgenre53)

        filmgenre54 = FilmGenre(film_id=20, genre_id=1)
        db.session.add(filmgenre54)

        filmgenre55 = FilmGenre(film_id=20, genre_id=5)
        db.session.add(filmgenre55)

        filmgenre56 = FilmGenre(film_id=20, genre_id=12)
        db.session.add(filmgenre56)

        rating1 = Rating(user_id=2, film_id=1, rating=5)
        db.session.add(rating1)

        rating2 = Rating(user_id=2, film_id=2, rating=4)
        db.session.add(rating2)

        rating3 = Rating(user_id=2, film_id=3, rating=3)
        db.session.add(rating3)

        rating4 = Rating(user_id=2, film_id=4, rating=3)
        db.session.add(rating4)

        rating5 = Rating(user_id=2, film_id=5, rating=1)
        db.session.add(rating5)

        rating6 = Rating(user_id=3, film_id=2, rating=5)
        db.session.add(rating6)

        rating7 = Rating(user_id=3, film_id=5, rating=4)
        db.session.add(rating7)

        rating8 = Rating(user_id=3, film_id=6, rating=4)
        db.session.add(rating8)

        rating9 = Rating(user_id=3, film_id=10, rating=5)
        db.session.add(rating9)

        rating10 = Rating(user_id=3, film_id=15, rating=3)
        db.session.add(rating10)

        db.session.commit()
        print("Table seeded")