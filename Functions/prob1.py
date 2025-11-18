#Make a program with a function login().Use a loop to allow 3 attempts.Inside the function, use if-else to check:

#If username and password are correct - Login Successful

#Otherwise - sho w remaining attempts.
def login():
    username = "tufail"
    password = "2580"

    attempts =3

    while attempts > 0:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == username and pwd == password:
            print("Login Successful!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print("Attempts left:", attempts)
            else:
                print("No attempts left.")

login()
