class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"₹{amount} credited successfully!")

    def debit(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} debited successfully!")

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")


# --- MAIN PROGRAM ---
name = input("Enter account holder's name: ")
account = BankAccount(name)

while True:
    print("\n----- MENU -----")
    print("1. Credit Money")
    print("2. Debit Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to credit: "))
        account.credit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to debit: "))
        account.debit(amount)

    elif choice == '3':
        account.check_balance()

    elif choice == '4':
        print("Thank you for using the Bank System!")
        break

    else:
        print("Invalid choice! Please try again.")
