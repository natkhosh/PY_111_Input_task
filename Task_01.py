"""
Модуль реализует библиотеку для хранения данных книг и поиск по каталогу.
"""

import json


def add_del_book(file: str, author: str, title: str, year: str, mode: str):
    """
    Функция добавления книги в библиотеку и удаления книги из библиотеки

    :param file: путь к файлу библиотки
    :param author: автор книги
    :param title: название книги
    :param year: год издания
    :param mode: команда (add - добавить, del - удалить)
    :return: True/False выполнена или не выполнена функция
    """
    book = {
        "Автор": author,
        "Название": title,
        "Год издания": year
    }
    function_result = False

    try:
        data = json.load(open(file, encoding="utf-8"))
    except FileNotFoundError:
        data = []
        if mode == 'add':
            data.append(book)
            function_result = True
    else:
        book_exist = False
        for books in data:
            if str(books["Автор"]) == author and str(books["Название"]) == title and str(books["Год издания"]) == year:
                if mode == 'add':
                    print("Такая книга уже есть в библиотеке.")
                book_exist = True
                break
            else:
                book_exist = False

        if book_exist is not True:
            if mode == 'add':
                data.append(book)
                function_result = True
        elif book_exist is True and mode == 'del':
            data.remove(book)
            function_result = True

    with open(file, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return function_result


def search_book(file: str, text: str) -> list:
    """
    Функция поиска книги в библиотеке.

    :param file: путь к файлу библиотки
    :param text: строка поиска
    :return: список найденных книг
    """
    books_find = []
    try:
        data = json.load(open(file, encoding="utf-8"))
    except FileNotFoundError:
        print("Файл библиотеки не создан.")
    else:
        t = text.upper()
        for books in data:
            if (t in str.upper(books["Автор"])) or (t in str.upper(books["Название"])) or (t in str.upper(books["Год издания"])):
                books_find.append(books)

    return books_find


def edit_book(file: str, author: str, title: str, year: str, new_author: str, new_title: str, new_year: str):
    """
    Функция редактирования информации о книге.
    :param file: путь к файлу библиотки
    :param author: автор книги (редактируемое значение)
    :param title: название книги (редактируемое значение)
    :param year: год издания (редактируемое значение)
    :param new_author: автор книги (обновленное значение)
    :param new_title: название книги (обновленное значение)
    :param new_year: год издания (обновленное значение)
    :return: True/False выполнена или не выполнена функция
    """
    if add_del_book(file, author, title, year, 'del'):
        if add_del_book(file, new_author, new_title, new_year, 'add'):
            return True
        else:
            return False
    else:
        return False


def main():
    """
    Функция реализует интерфейс взаимодействия с пользователем
    """
    print("Использовать библиотеку по умолчанию или создать новую?",
          '\n\t- yes (библиотка поумолчанию)', '\n\t- no (создать новую библиотеку)')
    file_lib = str(input("> "))
    if file_lib == 'yes' or file_lib == 'no':
        if file_lib == 'yes':
            file = "library_02.txt"
        else:
            file = str(input('Введите путь библиотеки: >  '))
    else:
        print('Некорректный ввод.', '\n')

    print('\n', 'Список допустимых команд:', '\n\t- add  --> Добавить книгу в библиотеку',
          '\n\t- del  --> Удалить книгу из библиотеку', '\n\t- edit --> Редактировать книгу',
          '\n\t- find --> Поиск книги', '\n\t- exit --> Выход', '\n')

    while True:
        command = str(input("Введите команду: > "))

        if command == 'add' or command == 'del' or command == 'edit' or command == 'find' or command == 'exit':
            if command == 'add':
                add_author = str(input('Введите автора книги: >  '))
                add_book_name = str(input('Введите название книги: >  '))
                add_book_year = str(input('Введите год издания книги: >  '))
                if add_del_book(file, add_author, add_book_name, add_book_year, 'add'):
                    print('> Книга добавлена', '\n')
                else:
                    print('> Книга не добавлена', '\n')

            if command == 'del':
                del_author = str(input('Введите автора книги: >  '))
                del_book_name = str(input('Введите название книги: >  '))
                del_book_year = str(input('Введите год издания книги: >  '))
                if add_del_book(file, del_author, del_book_name, del_book_year, 'del'):
                    print('> Книга удалена', '\n')
                else:
                    print('> Книга не удалена', '\n')

            if command == 'edit':
                add_author = str(input('Введите автора книги: >  '))
                add_book_name = str(input('Введите название книги: >  '))
                add_book_year = str(input('Введите год издания книги: >  '))
                add_author_new = str(input('Введите нового автора книги: >  '))
                add_book_name_new = str(input('Введите новое название книги: >  '))
                add_book_year_new = str(input('Введите новый год издания книги: >  '))
                if edit_book(file, add_author, add_book_name, add_book_year, add_author_new,  add_book_name_new, add_book_year_new):
                    print('> Книга отредактирована', '\n')
                else:
                    print('> Книга не отредактирована', '\n')

            if command == 'find':
                search_ = str(input('Введите поисковый запрос: >  '))
                print('Список найденных книг: >  ', search_book(file, search_), '\n')

            if command == 'exit':
                break
        else:
            print('Некорректный ввод.', '\nВедите комманду в соотвествии со списком команд.', '\n')


if __name__ == '__main__':
    main()
