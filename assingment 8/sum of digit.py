def sum_digit(num):
    count = 0
    sum = 0
    while (num > 0):
        num = num // 10
        count += 1
        sum = sum + count
    return sum
num = int(input("enter the number: "))
print(sum_digit(num))




