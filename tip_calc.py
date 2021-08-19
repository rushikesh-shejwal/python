print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill :- "))
tip = int(input("What percentage tip would you like to give '10, 12, 15' :- "))
split= int(input("How many people to split the bill :- "))
pay = (total_bill*(tip/100)+total_bill)/split
print(f"Each person should pay :- {round(pay,2)}")