def sum_of_no(num):
    if(num == 0):
        return 0
    else:
        return num + sum_of_no(num -1)
num = int(input("enter the number: "))
result = sum_of_no(num)
print(result)