data = [10,20,12,34,20,12,45]
x = int(input("Enter the num: "))
count = 0
for i in range(len(data)):
    if data[i] == x:
        count += 1

if count > 0:
    print("Element is present")
    print("it appears",count,"times")
else:
    print("element it not present")
    