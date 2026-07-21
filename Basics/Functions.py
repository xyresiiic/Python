def say_hello():
    print("Hello! Welcome to learning Python functions.")

def greet_person(name):
    print(f"Good morning, {name}!")

def add_numbers(num1, num2):
    result = num1 + num2
    return result


print("--- Calling say_hello() ---")
say_hello()

print("\n--- Calling greet_person() ---")
greet_person("Alex")
greet_person("Sam")

print("\n--- Calling add_numbers() ---")
total = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {total}.")
