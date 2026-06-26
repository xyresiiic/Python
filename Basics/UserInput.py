# This program demonstrates getting input from the user

# Ask the user for their name
name = input("What is your name? ")

# Say hello to the user
print(f"Hello, {name}! Nice to meet you.")

# Ask the user for a number
favorite_number = input("What is your favorite number? ")

# Input is always a string, so we need to convert it to an integer
number = int(favorite_number)

# Do a simple calculation with the number
doubled = number * 2
print(f"Did you know that your favorite number multiplied by 2 is {doubled}?")
