#WAP to calculate total salary of employee based on basic, da=10% of basic,
#ta=12% of basic, hra=15% of basic.
basic_salary = int(input("Enter the basic salary of employee: "))

da = 0.10 * basic_salary 
ta = 0.12 * basic_salary
hra = 0.15 * basic_salary
# total salary formula

total_salary = basic_salary + da + ta + hra
print("total salary of emplyee: ", total_salary )