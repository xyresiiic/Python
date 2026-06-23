# working with strings

# Create a simple string
greeting = "Hello, Python learner!"
print("Original string:", greeting)

# Convert to uppercase
print("Uppercase:", greeting.upper())

# Convert to lowercase
print("Lowercase:", greeting.lower())

# Replace a word
new_greeting = greeting.replace("learner", "programmer")
print("After replace:", new_greeting)

# Check the length of the string
length = len(greeting)
print(f"The string has {length} characters.")

# String formatting (combining variables)
first_name = "Alex"
last_name = "Smith"
full_name = f"{first_name} {last_name}"
print("Combined name:", full_name)
