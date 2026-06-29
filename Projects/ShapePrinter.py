class ShapePrinter:
    def print_square(self, side):
        print(f"\nSquare (Side: {side})")
        for _ in range(side):
            print("* " * side)

    def print_hollow_square(self, side):
        print(f"\nHollow Square (Side: {side})")
        if side <= 1:
            print("* " * side)
            return
        for i in range(side):
            if i == 0 or i == side - 1:
                print("* " * side)
            else:
                # 2 spaces per star except the first and last
                print("*" + "  " * (side - 2) + " *")

    def print_rectangle(self, length, width):
        print(f"\nRectangle (Length: {length}, Width: {width})")
        for _ in range(width):
            print("* " * length)

    def print_right_angled_triangle(self, rows):
        print(f"\nRight-Angled Triangle (Rows: {rows})")
        for i in range(1, rows + 1):
            print("* " * i)

    def print_pyramid(self, rows):
        print(f"\nPyramid (Rows: {rows})")
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "* " * i)

    def print_diamond(self, rows):
        print(f"\nDiamond (Half-Rows: {rows})")
        # Top half
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "* " * i)
        # Bottom half
        for i in range(rows - 1, 0, -1):
            print(" " * (rows - i) + "* " * i)

def main():
    printer = ShapePrinter()
    
    while True:
        print("\n--- Shape Printer Menu ---")
        print("1. Square")
        print("2. Hollow Square")
        print("3. Rectangle")
        print("4. Right-Angled Triangle")
        print("5. Pyramid")
        print("6. Diamond")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        try:
            if choice == '1':
                side = int(input("Enter side length: "))
                printer.print_square(side)
            elif choice == '2':
                side = int(input("Enter side length: "))
                printer.print_hollow_square(side)
            elif choice == '3':
                length = int(input("Enter length: "))
                width = int(input("Enter width: "))
                printer.print_rectangle(length, width)
            elif choice == '4':
                rows = int(input("Enter number of rows: "))
                printer.print_right_angled_triangle(rows)
            elif choice == '5':
                rows = int(input("Enter number of rows: "))
                printer.print_pyramid(rows)
            elif choice == '6':
                rows = int(input("Enter number of rows for half diamond: "))
                printer.print_diamond(rows)
            elif choice == '7':
                print("Exiting Shape Printer. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter an integer value.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
