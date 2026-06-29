def right_angled_triangle(rows):
    print("Right-Angled Triangle:")
    for i in range(1, rows + 1):
        print("*" * i)

def pyramid_triangle(rows):
    print("\nPyramid Triangle:")
    for i in range(1, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

if __name__ == "__main__":
    try:
        num_rows = int(input("Enter the number of rows: "))
        if num_rows <= 0:
            print("Please enter a positive integer.")
        else:
            right_angled_triangle(num_rows)
            pyramid_triangle(num_rows)
    except ValueError:
        print("Please enter a valid integer.")
