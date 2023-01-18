# --- Name While Loop Example ---
# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name >:( ")
#     name = input("Enter your name: ")
#
# print(f"Hello {name}")

# --- Age While Loop Example ---
# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Your age cannot be negative...")
#     age = int(input("Enter your age: "))
#
# print(f"You are {age} years old")

# --- While (not) Loop Example ---
# food = input("Enter a food you like (q to quit): ")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
#
# print("bye")

num = int(input("Enter a number between 1 thru 10: "))

while num < 1 or num > 10:
    print(f"{num} is invalid")
    num = int(input("Try again, enter a number between 1 thru 10: "))

print(f"Your number is {num}")
