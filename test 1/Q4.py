side = int(input("Enter the side :"))
cost_int = int(input("Enter the cost of interior :"))
cost_ext = int(input("Enter the cost of exterior :"))

totalarea = 4 * side *side
totalcost = totalarea * cost_int + totalarea * cost_ext
print("total cost of paining 2 room :RS ",2*totalcost)
