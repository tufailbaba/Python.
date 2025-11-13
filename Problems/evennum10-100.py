#Print even numbers between 10-100 and sum of all
sum = 0
for i in range(10, 100):
    if i % 2 == 0:
        print(i)
        sum +=i
print(sum)

