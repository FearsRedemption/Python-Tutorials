# Arithmetic Operators

# friends = 10
# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 3
# print(friends)
# print(remainder)


# Built-In Math Functions
x = 3.14
y = 4
z = 5
print(round(x))
print(abs(-y))
print(pow(y, 3))
print(max(x, y, z))

# Math Module
import math

print(math.pi)
print(math.e)
print(math.sqrt(64))
print(math.ceil(9.8))

# Circumference of a circle exercise
radius = float(input("Enter the radius of a circle: "))
circum = 2 * math.pi * radius

print(f"The circumference is {round(circum, 2)}cm")

# Area of a circle exercise
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)

print(f"The area of your circle is {round(area, 2)}cm^2")

# Hypotenuse

a = float(input("Enter side A size: "))
b = float(input("Enter side B size: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C is {c}")
