# working with dictionaries (key-value pairs)

# Create a dictionary representing a person
person = {
    "name": "Jordan",
    "age": 28,
    "city": "New York"
}
print("Original dictionary:", person)

# Access a value using its key
print("Person's name:", person["name"])
print("Person's age:", person["age"])

# Add a new key-value pair
person["profession"] = "Software Engineer"
print("After adding profession:", person)

# Change an existing value
person["age"] = 29
print("After updating age:", person)

# Check if a key exists
has_city = "city" in person
print(f"Does the dictionary have a 'city' key? {has_city}")
