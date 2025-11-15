# . Write a function calculator() that shows a menu inside a loop:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Use if-else to perform the chosen operation.”

def calculator():
    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '5':
            print("Exiting")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
                print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid input")

        
calculator()


    




