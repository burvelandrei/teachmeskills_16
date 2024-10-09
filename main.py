from orm.database import create_tables
from orm.author import Author_table
from orm.genre import Genre_table
from orm.book import Book_table


def main():
    """Функция для вывода меню и выбора действий. Точка входа в программу."""
    print("Программа для работы с БД через SQLAlchemy")
    create_tables()
    Author = Author_table()
    Genre = Genre_table()
    Book = Book_table()
    check = True
    while check:
        print(
            "\nМеню:\n"
            "0. Выйти\n"
            "1. Добавить запись в таблицу author\n"
            "2. Добавить запись в таблицу genre\n"
            "3. Добавить запись в таблицу book\n"
            "4. Вывести записи из таблицы author\n"
            "5. Вывести записи из таблицы genre\n"
            "6. Вывести записи из таблицы book\n"
            "7. Редактировать запись в таблице author\n"
            "8. Редактировать запись в таблице genre\n"
            "9. Редактировать запись в таблице book\n"
            "10. Удалить запись из таблицы author\n"
            "11. Удалить запись из таблицы genre\n"
            "12. Удалить запись из таблицы book\n"
            "13. Поиск книг по автору\n"
            "14. Поиск книг по жанру\n"
            "15. Поиск книг по частичному совпадению заголовка\n"
        )

        choice = input("Введите пункт меню: ")
        if choice == "0":
            print("\nДо свидания!!!")
            check = False
        elif choice == "1":
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            Author.insert(first_name, last_name)
        elif choice == "2":
            name = input("Введите наименование жанра: ")
            Genre.insert(name)
        elif choice == "3":
            title = input("Введите заголовок книги: ")
            publication_year = int(input("Введите год публикации книги: "))
            author_id = int(input("Введите id автора: "))
            genre_id = int(input("Введите id жанра: "))
            Book.insert(title, publication_year, author_id, genre_id)
        elif choice == "4":
            while True:
                print(
                    "\nПодменю\n"
                    "0. Назад\n"
                    "1. Вывести по имени\n"
                    "2. Вывести по фамилии\n")
                sub_choice = input("Введи пункт подменю: ")
                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    first_name = input("Введите имя для поиска: ")
                    print(Author.select_author_first_name(first_name))
                elif sub_choice == "2":
                    last_name = input("Введите фамилию для поиска: ")
                    print(Author.select_author_last_name(last_name))
                else:
                    print("\nТакого подпункта нет! Побробуй ввести ещё раз.")

        elif choice == "5":
            name = name = input("Введите наименование жанра: ")
            print(Genre.select_genre(name))

        elif choice == "6":
            title = input("Введите заголовок книги: ")
            print(Book.select_book_by_title(title))

        elif choice == "7":
            while True:
                print(
                    "\nПодменю\n"
                    "0. Назад\n"
                    "1. Изменить имя\n"
                    "2. Изменить фамилию\n")
                sub_choice = input("Введи пункт подменю: ")
                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    id = int(input("Введите id автора: "))
                    new_first_name = input("Введите новое имя: ")
                    Author.update_first_name_by_id(id, new_first_name)
                elif sub_choice == "2":
                    id = int(input("Введите id автора: "))
                    new_last_name = input("Введите новую фамилию: ")
                    Author.update_last_name_by_id(id, new_last_name)
                else:
                    print("\nТакого подпункта нет! Побробуй ввести ещё раз.")

        elif choice == "8":
            name = input("Введите жанр для изменения: ")
            nem_name = input("Введите новое наименование жанра: ")
            Genre.update_name(name, nem_name)

        elif choice == "9":
            while True:
                print(
                    "\nПодменю\n"
                    "0. Назад\n"
                    "1. Изменить заголовок\n"
                    "2. Изменить год публикации\n")
                sub_choice = input("Введи пункт подменю: ")
                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    title = input("Введите заголовок для изменения: ")
                    new_title = input("Введите новый заголовок: ")
                    Book.update_title(title, new_title)
                elif sub_choice == "2":
                    title = input("Введите заголовок для изменения года: ")
                    new_publication_year = int(input("Введите новый год публикации: "))
                    Book.update_publication_year_by_title(title, new_publication_year)
                else:
                    print("\nТакого подпункта нет! Побробуй ввести ещё раз.")

        elif choice == "10":
            id = int(input("Введите id для удаления записи: "))
            Author.delete_author_by_id(id)

        elif choice == "11":
            name = input("Введите наименование жанра для удаления: ")
            Genre.delete_genre(name)

        elif choice == "12":
            while True:
                print(
                    "\nПодменю\n"
                    "0. Назад\n"
                    "1. Удалить по id\n"
                    "2. Удалить по заголовку\n")
                sub_choice = input("Введи пункт подменю: ")
                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    id = int(input("Введите id для удаления записи: "))
                    Book.delete_book_by_id(id)
                elif sub_choice == "2":
                    title = input("Введите заголовок для удаления записи: ")
                    Book.delete_book_by_title(title)
                else:
                    print("\nТакого подпункта нет! Побробуй ввести ещё раз.")

        elif choice == "13":
            first_name = input("Введите имя автора: ")
            last_name = input("Введите фамилию автора: ")
            print(Author.select_book_by_author(first_name, last_name))

        elif choice == "14":
            name = input("Введите наименование жанра: ")
            print(Genre.select_book_by_genre(name))

        elif choice == "15":
            particulate = input("Введите часть заголовка: ")
            print(Book.select_book_by_partial_title(particulate))

        else:
            print("\nТакого пункта нет! Побробуй ввести ещё раз.")



if __name__=="__main__":
    main()