# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5
count = 0
for i in range(n):
    for j in range(i+1):
        count += 1
        print(count, end=' ')
    count = 0
    print()
