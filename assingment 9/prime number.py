def prime(num,i=2):
    if(num <= 1):
        return False
    if(num == i):
        return True
    if(num % i == 0):
        return False
    return prime(num,i+1)

num = int(input("Enter the number: "))
if(prime(num)):
    print("prime number")
else:
    print('not prime number')
    