email = input("Enter your email: ")

# index = email.index("@")
# username = email[:index]
# domain = email[index + 1:]

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username}")
print(f"The domain is {domain}")
