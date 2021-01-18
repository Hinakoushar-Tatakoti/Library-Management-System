from src.main.python.User import *
from src.main.python.Errors import *

user_file_path = "../../../database/UserData.txt"


class Login:

    def __init__(self, uname, passwd):
        self.username = uname
        self.password = passwd

    def user_condition(self, uname, passwd):
        return True if uname == self.username and passwd == self.password else False

    def login(self):
        access_type = self.check_user()
        user = User(self.username, access_type)
        if access_type == 'admin':
            print(f" {self.username}  Successfully logged In as {access_type}!!\n")
            user.admin_actions()
        elif access_type == 'staff' or access_type == 'student':
            print(f" {self.username}  Successfully logged In as {access_type} !!\n")
            user.student_professors_actions()
        else:
            print(f"login failed for {self.username} \n")
            exit()

    def check_user(self):
        with open(user_file_path, "r") as f:
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
        with open(user_file_path, "a") as f:
            f.write("\n")
            f.write(self.username + "," + self.password + "," + self.email + "," + self.type)
            print(f" {self.username} Successfully Registered in as {self.type}!!! ")


valid_user_check = lambda uname: True if re.match("^[a-zA-Z0-9_]+$", uname) else False

valid_password_check = lambda passwd: True if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passwd) else False

valid_email_check = lambda mail: True if re.search(r'[\w.-]+@[\w.-]+.\w+', mail) else False

valid_usertype_check = lambda t: True if any(word in t for word in ['student', 'staff', 'admin']) else False


def validate_user(u_name):
    try:
        if not valid_user_check(u_name):
            raise InvalidUserException
    except InvalidUserException:
        print(f"You entered invalid username {str(u_name)}")
        exit()


def validate_password(password):
    try:
        if not valid_password_check(password):
            raise InvalidPasswordException("Invalid password")
    except InvalidPasswordException:
        print(f"You entered invalid password {str(password)} and it should contain at least 8 chars")
        exit()


def validate_email(email):
    try:
        if not valid_email_check(email):
            raise InvalidEmailException("Invalid email")
    except InvalidEmailException:
        print(f"You entered invalid email format {str(email)}")
        exit()


def validate_type(user_ty):
    try:
        if not valid_usertype_check(user_ty):
            raise InvalidTypeException("Invalid usertype")
    except InvalidTypeException:
        print(f"Please enter valid user type {str(user_ty)}")
        exit()


class Start:
    def actions(self):
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
                print("You have selected 2nd option to Register to Beuth university Library")
                print("Please enter valid username, password, email and usertype[admin, student, staff]")
                username = input("Enter the Username:\n")
                validate_user(username)
                password = input("Enter the Password:\n")
                validate_password(password)
                email = input("Enter the Email Id:\n")
                validate_email(email)
                user_type = input("Enter the user type:\n")
                validate_type(user_type)
                register = Register(username, password, email, user_type)
                register.register_user()
            else:
                print("You decided to exit the Library")
                exit()


if __name__ == '__main__':
    st = Start
    st.actions()
