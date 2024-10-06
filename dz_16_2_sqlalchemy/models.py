from sqlalchemy import Table, Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(50), nullable=False)
    last_name= Column(VARCHAR(50), nullable=False)

class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(50), nullable=False)
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey(Author.id, ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey(Genre.id, ondelete="CASCADE"))
