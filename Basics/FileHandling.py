print("Writing data to a file called 'my_notes.txt'...")
file = open("my_notes.txt", "w")
file.write("Hello! This is my first text file created by Python.\n")
file.write("Learning to code is fun!\n")
file.close()

print("\nNow reading data back from the file:")
file = open("my_notes.txt", "r")
content = file.read()
print(content)
file.close()

print("--- Using the 'with' keyword to append data ---")

with open("my_notes.txt", "a") as file:
    file.write("P.S. Python handles files very easily!\n")

with open("my_notes.txt", "r") as file:
    updated_content = file.read()
    print("Updated file contents:\n" + updated_content)
