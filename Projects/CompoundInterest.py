# Project: Compound Interest Calculator

def calculate_compound_interest(principal, rate, times_compounded, years):
    # The formula for compound interest is:
    # A = P(1 + r/n)^(nt)
    # A = final amount
    # P = principal (initial money)
    # r = annual interest rate (as a decimal)
    # n = number of times interest is compounded per year
    # t = time (years)
    
    # First, convert the percentage rate to a decimal
    decimal_rate = rate / 100
    
    # Calculate the final amount using the formula
    # Remember: ** is used for exponents (powers) in Python
    amount = principal * (1 + decimal_rate / times_compounded) ** (times_compounded * years)
    
    return amount

print("--- Compound Interest Calculator ---")
print("Let's see how money grows over time!\n")

# Let's set up a scenario
initial_investment = 1000  # $1,000
interest_rate = 5          # 5% annual return
compounded = 12            # Compounded monthly (12 times a year)
time_in_years = 10         # Leaving it for 10 years

final_value = calculate_compound_interest(initial_investment, interest_rate, compounded, time_in_years)

# Calculate how much of that is purely profit (interest earned)
interest_earned = final_value - initial_investment

print(f"Initial Investment: ${initial_investment}")
print(f"Interest Rate:      {interest_rate}%")
print(f"Time:               {time_in_years} years\n")

print(f"Total Final Value:  ${final_value:.2f}")
print(f"Total Profit:       ${interest_earned:.2f}")
