from Login import *
from Register import *
from User import *


class Library:
    if __name__ == '__main__':
        while True:
            print("###################################\n")
            print("   Welcome to Beuth University of Applied Science Library   ")
            print("-------------------------------------------------------------------\n")
            print(""" ======LIBRARY MENU=======
                                         1. Login
                                         2. Register
                                         3. Exit            """)

            option = int(input("Enter the choice 1 or 2 or 3:\n"))
            if option == 1:
                username = login()
                u1 = User(username)
                u1.actions()
            elif option == 2:
                register_user()
            else:
                print("You decided to exit the Library")
                exit()
