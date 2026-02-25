def power(m,n):
    if(n ==0):
        return 1
    else:
        return m * power(m,n-1)
m = int(input("enter the m: "))
n = int(input("Enter the n: "))
result = power(m,n)
print(result)