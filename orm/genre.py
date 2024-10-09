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

    def insert(self, name: str):
        """
        Добавляет записи в таблицу genre.
        """
        try:
            conn = self.engine.connect()
            ins = insert(self.Genre).values(name=name)
            conn.execute(ins)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            print(str(e))
            self.engine.dispose()

    def select_genre(self, name: str) -> list[set]:
        """
        Получаем записи по name из таблицы genre в виде списка с кортежами
        """
        conn = self.engine.connect()
        try:
            s = select(self.Genre).where(self.Genre.c.name == name)
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

    def select_book_by_genre(self, name: str) -> list[set]:
        """
        Получаем title из book по genre в виде списка с кортежами
        """
        conn = self.engine.connect()
        try:
            s = (
                select(self.Genre, Book_orm.title, Author_orm.first_name, Author_orm.last_name)
                .where(self.Genre.c.name == name)
                .join(Book_orm, self.Genre.c.id == Book_orm.genre_id)
                .join(Author_orm, Author_orm.id == Book_orm.author_id)
            )
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

    def update_name(self, name: str, new_name: str):
        """
        Метод изменения данных в колонке name
        """
        conn = self.engine.connect()
        try:
            s = (
                update(self.Genre)
                .where(self.Genre.c.name == name)
                .values(name=new_name)
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

    def delete_genre(self, name: str):
        """
        Удаляет запись по name
        """
        conn = self.engine.connect()
        try:
            s = delete(self.Genre).where(self.Genre.c.name == name)
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
    s = Genre_table_orm()
    print(s.select_book_by_genre("Научная фантастика"))
