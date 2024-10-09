from raw.database import db_connection


class Genre_table_raw:
    @db_connection
    @staticmethod
    def insert(cursor, name: str):
        """
        Добавляет записи в таблицу genre.
        """
        cursor.execute(
            f"""
            insert into genre(name)
            values ('{name}');"""
        )

    @db_connection
    @staticmethod
    def select_genre(cursor, name: str) -> list[set]:
        """
        Получаем записи по name из таблицы genre в виде списка с кортежами
        """
        cursor.execute(
            f"""
            select id, name
            from genre
            where name = '{name}';"""
        )
        result = cursor.fetchall()
        return result

    @db_connection
    @staticmethod
    def select_book_by_genre(cursor, name: str) -> list[set]:
        """
        Получаем title из book по genre в виде списка с кортежами
        """
        cursor.execute(
            f"""
            select genre.name as genre_name,
                book.title as title,
                author.first_name as first_name,
                author.last_name  as last_name
            from genre
            inner join book on genre.id = book.genre_id
            inner join author on author.id = book.author_id
            where genre."name"  = '{name}';"""
        )
        result = cursor.fetchall()
        return result

    @db_connection
    @staticmethod
    def update_name(cursor, name: str, new_name: str):
        """
        Метод изменения данных в колонке name
        """
        cursor.execute(
            f"""
            update genre
            set name = '{new_name}'
            where name = '{name}';"""
        )

    @db_connection
    @staticmethod
    def delete_genre(cursor, name: str):
        """
        Удаляет запись по name
        """
        cursor.execute(
            f"""
            delete from genre
            where name = '{name}';"""
        )


if __name__ == "__main__":
    Genre_table_raw.insert("Комедия")
