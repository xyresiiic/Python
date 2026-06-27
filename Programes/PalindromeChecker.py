# Project: Palindrome Checker

def is_palindrome(text):
    # A palindrome is a word that reads the same forwards and backwards (like "racecar")
    
    # First, let's clean up the text! 
    # We want to ignore spaces and make everything lowercase so "Race car" works.
    cleaned_text = text.replace(" ", "").lower()
    
    # We can use the awesome Python slicing trick [::-1] to reverse the string!
    reversed_text = cleaned_text[::-1]
    
    # If the cleaned text is exactly the same as the reversed text, it's a palindrome!
    if cleaned_text == reversed_text:
        return True
    else:
        return False

print("--- Palindrome Checker ---")
print("Let's check if some words or phrases are palindromes!\n")

test_phrases = [
    "racecar",
    "hello",
    "A man a plan a canal Panama",
    "Python",
    "Taco cat"
]

for phrase in test_phrases:
    if is_palindrome(phrase):
        print(f"YES: '{phrase}' IS a palindrome!")
    else:
        print(f"NO:  '{phrase}' is NOT a palindrome.")
