# Project: Expense Splitter (Beginner Level)
# Split expenses easily among friends!
# Uses: Lists, Dictionaries, Loops, Functions, Input/Output

def show_menu():
    print("\n--- Expense Splitter ---")
    print("1. Add a Member")
    print("2. Add an Expense")
    print("3. View All Expenses")
    print("4. View Balances")
    print("5. Exit")

def add_member(members):
    name = input("\nEnter member name: ")
    if name in members:
        print(f"'{name}' is already added!")
    else:
        members.append(name)
        print(f"'{name}' added!")

def add_expense(members, expenses):
    if len(members) < 2:
        print("\nAdd at least 2 members first!")
        return

    item = input("\nWhat was the expense for? ")

    try:
        amount = float(input("How much was it? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Who paid?
    print("\nWho paid?")
    for i, name in enumerate(members, 1):
        print(f"  {i}. {name}")

    try:
        choice = int(input("Enter number: "))
        paid_by = members[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    # Split equally among everyone
    split = amount / len(members)
    expenses.append({"item": item, "amount": amount, "paid_by": paid_by, "split": split})
    print(f"\n'{item}' - Rs.{amount:.2f} paid by {paid_by}")
    print(f"Each person's share: Rs.{split:.2f}")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses yet!")
        return

    print("\n--- All Expenses ---")
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"  {i}. {exp['item']} - Rs.{exp['amount']:.2f} (Paid by: {exp['paid_by']})")
        total += exp["amount"]
    print(f"\nTotal: Rs.{total:.2f}")

def view_balances(members, expenses):
    if not expenses:
        print("\nNo expenses to show!")
        return

    # Calculate how much each person owes or is owed
    balances = {}
    for name in members:
        balances[name] = 0.0

    for exp in expenses:
        balances[exp["paid_by"]] += exp["amount"]  # Payer gets credit
        for name in members:
            balances[name] -= exp["split"]  # Everyone pays their share

    print("\n--- Balances ---")
    for name in members:
        if balances[name] > 0:
            print(f"  {name} gets back Rs.{balances[name]:.2f}")
        elif balances[name] < 0:
            print(f"  {name} owes Rs.{abs(balances[name]):.2f}")
        else:
            print(f"  {name} is settled!")

def main():
    members = []
    expenses = []

    print("Welcome to the Expense Splitter!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_member(members)
        elif choice == "2":
            add_expense(members, expenses)
        elif choice == "3":
            view_expenses(expenses)
        elif choice == "4":
            view_balances(members, expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Pick 1-5.")

if __name__ == "__main__":
    main()
