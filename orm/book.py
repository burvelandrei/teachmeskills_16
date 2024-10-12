from sqlalchemy import insert, select, update, MetaData, Table, delete
from orm.database import engine
from orm.models import Author_orm


class Book_table_orm:
    def __init__(self):
        self.engine = engine
        metadata = MetaData()
        self.Book = Table(
            "book", metadata, autoload_replace=True, autoload_with=self.engine
        )
        self.conn = self.engine.connect()

    def insert(self, title: str, publication_year: int, author_id: int, genre_id: int):
        """
        Добавляет записи в таблицу book.
        """
        try:
            ins = insert(self.Book).values(
                title=title,
                publication_year=publication_year,
                author_id=author_id,
                genre_id=genre_id,
            )
            self.conn.execute(ins)
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def select_book_by_title(self, title: str) -> list[set]:
        """
        Получаем записи по title из таблицы book в виде списка с кортежами
        """
        try:
            s = select(self.Book).where(self.Book.c.title == title)
            re = self.conn.execute(s)
            result = re.fetchall()
            return result
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def select_book_by_partial_title(self, particulate: str) -> list[set]:
        """
        Получаем записи по частичному совпадению title из таблицы book и author в виде списка с кортежами
        """
        try:
            s = (
                select(self.Book, Author_orm.first_name, Author_orm.last_name)
                .filter(self.Book.c.title.like(f"%{particulate}%"))
                .join(Author_orm, Author_orm.id == self.Book.c.author_id)
            )
            re = self.conn.execute(s)
            result = re.fetchall()
            return result
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def update_title(self, title: str, new_title: str):
        """
        Метод изменения данных в колонке title
        """
        conn = self.engine.connect()
        try:
            s = (
                update(self.Book)
                .where(self.Book.c.title == title)
                .values(title=new_title)
            )
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def update_publication_year_by_title(self, title: str, new_publication_year: int):
        """
        Метод изменения данных в колонке publication_year
        """
        try:
            s = (
                update(self.Book)
                .where(self.Book.c.title == title)
                .values(publication_year=new_publication_year)
            )
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def delete_book_by_id(self, id: int):
        """
        Удаляет запись по id
        """
        try:
            s = delete(self.Book).where(self.Book.c.id == id)
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def delete_book_by_title(self, title: str):
        """
        Удаляет запись по title
        """
        try:
            s = delete(self.Book).where(self.Book.c.title == title)
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))


if __name__ == "__main__":
    s = Book_table_orm()
    print(s.select_book_by_partial_title("вадц"))
