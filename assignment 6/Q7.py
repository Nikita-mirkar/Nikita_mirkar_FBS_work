for i in range(1,6):
    x=65
    for j in range(5-i):
        print(" ", end=" ")
    for j in range(2*i-1):
        print(chr(x +j), end=" ")
        
    print()

#         A 
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I