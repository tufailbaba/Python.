num = int(input("Enter a number: "))

def function (num):
    if num <=1:
        return num
    else:
        return function(num - 1) + function(num - 2)

print(function(num))
  


