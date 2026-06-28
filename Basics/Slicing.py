# working with slicing
# "Slicing" is a feature that lets you extract

# Let's create a string to slice
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("Original string:", alphabet)

print("\n--- Basic Slicing [start:stop] ---")

# Get the first 5 letters
first_five = alphabet[0:5]
print("First five letters [0:5]:", first_five)

# If you omit the start index, it assumes 0
print("First five again [:5]:", alphabet[:5])

# If you omit the end index, it goes all the way to the end
print("Everything after 'w' [23:]:", alphabet[23:])

print("\n--- Slicing with Steps [start:stop:step] ---")
# You can add a third number to skip characters!
# Let's get every second letter from the whole string
every_other = alphabet[0:26:2]
# Or shorter: alphabet[::2]
print("Every other letter [::2]:", alphabet[::2])

print("\n--- Negative Slicing ---")
# Negative indices count from the END of the string!
print("The very last letter [-1]:", alphabet[-1])
print("The last three letters [-3:]:", alphabet[-3:])

# A famous Python trick: Reversing a string or list!
reversed_alphabet = alphabet[::-1]
print("Reversed string [::-1]:", reversed_alphabet)

print("\n--- Slicing Lists ---")
# Slicing works exactly the same way on lists!
numbers = [10, 20, 30, 40, 50]
print("List of numbers:", numbers)
print("Middle three numbers [1:4]:", numbers[1:4])
