def start():
    print("###################################\n")
    print("   Welcome to Beuth University of Applied Science Library   ")
    print("-------------------------------------------------------------------\n")
    print(""" ======LIBRARY MENU=======
                      1. Login
                      2. Register
                      3. Exit
                      """)
    while (True):
        try:
            a = int(input("Select a choice from 1-3: "))
            if a == 1:
                print("Enter the UserName : ")
                userName = input(" ")
                print("Enter the Password : ")
                passWord = input(" ")
                with open("../UserData.txt", "r") as f:
                    lines = f.read()
                    line = lines.split("\n")
                    for l in list(line):
                        words = l.split(" ")
                        if words[0] == userName and words[1] == passWord:
                            falg = 1
                        else:
                            falg = 0
                        if (falg == 1):
                            print("Success")
                            return

            if a == 2:
                print("Enter the UserName : ")
                userName = input(" ")
                print("Enter the Password : ")
                passWord = input(" ")
                print("Enter the EmailId : ")
                emailId = input(" ")
                print("Enter the UserType : ")
                userType = input(" ")
                with open("../UserData.txt", "a") as f:
                    f.write(userName + " " + passWord + " " + emailId + " " + userType)
                    f.write("\n")
            if a == 3:
                print("Thank you for using library management system")
                break

        except ValueError as ve:
            print(f"Please input as suggested. {ve}")


start()
