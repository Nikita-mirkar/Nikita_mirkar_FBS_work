start = int(input("Enter the start: "))
stop = int(input("Enter the stop: "))
for x in range(start, stop +1):
    for i in range(2, x):
        if(x % i == 0):
            break
    else:
        print(x)


    



        