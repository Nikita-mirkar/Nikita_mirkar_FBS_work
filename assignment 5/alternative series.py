x = int(input("Enter the number: "))
num = int(input("Enter the number: "))
sum = 0
for i in range(1, num+1):
    sign = (-1) ** (i + 1)
    term = sign * (x ** i) / (2 * i - 1)
    sum += term
print(sum)