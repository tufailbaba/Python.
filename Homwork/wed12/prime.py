#checking if a number is prime or not
num = int(input("Enter a number: "))

for i in range (2, num):
    if num % i == 0 :
        print("Entered number ",num," is not prime")
        break
else:
        print("Entered number ",num," is Prime")
        
        
#printing all prime numbers in a given range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Prime numbers between", lower, "and", upper, "are: ")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)