colors = ["red", "green", "blue", "yellow"]
print("Original list:", colors)

print("First color:", colors[0])
print("Second color:", colors[1])

colors.append("purple")
print("After adding purple:", colors)

colors[0] = "orange"
print("After changing the first color:", colors)

total_colors = len(colors)
print(f"There are {total_colors} colors in the list.")
