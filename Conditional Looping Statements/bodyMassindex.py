weight=float(input("Enter your weight: "))
height=float(input("Enter your height: "))

bmi=weight/(height**2)

if bmi<=18.5:
    print(f"Your bmi is {bmi}")
    print("You are in the 'underweight' range")
elif bmi>=18.5 and bmi<=24.9:
    print(f"Your bmi is {bmi}")
    print("You are in the 'normal' range.")
elif bmi>=25 and bmi<=29.9:
    print(f"Your bmi is {bmi}")
    print("You are in the 'overweight' range.")
else:
    print(f"Your bmi is {bmi}")
    print("You are in the 'obese' range.")