def login():
    username = input("Enter username:")
    password = input("Enter password:")
    if username == password:
        print("Login successfull")
    else:
        print("invalid credential")

login() #calling function