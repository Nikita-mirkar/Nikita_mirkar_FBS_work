def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact


def sum_Fact(n):
    sum = 0
    for i in range(1,n+1):
        sum += fact(i)
    return sum

n = int(input("Enter the number: "))
result = sum_Fact(n)
print(result)

