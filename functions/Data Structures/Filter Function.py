
items = [
    ("product1",10),
    ("product2", 89),
    ("product3", 23)
]
filtered = list(filter(lambda item: item[1] >= 10,items))
print(filtered)