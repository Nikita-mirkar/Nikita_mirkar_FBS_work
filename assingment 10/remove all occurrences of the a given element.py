data = [1,2,3,2,1,5,4,7]
x = int(input("Enter the number: "))
new_list = []
for i in data:
    if x != i:
        new_list.append(i)
print(new_list)
        