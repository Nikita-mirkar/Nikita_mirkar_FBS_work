data = [2,3,4,7,10,20,30,40,21,24]
m = int(input("Enter the number: "))
n = int(input("Enter the number: "))
new_list = []
for i in data:
    if(i % m == 0 or i % n == 0):
        new_list.append(i)
print(new_list)
