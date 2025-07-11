num = int(input("Enter the no :"))
copy = num
a = num%10
num = num//10
b = num%10
reverse = (a*10)+b
c = num//10
reverse =(reverse * 10)+c
print("reverse no:",reverse)
if(num >= 100 and num <= 999):
    print("this is a palindrome.")