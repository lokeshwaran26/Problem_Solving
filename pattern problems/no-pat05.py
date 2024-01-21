# 54321
#  4321
#   321
#    21
#     1

n = 5
k = 5
for i in range(n):
    p=k
    for j in range(i):
        print(' ', end='')
    for j in range(i, n):
        print(p, end='')
        p-=1
    k-=1
    print()