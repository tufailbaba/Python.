#checking if a number is prime or not
num = int(input("Enter a number: "))

for i in range (2, num):
    if num % i == 0 :
        print("Entered number ",num," is not prime")
        break
else:
        print("Entered number ",num," is Prime")
        
    
        
        
        
# #printing all prime numbers in a given range
# for num in range(2, 100):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)