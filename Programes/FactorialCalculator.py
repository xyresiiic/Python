# Program to find the factorial of a number
import math

def calculate_factorial(n):
    # The factorial of a number (like 5!) is 5 * 4 * 3 * 2 * 1
    # We can calculate this using a loop!
    
    # 0! is always 1
    if n == 0 or n == 1:
        return 1
        
    result = 1
    for i in range(2, n + 1):
        result = result * i
        
    return result

print("--- Factorial Calculator ---")

number_to_test = 5

# Method 1: Using our custom loop function
custom_result = calculate_factorial(number_to_test)
print(f"Using our loop function: {number_to_test}! = {custom_result}")

# Method 2: Using Python's built-in math module
# (Python is great because it often has built-in tools for common math problems)
builtin_result = math.factorial(number_to_test)
print(f"Using the math module:   {number_to_test}! = {builtin_result}")

print("\nLet's test a bigger number:")
big_number = 10
print(f"{big_number}! = {math.factorial(big_number)}")
