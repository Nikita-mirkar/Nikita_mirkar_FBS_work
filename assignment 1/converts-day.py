#to convert days into years, weeks,and days

days = int(input("Enter the no of days: "))
years = days//365
days = days%365
week = days//7
days = days%7
# print("years:",years)
# print("week:",week)
# print("days",days)
print("years:",years,"week:",week,"days:",days)
