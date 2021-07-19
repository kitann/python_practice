items = [
    ("tomatoes", 23),
    ("orange", 12),
    ("apple", 45),
    ("peach", 18),
    ("avocado", 5),
    ("rice", 9),
    ("beans", 3),
    ("peanut", 15),
    ("yam", 7.3),
    ("melon", 9.95),
]

# [expression for item in items]
prices = [item[1] for item in items]
print(prices)

print(items)
filtered = [item for item in items if item[1] >= 10]
print(filtered)

filtered = [item for item in items if 'p' in item[0]]
print(filtered)