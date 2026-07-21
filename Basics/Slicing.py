alphabet = "abcdefghijklmnopqrstuvwxyz"
print("Original string:", alphabet)

print("\n--- Basic Slicing [start:stop] ---")

first_five = alphabet[0:5]
print("First five letters [0:5]:", first_five)

print("First five again [:5]:", alphabet[:5])

print("Everything after 'w' [23:]:", alphabet[23:])

print("\n--- Slicing with Steps [start:stop:step] ---")
every_other = alphabet[0:26:2]
print("Every other letter [::2]:", alphabet[::2])

print("\n--- Negative Slicing ---")
print("The very last letter [-1]:", alphabet[-1])
print("The last three letters [-3:]:", alphabet[-3:])

reversed_alphabet = alphabet[::-1]
print("Reversed string [::-1]:", reversed_alphabet)

print("\n--- Slicing Lists ---")
numbers = [10, 20, 30, 40, 50]
print("List of numbers:", numbers)
print("Middle three numbers [1:4]:", numbers[1:4])
