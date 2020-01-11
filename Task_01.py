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
    """
    book = {
        "author": author,
        "title": title,
        "year": year
    }

    try:
        data = json.load(open(file, encoding="utf-8"))
    except FileNotFoundError:
        data = []
        if mode == 'add':
            data.append(book)
    else:
        book_exist = False
        for books in data:
            if str(books["author"]) == author and str(books["title"]) == title and str(books["year"]) == year:
                print("Book exist")
                book_exist = True
                break
            else:
                book_exist = False

        if book_exist is not True:
            if mode == 'add':
                data.append(book)
        elif book_exist is True and mode == 'del':
             data.remove(book)

    with open(file, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def search_book(file, text):
    books_find = []
    try:
        data = json.load(open(file, encoding="utf-8"))
    except FileNotFoundError:
        print("Файл библиотеки не создан.")
    else:
        for books in data:
            if (str(books["author"]) == text) or (str(books["title"]) == text) or (str(books["year"]) == text):
                books_find.append(books)
    return books_find


def edit_book(file, author, title, year, new_author, new_title, new_year):
    add_del_book(file, author, title, year, 'del')
    add_del_book(file, new_author, new_title, new_year, 'add')


if __name__ == '__main__':

    add_del_book("library__.txt", "ПАМффф", "Роковые яйца", "1924", 'add')


    # edit_book("library.txt", "Test002", "Title002 test", "2002", "Test003!!!", "Title003 test", "2003")


    # print(search_book("library.txt", "2003"))


