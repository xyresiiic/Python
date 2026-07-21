def is_palindrome(text):

    cleaned_text = text.replace(" ", "").lower()

    reversed_text = cleaned_text[::-1]

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
