def get_exchange_rates():
    """Returns exchange rates relative to 1 INR (Indian Rupee)."""
    rates = {
        "INR": 1.0,
        "USD": 0.012,
        "EUR": 0.011,
        "GBP": 0.0094,
        "JPY": 1.82,
        "AUD": 0.019,
        "CAD": 0.016,
        "CNY": 0.087,
        "AED": 0.044,
        "BDT": 1.44,
    }
    return rates

def show_menu():
    print("\n--- Currency Converter ---")
    print("1. Convert Currency")
    print("2. View Available Currencies")
    print("3. View Exchange Rates (Base: INR)")
    print("4. Add a Custom Currency")
    print("5. Exit")

def show_currencies(rates):
    print("\n--- Available Currencies ---")
    for i, code in enumerate(rates, 1):
        print(f"  {i}. {code}")
    print(f"\nTotal: {len(rates)} currencies")

def show_rates(rates):
    print("\n--- Exchange Rates (1 INR = ?) ---")
    for code, rate in rates.items():
        if code == "INR":
            continue
        print(f"  1 INR = {rate} {code}")

def convert_currency(rates):
    print("\nAvailable currencies:", ", ".join(rates.keys()))

    source = input("\nEnter source currency code: ").upper().strip()
    if source not in rates:
        print(f"'{source}' is not available!")
        return

    target = input("Enter target currency code: ").upper().strip()
    if target not in rates:
        print(f"'{target}' is not available!")
        return

    if source == target:
        print("Source and target are the same!")
        return

    try:
        amount = float(input(f"Enter amount in {source}: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    amount_in_inr = amount / rates[source]
    converted = amount_in_inr * rates[target]

    print(f"\n--- Result ---")
    print(f"  {amount:.2f} {source} = {converted:.2f} {target}")
    print(f"  (Rate: 1 {source} = {rates[target] / rates[source]:.6f} {target})")

def add_currency(rates):
    code = input("\nEnter new currency code (e.g., KRW): ").upper().strip()

    if not code.isalpha() or len(code) != 3:
        print("Currency code must be exactly 3 letters!")
        return

    if code in rates:
        print(f"'{code}' already exists!")
        return

    try:
        rate = float(input(f"Enter how much 1 INR equals in {code}: "))
        if rate <= 0:
            print("Rate must be positive!")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    rates[code] = rate
    print(f"\n'{code}' added! (1 INR = {rate} {code})")

def main():
    rates = get_exchange_rates()

    print("Welcome to the Currency Converter!")
    print("Note: Exchange rates are approximate and for learning purposes.")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            convert_currency(rates)
        elif choice == "2":
            show_currencies(rates)
        elif choice == "3":
            show_rates(rates)
        elif choice == "4":
            add_currency(rates)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Pick 1-5.")

if __name__ == "__main__":
    main()
