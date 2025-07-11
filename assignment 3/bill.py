unit = int(input("Enter the unit :"))
if(unit <= 50):
    bill = unit * 0.5
elif(unit > 50 and unit >= 150):
    bill = 50 * 0.5
    unit = unit - 50
    bill += unit * 0.75
elif(unit > 150 and unit <= 250):
    bill = 50 * 0.50
    unit = unit - 50
    bill += 100 * 0.75
    unit = unit - 100
    bill += unit * 120
else:
    bill = 50 * 0.50
    unit = unit - 50 
    bill += 100 * 0.75
    unit = unit - 100
    bill += 100 * 120
    unit = unit - 100
    bill += unit * 1.50

bill = bill+ (bill * 0.20)
print(bill)