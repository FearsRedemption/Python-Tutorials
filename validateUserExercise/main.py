username = input("Enter a username: ")

if len(username) > 12:
    print("Username cannot be more than 12 characters long")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain numbers")
else:
    print(f"Welcome {username}")
