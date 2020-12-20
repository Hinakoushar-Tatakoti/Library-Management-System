class Login:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def set_username(self, username: str):
        self._username = username

    def get_username(self):
        return self._username

    def set_password(self, password: str):
        self._password = password

    def get_password(self):
        return self._password

    def check_user(self,username, password):
        with open("../data/UserData.txt", "r") as f:
            lines = f.read()
            line = lines.split("\n")
            for l in list(line):
                words = l.split(" ")
                if words[0] == username and words[1] == password:
                    flag = 1
                else:
                    flag = 0
                if flag == 1:
                    return True


