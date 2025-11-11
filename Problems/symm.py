
word = input("Enter a word: ")

half = len(word) // 2       
first = word[:half]         
second = word[-half:]       

if first == second:
    print("The word is symmetric.")
else:
    print("The word is not symmetric.")
