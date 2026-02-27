list1 = []
list2 = []
list3 = []
num = int(input("Enter the number: "))
for i in range(num):
    list1.append(i)
    list2.append(i ** 2)
    list3.append(i ** 3)
print("data:",list1)
print("squares:",list2)
print("cubes:",list3)