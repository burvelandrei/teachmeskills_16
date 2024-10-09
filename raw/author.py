from raw.database import db_connection


class Author_table_raw:
    @db_connection
    @staticmethod
    def insert(cursor, first_name: str, last_name: str):
        """
        Добавляет записи в таблицу author.
        """
        cursor.execute(
            f"""
            insert into author(first_name, last_name)
            values ('{first_name}', '{last_name}');"""
        )

    @db_connection
    @staticmethod
    def select_author_first_name(cursor, first_name: str) -> list[set]:
        """
        Получаем записи по first_name из таблицы author в виде списка с кортежами
        """
        cursor.execute(
            f"""
            select id, first_name, last_name
            from author
            where first_name = '{first_name}';"""
        )
        result = cursor.fetchall()
        return result

    @db_connection
    @staticmethod
    def select_author_last_name(cursor, last_name: str) -> list[set]:
        """
        Получаем записи по last_name из таблицы author в виде списка с кортежами
        """
        cursor.execute(
            f"""
            select id, first_name, last_name
            from author
            where last_name = '{last_name}';"""
        )
        result = cursor.fetchall()
        return result

    @db_connection
    @staticmethod
    def select_book_by_author(cursor, first_name: str, last_name: str) -> list[set]:
        """
        Получаем title из book по first_name и last_name в виде списка с кортежами
        """
        cursor.execute(
            f"""
            select author.first_name as first_name,
                author.last_name as last_name,
                book.title as title
            from author
            inner join book on author.id = book.author_id
            where author.first_name = '{first_name}' and author.last_name = '{last_name}';"""
        )
        result = cursor.fetchall()
        return result

    @db_connection
    @staticmethod
    def update_first_name_by_id(cursor, id: int, new_first_name: str):
        """
        Метод изменения данных в колонке first_name
        """
        cursor.execute(
            f"""
            update author
            set first_name = '{new_first_name}'
            where id = {id};"""
        )

    @db_connection
    @staticmethod
    def update_last_name_by_id(cursor, id: int, new_last_name: str):
        """
        Метод изменения данных в колонке last_name
        """
        cursor.execute(
            f"""
            update author
            set first_name = '{new_last_name}'
            where id = {id};"""
        )

    @db_connection
    @staticmethod
    def update_last_name_by_id(cursor, id: int):
        """
        Удаляет запись по id
        """
        cursor.execute(
            f"""
            delete from author
            where id = {id};"""
        )


if __name__ == "__main__":
    Author_table_raw.insert('Жюль', 'Верн')
