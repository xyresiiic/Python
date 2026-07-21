greeting = "Hello, Python learner!"
print("Original string:", greeting)

print("Uppercase:", greeting.upper())

print("Lowercase:", greeting.lower())

new_greeting = greeting.replace("learner", "programmer")
print("After replace:", new_greeting)

length = len(greeting)
print(f"The string has {length} characters.")

first_name = "Alex"
last_name = "Smith"
full_name = f"{first_name} {last_name}"
print("Combined name:", full_name)
