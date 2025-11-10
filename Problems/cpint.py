# Calculate compound interest in Python through basic steps
input_principal = float(input("Enter the principal amount: "))
input_rate = float(input("Enter the annual interest rate (in %): "))
input_time = float(input("Enter the time period (in years): "))
input_n = int(input("Enter the number of times interest is compounded per year: "))

#calculate compound interest
amount = input_principal * (1 + (input_rate / (100 * input_n))) ** (input_n * input_time)
compound_interest = amount - input_principal    
print("The compound interest is: ", compound_interest)
print("The total amount after interest is: ", amount)