num = int(input("Enter the digit no : "))
a = num%10
num = num//10
b = num%10
reverse = (a*10)+b
c = num//10
reverse =(reverse * 10)+c
print("reverse no:",reverse)
