# maximum value in the list
data = [10,20,30,40,50]
max_value = data[0]
for i in range(1,len(data)):
    data[i] < max_value
    max_value = data[i]
print(max_value)

# minimum value in the list
data = [10,20,30,40,50]
min = data[0]
for i in range(1, len(data)):
    if data[i] < min:
        min = data[i]
print("Minimum:", min)