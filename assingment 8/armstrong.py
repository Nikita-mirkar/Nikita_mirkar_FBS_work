def armstrong(num):
    temp = num
    count = 0
    while (temp > 0):
        temp = temp // 10
        count += 1

    temp = num
    sum = 0
    while (temp > 0):
        a = temp % 10
        sum += a ** count
        temp = temp // 10

    if(sum == num):
        print("it is an armstrong number")
    else:
        print("it is not armstrong number")
num = int(input("Enter the number: "))
print(armstrong(num))