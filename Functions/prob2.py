# Q2. Write a program which reverse a number 
# If input = 31
# Output = 13

#not returns integer
# input_num = input("Enter a number: ")
# revNum = input_num[::-1]
# print(revNum)

def reverse_number(num):
    return int(str(num)[::-1])

n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))

