def display_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(tasks):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{index + 1}. {status} {task['name']}")

def add_task(tasks):
    task_name = input("\nEnter the task: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully!")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed['name']}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['name']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    main()
