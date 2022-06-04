from sqlalchemy import create_engine, select, or_
from sqlalchemy.orm import sessionmaker
from SQLalchemy_base import Movies, Directors, PASSWORD


eng = create_engine(f'mysql+mysqlconnector://root:{PASSWORD}@localhost:3306/cinematic')

Session = sessionmaker(bind=eng)
db_session = Session()

# ORM API
print('\nORM API')
print("\nAll directors:")
director_rows = db_session.query(Directors).all()
for row in director_rows:
    print(row)

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
movie_rows = db_session.query(Movies).filter(or_(Movies.movie_director_id == 2, Movies.movie_director_id == 4)).all()
for row in movie_rows:
    print(row)


print("\nNumber of movies:")
movie_count = db_session.query(Movies).count()
print(movie_count)


# CORE API
print('\nCORE API')
select = select([Movies]).where(Movies.movie_year > 1990)
result = eng.execute(select)
for row in result.fetchall():
    print(row)
