#checking the smaller among all given number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# if num1 >num2:
#     if num1 > num3:
#         print(num1," is Greater than ",num2," and ",num3)
#         if num2 > num1:
#             if num2 > num3:
#                 print(num2," is Greater than ",num1," and ",num3)
#             else:
#                 print(num3," is Greater than ",num1," and ",num2)
    

if num1 > num2 and num1>num3:
    print(num1," is Greater the ",num2," and ",num3)
elif num2 > num1 and num2 > num3 :
    print(num2 ," is Greater than",num1," and", num3)
elif num3 > num2 and num3 > num1:
    print( num3," is Greater than ",num1,"  and", num2)
else:
    print("Entered numbers are same")