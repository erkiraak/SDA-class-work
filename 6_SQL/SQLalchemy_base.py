from os import environ
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

PASSWORD = environ.get("SQL_PASS")

# CONNECTION EXAMPLE
# db = create_engine(f'mysql+mysqlconnector://root:{PASSWORD}@localhost:3306/cinematic')


# CREATE TABLE EXAMPLE

eng = create_engine(f'mysql+mysqlconnector://root:{PASSWORD}@localhost:3306/cinematic')
base = declarative_base()


class Directors(base):
    __tablename__ = 'directors'

    director_id = Column(Integer, primary_key=True, autoincrement=True)
    director_name = Column(String(50), nullable=False)
    director_surname = Column(String(50), nullable=False)
    director_rating = Column(Integer, nullable=False)
    movies = relationship("Movies", back_populates="directors")
    UniqueConstraint(director_name, director_surname)

    def __str__(self):
        return f"{self.director_name} {self.director_surname} ({self.director_rating})"


class Movies(base):
    __tablename__ = 'movies'
    movie_id = Column(Integer, primary_key=True, autoincrement=True)
    movie_name = Column(String(50), nullable=False)
    movie_year = Column(Integer, nullable=False)
    movie_category = Column(String(50), nullable=False)
    movie_director_id = Column(Integer, ForeignKey('directors.director_id'))
    movie_rating = Column(Integer, nullable=False)
    directors = relationship("Directors", back_populates="movies")
    UniqueConstraint(movie_name, movie_year, movie_director_id)

    def __str__(self):
        return f"{self.movie_name} ({self.movie_year}), {self.movie_category}, " \
               f"{self.movie_director_id}, {self.movie_rating}"


base.metadata.create_all(eng)
