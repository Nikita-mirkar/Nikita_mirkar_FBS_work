# data = [10,20,30,40,50]
# rev = []
# i = len(data) - 1
# while i >= 0:
#     rev.append(data[i])
#     i -= 1
# print(rev)

data = [10,20,30,40,50]
rev = []
for i in range(len(data)):
    rev.insert(0,data[i])
print(rev)