from Books import Books

b1 = Books()


class User:

    def actions(self):
        while (True):
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
                    found = b1.searchByName(book_name)
                    if found:
                        print(f"\n The Book {book_name} is found !! \n)")
                    else:
                        print(f"\nThe Book {book_name} your searching is not found !! give it another short\n")

                elif user_choice == 3:
                    book = input("please Enter the name of the book you want to borrow :")
                    user = input("please enter your name:")
                    b1.borrow_book(book, user)
                    print("\n")

                elif user_choice == 4:
                    book = input("please Enter the name of the book you want to return :")
                    user = input("please enter your name:")
                    b1.return_book(book, user)
                    print("\n")

                elif user_choice == 5:
                    book = input("please Enter the name of the book having fine :")
                    user = input("please enter your name:")
                    b1.cheack_fine(book, user)


