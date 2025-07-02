# find the sum of the three digit no

num =int(input("Enter the num : "))
a = num %10
num = num // 10
b = num %10
c = num//10

sum = a+b+c

print("sum of three digit no:",sum)
print("a :",a)