# working with basic slicing

# "Slicing" lets you grab a specific part of a string or list.
# We use brackets and a colon like this: [start:stop]

word = "Programming"
print("Original word:", word)

# 1. Grab the first 3 letters (starts at 0, stops before 3)
first_part = word[0:3]
print("First 3 letters [0:3]:", first_part)

# 2. Grab the letters in the middle (starts at 3, stops before 7)
middle_part = word[3:7]
print("Middle letters [3:7]:", middle_part)

# 3. If you leave out the start number, it assumes 0 (the beginning)
start_to_five = word[:5]
print("Beginning to 5 [:5]:", start_to_five)

# 4. If you leave out the stop number, it goes all the way to the end
three_to_end = word[3:]
print("From 3 to the end [3:]:", three_to_end)

# Slicing also works exactly the same way on lists!
numbers = [10, 20, 30, 40, 50]
print("\nOriginal list:", numbers)
print("Middle numbers [1:4]:", numbers[1:4])
