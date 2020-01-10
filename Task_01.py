import json

def add_del(file, author, title, year, todo):
    book = {
        "author": author,
        "title": title,
        "year": year
    }

    try:
        data = json.load(open(file))
        book_exist = False
        for books in data:
            if str(books["author"]) == author and str(books["title"]) == title and str(books["year"]) == year:
                print("Book exist")
                book_exist = True
                break
            else:
                book_exist = False
        if book_exist != True:
            if todo == 'add':
                data.append(book)
        elif book_exist == True and todo == 'del':
            data.remove(book)
    except:
        data = []
        if todo == 'add':
            data.append(book)

    with open(file, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def search_book(file, text):
    books_find = []
    try:
        data = json.load(open(file))
        for books in data:
            if (str(books["author"]) == text) or (str(books["title"]) == text) or (str(books["year"]) == text):
                books_find.append(books)
    except:
        print("No library")
    return books_find


def edit_book(file, author, title, year, new_author, new_title, new_year):
    add_del(file, author, title, year, 'del')
    add_del(file, new_author, new_title, new_year, 'add')


if __name__ == '__main__':

    # add_del("library.txt", "Test001", "Title001 test", "2001", 'add')
    # add_del("library.txt", "Test001", "Title001 test", "2001", 'add')
    # add_del("library.txt", "Test002", "Title002 test", "2002", 'add')
    # add_del("library.txt", "Test003", "Title003 test", "2003", 'add')
    # add_del("library.txt", "Test001", "Title001 test", "2001", 'add')
    # edit_book("library.txt", "Test002", "Title002 test", "2002", "Test003!!!", "Title003 test", "2003")


    print(search_book("library.txt", "2003"))


