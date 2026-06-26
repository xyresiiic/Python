# Basic Project: Number Guessing Game

import random

print("-----------------------Welcome to the Number Guessing Game---------------------------")
print("-------------------------------------------------------------------------------------")
print("I'm thinking of a number between 1 and 100.")

# to generate a random number
secret_number = random.randint(1, 100)

# track tries the user has taken
attempts = 0
guessed_correctly = False

# Keep asking the user until they guess the right number
while not guessed_correctly:
    user_guess_text = input("\nEnter your guess: ")
    
    #in case the user doesn't type a real number!
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
        print("That doesn't look like a valid number. Please try again.")

print("\nThanks for playing")
