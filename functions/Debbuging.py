def multiply(*numbers):
    total = 1
    for number in numbers:
        #print(number)
        total *=number
    return total
print("Start")
print(multiply(1,2,3))