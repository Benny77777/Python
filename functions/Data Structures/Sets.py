numbers = [1,2,3,7,8]
uniques = set(numbers)
print(uniques)
second = {1,4}
second.add(9)#second.remove(7)
print(second)


first = uniques
second = {1,5}
union = first | second
print(union)
intersection = first & second
print(intersection)
difference = first - second
print(difference)
symmetric = first ^ second
print(symmetric)

if 10 in second:
    print("Yes")
else:
    print("not present")
