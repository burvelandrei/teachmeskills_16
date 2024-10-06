from sqlalchemy import insert, select, update, MetaData, Table, delete
from database import engine


class Author_table:
    def __init__(self):
        self.engine = engine
        metadata = MetaData()
        self.Author = Table(
            "author", metadata, autoload_replace=True, autoload_with=self.engine
        )

    def Insert(self, first_name: str, last_name: str):
        """
        Добавляет записи в таблицу author.
        """
        try:
            conn = self.engine.connect()
            ins = insert(self.Author).values(first_name=first_name, last_name=last_name)
            conn.execute(ins)
            conn.commit()
            conn.close()
            self.engine.dispose()
        except Exception as e:
            conn.rollback()
            conn.commit()
            print(str(e))
            self.engine.dispose()

    def Select_author_first_name(self, first_name: str) -> list[set]:
        """
        Получаем записи по first_name из таблицы author в виде списка с кортежами
        """
        conn = self.engine.connect()
        try:
            s = select(self.Author).where(self.Author.c.first_name == first_name)
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

    def Select_author_last_name(self, last_name: str) -> list[set]:
        """
        Получаем записи по last_name из таблицы author в виде списка с кортежами
        """
        conn = self.engine.connect()
        try:
            s = select(self.Author).where(self.Author.c.last_name == last_name)
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

    def Update_first_name_by_id(self, id: int, new_first_name: str):
        """
        Метод изменения данных в колонке first_name
        """
        conn = self.engine.connect()
        try:
            s = (
                update(self.Author)
                .where(self.Author.c.id == id)
                .values(first_name=new_first_name)
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

    def Update_last_name_by_id(self, id: int, new_last_name: str):
        """
        Метод изменения данных в колонке last_name
        """
        conn = self.engine.connect()
        try:
            s = (
                update(self.Author)
                .where(self.Author.c.id == id)
                .values(last_name=new_last_name)
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

    def Delete_author_by_id(self, id: int):
        """
        Удаляет запись по id
        """
        conn = self.engine.connect()
        try:
            s = delete(self.Author).where(self.Author.c.id == id)
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
    s = Author_table()
    s.Update_first_name_by_id(id=1, new_first_name="Алекс")
