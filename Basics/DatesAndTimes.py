# working with dates and times

# Python has a built-in module called 'datetime' to help us work with dates and times.
import datetime

print("--- Getting the current date and time ---")
# Get the current date and time right now
now = datetime.datetime.now()
print("Right now it is:", now)

print("\n--- Getting specific parts of the date ---")
# We can pull out just the year, month, or day
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print("\n--- Formatting dates to look nice ---")
# We can use the strftime() method to format the date exactly how we want it!
# %Y = Year, %m = Month, %d = Day
# %H = Hour, %M = Minute, %S = Second
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Nicely formatted date:", formatted_date)

# Another example format
friendly_date = now.strftime("%A, %B %d, %Y")
print("Friendly format:", friendly_date)

print("\n--- Creating a specific date ---")
# We can create a specific date in the past or future
new_years_2030 = datetime.datetime(2030, 1, 1)
print("New Year's Day 2030 is on a:", new_years_2030.strftime("%A"))
