#Problems on match case and if else statements
#Using match case to display the day of the week based on user input
day = int(input("Enter a number (1-7) to get the day of the week: ")) 
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")    
    case 3:
        print("Wednesday")  
    case 4:
        print("Thursday")   
    case 5:
        print("Friday") 
    case 6:
        print("Saturday")   
    case 7:
        print("Sunday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")

# user_input = input("Enter a command")
# match user_input:
#     case "start":
#         print("System started")
#     case "end":
#         print("Process ended")  
#     case _:
#         print("invalid operation") 
