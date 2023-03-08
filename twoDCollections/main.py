# This works with lists, sets, and tuples
groceries = [
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"]
]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

keypad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)

for row in keypad:
    for num in row:
        print(num, end=" ")
    print()
