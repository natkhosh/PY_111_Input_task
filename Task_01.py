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
    """
    if add_del_book(file, author, title, year, 'del'):
        if add_del_book(file, new_author, new_title, new_year, 'add'):
            return True
        else:
            return False
    else:
        return False



if __name__ == '__main__':

    # add_del_book("library_02.txt", "Анна Ахматова", "Реквием", "1963", 'add')

    if edit_book("library_02.txt", "Анна Ахматова", "Реквием", "1963", "Анна Ахматова", "Белая стая", "1922"):
        print('Книга отредактирована')
    else:
        print('Книга не отредактирована')


    # print(search_book("library_02.txt", "аннА"))


