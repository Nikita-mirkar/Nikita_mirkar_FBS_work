user_id = "Nikita"
pass1 = "Nikita123"


for i in range(1,4):
    user_id = input("Enter the user id: ")
    pass1 = input("Enter the password: ")
    if(user_id == "Nikita" and pass1 == "Nikita123"):
        print("login successful")
        break
    elif(i>=3):
        print("re-enter")
    i+=3
    