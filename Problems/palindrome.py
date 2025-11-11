#check palindrome through basic string operation   
# palindrome is a string that reads the same forwards and backwards
string = input("Enter a string: ")
stringrev = string[::-1]
print(string == stringrev) 