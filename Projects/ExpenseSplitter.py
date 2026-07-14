# Project: Expense Splitter
# This project uses Classes, Dictionaries, and Loops to split expenses among group members!
# Features: Add members, log expenses, view balances, see who owes whom, and settle debts.

class Expense:
    """Represents a single expense entry."""
    def __init__(self, description, amount, paid_by, split_among):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.split_among = split_among  # List of member names
        self.per_person = amount / len(split_among)


class ExpenseSplitter:
    """Manages a group of members and their shared expenses."""
    def __init__(self, project_name):
        self.project_name = project_name
        self.members = []
        self.expenses = []

    # ---- Member Management ----

    def add_member(self):
        name = input("\nEnter member name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        if name in self.members:
            print(f"'{name}' is already a member.")
        else:
            self.members.append(name)
            print(f"'{name}' added to the group.")

    def view_members(self):
        if not self.members:
            print("\nNo members yet. Add some first!")
        else:
            print(f"\n--- Members of '{self.project_name}' ---")
            for i, member in enumerate(self.members, 1):
                print(f"  {i}. {member}")

    # ---- Expense Logging ----

    def add_expense(self):
        if len(self.members) < 2:
            print("\nYou need at least 2 members to split an expense.")
            return

        description = input("\nExpense description: ").strip()
        if not description:
            print("Description cannot be empty.")
            return

        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        # Who paid?
        print("\nWho paid?")
        for i, member in enumerate(self.members, 1):
            print(f"  {i}. {member}")
        try:
            payer_idx = int(input("Enter number: ")) - 1
            if not (0 <= payer_idx < len(self.members)):
                print("Invalid selection.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return
        paid_by = self.members[payer_idx]

        # Split among whom?
        print("\nSplit among whom?")
        print("  0. Everyone")
        for i, member in enumerate(self.members, 1):
            print(f"  {i}. {member}")
        selection = input("Enter numbers separated by commas (e.g. 1,3) or 0 for all: ").strip()

        if selection == "0":
            split_among = list(self.members)
        else:
            try:
                indices = [int(x.strip()) - 1 for x in selection.split(",")]
                split_among = []
                for idx in indices:
                    if 0 <= idx < len(self.members):
                        if self.members[idx] not in split_among:
                            split_among.append(self.members[idx])
                    else:
                        print(f"Skipping invalid number: {idx + 1}")
                if not split_among:
                    print("No valid members selected.")
                    return
            except ValueError:
                print("Invalid input. Use comma-separated numbers.")
                return

        expense = Expense(description, amount, paid_by, split_among)
        self.expenses.append(expense)
        print(f"\nExpense added: '{description}' — ₹{amount:.2f} paid by {paid_by}")
        print(f"  Split among {len(split_among)} member(s): ₹{expense.per_person:.2f} each")

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return

        print(f"\n--- All Expenses for '{self.project_name}' ---")
        total = 0
        for i, exp in enumerate(self.expenses, 1):
            total += exp.amount
            split_names = ", ".join(exp.split_among)
            print(f"  {i}. {exp.description.ljust(20)} | ₹{exp.amount:>9.2f} | Paid by: {exp.paid_by}")
            print(f"     Split among: {split_names} (₹{exp.per_person:.2f} each)")
        print(f"\n  Total Expenses: ₹{total:.2f}")

    # ---- Balance Calculations ----

    def _calculate_balances(self):
        """Returns a dict: {member: net_balance} where positive = owed money, negative = owes money."""
        balances = {member: 0.0 for member in self.members}
        for exp in self.expenses:
            # The payer is credited
            balances[exp.paid_by] += exp.amount
            # Everyone in the split is debited their share
            for person in exp.split_among:
                balances[person] -= exp.per_person
        return balances

    def view_balances(self):
        if not self.expenses:
            print("\nNo expenses to calculate balances from.")
            return

        balances = self._calculate_balances()
        print(f"\n--- Net Balances ---")
        for member, balance in balances.items():
            if balance > 0.005:
                print(f"  {member.ljust(15)} gets back  ₹{balance:.2f}")
            elif balance < -0.005:
                print(f"  {member.ljust(15)} owes       ₹{abs(balance):.2f}")
            else:
                print(f"  {member.ljust(15)} is settled up ✓")

    def view_settlements(self):
        """Uses a greedy algorithm to minimize the number of transactions needed to settle all debts."""
        if not self.expenses:
            print("\nNo expenses to settle.")
            return

        balances = self._calculate_balances()

        # Separate into debtors (owe money) and creditors (are owed money)
        debtors = []   # (name, amount_they_owe)  — positive values
        creditors = []  # (name, amount_owed_to_them) — positive values

        for member, balance in balances.items():
            if balance < -0.005:
                debtors.append([member, -balance])
            elif balance > 0.005:
                creditors.append([member, balance])

        if not debtors and not creditors:
            print("\nEveryone is settled up! No payments needed. ✓")
            return

        # Greedy settlement
        settlements = []
        i, j = 0, 0
        while i < len(debtors) and j < len(creditors):
            debtor_name, debt = debtors[i]
            creditor_name, credit = creditors[j]
            transfer = min(debt, credit)
            settlements.append((debtor_name, creditor_name, transfer))
            debtors[i][1] -= transfer
            creditors[j][1] -= transfer
            if debtors[i][1] < 0.005:
                i += 1
            if creditors[j][1] < 0.005:
                j += 1

        print(f"\n--- Suggested Settlements ---")
        for debtor, creditor, amount in settlements:
            print(f"  {debtor}  ──►  pays ₹{amount:.2f}  ──►  {creditor}")
        print(f"\n  ({len(settlements)} transaction(s) needed to settle all debts)")

    # ---- Expense Removal ----

    def remove_expense(self):
        self.view_expenses()
        if not self.expenses:
            return
        try:
            num = int(input("\nEnter expense number to remove: "))
            if 1 <= num <= len(self.expenses):
                removed = self.expenses.pop(num - 1)
                print(f"Removed expense: '{removed.description}'")
            else:
                print("Invalid expense number.")
        except ValueError:
            print("Please enter a valid number.")


# ---- Main Menu ----

def display_menu():
    print("\n╔══════════════════════════════════╗")
    print("║     💰 Expense Splitter 💰       ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Add a Member                ║")
    print("║  2. View Members                ║")
    print("║  3. Add an Expense              ║")
    print("║  4. View All Expenses            ║")
    print("║  5. View Balances               ║")
    print("║  6. View Settlements (Who Pays?) ║")
    print("║  7. Remove an Expense            ║")
    print("║  8. Exit                         ║")
    print("╚══════════════════════════════════╝")


def main():
    project_name = input("Enter project/group name: ").strip()
    if not project_name:
        project_name = "My Project"

    splitter = ExpenseSplitter(project_name)
    print(f"\n🎉 Expense Splitter ready for '{project_name}'!")

    while True:
        display_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            splitter.add_member()
        elif choice == "2":
            splitter.view_members()
        elif choice == "3":
            splitter.add_expense()
        elif choice == "4":
            splitter.view_expenses()
        elif choice == "5":
            splitter.view_balances()
        elif choice == "6":
            splitter.view_settlements()
        elif choice == "7":
            splitter.remove_expense()
        elif choice == "8":
            print(f"\nGoodbye! All expenses for '{project_name}' cleared. 👋")
            break
        else:
            print("Invalid choice. Please select between 1 and 8.")


if __name__ == "__main__":
    main()
