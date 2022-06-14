from sqlalchemy import create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from SQLalchemy_base import Movies, Directors, PASSWORD

eng = create_engine(f'mysql+mysqlconnector://root:{PASSWORD}@localhost:3306/cinematic')

Session = sessionmaker(bind=eng)
db_session = Session()

directors = [
    Directors(director_name="Frank", director_surname="Darabont", director_rating=7),
    Directors(director_name="Francis", director_surname="Ford Coppola", director_rating=8),
    Directors(director_name="Quentin", director_surname="Tarantino", director_rating=10),
    Directors(director_name="Christopher", director_surname="Nolan", director_rating=9),
    Directors(director_name="David", director_surname="Fincher", director_rating=7),
    Directors(director_name="Martin", director_surname="Scorsese", director_rating=8),
    Directors(director_name="James", director_surname="Cameron", director_rating=7),
    Directors(director_name="Steven", director_surname="Spielberg", director_rating=8),
    Directors(director_name="Ridley", director_surname="Scott", director_rating=7),
    Directors(director_name="Alfred", director_surname="Hitchcock", director_rating=8),
]

movies = [
    Movies(movie_name="The Shawshank Redemption", movie_year=1994, movie_category="Drama", movie_director_id=1,
           movie_rating=9.3),
    Movies(movie_name="The Green Mile", movie_year=1999, movie_category="Drama", movie_director_id=1, movie_rating=8.6),
    Movies(movie_name="The Godfather", movie_year=1972, movie_category="Drama", movie_director_id=2, movie_rating=9.2),
    Movies(movie_name="The Godfather: Part II", movie_year=1974, movie_category="Drama", movie_director_id=2,
           movie_rating=9.0),
    Movies(movie_name="The Dark Knight", movie_year=2008, movie_category="Action", movie_director_id=4,
           movie_rating=9.0),
    Movies(movie_name="Pulp Fiction", movie_year=1994, movie_category="Crime", movie_director_id=3, movie_rating=8.9),
    Movies(movie_name="Schindler's List", movie_year=1993, movie_category="Biography", movie_director_id=2,
           movie_rating=8.9),
    Movies(movie_name="Inglourious Basterds", movie_year=2009, movie_category="War", movie_director_id=3,
           movie_rating=8.9),
    Movies(movie_name="Interstellar", movie_year=2014, movie_category="Sci-Fi", movie_director_id=3, movie_rating=8.7),
    Movies(movie_name="The Good, the Bad and the Ugly", movie_year=1966, movie_category="Western", movie_director_id=4,
           movie_rating=8.9),
    Movies(movie_name="Fight Club", movie_year=1999, movie_category="Drama", movie_director_id=5, movie_rating=8.8),
    Movies(movie_name="The Lord of the Rings: The Return of the King", movie_year=2003, movie_category="Fantasy",
           movie_director_id=3, movie_rating=8.9),
    Movies(movie_name="The Prestige", movie_year=2006, movie_category="Drama", movie_director_id=3, movie_rating=8.5),
    Movies(movie_name="Zodiac", movie_year=2007, movie_category="Crime", movie_director_id=5, movie_rating=8.5),
    Movies(movie_name="Seven", movie_year=1995, movie_category="Thriller", movie_director_id=5, movie_rating=8.6),
    Movies(movie_name="The Matrix", movie_year=1999, movie_category="Sci-Fi", movie_director_id=3, movie_rating=8.7),
    Movies(movie_name="The Lord of the Rings: The Fellowship of the Ring", movie_year=2001, movie_category="Fantasy",
           movie_director_id=3, movie_rating=8.8),
    Movies(movie_name="The Dark Knight Rises", movie_year=2012, movie_category="Action", movie_director_id=4,
           movie_rating=8.5),
    Movies(movie_name="Inception", movie_year=2010, movie_category="Sci-Fi", movie_director_id=3, movie_rating=8.8),
    Movies(movie_name="The Lord of the Rings: The Two Towers", movie_year=2002, movie_category="Fantasy",
           movie_director_id=3, movie_rating=8.7),
    Movies(movie_name="Forrest Gump", movie_year=1994, movie_category="Drama", movie_director_id=5, movie_rating=8.8),
]

for director in directors:
    try:
        db_session.add(director)
        db_session.commit()
    except IntegrityError:
        print("Director already exists")
        db_session.rollback()
    else:
        print(f"Director {director.director_name} {director.director_surname} added")

for movie in movies:
    try:
        db_session.add(movie)
        db_session.commit()
    except IntegrityError:
        print("Movie already exists")
        db_session.rollback()
    else:
        print(f"Movie {movie.movie_name}({movie.movie_year}) added")
