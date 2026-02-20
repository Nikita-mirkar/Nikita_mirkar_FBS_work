def palindrome(num):
    temp = num
    reverse = 0
    while (temp > 0):
        a = temp% 10
        reverse = (reverse * 10) + a
        temp = temp // 10
    if(num == reverse):
        print("it is a palindrome number: ")
    else:
        print("it is not palindrome number: ")

num = int(input("Enter the number: "))
result = palindrome(num)
print(result)
