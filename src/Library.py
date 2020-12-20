from Login import Login
from Register import Register
from User import User


def login():
    username = input("Enter the Username:\n")
    password = input("Enter the Password:\n")
    log = Login(username, password)
    if log.check_user(log.get_username(), log.get_password()):
        print(f"Successfully logged in {username} \n")
    else:
        print(f"login failed for {username} \n")
        exit()


def register_user():
    username = input("Enter the Username:\n")
    password = input("Enter the Password:\n")
    email = input("Enter the Email Id:\n")
    type = input("Enter the user type:\n")
    reg = Register(username, password, email, type)
    if reg.register_user(reg.get_username(), reg.get_password(), reg.get_email(), reg.get_type()):
        print("Successfully logged in!!! " + reg.get_username())
    else:
        print(" Registration failed for !!! " + reg.get_username())
        exit()


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
                u1 = User()
                u1.actions()
            elif option == 2:
                register_user()
            else:
                print("You decided to exit the Library")
                exit()
