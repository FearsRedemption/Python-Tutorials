fakeMasterCard = "5555-5555-5555-4444"

sumOdd = 0
sumEven = 0
total = 0

# Step 1
cardNumber = input("Enter a credit card number: ")
cardNumber = cardNumber.replace("-", "")
cardNumber = cardNumber.replace(" ", "")
cardNumber = cardNumber[::-1]

# Step 2
for x in cardNumber[::2]:
    sumOdd += int(x)

# Step 3
for x in cardNumber[1::2]:
    x = int(x) * 2
    if x >= 10:
        sumEven += (1 + (x % 10))
    else:
        sumEven += x

# Step 4
total = sumOdd + sumEven

# Step 5
if total % 10 == 0:
    print("Valid card")
else:
    print("Invalid card")
