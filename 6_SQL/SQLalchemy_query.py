from sqlalchemy import create_engine, select, or_, between
from sqlalchemy.orm import sessionmaker
from SQLalchemy_base import Movies, Directors, PASSWORD


eng = create_engine(f'mysql+mysqlconnector://root:{PASSWORD}@localhost:3306/cinematic', echo=True)

Session = sessionmaker(bind=eng)
db_session = Session()

# ORM API
print('\nORM API')
print("\nAll directors:")
director_rows = db_session.query(Directors).all()
for row in director_rows:
    print(row)

print("\nDirector with ID 3 using primary key command get():")
director = db_session.query(Directors).get(3)
print(director)

print("\nDirectors with rating >= 8:")
director_rows = db_session.query(Directors).filter(Directors.director_rating >= 8).all()
for row in director_rows:
    print(row)

print("\nAll movies:")
movie_rows = db_session.query(Movies).all()
for row in movie_rows:
    print(row)

print("\nMovies year after 2000 and name contains 'in':")
movie_rows = db_session.query(Movies).filter(Movies.movie_year > 1950, Movies.movie_name.like("%in%")).all()
for row in movie_rows:
    print(row)

print("\nMovies with rating >= 6 and in 'Sci-Fi' genre:")
movie_rows = db_session.query(Movies).filter(Movies.movie_rating > 6, Movies.movie_category.like("%Sci-Fi%")).all()
for row in movie_rows:
    print(row)

print("\nMovies directed by directors_id 2 OR 4:")
director_rows = db_session.query(Movies).filter(or_(Movies.movie_director_id == 2, Movies.movie_director_id == 4)).all()
for row in director_rows:
    print(row)


print("\nNumber of movies:")
movie_count = db_session.query(Movies).count()
print(movie_count)


print("\nmovies from the Drama category that were produced after 1994:")
movie_rows = db_session.query(Movies).filter(Movies.movie_year > 1994, Movies.movie_category.like("Drama")).all()
for row in movie_rows:
    print(row)


print("\nList the categories of all films and their ranking for films that were produced in the years 2000-2010 "
      "and whose ranking is greater than 7, sorting by ranking. Use query ().:")
movie_rows = db_session.query(Movies.movie_category, Movies.movie_rating).\
    filter(between(Movies.movie_year, 2000, 2010), Movies.movie_rating >= 7).\
    order_by(Movies.movie_rating.desc()).all()
for row in movie_rows:
    print(row)


print("\nnames of all directors whose ranking is greater than or equal to 6 "
      "and whose first name starts with the letter 'D' or ends with the letter 'n'")
director_rows = db_session.query(Directors.director_name, Directors.director_surname).\
    filter(Directors.director_rating >= 6, or_(Directors.director_name.like('D%'), Directors.director_name.like('%n')))\
    .all()
for row in director_rows:
    print(row)


# CORE API
print('\nCORE API')
select_obj = select([Movies]).where(Movies.movie_year > 1990)
result = eng.execute(select_obj)
for row in result.fetchall():
    print(row)


print('\nmovies from the Drama category that were produced after 1994')
select_obj = select([Movies]).where(Movies.movie_year > 1994, Movies.movie_category == "Drama")
result = eng.execute(select_obj)
for row in result.fetchall():
    print(row)
