from Login import Login


def login():
    username = input("Enter the Username:\n")
    password = input("Enter the Password:\n")
    log = Login(username, password)
    print(log)
    if log.check_user(log.get_username(), log.get_password()):
        print("Successfully logged in!!! " + username)
    else:
        print(" login failed for !!! " + username)
        exit()


def register_user():
    pass


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
                login()
            elif option == 2:
                register_user()
            else:
                print("You decided to exit the Library")
                exit()
