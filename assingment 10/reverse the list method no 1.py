data = [10,20,30,20,40]
start = 0
end = len(data) -1
while start < end:
    data[start],data[end] = data[end],data[start]
    start += 1
    end -= 1
print("reversed list: ",data)