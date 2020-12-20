class Books:
    def display_books(self):
        with open("../data/Books.txt", "r") as f:
            books = f.read()
            print("The books are present at the Beuth University Library")
            print(books)

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def cheack_fine(self):
        pass

    def searchByName(self,book_name):
        with open("../data/Books.txt", "r") as f:
            lines = f.read()
            books = lines.split("\n")
            for book in list(books):
                if book == book_name:
                    return True
        return False

