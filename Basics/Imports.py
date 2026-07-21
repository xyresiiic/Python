import random
import math

print("--- Using the 'random' module ---")

random_number = random.randint(1, 10)
print(f"I picked a random number between 1 and 10: {random_number}")

colors = ["red", "blue", "green", "yellow", "purple"]
chosen_color = random.choice(colors)
print(f"I picked a random color from the list: {chosen_color}")


print("\n--- Using the 'math' module ---")

number_to_root = 25
square_root = math.sqrt(number_to_root)
print(f"The square root of {number_to_root} is {square_root}")

print(f"The value of Pi is roughly: {math.pi}")
