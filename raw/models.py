from raw.database import db_connection


@db_connection
def author_model(cursor):
    cursor.execute(
        f"""
    create table if not exists author(
	id serial primary key,
	first_name varchar(50),
	last_name varchar(50)
	);"""
    )


@db_connection
def genre_model(cursor):
    cursor.execute(
        f"""
    create table if not exists genre(
	id serial primary key,
	name varchar(50)
	);"""
    )


@db_connection
def book_model(cursor):
    cursor.execute(
        f"""
    create table if not exists book(
	id serial primary key,
	title varchar(70),
	publication_year int,
	author_id int,
	genre_id int,
	foreign key (author_id) references author(id) on delete cascade,
	foreign key (genre_id) references genre(id) on delete cascade
	);"""
    )


def create_tables_raw():
    """
    Функция для создания всех таблиц.
    """
    author_model()
    genre_model()
    book_model()

if __name__ == "__main__":
    create_tables_raw()
