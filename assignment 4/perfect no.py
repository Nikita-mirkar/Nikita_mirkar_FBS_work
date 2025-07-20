num = int(input("Enter the num: "))
sum =0
for i in range(1 , num):
    if(num % i==0 ):
        sum += i
        print(sum)
if(sum == num):
    print("perfect number")
else:
    print("not perfect number")