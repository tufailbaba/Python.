#Checking whether a given number is odd and greater than 100

num = float(input("Enter a number: "))
if num>100 and num%2 != 0:
    print(num, " Satisfies the condition")
else:
    print(int(num), "Does not satisfy the condition")