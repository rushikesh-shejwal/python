age = int(input("Enter your current Age :- "))

""" # Current age left Days, Weeks, Months
current_days = age*365
current_weeks = age*52
current_months = age*12

# Total Days, Weeks, Months in 90 years
total_days = 365*90
total_weeks = 52*90
total_months = 12*90
# Total Days, Weeks, Months You have left from your current age

left_days = total_days - current_days
left_weeks = total_weeks - current_weeks
left_months = total_months - current_months

# Now print the left Days, Weeks, Months
print(f"You have left {left_days} Days, {left_weeks} Weeks, {left_months} Months")
 """

years_left = 90 - age
days_left = years_left *365
weeks_left = years_left * 52
months_left = years_left *12
print(f"You have left {days_left} Days, {weeks_left} Weeks, {months_left} Months")
