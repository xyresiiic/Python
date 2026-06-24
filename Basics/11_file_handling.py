# working with files (reading and writing)

# In Python, we can easily create, write to, and read from text files.

# 1. Writing to a file
# The "w" mode means "write". If the file doesn't exist, Python creates it.
# Warning: "w" will overwrite any existing content in the file!
print("Writing data to a file called 'my_notes.txt'...")
file = open("my_notes.txt", "w")
file.write("Hello! This is my first text file created by Python.\n")
file.write("Learning to code is fun!\n")
file.close() # Always remember to close the file when you're done!

# 2. Reading from a file
# The "r" mode means "read".
print("\nNow reading data back from the file:")
file = open("my_notes.txt", "r")
content = file.read()
print(content)
file.close()

# 3. A safer way to handle files using 'with'
# The 'with' keyword automatically closes the file for us when the block is finished,
# even if an error happens! This is the recommended way to handle files.
print("--- Using the 'with' keyword to append data ---")

# The "a" mode means "append" (add to the end without overwriting)
with open("my_notes.txt", "a") as file:
    file.write("P.S. Python handles files very easily!\n")

# Read it one more time to see the added line
with open("my_notes.txt", "r") as file:
    updated_content = file.read()
    print("Updated file contents:\n" + updated_content)
