from sqlalchemy import create_engine, select, or_, and_, between, within_group, func, text, bindparam, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from SQLalchemy_base import Movies, Directors, PASSWORD

eng = create_engine(f'mysql+mysqlconnector://root:{PASSWORD}@localhost:3306/cinematic', echo=True)

Session = sessionmaker(bind=eng, autocommit=True)
db_s = Session()


def task_8():
    with db_s.begin():
        print("\nList the names and surnames of all directors whose films were made between 2011 and 2014, "
              "and the rating of their films is less than 9")
        subquery = db_s.query(Directors.director_id).filter(
            and_(Directors.director_name.like("Quentin"))).subquery()

        db_s.query(Movies).filter(Movies.movie_director_id.in_(select(subquery))).delete(
            synchronize_session='fetch')
        db_s.query(Directors).filter(Directors.director_id.in_(select(subquery))).delete(
            synchronize_session='fetch')


def task_9(name: str=None, surname: str=None):

    if name and surname is None:
        q_text = (text("SELECT directors.director_id AS ID FROM directors WHERE directors.director_name = :name"))
        q_text.bindparams(
            bindparam('name', type_=String))
    elif name is None and surname:
        q_text = (text("SELECT directors.director_id AS ID FROM directors WHERE directors.director_surname = :surname"))
        q_text.bindparams(
            bindparam('surname', type_=String))
    elif name and surname:
        q_text = (text("SELECT directors.director_id AS ID FROM directors WHERE directors.director_name = :name "
                       "AND directors.director_surname = :surname"))
        q_text.bindparams(
            bindparam('name', type_=String),
            bindparam('surname', type_=String))

    else:
        raise ValueError("Name OR surname must be specified")

    directors_to_delete = db_s.query(text("ID")).from_statement(q_text).params(name=name, surname=surname).all()

    for director in directors_to_delete:
        with db_s.begin():

            print(director)
            db_s.query(Movies).filter(Movies.movie_director_id.in_(director)).delete()
            db_s.query(Directors).filter(Directors.director_id.in_(director)).delete()


if __name__ == "__main__":
    task_9(name="James")
