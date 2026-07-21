import math

def is_strong_number(number):

    total_sum = 0


    temp_str = str(number)

    for char in temp_str:
        digit = int(char)

        digit_factorial = math.factorial(digit)
        total_sum += digit_factorial

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
