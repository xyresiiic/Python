# Program to check if a number is prime or not

def is_prime(number):
    # A prime number must be greater than 1
    if number <= 1:
        return False
        
    # Check for factors from 2 up to (number - 1)
    # We can optimize this by only checking up to the square root of the number,
    # or roughly halfway (number // 2 + 1), but checking all is fine for beginners!
    for i in range(2, number):
        # If the number is evenly divisible by 'i', it's not prime
        if number % i == 0:
            return False
            
    # If the loop finishes and finds no factors, it IS a prime number!
    return True

print("--- Prime Number Checker ---")
print("A prime number is a number greater than 1 that can only be divided by 1 and itself.\n")

# Let's test a few numbers
test_numbers = [2, 4, 7, 10, 13, 25, 29]

for num in test_numbers:
    if is_prime(num):
        print(f"{num} is a PRIME number!")
    else:
        print(f"{num} is NOT a prime number.")
