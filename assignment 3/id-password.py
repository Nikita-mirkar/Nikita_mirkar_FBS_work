import random 

userid = input("Enter userid :")
Pass1 = input("Enter password :")

if(userid == "Nikita" and Pass1 == "Nikita123"):
    captch = random.randint(1000,9999)
    print("captch :", captch)
    user_captch = input("Enter the captch:")
    print("captch:", user_captch)
    if(user_captch == captch):
        print("it is correct successful login")
    else:
        print("it is login is fail.")

