def sum_prime(n):
    sum = 0
    for i in range(2,n+1):
        prime = True
        for j in range(2,i):
            if(i % j == 0):
                prime = False
        if prime:
            sum += i

    return sum
n = int(input("Enter the number: "))
print(sum_prime(n))



        


    

