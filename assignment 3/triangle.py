side1= int(input("enter the side: "))
side2= int(input("enter the side: "))
side3= int(input("enter the side: "))

if(side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("It is valid triangle")
else:
    print("It is not valid")