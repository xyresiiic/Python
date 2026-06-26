# working with list comprehensions

# A "List Comprehension" is a very cool, "Pythonic" way to create a new list
# based on an existing list, usually taking just a single line of code!

print("--- The Long Way (using a standard for loop) ---")
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print("Original numbers:", numbers)
print("Doubled numbers:", doubled_numbers)


print("\n--- The Pythonic Way (List Comprehension) ---")
# We can do the exact same thing in ONE line!
# Syntax: [expression for item in list]
tripled_numbers = [num * 3 for num in numbers]
print("Tripled numbers:", tripled_numbers)


print("\n--- Adding a condition (if statement) ---")
# We can also add an 'if' statement at the end to filter items!
# Let's get only the even numbers from a list of 1 to 10
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# "Give me 'num', for every 'num' in all_numbers, IF 'num' is even"
even_numbers = [num for num in all_numbers if num % 2 == 0]
print("All numbers:", all_numbers)
print("Only even numbers:", even_numbers)
