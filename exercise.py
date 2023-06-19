"""My_List = input("Enter a list of strings: ").split(",")
for i in range (len(My_List)):
    for j in range (i+1,len(My_List)):
        if My_List[i] > My_List[j]:
            My_List[i], My_List[j] = My_List[j], My_List[i]
print(My_List)"""
a = 10
b = 11
print(a>=b)
mark = float(input("Enter a mark"))
"""mark >= 80):
    print("A")
if(mark >= 70 and mark < 80):
    print("B+")
if(mark >= 60 and mark < 70):
    print("B")
if(mark >= 55 and mark < 60):
    print("C+")
if(mark >= 50 and mark < 55):
    print("C")
if(mark < 50):
    print("F")"""
if(mark >= 80):
    print("A")
elif(mark >= 70):
    print("B+")
elif(mark >= 60):
    print("B")
elif(mark >= 55):
    print("C+")
elif(mark >= 50):
    print("C")
elif(mark < 50):
    print("F")
else:
    print("F")