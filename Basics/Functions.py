# working with functions

# A function is a reusable block of code that performs a specific task.
# We define a function using the 'def' keyword.

# 1. A simple function that just prints a message
def say_hello():
    print("Hello! Welcome to learning Python functions.")

# 2. A function that takes an argument (input)
def greet_person(name):
    print(f"Good morning, {name}!")

# 3. A function that calculates something and returns a result
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# --- Now let's USE (call) our functions! ---

print("--- Calling say_hello() ---")
say_hello()

print("\n--- Calling greet_person() ---")
greet_person("Alex")
greet_person("Sam")

print("\n--- Calling add_numbers() ---")
# We save the result of the function in a variable
total = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {total}.")
