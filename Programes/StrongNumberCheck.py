# Program to check if a number is a Strong Number
import math

def is_strong_number(number):
    # A Strong Number is a number where the sum of the factorials 
    # of its digits equals the original number itself!
    # Example: 145 -> 1! + 4! + 5! = 1 + 24 + 120 = 145
    
    # Let's keep track of our total sum
    total_sum = 0
    
    # We need to process each digit. Converting the number to a string 
    # makes it super easy to loop through each digit one by one!
    temp_str = str(number)
    
    for char in temp_str:
        # Convert the character back to an integer
        digit = int(char)
        
        # Calculate the factorial of the digit and add it to our total
        digit_factorial = math.factorial(digit)
        total_sum += digit_factorial
        
    # Finally, check if the total sum matches the original number
    if total_sum == number:
        return True
    else:
        return False

print("--- Strong Number Checker ---")
print("A Strong Number's digits' factorials add up to the number itself!\n")

test_numbers = [145, 2, 5, 40585, 123]

for num in test_numbers:
    if is_strong_number(num):
        print(f"YES: {num} is a Strong Number!")
    else:
        print(f"NO:  {num} is NOT a Strong Number.")
