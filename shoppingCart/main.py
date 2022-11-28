item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
qty = int(input("How many would you like? "))

total = price * qty
print(f"You have bought {qty} x {item}(s)")
print(f"Your total is: ${round(total, 2)}")
