weight = float(input("Enter your weight here :- "))
height = float(input("Enter your hight here :- "))
bmi= round(weight/height**2)
print("Hello World")
if bmi<=18.5:
    print(f"Your BMI is {bmi}, You are Underweight")
elif bmi>18.5:
    if bmi<25:
        print(f"Your BMI is {bmi}, You have a normal weight")
elif bmi>25:
    if bmi<30:
        print(f"Your BMI is {bmi}, You are OverWeight")
elif bmi>30:
    if bmi<35:
        print(f"Your BMI is {bmi}, You are Obese")
else:
    print(f"Your BMI is {bmi}, You are clinically Obese")
