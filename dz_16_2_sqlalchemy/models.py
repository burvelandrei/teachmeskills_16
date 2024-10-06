from sqlalchemy import Table, Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


# Базовый класс для всех моделей
Base = declarative_base()


# Определям модель таблицы author
class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)


# Определям модель таблицы genre
class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False)


# Определям модель таблицы book
class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(50), nullable=False)
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey(Author.id, ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey(Genre.id, ondelete="CASCADE"))
