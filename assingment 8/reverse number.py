def reverse_no(num):
    reverse = 0
    while(num > 0):
        a = num % 10
        reverse = (reverse * 10) + a
        num = num // 10
    return reverse
num = int(input("enter the number: "))
print(reverse_no(num))