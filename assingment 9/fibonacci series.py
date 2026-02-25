def fibo(a,b,num):
    if(num == 0):
        return
    else:
        print(a)
        fibo(b,a+b, num-1)
num = int(input("enter the number: "))
result = fibo(0,1,num)
print(result)
