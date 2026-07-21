def calculate_compound_interest(principal, rate, times_compounded, years):

    decimal_rate = rate / 100

    amount = principal * (1 + decimal_rate / times_compounded) ** (times_compounded * years)

    return amount

print("--- Compound Interest Calculator ---")
print("Let's see how money grows over time!\n")

initial_investment = 1000
interest_rate = 5
compounded = 12
time_in_years = 10

final_value = calculate_compound_interest(initial_investment, interest_rate, compounded, time_in_years)

interest_earned = final_value - initial_investment

print(f"Initial Investment: ${initial_investment}")
print(f"Interest Rate:      {interest_rate}%")
print(f"Time:               {time_in_years} years\n")

print(f"Total Final Value:  ${final_value:.2f}")
print(f"Total Profit:       ${interest_earned:.2f}")
