import random

print("Welcome to Rock, Paper, Scissors!")
print("Type rock, paper or scissors. Type exit to stop.\n")

while True:
    
    user_choice = input("Your move: ").lower()

    if user_choice == "exit":
        print("Okay, thanks for playing!")
        break

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("Please enter a valid choice.\n")
        continue

 
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!\n")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.\n")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.\n")

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.\n")

    else:
        print("You lose this round.\n")
