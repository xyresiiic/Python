# working with lists

# Create a list of colors
colors = ["red", "green", "blue", "yellow"]
print("Original list:", colors)

# Access items by their position (index starts at 0)
print("First color:", colors[0])
print("Second color:", colors[1])

# Add a new color to the end of the list
colors.append("purple")
print("After adding purple:", colors)

# Change an item
colors[0] = "orange"
print("After changing the first color:", colors)

# Count how many items are in the list
total_colors = len(colors)
print(f"There are {total_colors} colors in the list.")
