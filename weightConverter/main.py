weight = float(input("Enter your weight: "))
unit = input("(K)ilograms or (P)ounds? (K or P): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is {round(weight, 1)}{unit}")
elif unit == "P":
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is {round(weight, 1)}{unit}")
else:
    print(f"{unit} was not a valid input")
