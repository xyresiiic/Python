# working with error handling (try and except)

# Sometimes our code might run into an error (like trying to divide by zero,
# or asking the user for a number but they type a word instead).
# Instead of the whole program crashing, we can "catch" the error and handle it nicely!

print("--- Example 1: Avoiding a crash ---")

# Let's try dividing by zero (which normally crashes a program)
try:
    result = 10 / 0
    print("The result is:", result)
except ZeroDivisionError:
    # If a ZeroDivisionError happens, it jumps here instead of crashing
    print("Oops! You cannot divide by zero.")

print("\n--- Example 2: Handling user mistakes ---")

# We can use this for user input too!
user_input = "five" # Imagine the user typed this instead of a number like "5"

try:
    # Trying to turn the word "five" into a number will cause a ValueError
    number = int(user_input)
    print(f"Your number multiplied by 2 is {number * 2}")
except ValueError:
    # We catch the mistake and show a friendly message
    print(f"Oops! '{user_input}' is not a valid number. Please use digits (like 5).")

print("\nThe program finished successfully without crashing!")
