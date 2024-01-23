data = [1, 2, -3, -4]
for i in range(len(data)):
    if (data[i] < 0):
        data[i] = 0
print(data)

data1 = [1, 2, -3, -4]
for idx, num in enumerate(data1):
    if (num < 0):
        num[idx] = 0
print(data)
