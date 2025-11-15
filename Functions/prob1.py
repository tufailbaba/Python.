#Make a program with a function login().Use a loop to allow 3 attempts.Inside the function, use if-else to check:

#If username and password are correct - Login Successful

#Otherwise - show remaining attempts.
def login():
    username = "admin"
    password = "1234"

    attempts = 3

    while attempts > 0:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == username and pwd == password:
            print("Login Successful!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print("Wrong credentials! Attempts left:", attempts)
            else:
                print("No attempts left. Login failed.")

login()
