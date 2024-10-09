from sqlalchemy import Table, Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from orm.database import engine


# Базовый класс для всех моделей
Base = declarative_base()


# Определям модель таблицы author
class Author_orm(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)


# Определям модель таблицы genre
class Genre_orm(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False)


# Определям модель таблицы book
class Book_orm(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(50), nullable=False)
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey(Author_orm.id, ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey(Genre_orm.id, ondelete="CASCADE"))



def create_tables_orm():
    """
    Функция для создания всех таблиц.
    """
    Base.metadata.create_all(engine)
    engine.echo = False