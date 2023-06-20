a=int(input("enter a"))
b = int(input("enter b"))
sum=a+b
print("the result is",sum)
for i in range(10):
    print(i)
for i in range(1,11,1):
    print(i,"square=",i**2)
for book in range(1,11,1):
    for page in range(1,21,1):
        print ("book",book,"page",page)

for i in range(1,13,1):
    for j in range(1,13,1):
        print(i,"*",j,"=",i*j)
count = 1
while(count<11):
    print(count)
    count = count + 1
number = 7
while(number>5):
    number = int(input("Enter number less than 5"))
print(number)
''
age  =int(input("Enter the age:"))
if age<18:
    print("you are a teen")
else:
    print("adult hood will show you stars")
a = int(input("a = :"))
b = int(input("b = :"))
c = int(input("c = :"))
if(a>b and a> c):
    print("a is the biggest number")
elif(b>a and b>c):
    print("b is the biggest number")
else:
    print("c is the biggest number")

if a>b:
    if a>c:
        print("biggest number is",a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
        print(c)
