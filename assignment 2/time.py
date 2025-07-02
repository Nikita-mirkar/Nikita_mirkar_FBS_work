# convert the time entered in hh, min and sec into second
hours = int(input("Enter hours: "))
min = int(input("Enter min: "))
second = int(input("Enter second: "))

total_seconds = (hours * 3600) + (min * 60) + second
print("total_seconds: ",total_seconds)

# second = int(input("Enter the no of second: "))
# hours = second//3600
# second = second%3600
# min =second//60
# sec = second%60
# print("hours:",hours)
# print("min: ",min)
# print("sec: ",sec)
