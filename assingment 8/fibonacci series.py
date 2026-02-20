def fibo(n):
    a = 0
    b = 1 
    for i in range(1,n+1):
        c = a +b
        print(c)
        a = b
        b = c
n = int(input("Enter the number: "))
print(fibo(n))