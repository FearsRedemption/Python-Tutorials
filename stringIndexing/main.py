# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step ]

creditCard = "1234-5678-9012-3456"

print(creditCard[4])
# this will show the '-'

print(creditCard[0:4])
# this will show "1234"
# [:4] will work as well since python assumes the starting number is 0

print(creditCard[5:9])
# this will output "5678"

print(creditCard[5:])
# this will output "5678-9012-3456"
# having the end sequence empty python will assume you mean the last index

print(creditCard[-1])
# this will go backwards and output the final '6'

print(creditCard[::3])
# this will print every 3rd character in the string

# Exercises
lastDigits = creditCard[-4:]
print(f"XXXX-XXXX-XXXX-{lastDigits}")

# To reverse a string set step -1
creditCard = creditCard[::-1]
print(creditCard)
