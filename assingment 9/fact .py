def fact(num):
    if(num == 0) :
        return 1
    else:
        return num * fact(num -1)


def sum(num):
    if (num == 1):
        return 1
    else:
        return fact(num) + sum(num-1)

num = int(input("Enter the number: "))
result= sum(num)
print(result)