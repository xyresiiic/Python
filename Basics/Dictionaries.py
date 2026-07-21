person = {
    "name": "Jordan",
    "age": 28,
    "city": "New York"
}
print("Original dictionary:", person)

print("Person's name:", person["name"])
print("Person's age:", person["age"])

person["profession"] = "Software Engineer"
print("After adding profession:", person)

person["age"] = 29
print("After updating age:", person)

has_city = "city" in person
print(f"Does the dictionary have a 'city' key? {has_city}")
