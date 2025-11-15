# #Swapping values without using a 3rd variable
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# a = a + b
# b = a - b
# a = a - b
# print("After swapping:")
# print("First number: ", a)
# print("Second number: ", b)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# a, b = b, a
# print("After swapping:")
# print("First number: ", a)
# print("Second number: ", b)

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

num1,num2 = num2,num1

print("First number: ", num1)
print("Second number: ", num2)