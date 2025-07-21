num = int(input("Enter the num: "))
temp = num
count = 0
while(num != 0):
    a = num % 10
    num = num // 10
    count += 1

print(count)
num = temp
sum = 0

while(num != 0):
    a = num % 10
    num = num // 10
    sum = sum + ( a ** count)
if(sum == temp):
    print("yes, it is amstrong.")
else:
    print("no , not amstrong")