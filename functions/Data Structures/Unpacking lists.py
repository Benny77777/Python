numbers = [1,2,3]
first,second,Third = numbers
print(first)
print(second)
print(Third)
numbers = [1,4,5,7,2,9,8,20]
first,second,*Others = numbers
print(first)
print(second)
print(Others)
print(*Others)

first,*Other,last = numbers
print(first,last)
print(Other)



first = numbers[0]
Second = numbers[1]
Third = numbers[2]


def multiply(*numbers):
    mult = 1
    for number in numbers:
     mult*=number
    return mult
print(multiply(1,2,3,4))