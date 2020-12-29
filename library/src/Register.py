class Register:
    def __init__(self, username: str, password: str, email: str, type: str):
        self._username = username
        self._password = password
        self._email = email
        self._type = type

    def set_username(self, username: str):
        self._username = username

    def get_username(self):
        return self._username

    def set_password(self, password: str):
        self._password = password

    def get_password(self):
        return self._password

    def set_email(self, email: str):
        self._email = email

    def get_email(self):
        return self._email

    def set_type(self, type: str):
        self._type = type

    def get_type(self):
        return self._type

    def register_user(self, username, password, email, usertype):
        with open("../database/UserData.txt", "a") as f:
            f.write(username + " " + password + " " + email + " " + usertype)
            f.write("\n")
        return True


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


