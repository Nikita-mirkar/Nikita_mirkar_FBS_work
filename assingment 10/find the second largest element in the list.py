data = [10,20,3,5,9,29,30,45]
first = data[0]
second = data[1]
if first < second:
    first,second = second,first
if second < first:
    second ,first = first,second

for i in range(2,len(data)):
    if data[i] > first:
        second = first
        first = data[i]
    elif data[i] > second:
        second = data[i]
print(second)