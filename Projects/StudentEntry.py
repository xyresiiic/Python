import json
import os

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_students(self):
        with open(self.filename, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, roll_no, name, age, course):
        # Check if student exists
        for student in self.students:
            if student['roll_no'] == roll_no:
                print(f"Student with Roll No {roll_no} already exists!")
                return
        
        student_data = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "course": course
        }
        self.students.append(student_data)
        self.save_students()
        print(f"Student '{name}' added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n--- Student Records ---")
        print(f"{'Roll No':<10} | {'Name':<20} | {'Age':<5} | {'Course':<15}")
        print("-" * 55)
        for student in self.students:
            print(f"{student['roll_no']:<10} | {student['name']:<20} | {student['age']:<5} | {student['course']:<15}")
        print("-" * 55)

    def search_student(self, roll_no):
        for student in self.students:
            if student['roll_no'] == roll_no:
                print("\nStudent Found:")
                print(f"Roll No : {student['roll_no']}")
                print(f"Name    : {student['name']}")
                print(f"Age     : {student['age']}")
                print(f"Course  : {student['course']}")
                return
        print(f"No student found with Roll No {roll_no}.")

def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Entry System ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            roll_no = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            
            try:
                age = int(input("Enter Age: "))
            except ValueError:
                print("Invalid age! Please enter a number.")
                continue
                
            course = input("Enter Course: ")
            manager.add_student(roll_no, name, age, course)

        elif choice == '2':
            manager.view_students()

        elif choice == '3':
            roll_no = input("Enter Roll Number to search: ")
            manager.search_student(roll_no)

        elif choice == '4':
            print("Exiting Student Entry System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
