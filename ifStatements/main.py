# INT EXAMPLE
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")

# DOUBLE EQUALS IS COMPARISON
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food")
else:
    print("Don't have food")

# EMPTY STRING EXAMPLE
name = input("Enter your name: ")

if name == "":
    print("You didn't enter your name...")
else:
    print(f"Hello {name}")

# BOOLEAN EXAMPLE
online = True

if online:
    print("The user is ONLINE")
else:
    print("The user is OFFLINE")

