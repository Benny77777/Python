
items = [
    ("product1",10),
    ("product2", 89),
    ("product3", 23)
]

prices = list(map(lambda item:item[1],items))
print(prices)
price = [item[1] for item in items]
print(price)
filtered1 = list(filter(lambda item: item[1] >= 10,items))
filtered2 = [item for item in items if item[1]>=20]
print(filtered2)
