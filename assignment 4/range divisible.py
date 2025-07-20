start = int(input("Enter the start num: "))
stop = int(input("Enter the stop num: "))
divi = int(input("Enter the divisible num: "))

for i in range(start , stop + 1):
    if(i % divi ==0):
        print(i)