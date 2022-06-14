from mysql.connector import Error, connect
from os import environ

PASSWORD = environ.get("SQL_PASS")


def create_database(database_name):
    try:
        with connect(host="localhost", user='root', password=PASSWORD) as conn:
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"

            with conn.cursor() as cursor:
                cursor.execute(create_db_query)
    except Error as e:
        print(e)


def drop_database(database_name):
    try:
        with connect(host="localhost", user='root', password=PASSWORD) as conn:
            drop_db_query = f"DROP DATABASE IF EXISTS {database_name}"

            with conn.cursor() as cursor:
                cursor.execute(drop_db_query)
    except Error as e:
        print(e)


def create_tables(database_name, table_name, table_data):
    try:
        with connect(host="localhost", user='root', password=PASSWORD, database=database_name) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({table_data});")
    except Error as e:
        print(e)


def drop_table(database_name, table_name):
    try:
        with connect(host="localhost", user='root', password=PASSWORD, database=database_name) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")


    except Error as e:
        print(e)

def show_tables(database_name):
    try:
        with connect(host="localhost", user='root', password=PASSWORD, database=database_name) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SHOW TABLES")
                result = cursor.fetchall()
                return_list = []
                for row in result:
                    print(*row)
                    return_list.append(row[0])
                return return_list
    except Error as e:
        print(e)

def insert_data(database_name, table_name, query, data):

    try:
        with connect(host="localhost", user='root', password=PASSWORD, database=database_name) as conn:

            final_query = f"INSERT INTO {table_name} {query}"

            with conn.cursor() as cursor:
                cursor.executemany(final_query, data)
                conn.commit()

    except Error as e:
        print(e)


def sql_query(query):
    try:
        with connect(host="localhost", user='root', password=PASSWORD, database="cinematic") as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(*row)
    except Error as e:
        print(e)


select_query_2002 = """
            SELECT * 
            FROM movies
            WHERE movie_year > 2002
            """

tables = {
    "cinematic": {
                "directors": """
                        director_id INT AUTO_INCREMENT PRIMARY KEY,
                        director_name VARCHAR(50) NOT NULL,
                        director_surname VARCHAR(50) NOT NULL,
                        director_rating FLOAT NOT NULL
                        """,
                "movies": """
                        movie_id INT AUTO_INCREMENT PRIMARY KEY,
                        movie_name VARCHAR(50) NOT NULL,
                        movie_year INT NOT NULL,
                        movie_category VARCHAR(50) NOT NULL,
                        movie_director_id INT NOT NULL,
                        movie_rating FLOAT NOT NULL,
                        FOREIGN KEY (movie_director_id) REFERENCES directors(director_id));
                        """
    }
}

data = {
    "cinematic": {
        "directors": {
            "query": "(director_name, director_surname, director_rating) VALUES (%s, %s, %s)",
            "data": [
                ('Frank', 'Darabont', 7),
                ('Francis Ford', 'Coppola', 8),
                ('Quentin', 'Tarantino', 10),
                ('Christopher', 'Nolan', 9),
                ('David', 'Fincher', 7)
            ],
        },
        "movies": {
            "query": "(movie_name, movie_year, movie_category, movie_director_id, movie_rating) VALUES (%s, %s, %s, %s, %s)",
            "data": [
                ('The Shawshank Redemption', 1994, 'Drama', 1, 8),
                ('The Green Mile', 1999, 'Drama', 1, 6),
                ('The Godfather', 1972, 'Crime', 2, 7),
                ('The Godfather III', 1990, 'Crime', 2, 6),
                ('Pulp Fiction', 1994, 'Crime', 3, 9),
                ('Inglourious Basterds', 2009, 'War', 3, 8),
                ('The Dark Knight', 2008, 'Action', 4, 9),
                ('Interstellar', 2014, 'Sci-fi', 4, 8),
                ('The Prestige', 2006, 'Drama', 4, 10),
                ('Fight Club', 1999, 'Drama', 5, 7),
                ('Zodiac', 2007, 'Crime', 5, 5),
                ('Seven', 1995, 'Drama', 5, 8),
                ('Alien 3', 1992, 'Horror', 5, 5)
            ],
        }
    }
}

#
create_database('cinematic')
## drop_database("cinematic")
# for database, table in tables.items():
#     for table_name, table_schema in table.items():
#         create_tables(database, table_name, table_schema)
#
# for database, table in data.items():
#     for table_name, table_data in table.items():
#         insert_data(database, table_name, table_data['query'], table_data['data'])

# for database, table in tables.items():
#     for table_name, _ in table.items():
#         drop_table(database, table_name)
#
# while tables := show_tables("cinematic"):
#     for table in tables:
#         drop_table("cinematic", table)

# sql_query(select_query_2002)
# sql_query("select * from movies left join directors on movies.movie_director_id = directors.director_id")

# print(show_tables("cinematic"))

