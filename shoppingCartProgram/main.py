# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("What food would you like (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food.capitalize())

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")
