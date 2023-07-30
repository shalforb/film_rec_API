# **Film Rating API Web Server Documentation**


## **Installation and Setup**

- Create a folder locally to store the API. 
- Clone or download the repository from Github.

Connect to a PostgreSQL database from the Flask application. Run the PostgreSQL prompt in the terminal:
```postgresql
psql
```

Create the database:
```postgresql
CREATE DATABASE film_rec_db;
```

Connect to the database:
```postgresql
\c film_rec_db;
```

Create a user and set a password:
```postgresql
CREATE USER db_dev WITH PASSWORD '123456';
```

Grant user privileges:
```postgresql
GRANT ALL PRIVILEGES ON DATABASE film_rec_db TO db_dev;
```
<div style="page-break-after: always;"></div>

Open another terminal and run the following commands:

cd into the src folder inside the project folder and create/ activate the virtual environment:
```
virtualenv venv
```
```
source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Create a .env file at the root of the project with the following contents:
```
DATABASE_URL="postgresql+psycopg2://db_dev:123456@localhost:5432/film_rec_db"
SECRET_KEY="secret"
```

Create and seed the database then run the Flask application with the following cli commands:
```
flask db create
flask db seed
flask run
```


Search 127.0.0.1:8080/ in the browser or Postman/ Insomnia. Refer to *API Endpoints* documentation to make requests.

<div style="page-break-after: always;"></div>

## **R1 / R2: Problem Identification and Justification**

### The App

Currently in the development phase, this user-focused & innovative application aims to change the way film enthusiasts discover and enjoy movies. With a goal to make the process of finding new films engaging and personalised, the application's mission is to transform the often tedious task of movie discovery into a seamless, enjoyable experience.

As it stands, the application currently functions as an API web server, facilitating user interaction with a vast film database. The users can explore, rate, and review films, as well as maintain their personal user profiles. The server-side logic allows for user authentication, rating films, and browsing through the expansive film library, which sets the stage for future plans.

The core aspect of the application, a personalised film recommendation feature, is currently under development. This feature will incorporate user's film ratings, viewing history, and their unique interests to offer a curated selection of movies catered to their personal taste. This has the potential to significantly reduce the time users spend searching for new films to watch, enhancing user experience, and fostering a deeper engagement with the platform.

### The Problem
The problem this application aims to solve is the lack of personalised film recommendations for users. Many film databases exist, but very few of them offer recommendations that are tailored to a user's viewing history and interests. This lack of personalization can make finding new films to watch a daunting task given the vast number of options available. This is where the application will truly shine - by providing a personalised movie discovery experience that is as enjoyable as watching the films themselves.

The problem this app is designed to solve is providing personalised film recommendations to users. While there are many film databases available, not all of them offer personalised recommendations based on a user's viewing history and interests. Finding new films to watch can be overwhelming given the vast number of options available. Providing personalised recommendations makes the process easier and more enjoyable for users, and can lead to them discovering films they might not have found on their own.

This problem significantly affects users who are avid film enthusiasts and constantly looking for new films to watch. Without personalised recommendations, they often end up wasting a significant amount of time scrolling through countless films, sometimes ending up with choices that don't align with their preferences. This process can be frustrating and may lead to a lack of interest in exploring new films over time.

### The Power of Personalization
The importance of personalization can't be understated in today's world. Users are more likely to engage with platforms that provide personalised experiences. This is because these platforms not only offer convenience but also cater to individual tastes and preferences, which is crucial in an age where the consumption of media content is at an all-time high.

Existing film databases, while comprehensive, often fall short when it comes to providing a truly personalised experience. Some of them do offer a basic level of personalization but it's not up to par with the rapidly evolving tastes and preferences of users. Users end up having to resort to multiple platforms to get relevant film recommendations, creating a disjointed and inconvenient experience.

Hence, there is a clear need for a more sophisticated and user-focused film recommendation platform. By offering personalised film recommendations, this app aims to fill this gap, streamlining users' search for new films and enhancing their overall film discovery experience. This, in turn, will increase user engagement and satisfaction, while also promoting a diverse range of films that might otherwise get overlooked.

## **R3: Database System Selection and Justification**

For the core data storage and management of the application, the relational database system, PostgreSQL has been selected. The choice is guided by several factors and an evaluation of the benefits and drawbacks it offers, tailored to the application's requirements.

### Structured Data Management
 
 Given the nature of the application, dealing primarily with structured data (like users, films, genres, and ratings), PostgreSQL's capability for handling such data types is a perfect fit. It offers efficient storage and querying capabilities, which is essential for providing quick responses to user requests.

### ACID Transactions

One of the primary reasons for choosing PostgreSQL is its support for ACID (Atomicity, Consistency, Isolation, Durability) transactions. This is critical for maintaining data integrity and ensuring that all operations, such as user registration, rating a film, or updating profile information, are processed reliably.

### Advanced Features 

PostgreSQL also supports advanced functionalities such as stored procedures, triggers, and views, which could be beneficial for complex query operations and ensuring data consistency.

## Drawbacks

### Scalability

One of the potential challenges with PostgreSQL, like many other relational databases, is scalability. While it can handle large amounts of data, it might not scale horizontally as effortlessly as NoSQL databases, which could potentially limit its performance as the data grows.

### Flexibility with Unstructured Data

 Although the application mainly deals with structured data, the flexibility to handle unstructured data offered by NoSQL databases, like MongoDB, could be a limitation for PostgreSQL. If it is decided to incorporate unstructured data in the future (e.g., user comments or reviews), this might pose some challenges.

However, the drawbacks should not significantly impact the application at its current state and the foreseeable future. The benefits of PostgreSQL, particularly in terms of structured data management and ACID transactions, offer a compelling case for its selection. This choice will aid in delivering a robust, efficient, and reliable film recommendation service to its users.

## **R4: Functionalities and Benefits of an ORM**

### CRUD Operations 

ORMs provide an abstraction for performing CRUD (Create, Read, Update, Delete) operations. This means that instead of writing SQL queries, developers can use methods like save(), delete(), and update() directly on the objects. This abstracted layer makes it easier to work with databases, as developers can focus on manipulating objects in their chosen programming language rather than writing and debugging SQL queries.

### Managing Relationships

ORMs also make it easier to handle relationships between different entities or tables. Relationships such as One-to-One, One-to-Many, and Many-to-Many can be easily managed using object-oriented constructs. For example, retrieving related data across multiple tables can be done without the need for complex JOIN SQL statements, which significantly simplifies the development process.

### Transactions

ORMs typically provide a way to group database operations into a single transaction, ensuring that all operations either succeed or fail as a unit. This capability is important for maintaining data integrity and consistency.

### Migrations

Migrations are a way to manage changes in the database schema over time. ORMs can generate and manage migrations, making it easier to evolve the database schema while preserving existing data.

## Key Benefits

### Increased Productivity

 Since ORMs allow developers to use their preferred programming language's syntax to interact with databases, they can reduce the time spent on learning SQL syntax and writing SQL queries. This boosts productivity, as developers can focus more on business logic and less on data access mechanics.

### Code Maintainability

 The code written with ORM is more maintainable and readable. Since the code is in the same language as the rest of the application, it is easier for developers to understand and modify it.

### Security

ORMs typically provide protection against SQL injection attacks, one of the most common security threats to databases. By using parameterized queries and escaping inputs, ORMs help to make applications more secure.

### Database Agnostic

Most ORMs are database-agnostic, meaning they can interact with different types of databases. This can be very advantageous if there's a need to switch the underlying database in the future.

### Abstraction of Database Schema

ORMs provide a mapping between the object model and the database schema. This abstraction allows developers to work with a more intuitive data model, and reduces coupling between the application and the database, allowing each to evolve more independently.

These features and benefits collectively justify the value of ORMs in modern web development, offering an intuitive and secure way to interact with the database, while enhancing developer productivity and code maintainability.

## **R5: API Endpoints**

## Auth Routes

## **`/auth/login`**

- Method: POST
- Description: Registers a new user. The body must contain an email, a username, and a password, along with the password confirmation.
- Authentication: Anyone can access this route.
- Authorization: Not required.

## **`/auth/register`**

- Method: POST
- Description: Logs in an existing user. The body must contain the user's email and password. Returns a token for authenticated routes and checks for failed login attempts.
- Authentication: No, anyone can access this route.
- Authorization: Not required.

## User Routes

## **`GET /users/`**

- Method: GET
- Description: Fetches all users.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can access this route.

## **`GET /users/<id>`**

- Method: GET
- Description: Fetches a specific user by ID.
- Authentication: Anyone can access this route.
- Authorization: The route does not restrict access based on user roles.

## **`POST /users/`**

- Method: POST
- Description: Creates a new user.
- Authentication: Anyone can create a new user.
- Authorization: The route does not restrict access based on user roles.


## **`PUT /users/<id>`**

- Method: PUT
- Description: Updates a specific user by ID.
- Authentication: Requires a JWT token.
- Authorization: Users can only update their own details.

## **`DELETE /users/<id>`**

- Method: DELETE
- Description: Deletes a specific user by ID.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can delete a user or users can delete their own account.

## **`GET /users/me`**

- Method: GET
- Description: Fetches the details of the currently logged-in user.
- Authentication: Requires a JWT token.
- Authorization: The route does not restrict access based on user roles, but users can only see their own details.

## Film Routes

## **`GET /films`**

- Method: GET
- Description: Fetches all films.
- Authentication: Anyone can access this route.
- Authorization: The route does not restrict access based on user roles.

## **`GET /films/<id>`**

- Method: GET
- Description: Fetches a specific film by ID.
- Authentication: Anyone can access this route.
- Authorization: The route does not restrict access based on user roles.

## **`GET /films/search/<title>`**

- Method: GET
- Description: Searches for films by title.
- Authentication: Anyone can access this route.
- Authorization: The route does not restrict access based on user roles.

## **`GET /films/year/<year>`**

- Method: GET
- Description: Fetches all films released in a specific year.
- Authentication: Anyone can access this route.
- Authorization: The route does not restrict access based on user roles.

## **`GET /films/director/<director>`**

- Method: GET
- Description: Fetches all films directed by a specific director.
- Authentication: Anyone can access this route.
- Authorization: The route does not restrict access based on user roles.

## **`GET /films/genre/<genre_id>`**

- Method: GET
- Description: Fetches all films belonging to a specific genre.
- Authentication: Anyone can access this route.
- Authorization: The route does not restrict access based on user roles.

## **`POST /films/`**

- Method: POST
- Description: Creates a new film.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can create a new film.

## **`PUT /films/<id>`**

- Method: PUT
- Description: Updates a specific film by ID.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can update film details.

## **`DELETE /films/protected/<id>`**

- Method: DELETE
- Description: Deletes a specific film by ID.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can delete a film.

## Genre Routes

## **`GET /genres`**

- Method: GET
- Description: Fetches all genres.
- Authentication: Anyone can access this route.
- Authorization: Not required.

## **`GET /genres/<id>`**

- Method: GET
- Description: Fetches a specific genre by ID.
- Authentication: Anyone can access this route.
- Authorization: Not required.

## **`POST /genres`**

- Method: POST
- Description: Allows an admin user to create a new genre.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can create a genre.

## **`PUT /genres/<id>`**

- Method: PUT
- Description: Allows an admin user to update a specific genre by ID.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can update a genre.

## **`DELETE /genres/<id>`**

- Method: DELETE
- Description: Allows an admin user to delete a specific genre by ID.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can delete a genre.

## Ratings Routes

## **`POST /ratings/`**

- Method: POST
- Description: Allows a logged-in user to create a rating.
- Authentication: Requires a JWT token.
- Authorization: Not required, any authenticated user can create a rating.

## **`PUT /ratings/<id>`**

- Method: PUT
- Description: Allows a logged-in user to update a specific rating by ID.
- Authentication: Requires a JWT token.
- Authorization: Users can only update ratings they've created.

## **`DELETE /ratings/<id>`**

- Method: DELETE
- Description: Allows a logged-in user to delete a specific rating by ID.
- Authentication: Requires a JWT token.
- Authorization: Users can only delete ratings they've created.

## **`GET /ratings/user/<user_id>`**

- Method: GET
- Description: Fetches all ratings made by a specific user.
- Authentication: Requires a JWT token.
- Authorization: Users can only fetch ratings they've created.

## **`GET /ratings/film/<film_id>`**

- Method: GET
- Description: Fetches all ratings for a specific film.
- Authentication: Anyone can access this route.
- Authorization: Not required.

## **`GET /ratings/film/<film_id>/average`**

- Method: GET
- Description: Fetches the average rating for a specific film.
- Authentication: Anyone can access this route.
- Authorization: Not required.

## **`DELETE /ratings/user/<user_id>`**

- Method: DELETE
- Description: Deletes all ratings made by a specific user.
- Authentication: Requires a JWT token.
- Authorization: Users can only delete ratings they've created.

## FilmGenre Routes

## **`GET /filmgenres/<film_id>`**

- Method: GET
- Description: Fetches all genres associated with a specific film.
- Authentication: Anyone can access this route.
- Authorization: Not required.

## **`POST /filmgenres/<film_id>/<genre_id>`**

- Method: POST
- Description: Allows an admin to associate a specific genre with a film.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can add genres to a film.

## **`DELETE /filmgenres/<film_id>/<genre_id>`**

- Method: DELETE
- Description: Allows an admin to remove the association between a specific genre and a film.
- Authentication: Requires a JWT token.
- Authorization: Only admin users can remove genres from a film.

## **R6 / R9: Explanation of ERD and Database Relations Implementation**

<br>

<img src = "./docs/Film_Rec_ERD.png">

<br>

Let's revisit the data architecture of the film recommendation application, focusing specifically on its Entity Relationship Diagram (ERD) and how it is pertinent to the project.

The ERD is a visual representation of various entities within the application's database—specifically, the User, Film, Genre, Ratings, and FilmGenre models—and the relationships between them. In the context of the film recommendation application, this diagram is an essential tool for understanding how the different aspects of the application interrelate.

Two types of relationships are prominently featured in the ERD: **one-to-many** and **many-to-many**.

Consider the one-to-many relationship between the User and Ratings models, a crucial aspect of the application. It ensures that an individual user can create multiple ratings, enhancing user interactivity within the application. However, each rating is uniquely associated with one user, maintaining the authenticity of the feedback provided. The foreign key, user_id, in the Ratings table facilitates this relationship. Similarly, there is a one-to-many relationship between the Film and Ratings models, a necessary function in a film review context. Each film can receive numerous ratings from users, but a single rating can only pertain to one film. The film_id in the Ratings table secures this association.

The many-to-many relationship between the Film and Genre models is another vital feature of the application, permitting a single film to be categorised under multiple genres. This flexible association enriches the film categorization system within the application, enhancing user search and discovery. On the flip side, a single genre can encapsulate numerous films, ensuring a broad collection within each genre. The junction table, FilmGenre, resolves this many-to-many relationship by storing the film_id and genre_id, thereby recording each instance of a film's association with a genre.

In addition to serving as an illustrative guide, the ERD contributes to discerning data redundancies and optimising the database structure. It assists in establishing the integrity constraints, such as primary and foreign keys, crucial for enhancing data consistency and preventing anomalies.

From the standpoint of database implementation, the ERD's illustrative design is crucial for understanding how these relationships are crucial for the film recommendation application. These associations facilitate efficient data operations, such as retrieval, modification, and deletion, while ensuring data integrity.

In essence, the ERD acts as a foundational blueprint for the film recommendation application. It presents a comprehensive view of the data organisation, guiding the establishment of relationships between various entities, thereby contributing to the smooth functioning of the application.

## **R7: Third Party Services**

In modern software development, particularly in building web applications, leveraging third-party services or libraries is a crucial aspect that can dramatically speed up the development process and enhance the overall application performance and security. These services provide pre-implemented, tested, and optimised functionalities that developers can utilise, rather than reinventing the wheel. In the context of this Flask-based application, several such services play key roles in shaping the functionality and security profile of the application. From Flask, which provides the foundational web framework, to libraries such as SQLAlchemy for database interaction, Flask-Marshmallow for data serialisation and validation, and Flask-Bcrypt for password security, each service contributes to a specific aspect of the application. 

## Flask

Flask is an integral part of the application. It is a lightweight WSGI web application framework that is designed to make getting started quick and easy, with the ability to scale up to complex applications. It is classified as a microframework due to its minimalist nature, yet it does not compromise on flexibility. It provides the basic framework – request dispatching, URI routing, response delivery, and error handling – for building the web application. In this context, Flask is used as the foundation upon which all other functionalities are built.

## SQLAlchemy: 

At the heart of data persistence in the application lies SQLAlchemy. It is a SQL toolkit and Object-Relational Mapping (ORM) system for Python, which gives application developers the full power and flexibility of SQL. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access. Its major role in this application is to abstract the database interactions, allowing the developer to interact with Python objects instead of writing SQL queries.

## Flask-SQLAlchemy 

Building on SQLAlchemy, Flask-SQLAlchemy is a Flask extension that simplifies the management of SQLAlchemy inside a Flask application. It helps handle connections to different database servers and provides a centralised way to create models that define the structure of the data that is to be stored in the database. It is also responsible for session management, an essential aspect of interacting with SQLAlchemy.

## Flask-Marshmallow 

Flask-Marshmallow plays an essential role in data serialisation and deserialisation. It provides a simple way to control how objects are converted to or from complex data types, like JSON, which is an important part of handling HTTP requests and responses in the application. Marshmallow also provides validation for input data. This ensures that data being sent to the application adheres to predefined rules, thereby maintaining the integrity of the application.

## Flask-Bcrypt

Security is a primary concern in web applications, especially when handling sensitive data like user passwords. Flask-Bcrypt is an extension that handles password hashing. It offers a safe way to store user passwords in the database. When a user creates an account or changes their password, Flask-Bcrypt is used to encrypt the password before it is stored in the database. It is also used to verify user passwords when logging in.

## Flask-JWT-Extended

Authentication and authorization are other critical aspects of web application security. Flask-JWT-Extended provides support for JSON Web Tokens (JWT) in Flask. JWTs are a secure and efficient method of transferring data between two parties. In this application, JWTs are used to authenticate users and ensure that they are authorised to access certain routes in the application.

## psycopg2

Exception handling is an important part of building robust applications. psycopg2 is the PostgreSQL adapter for Python, and it is used in this application for handling exceptions that can occur when interacting with the database. Specific error codes are used to inform the user about what went wrong in a clear and helpful way.

## Python Decorators

The Python built-in functools module is used in the application to create decorator functions. Decorators allow for augmenting and modifying the behaviour of a function or class without permanently changing it. In this application, decorators are used to enforce access control rules. The admin_required decorator ensures that a route can only be accessed by an administrator, and the user_required decorator ensures that a user can only access data associated with their account.

## Python datetime module

In any application that uses authentication, managing session lifetimes is crucial. The Python datetime module is used to define the amount of time a user remains logged in through the use of JWT expiration times.

## Marshmallow

Marshmallow is used for object serialisation/deserialisation. It offers a simple way to control how objects are converted to or from complex data types. It's a crucial part of the application as it validates user input before it is processed or saved in the database.

The third-party services used in the application work together to provide a robust, secure, and efficient framework for building a web application. Flask forms the foundation, while SQLAlchemy and Flask-SQLAlchemy manage the database interactions. Flask-Marshmallow and Marshmallow handle serialisation, deserialisation, and validation of data, while Flask-Bcrypt and Flask-JWT-Extended take care of the security aspects. psycopg2 aids in error handling, and Python's datetime and functools modules handle session management and access control, respectively. Together, these services are integral to the functionality of the application.

## **R8: Project Models and their Relationships with each other**


In the film recommendation application, five models - Film, FilmGenre, Rating, User, and Genre - form the foundational architecture. Each model's structure, attributes, and relationships are purposefully designed for efficient data management and functionality of the application.

```

class Film(db.Model):
    __tablename__ = 'films'

    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    director = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    # Relationship
    ratings = db.relationship('Rating', backref='film', lazy=True)
    film_genres = db.relationship('FilmGenre', backref='film', lazy=True)

```


The Film model, serving as a cornerstone of the application, represents the films to be reviewed and rated by users. It comprises four attributes: film_id, title, director, and year. The film_id serves as the primary key, a unique identifier for each film. The title attribute stores the film's name, while the director attribute keeps the director's name. The year attribute stores the release year of the film. All attributes, except the title, are non-nullable, meaning they must always hold a value. The model also includes 'ratings' and 'film_genres' relationships, referring to the Rating and FilmGenre models respectively, thus creating one-to-many relationships.

```
class FilmGenre(db.Model):
    __tablename__ = 'film_genres'

    filmgenre_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('films.film_id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
```

The FilmGenre model, functioning as a junction table, resolves the many-to-many relationship between films and genres. It consists of three attributes: filmgenre_id, film_id, and genre_id. The filmgenre_id is the primary key, while film_id and genre_id serve as foreign keys linking to the Film and Genre models, respectively. These attributes must always hold a value, ensuring every entry in the FilmGenre table corresponds to a valid film and genre.

```
class Rating(db.Model):
    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('films.film_id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
```

The Rating model represents user feedback on films and includes four attributes: rating_id, user_id, film_id, and rating. The rating_id serves as the primary key. The user_id and film_id are foreign keys referencing the User and Film models, respectively, ensuring each rating associates with a specific user and film. The 'rating' attribute stores the rating value given by a user to a film. These attributes are non-nullable, ensuring that they always hold a value.

```
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password= db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationship
    ratings = db.relationship('Rating', backref='user', lazy=True)
```

The User model represents the registered users of the application. It includes five attributes: user_id, username, password, email, and is_admin. The user_id serves as the primary key. The username and email attributes, both unique, store the user's chosen username and email address. The password attribute stores the user's password, while the is_admin attribute indicates administrative privileges. The User model has a 'ratings' relationship with the Rating model, establishing a one-to-many relationship that a user can have multiple ratings.

```
class Genre(db.Model):
    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(64), unique=True, nullable=False)

    # Relationship
    film_genres = db.relationship('FilmGenre', backref='genre', lazy=True)
```

The Genre model, the final addition, represents the different genres that a film can be classified under. It includes two attributes: genre_id and genre_name. The genre_id serves as the primary key, and the genre_name attribute, which is unique, stores the genre's name. The Genre model also has a 'film_genres' relationship with the FilmGenre model, resulting in a one-to-many relationship.

Collectively, these models provide a clear, efficient, and consistent structure for the application's database, enhancing its usability and the overall user experience. They store critical information and establish relationships to ensure proper data organisation and manipulation, serving as the backbone of the film recommendation application.

## References

- Ronacher, A. (2010). Welcome | Flask (A Python Microframework). Pocoo. Available at: https://flask.palletsprojects.com/ 

- PostgreSQL Global Development Group. (2021). PostgreSQL: The world's most advanced open source database. Postgresql.org. Available at: https://www.postgresql.org/ 

- Momjian, B. (2001). ACID Compliance. In PostgreSQL: Introduction and Concepts. Addison-Wesley Longman Publishing Co. Available at: https://momjian.us/main/writings/pgsql/acid.pdf 

- Bayer, M. (2012). SQLAlchemy - The Database Toolkit for Python. SQLAlchemy. Available at: https://www.sqlalchemy.org/ 

- Flask-Bcrypt. (2012). Flask-Bcrypt — Flask-Bcrypt Documentation (0.7.1). Flask-bcrypt.readthedocs.io. Available at: https://flask-bcrypt.readthedocs.io/ 

- Flask-JWT-Extended. (2017). Flask-JWT-Extended — Flask-JWT-Extended documentation. Flask-jwt-extended.readthedocs.io. Available at: https://flask-jwt-extended.readthedocs.io/ 

- Marshmallow. (2014). Marshmallow: simplified object serialization¶. Marshmallow.readthedocs.io. Available at: https://marshmallow.readthedocs.io/ 

- Grinberg, M. (2018). The Flask Mega-Tutorial Part IV: Database - miguelgrinberg.com. Miguelgrinberg.com. Available at: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database 

- Bader, D. (2019). Python’s Requests Library (Guide) – Real Python. Realpython.com. Available at: https://realpython.com/python-requests/ 

- W3Schools. (2023). Python RegEx. W3Schools. Available at: https://www.w3schools.com/python/python_regex.asp 

- Ambler, S. (2002). Mapping Objects to Relational Databases: O/R Mapping In Detail. AgileData. Available at: http://www.agiledata.org/essays/mappingObjects.html#CrudMatrix 