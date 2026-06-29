def main():
    print("--- 1. Iterating over a range ---")
    # range(start, stop) -> goes from start up to stop-1
    for i in range(1, 6):
        print(f"Number: {i}")

    print("\n--- 2. Iterating over a list ---")
    fruits = ["Apple", "Banana", "Cherry", "Date"]
    for fruit in fruits:
        print(f"Fruit: {fruit}")

    print("\n--- 3. Iterating over a string ---")
    word = "Python"
    for char in word:
        print(f"Character: {char}")

    print("\n--- 4. Iterating with an index (using enumerate) ---")
    colors = ["Red", "Green", "Blue"]
    for index, color in enumerate(colors):
        print(f"Index {index}: {color}")

    print("\n--- 5. Iterating over a dictionary ---")
    student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
    for name, score in student_scores.items():
        print(f"{name}'s score is {score}")

if __name__ == "__main__":
    main()
