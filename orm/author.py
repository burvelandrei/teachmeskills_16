from sqlalchemy import insert, select, update, MetaData, Table, delete
from orm.database import engine
from orm.models import Book_orm


class Author_table_orm:
    def __init__(self):
        self.engine = engine
        metadata = MetaData()
        self.Author = Table(
            "author", metadata, autoload_replace=True, autoload_with=self.engine
        )
        self.conn = self.engine.connect()

    def insert(self, first_name: str, last_name: str):
        """
        Добавляет записи в таблицу author.
        """
        try:
            ins = insert(self.Author).values(first_name=first_name, last_name=last_name)
            self.conn.execute(ins)
        except Exception as e:
            self.conn.rollback()

            print(str(e))

    def select_author_first_name(self, first_name: str) -> list[set]:
        """
        Получаем записи по first_name из таблицы author в виде списка с кортежами
        """
        try:
            s = select(self.Author).where(self.Author.c.first_name == first_name)
            re = self.conn.execute(s)
            result = re.fetchall()
            return result
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def select_author_last_name(self, last_name: str) -> list[set]:
        """
        Получаем записи по last_name из таблицы author в виде списка с кортежами
        """
        try:
            s = select(self.Author).where(self.Author.c.last_name == last_name)
            re = self.conn.execute(s)
            result = re.fetchall()
            return result
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def select_book_by_author(self, first_name: str, last_name: str) -> list[set]:
        """
        Получаем title из book по first_name и last_name в виде списка с кортежами
        """
        try:
            s = (
                select(self.Author, Book_orm.title)
                .where(
                    self.Author.c.first_name == first_name
                    and self.Author.c.last_name == last_name
                )
                .join(Book_orm, self.Author.c.id == Book_orm.author_id)
            )
            re = self.conn.execute(s)
            result = re.fetchall()
            return result
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def update_first_name_by_id(self, id: int, new_first_name: str):
        """
        Метод изменения данных в колонке first_name
        """
        try:
            s = (
                update(self.Author)
                .where(self.Author.c.id == id)
                .values(first_name=new_first_name)
            )
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def update_last_name_by_id(self, id: int, new_last_name: str):
        """
        Метод изменения данных в колонке last_name
        """
        try:
            s = (
                update(self.Author)
                .where(self.Author.c.id == id)
                .values(last_name=new_last_name)
            )
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def delete_author_by_id(self, id: int):
        """
        Удаляет запись по id
        """
        try:
            s = delete(self.Author).where(self.Author.c.id == id)
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))


if __name__ == "__main__":
    s = Author_table_orm()
    print(s.select_book_by_author(first_name="Жюль", last_name="Верн"))
