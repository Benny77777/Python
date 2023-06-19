def greet(name):
    print("Hi there")
    print(f"{name}")
    print("Welcome aboard")
n = input("Enter Your name: ")
greet(n)
def Add(a,b):
    sum = a+b
    return sum
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
result = Add(num1,num2)
print(num1,"+", num2,"=",result)


def grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B+"
    elif mark >= 60:
        return "B"
    elif mark >= 55:
        return "C+"
    elif mark >= 50:
        return "C"
    elif mark < 50:
        return "F"


m = float(input("Enter the marks"))
print(grade(m))