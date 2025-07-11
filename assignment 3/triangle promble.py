side1 = int(input("Enter the first side :"))
side2 = int(input("Enter the second side :"))
side3 = int(input("Enter the third side : "))

if(side1==side2==side3):
    print("It is a equilateral triangle ")
elif(side1==side2 and side2 ==side3 ):
    print("It is a isosceles triangle ")
else:
    print("It is a scalene triangle ")