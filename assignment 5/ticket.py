passenger =int(input("Enter the number passenger: "))
cost_ticket = int(input("Enter the cost of ticket: "))
total_amount = 0
for i in range(1,passenger + 1):
    age = int(input("Enter the age of passenger: "))
    if(age < 12):
        discount =0.30
    elif(age >59):
        discount =0.50
    else: 
        discount =0.0
    final_cost =cost_ticket * (1-discount)
    total_amount += final_cost
print("the cost of all passerger is: ", total_amount)
    
