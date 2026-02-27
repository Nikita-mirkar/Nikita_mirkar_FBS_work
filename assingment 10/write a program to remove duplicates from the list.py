data = [10,20,30,20,10,40,50,43]
unique = []
for i in range(0,len(data)):
    if data[i] not in unique:
        unique.append(data[i])
print(unique)

