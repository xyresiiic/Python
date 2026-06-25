# working with tuples and sets

print("--- Tuples ---")
# A Tuple is like a list, but it cannot be changed once created (it is "immutable").
# We use parentheses () to create a tuple.
coordinates = (10, 20)

print("Original tuple:", coordinates)
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# This would cause an error because tuples cannot be modified:
# coordinates[0] = 15  <- ERROR!

print("\n--- Sets ---")
# A Set is an unordered collection of unique items.
# It automatically removes duplicates!
# We use curly braces {} to create a set.
unique_numbers = {1, 2, 3, 3, 3, 4, 5, 5}

print("Original set (notice duplicates are gone!):", unique_numbers)

# We can add and remove items from a set
unique_numbers.add(6)
unique_numbers.remove(2)
print("After adding 6 and removing 2:", unique_numbers)

# Sets are great for checking if something exists very quickly
if 4 in unique_numbers:
    print("The number 4 is in our set!")
