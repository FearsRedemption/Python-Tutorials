# Explicit type casting
name = "Chris"
age = 35
gpa = 3.5
student = False

print(type(name))

# age = float(age)
# print(type(age))
# gpa = int(gpa)
# print(gpa)
# student = str(student)
# print(student)

# If someone types in their username it'll be true, but if they leave it empty it'll be false
name = bool(name)
print(name)

# Implicit type casting
x = 2
y = 2.0
x = x / y
print(x)
