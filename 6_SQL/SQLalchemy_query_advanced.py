from sqlalchemy import create_engine, select, or_, and_, between, within_group, func, text
from sqlalchemy.orm import sessionmaker
from SQLalchemy_base import Movies, Directors, PASSWORD

eng = create_engine(f'mysql+mysqlconnector://root:{PASSWORD}@localhost:3306/cinematic', echo=True)

Session = sessionmaker(bind=eng)
db_session = Session()

print("\nList the names and surnames of all directors whose films were made between 2011 and 2014, "
      "and the rating of their films is less than 9")
# Movies.movie_director_id == Directors.director_id) not needed here, is automatically added via foreign key
rows = db_session.query(Directors.director_name, Directors.director_surname, Movies.movie_name) \
    .join(Movies, Movies.movie_director_id == Directors.director_id) \
    .filter(Movies.movie_rating <= 9, between(Movies.movie_year, 2011, 2014)) \
    .all()
for row in rows:
    print(row)

print("\nList the total number of films created for each director, his full name, "
      "and the average rating for each director based on the ratings of their films.")
# Movies.movie_director_id == Directors.director_id) not needed here, is automatically added via foreign key
rows = db_session.query(func.count(Movies.movie_id).label("#OfMovies"), Directors.director_name,
                        Directors.director_surname,
                        func.round(func.avg(Movies.movie_rating), 2).label("AvgMovieRating")) \
    .join(Movies, Movies.movie_director_id == Directors.director_id, isouter=True) \
    .group_by(Directors.director_id) \
    .all()
for row in rows:
    print(row)

print("\nCheck the generated SQL query from the previous task.")
# Movies.movie_director_id == Directors.director_id) not needed here, is automatically added via foreign key
rows = db_session.query(func.count(Movies.movie_id).label("#OfMovies"), Directors.director_name,
                        Directors.director_surname,
                        func.round(func.avg(Movies.movie_rating), 2).label("AvgMovieRating")) \
    .join(Movies, Movies.movie_director_id == Directors.director_id, isouter=True) \
    .group_by(Directors.director_id)
print(rows)

print("\nFormat the query you received from the previous task using text(). Modify them so that this query can be used "
      "by specifying the range of years the directors created the movies as parameter to the query..")

rows = db_session.query(text('OfMovies'), Directors.director_name, Directors.director_surname, text('AvgMovieRating')) \
    .from_statement(text(
    """SELECT count(directors.director_id) AS `OfMovies`, directors.director_name, directors.director_surname,
    avg(movies.movie_rating) AS `AvgMovieRating` 
    FROM directors 
    INNER JOIN movies 
    ON movies.movie_director_id = directors.director_id 
    WHERE movies.movie_year BETWEEN :start_year AND :end_year 
    GROUP BY directors.director_id""")) \
    .params(start_year=2000, end_year=2020).all()
print(rows)


def get_directors_statistics(session, start: int, end: int):
    rows = session.query(text('OfMovies'), Directors.director_name, Directors.director_surname,
                         text('AvgMovieRating')) \
        .from_statement(text(
        """SELECT count(directors.director_id) AS `OfMovies`, directors.director_name, directors.director_surname,
        avg(movies.movie_rating) AS `AvgMovieRating` 
        FROM directors 
        INNER JOIN movies 
        ON movies.movie_director_id = directors.director_id 
        WHERE movies.movie_year BETWEEN :start_year AND :end_year 
        GROUP BY directors.director_id""")) \
        .params(start_year=start, end_year=end).all()
    return rows


def task_6():
    # print(get_directors_statistics(db_s, 2000, 2020))
    director_rows = db_session.query(Directors).all()
    for row in director_rows:
        print(row)

    subquery = db_session.query(Movies.movie_director_id).filter(and_(Movies.movie_year < 2001)).subquery()

    db_session.query(Directors).filter(Directors.director_id.in_(select(subquery))).update(
        {'director_rating': (Directors.director_rating + 1)}, synchronize_session='fetch')
    db_session.commit()

    director_rows = db_session.query(Directors).all()
    for row in director_rows:
        print(row)


def task_7():
    # print(get_directors_statistics(db_s, 2000, 2020))
    director_rows = db_session.query(Directors).all()
    for row in director_rows:
        print(row)

    subquery = db_session.query(Movies.movie_director_id).filter(and_(Movies.movie_year < 2001)).subquery()

    db_session.query(Directors).filter(Directors.director_id.in_(select(subquery))).update(
        {'director_rating': (Directors.director_rating + 1)}, synchronize_session='fetch')
    db_session.commit()

    director_rows = db_session.query(Directors).all()
    for row in director_rows:
        print(row)

task_7()
# "HAVING
#
# rows = db_s.query(Directors).from_statement(text(
#     "SELECT count(directors.director_id) AS `#OfMovies`, directors.director_name, directors.director_surname, "
#     "avg(movies.movie_rating) AS `AvgMovieRating` "
#     "FROM directors "
#     "INNER JOIN movies "
#     "ON movies.movie_director_id = directors.director_id "
#     "WHERE movies.movie_year BETWEEN :start_year AND :end_year"
#     "GROUP BY directors.director_id "
# )).params(start_year=2000, end_year=2020).all()
