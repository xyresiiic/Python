print("--- Example 1: Avoiding a crash ---")

try:
    result = 10 / 0
    print("The result is:", result)
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")

print("\n--- Example 2: Handling user mistakes ---")

user_input = "five"

try:
    number = int(user_input)
    print(f"Your number multiplied by 2 is {number * 2}")
except ValueError:
    print(f"Oops! '{user_input}' is not a valid number. Please use digits (like 5).")

print("\nThe program finished successfully without crashing!")
