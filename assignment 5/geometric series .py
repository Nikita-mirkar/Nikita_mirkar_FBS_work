num = int(input("Enter the number: "))
sum = 0
term = 1
for i in range(num):
    sum += term
    term *=2
print(term)