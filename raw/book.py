from raw.database import db_connection


class Book_table_raw:
    @db_connection
    @staticmethod
    def insert(cursor, title: str, publication_year: int, author_id: int, genre_id: int):
        """
        Добавляет записи в таблицу book.
        """
        cursor.execute(
            f"""
            insert into book(title, publication_year, author_id, genre_id)
            values ('{title}', {publication_year}, {author_id}, {genre_id});"""
        )

    @db_connection
    @staticmethod
    def select_book_by_title(cursor, title: str) -> list[set]:
        """
        Получаем записи по title из таблицы book в виде списка с кортежами
        """
        cursor.execute(
            f"""
            select id, title, publication_year, author_id, genre_id
            from book
            where name = '{title}';"""
        )
        result = cursor.fetchall()
        return result

    @db_connection
    @staticmethod
    def select_book_by_partial_title(cursor, particulate: str) -> list[set]:
        """
        Получаем записи по частичному совпадению title из таблицы book и author в виде списка с кортежами
        """
        cursor.execute(
            f"""
            select book.title as book,
                book.publication_year as publication_year,
                author.first_name as author_first_name,
                author.last_name as author_last_name
            from book
            inner join author on author.id = book.author_id
            where book.title like '%{particulate}%';"""
        )
        result = cursor.fetchall()
        return result


    @db_connection
    @staticmethod
    def update_title(cursor, title: str, new_title: str):
        """
        Метод изменения данных в колонке title
        """
        cursor.execute(
            f"""
            update book
            set title = '{title}'
                where title = '{new_title}';"""
        )

    @db_connection
    @staticmethod
    def update_publication_year_by_title(cursor, title: str, new_publication_year: int):
        """
        Метод изменения данных в колонке publication_year
        """
        cursor.execute(
            f"""
            update book
            set publication_year  = '{new_publication_year}'
            where title = '{title}';"""
        )

    @db_connection
    @staticmethod
    def delete_book_by_id(cursor, id: int):
        """
        Удаляет запись по id
        """
        cursor.execute(
            f"""
            delete from book
            where id = '{id}';"""
        )

    @db_connection
    @staticmethod
    def delete_book_by_title(cursor, title: str):
        """
        Удаляет запись по title
        """
        cursor.execute(
            f"""
            delete from book
            where title = '{title}';"""
        )


if __name__ == "__main__":
    Book_table_raw.insert('Двадцать тысяч лье под водой', 1869, 1, 4)
