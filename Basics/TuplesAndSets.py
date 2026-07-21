print("--- Tuples ---")
coordinates = (10, 20)

print("Original tuple:", coordinates)
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])


print("\n--- Sets ---")
unique_numbers = {1, 2, 3, 3, 3, 4, 5, 5}

print("Original set (notice duplicates are gone!):", unique_numbers)

unique_numbers.add(6)
unique_numbers.remove(2)
print("After adding 6 and removing 2:", unique_numbers)

if 4 in unique_numbers:
    print("The number 4 is in our set!")
