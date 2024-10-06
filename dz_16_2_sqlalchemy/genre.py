from sqlalchemy import insert, select, update, MetaData, Table, delete
from database import engine


class Genre_table:
    def __init__(self):
        self.engine = engine
        metadata = MetaData()
        self.Genre = Table(
            "genre", metadata, autoload_replace=True, autoload_with=self.engine
        )

    def Insert(self, name: str):
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

    def Select_genre(self, name: str) -> list[set]:
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

    def Update_name(self, name: str, new_name: str):
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

    def Delete_genre(self, name: str):
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
    s = Genre_table()
    s.Insert(1, "Драма")
