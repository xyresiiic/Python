# Basic Project: Mad Libs Story Generator
# This project combines variables, strings, and user input!

print("Welcome to the Mad Libs Story Generator!")
print("Please provide the following words to create a funny story.\n")

# Collect input from the user
adjective1 = input("Enter an adjective (e.g., fluffy, smelly, bright): ")
noun1 = input("Enter a noun (e.g., dog, spaceship, pizza): ")
verb_past_tense = input("Enter a verb ending in 'ed' (e.g., jumped, sneezed, rolled): ")
adverb = input("Enter an adverb (e.g., quickly, loudly, happily): ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")

print("\n------------------------------------")
print("Here is your Mad Libs Story:")
print("------------------------------------\n")

# Use f-strings (string formatting) to inject the variables into a story
story = f"One day, a {adjective1} {noun1} decided to go for a walk. " \
        f"Suddenly, it {verb_past_tense} {adverb} into a {adjective2} {noun2}! " \
        f"Everyone was very surprised."

print(story)
print("\n------------------------------------")
print("The End!")
