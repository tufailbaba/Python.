# Comprehensions Example in Python

nums = [1, 2, 2, 3, 4, 5, 5]

# 1️⃣ List Comprehension → Create a list of squares
squares = [n * n for n in nums]
print("List Comprehension (Squares):", squares)

# 2️⃣ Set Comprehension → Unique squares only
unique_squares = {n * n for n in nums}
print("Set Comprehension (Unique Squares):", unique_squares)

# 3️⃣ Dictionary Comprehension → Map number to its square
square_dict = {n: n * n for n in nums}
print("Dictionary Comprehension:", square_dict)

# 4️⃣ With condition → Even numbers only
even_squares = [n * n for n in nums if n % 2 == 0]
print("Even Squares (with condition):", even_squares)
