num = int(input("Enter the number: "))
data = []
for i in range(num):
    data.append(i)

even = []
odd = []
for x in data:
    if(x % 2 == 0):
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)
    
