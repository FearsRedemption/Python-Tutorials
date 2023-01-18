principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = int(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be 0 or negative number")

while rate <= 0:
    rate = int(input("Enter the interest rate amount: "))
    if rate <= 0:
        print("Interest rate cannot be 0 or negative number")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time cannot be 0 or negative number")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year(s): ${total:.2f}")
