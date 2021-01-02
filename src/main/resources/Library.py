from User import *


class Login:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_condition(self, uname, passwd):
        return True if uname == self.username and passwd == self.password else False

    def login(self):
        if self.check_user():
            print(f" {self.username}  Successfully logged In !!\n")
            return self.username;
        else:
            print(f"login failed for {username} \n")
            exit()

    def check_user(self):
        with open("../../../database/UserData.txt", "r") as f:
            content = f.read().splitlines()
            for line in content:
                words = line.split(",")
                if self.user_condition(words[0], words[1]):
                    return True


class Register:
    def __init__(self, uname, passwd, mail, type_of_user):
        self.username = uname
        self.password = passwd
        self.email = mail
        self.type = type_of_user

    def register_user(self):
        with open("../../../database/UserData.txt", "a") as f:
            f.write("\n")
            f.write(self.username + "," + self.password + "," + self.email + "," + self.type)
        return True


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
            username = input("Enter the Username:\n")
            password = input("Enter the Password:\n")
            login = Login(username, password)
            login.login()
            user = User(username)
            user.actions()
        elif option == 2:
            username = input("Enter the Username:\n")
            password = input("Enter the Password:\n")
            email = input("Enter the Email Id:\n")
            user_type = input("Enter the user type:\n")
            register = Register(username, password, email, user_type)
            res = register.register_user()
            if res:
                print(f" {username} Successfully Registered in!!! ")
            else:
                print(f" {username} Registration failed !! :( ")
                exit()
        else:
            print("You decided to exit the Library")
            exit()
