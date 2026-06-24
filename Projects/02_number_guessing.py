# Basic Project: Number Guessing Game
# This project combines imports, loops, conditionals, inputs, and variables!

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random secret number
secret_number = random.randint(1, 100)

# We'll use a variable to track how many tries the user has taken
attempts = 0
guessed_correctly = False

# Keep asking the user until they guess the right number
while not guessed_correctly:
    user_guess_text = input("\nEnter your guess: ")
    
    # We should handle the error in case the user doesn't type a real number!
    try:
        user_guess = int(user_guess_text)
        attempts += 1 # Add 1 to the number of attempts
        
        # Check if the guess is too low, too high, or correct
        if user_guess < secret_number:
            print("Too low! Try a higher number.")
        elif user_guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"\nCongratulations! You guessed my number in {attempts} attempts!")
            guessed_correctly = True # This will stop the while loop
            
    except ValueError:
        print("Oops! That doesn't look like a valid number. Please try again.")

print("\nThanks for playing!")
