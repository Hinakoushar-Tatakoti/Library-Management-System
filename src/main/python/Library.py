import User
import re


class Login:

    def __init__(self, uname, passwd):
        self.username = uname
        self.password = passwd

    def user_condition(self, uname, passwd):
        return True if uname == self.username and passwd == self.password else False

    def login(self):
        access_type = self.check_user()
        user = User(username, access_type)
        if access_type == 'admin' :
            print(f" {self.username}  Successfully logged In as {access_type}!!\n")
            user.admin_actions()
        elif access_type == 'staff' or access_type == 'student':
            print(f" {self.username}  Successfully logged In as {access_type} !!\n")
            user.student_professors_actions()
        else:
            print(f"login failed for {username} \n")
            exit()

    def check_user(self):
        with open("../../../database/UserData.txt", "r") as f:
            content = f.read().splitlines()
            for line in content:
                if len(line) != 0:
                    words = line.split(",")
                    if self.user_condition(words[0], words[1]):
                        return words[3]


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
            print(f" {username} Successfully Registered in as {self.type}!!! ")

    def check_validation(self):
        if not valid_user_check(self.username):
            raise Exception("Invalid username!!")
        if not valid_password_check(self.password):
            raise Exception("Invalid password!!")
        if not valid_email_check(self.email):
            raise Exception("Invalid email address!!")
        if not valid_usertype_check(self.type):
            raise Exception("Invalid user type!!")


user_type = ['student', 'staff', 'admin']

valid_user_check = lambda uname: True if re.match("^[a-zA-Z0-9_]+$", uname) else False

valid_password_check = lambda passwd: True if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passwd) else False

valid_email_check = lambda mail: True if re.search(r'[\w.-]+@[\w.-]+.\w+', email) else False

valid_usertype_check = lambda t: True if any(word in t for word in user_type) else False

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
        elif option == 2:
            username = input("Enter the Username:\n")
            password = input("Enter the Password:\n")
            email = input("Enter the Email Id:\n")
            user_type = input("Enter the user type:\n")
            register = Register(username, password, email, user_type)
            register.check_validation()
            register.register_user()
        else:
            print("You decided to exit the Library")
            exit()
