class BankAccount:

    def __init__(self, owner_name):
        self.owner = owner_name
        self.balance = 0.0
        print(f"Account created for {self.owner}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("You must deposit an amount greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal denied! Insufficient funds. Balance is only ${self.balance:.2f}")
        elif amount <= 0:
            print("You must withdraw an amount greater than 0.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"{self.owner}'s Account Balance: ${self.balance:.2f}")


print("--- Starting the Simulation ---\n")

alice_account = BankAccount("Alice")
bob_account = BankAccount("Bob")

print("\n--- Alice's Transactions ---")
alice_account.deposit(150.00)
alice_account.withdraw(50.00)
alice_account.withdraw(200.00)

print("\n--- Bob's Transactions ---")
bob_account.deposit(500.00)
bob_account.withdraw(125.50)

print("\n--- Final Balances ---")
alice_account.check_balance()
bob_account.check_balance()
