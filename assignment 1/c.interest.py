p = int(input("Enter principle amount:"))
rate = float(input("Enter rate of interest:"))
n = int(input("Enter number of times interest:"))
t = int(input("Enter no of year:"))

interest = p*(1+(rate/n)**(n*t))
print("compound interest",interest)