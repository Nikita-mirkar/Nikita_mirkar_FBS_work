 
start = int(input("Enter the start num: "))
stop = int(input("Enter the stop num: "))

for i in range(start, stop):
    temp = i
    num = i  
    count = 0
    sum = 0
    
    while num != 0:
        a = num % 10
        num = num // 10
        count += 1

    num = i  

    
    while num != 0:
        a = num % 10
        sum += a ** count
        num = num // 10

    
    if sum == temp:
        print(temp)
