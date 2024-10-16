from sqlalchemy import insert, select, update, MetaData, Table, delete
from orm.database import engine
from orm.models import Book_orm, Author_orm


class Genre_table_orm:
    def __init__(self):
        self.engine = engine
        metadata = MetaData()
        self.Genre = Table(
            "genre", metadata, autoload_replace=True, autoload_with=self.engine
        )
        self.conn = self.engine.connect()

    def insert(self, name: str):
        """
        Добавляет записи в таблицу genre.
        """
        try:
            ins = insert(self.Genre).values(name=name)
            self.conn.execute(ins)
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def select_genre(self, name: str) -> list[set]:
        """
        Получаем записи по name из таблицы genre в виде списка с кортежами
        """
        try:
            s = select(self.Genre).where(self.Genre.c.name == name)
            re = self.conn.execute(s)
            result = re.fetchall()
            return result
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def select_book_by_genre(self, name: str) -> list[set]:
        """
        Получаем title из book по genre в виде списка с кортежами
        """
        try:
            s = (
                select(
                    self.Genre,
                    Book_orm.title,
                    Author_orm.first_name,
                    Author_orm.last_name,
                )
                .where(self.Genre.c.name == name)
                .join(Book_orm, self.Genre.c.id == Book_orm.genre_id)
                .join(Author_orm, Author_orm.id == Book_orm.author_id)
            )
            re = self.conn.execute(s)
            result = re.fetchall()
            return result
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def update_name(self, name: str, new_name: str):
        """
        Метод изменения данных в колонке name
        """
        try:
            s = (
                update(self.Genre)
                .where(self.Genre.c.name == name)
                .values(name=new_name)
            )
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def delete_genre(self, name: str):
        """
        Удаляет запись по name
        """
        try:
            s = delete(self.Genre).where(self.Genre.c.name == name)
            self.conn.execute(s)
        except Exception as e:
            self.conn.rollback()
            print(str(e))


if __name__ == "__main__":
    s = Genre_table_orm()
    print(s.select_book_by_genre("Научная фантастика"))
