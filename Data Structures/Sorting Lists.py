Numbers = [5,25,78,43,68,9]
Numbers.sort()
print(Numbers)
Numbers.sort(reverse = True)
print(Numbers)
print(sorted(Numbers))
print(sorted(Numbers,reverse = True))

items = [
    ("product1",10),
    ("product2", 89),
    ("product3", 23)
]

#def sort_item(item):
#    return item[1]
#items.sort(key = sort_item)

items.sort(key = lambda item:item[1])
print(items)