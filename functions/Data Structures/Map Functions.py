
items = [
    ("product1",10),
    ("product2", 89),
    ("product3", 23)
]
prices = []
for item in items:
    prices.append(item[1])
print(prices)


x = map(lambda item:item[1],items)
for item in x:
    print(item)

prices = list(map(lambda item:item[1],items))
print(prices)
