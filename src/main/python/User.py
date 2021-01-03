from Books import *


class User:
    def __init__(self, username,access_type):
        self._username = username
        self._access_type = access_type

    def student_professors_actions(self):
        b1 = Books(self._username)
        while True:
            print("Let's do some actions on the account!!")
            print("1", "display_books")
            print("2", "search book By book_Name")
            print("3", "borrow_book")
            print("4", "return book")
            print("5", "pay fine")
            print("Press any number for exit")
            user_choice = input("Enter your choice \n")
            if user_choice not in ["1", "2", "3", "4", "5"]:
                print("You have selected different choice and logging out from the system")
                exit()
            else:
                user_choice = int(user_choice)
                if user_choice == 1:
                    b1.display_books()
                    print("\n")

                elif user_choice == 2:
                    book_name = input("Enter the name of book: ")
                    if b1.searchByName(book_name):
                        print(f"\n The Book {book_name} is found !! \n")
                    else:
                        print(f"\nThe Book {book_name} your searching is not found !! give it another short\n")

                elif user_choice == 3:
                    book = input("please Enter the name of the book you want to borrow :")
                    b1.borrow_book(book)
                    print("\n")

                elif user_choice == 4:
                    book = input("please Enter the name of the book you want to return :")
                    user = input("please enter your name:")
                    b1.return_book(book, user)
                    print("\n")

                elif user_choice == 5:
                    book = input("please Enter the name of the book having fine :")
                    b1.check_fine(self._username, book)

    def admin_actions(self):
        b1 = Books(self._username)
        while True:
            print("Let's do some actions as admin!!")
            print("1", "Display a book")
            print("2", "Add a book")
            print("3", "Remove a book")
            print("Press any number for exit")
            admin_choice = int(input("Enter your choice \n"))
            if admin_choice == 1:
                b1.display_books()
                print("\n")

            elif admin_choice == 2:
                book_name = input("Enter the name of book : ")
                author = input("Enter the author name :  ")
                numbers = input("Enter the number of copies :  ")
                price = input("Enter the price of the book : ")
                b1.add_book(book_name, author, numbers, price)

            elif admin_choice == 3:
                book = input("please Enter the name of the book you want to delete :")
                author = input("please Enter the Author name :")
                b1.remove_book(book, author)
                print("\n")

            else:
                exit()
