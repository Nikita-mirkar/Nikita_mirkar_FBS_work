#WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter the no:"))
discount = float(input("Enter the no:"))
#cost price formula
discount_amount = (discount / 100) * cost_price

# selling price formule
selling_price = cost_price - discount_amount
print("selling price of the book:",selling_price )
