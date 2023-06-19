value = []
for x in range(5):
    value.append(x*2)

values = [x*2 for x in range(5)]
print(values)
values = {x*2 for x in range(5)}#Sets
print(values)

values = {x :x*2 for x in range(5)}#dictionaries
print(values)
values = tuple(x*2 for x in range(5))
print(values)




