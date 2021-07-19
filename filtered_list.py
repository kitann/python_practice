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
prices = list(map(lambda item: item[1], items))
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)