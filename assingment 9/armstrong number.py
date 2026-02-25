def armstrong(num,power):
    if(num == 0):
        return 0
    else:
        digit = num % 10
        return (digit ** power) + armstrong(num // 10, power)

num = int(input("Enter the number: "))
power = len(str(num))

result = armstrong(num, power)
if (result == num):
    print("it is armstrong number")
else:
    print("it is not armstrong number")


