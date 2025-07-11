s1 = int(input("Enter the s1 :"))
s2 = int(input("Enter the s2 :"))
s3 = int(input("Enter the s3 :"))
s4 = int(input("Enter the s4 :"))
s5 = int(input("Enter the s5 :"))
total_sub = s1 + s2 + s3 + s4 +s5
total_marks = 500
per = total_sub /total_marks * 100
print("per :", per)

if(per >= 80 and per <=100):
    print("first class and distanction ")
elif(per >= 70 and per < 80):
    print("first class ")
elif(per >=60 and per < 70):
    print("highter first class ")
elif(per >=40 and per < 60):
    print("second class ")
elif(per < 40 and per >=0):
    print("fail")
else:
    print("wrong input ")