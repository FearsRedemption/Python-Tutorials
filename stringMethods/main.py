name = input("Enter your full name: ")

# To find a length of a string
# result = len(name)

# Find the first position of a character
# result = name.find(" ")
# Type "John Snow" it returns index 4

# Reverse Find, find the last occurrence of given character
# result = name.rfind("o")
# Type "John Snow" it returns index 7
# Returns -1 if no results

# Capitalize the first letter
# result = name.capitalize()
# Type "john snow" it returns "John snow"

# Uppercase all letters
# result = name.upper()

# Lowercase all letters
# result = name.lower()

# Check if ONLY digits in the string
# result = name.isdigit()
# 123 will return True, Bro123, abcdef, and 123abc will return False

# Check if ONLY alpha characters in the string
# result = name.isalpha()
# abc will return True, but Bro123, 123456, and 123abc will return False

# phoneNumber = input("Enter your phone number (XXX-XXX-XXXX): ")
# result = phoneNumber.count("-")
# if you type 1-123-456-7890 will return 3

# phoneNumber = input("Enter your phone number (XXX-XXX-XXXX): ")
# result = phoneNumber.replace("-", " ")
# if given "1-234-567-8901" it will return "1 234 567 8901"

# For a more extensive list of methods for strings you can do the following
print(help(str))
