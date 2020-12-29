from datetime import date, timedelta


class Books:
    def __init__(self, username):
        """ Fetching all the book data"""
        self.books = list_of_books()
        self._username = username
        self.fine = load_fine()

    def display_books(self):
        print("The books are present at the Beuth University Library")
        for book in self.books:
            print(book)

    def borrow_book(self, book_name):
        found = [book[0] == book_name for book in self.books]
        if found:
            issued_date = date.today()
            return_date = date.today() + timedelta(days=15)
            with open("../database/IssuedBook.txt", "a+") as f:
                f.write(self._username + "," + book_name + "," + str(issued_date) + "," + str(return_date))
                f.write("\n")
            # updateBooks(book_name)
            print(f"You have borrowed {book_name} and you have 15 days to read book. please return book on time "
                  f"otherwise 1 EURO/day fine will be charged")

    def return_book(self, book_name, username):
        fine = self.check_fine(username)
        print(f"You have {fine} please pay before returning {book_name}")

    def check_fine(self, username):
        for f in self.fine:
            for g in f:
                print("G is ", g)
                l = g.split(",")
                if username == l[0]:
                    return l[1]

    def searchByName(self, book_name):
        return [book[0] == book_name for book in self.books]


def list_of_books():
    books = []
    with open("../database/Books.txt", "r") as bf:
        book_list = bf.readlines()
        for i in book_list:
            j = i.replace('\n', '').split(',')
            books.append(j)
        return books


def load_fine():
    fines = []
    with open("../database/Fine.txt", "r") as bf:
        pay = bf.readlines()
        for f in pay:
            j = f.replace('\n', '').split(',')
            fines.append(j)
    return fines
