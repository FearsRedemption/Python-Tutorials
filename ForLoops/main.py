for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR")

for x in range(1, 11, 2):
    print(x)

credit_card = "1234-5678-9123-4567"
for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue  # This will skip over the number 13 in this instance
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break  # This will leave the function entirely
    else:
        print(x)
