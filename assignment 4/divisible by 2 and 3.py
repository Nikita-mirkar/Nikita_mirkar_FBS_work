num = int(input("Enter the num: "))
for i in range(1 , num +1):
    if(i % 2 != 0 and i % 3 != 0):
        print(i)