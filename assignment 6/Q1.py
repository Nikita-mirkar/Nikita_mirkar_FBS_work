for i in range(1,6):
    for j in range(1,6):

        if(i==5 or j ==5 or i==1 or j==1):
            print("*", end =" ")
        else:
            print(" ", end =" ")
    print()


# * * * * * 
# *       *
# *       *
# *       *
# * * * * *