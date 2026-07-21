def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print("--- Prime Number Checker ---")
print("A prime number is a number greater than 1 that can only be divided by 1 and itself.\n")

test_numbers = [2, 4, 7, 10, 13, 25, 29]

for num in test_numbers:
    if is_prime(num):
        print(f"{num} is a PRIME number!")
    else:
        print(f"{num} is NOT a prime number.")
