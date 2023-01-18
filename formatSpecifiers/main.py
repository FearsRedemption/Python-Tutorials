# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive value
# := = place a sign to leftmost positive
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 123456789.90

print(f"Price 1 is ${price1:.3f}")
# output: 3.142
print(f"Price 2 is ${price2:.3f}")
# output -987.650
print(f"Price 3 is ${price3:.3f}")
# output 12.340

print(f"Price 1 is ${price1:10}")
# output: $   3.14159
print(f"Price 2 is ${price2:<10}")
# output $-987.65
print(f"Price 3 is ${price3:<010}")
# output $12.3400000
print(f"Price 3 is ${price3:>10}")
# output $     12.34
print(f"Price 3 is ${price3:^010}")
# output $0012.34000

print(f"Price 2 is ${price2:+}")
# output $-987.65
print(f"Price 3 is ${price3:+}")
# output $+12.34

print(f"Price 1 is ${price4:,}")
# output: $123,456,789.9

print(f"Price 1 is ${price4:+,.3f}")
# output: $+123,456,789.900
