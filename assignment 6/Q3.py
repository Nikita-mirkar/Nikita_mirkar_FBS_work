for i in range(4):
    for j in range(1, 4-i):
        print(" ", end=" ")
    
    x = 1
    for j in range(i+1):
        print(x, end=" ")
        x = x *(i - j) // (j +1)
    print()