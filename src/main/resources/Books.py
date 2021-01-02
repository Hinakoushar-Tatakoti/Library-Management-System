import datetime


class Books:
    def __init__(self, username):
        """ Fetching all the book data"""
        self.books = list_of_books()
        self._username = username

    def display_books(self):
        print("The books are present at the Beuth University Library")
        for book in self.books:
            print(book)

    def borrow_book(self, book_name):
        found = [book[0] == book_name for book in self.books]
        if found:
            issued_date = datetime.datetime.today()
            return_date = datetime.datetime.today() + datetime.timedelta(days=15)
            with open("../../../database/IssuedBook.txt", "a+") as f:
                f.write(self._username + "," + book_name + "," + str(issued_date) + "," + str(return_date))
                f.write("\n")
            # updateBooks(book_name)
            print(f"You have borrowed {book_name} and you have 15 days to read book. please return book on time "
                  f"otherwise 1 EURO/day fine will be charged")

    def return_book(self, book_name, username):
        self.check_fine(username, book_name)

    def check_fine(self, username, book):
        money = 0
        with open("../../../database/IssuedBook.txt", "r") as f:
            book_list = f.readlines()
            for b in book_list:
                con = b.split(",")
                print(con)
                if con[0] == username and con[1] == book:
                    con[3] = con[3].strip('\n')
                    d1 = datetime.datetime.strptime(con[2], '%Y-%m-%d %H:%M:%S.%f')
                    d2 = datetime.datetime.strptime(con[3], '%Y-%m-%d %H:%M:%S.%f')
                    fine = 15 - abs(d1.day - d2.day)
                    if fine < 0:
                        money = abs(fine)

        print(f"You have {money} Euro fine !!! :( please pay before returning {book}")

    def searchByName(self, book_name):
        return [book[0] == book_name for book in self.books]


def list_of_books():
    books = []
    with open("../../../database/Books.txt", "r") as bf:
        book_list = bf.readlines()
        [books.append(load(i)) for i in book_list]
        return books


load = lambda x: x.replace('\n', '').split(',')
