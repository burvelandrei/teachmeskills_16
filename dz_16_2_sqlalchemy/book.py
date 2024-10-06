from sqlalchemy import insert, select, update, MetaData, Table, delete
from database import engine


class Book_table:
    def __init__(self):
        self.engine = engine
        metadata = MetaData()
        self.Book = Table(
            "book", metadata, autoload_replace=True, autoload_with=self.engine
        )

    def Insert(self, title: str, publication_year: int, author_id: int, genre_id: int):
        """
        Добавляет записи в таблицу book.
        """
        try:
            conn = self.engine.connect()
            ins = insert(self.Book).values(
                title=title,
                publication_year=publication_year,
                author_id=author_id,
                genre_id=genre_id,
            )
            conn.execute(ins)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            print(str(e))
            self.engine.dispose()

    def Select_book_by_title(self, title: str) -> list[set]:
        """
        Получаем записи по title из таблицы book в виде списка с кортежами
        """
        conn = self.engine.connect()
        try:
            s = select(self.Book).where(self.Book.c.title == title)
            re = conn.execute(s)
            result = re.fetchall()
            conn.commit()
            conn.close()
            self.engine.dispose()
            return result
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def Update_title(self, title: str, new_title: str):
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
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def Update_publication_year_by_title(self, title: str, new_publication_year: int):
        """
        Метод изменения данных в колонке publication_year
        """
        conn = self.engine.connect()
        try:
            s = (
                update(self.Book)
                .where(self.Book.c.title == title)
                .values(publication_year=new_publication_year)
            )
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def Delete_book_by_id(self, id: int):
        """
        Удаляет запись по id
        """
        conn = self.engine.connect()
        try:
            s = delete(self.Book).where(self.Book.c.id == id)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))

    def Delete_book_by_title(self, title: str):
        """
        Удаляет запись по title
        """
        conn = self.engine.connect()
        try:
            s = delete(self.Book).where(self.Book.c.title == title)
            conn.execute(s)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            self.engine.dispose()
            print(str(e))


if __name__ == "__main__":
    s = Book_table()
    s.Insert(1, "Двадцать лет спустя", 1845, 1, 1)
