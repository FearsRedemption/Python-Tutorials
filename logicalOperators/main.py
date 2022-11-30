temp = 40
sunny = True

# if temp > 0 and temp < 30:
if 0 < temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")

if temp <= 0 or temp >= 30:
    print("The temperature is good")
else:
    print("The temperature is bad")

if not sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")
