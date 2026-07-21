import datetime

print("--- Getting the current date and time ---")
now = datetime.datetime.now()
print("Right now it is:", now)

print("\n--- Getting specific parts of the date ---")
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print("\n--- Formatting dates to look nice ---")
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Nicely formatted date:", formatted_date)

friendly_date = now.strftime("%A, %B %d, %Y")
print("Friendly format:", friendly_date)

print("\n--- Creating a specific date ---")
new_years_2030 = datetime.datetime(2030, 1, 1)
print("New Year's Day 2030 is on a:", new_years_2030.strftime("%A"))
