# working with imports (modules)

# Python comes with many built-in "modules" that contain pre-written code.
# To use them, we have to "import" them first.

import random
import math

print("--- Using the 'random' module ---")

# random.randint() gives us a random number between the two numbers we provide
random_number = random.randint(1, 10)
print(f"I picked a random number between 1 and 10: {random_number}")

# random.choice() picks a random item from a list
colors = ["red", "blue", "green", "yellow", "purple"]
chosen_color = random.choice(colors)
print(f"I picked a random color from the list: {chosen_color}")


print("\n--- Using the 'math' module ---")

# math.sqrt() calculates the square root of a number
number_to_root = 25
square_root = math.sqrt(number_to_root)
print(f"The square root of {number_to_root} is {square_root}")

# math.pi gives us the value of Pi
print(f"The value of Pi is roughly: {math.pi}")
