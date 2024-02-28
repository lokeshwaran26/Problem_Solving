# *
# * *
# * * *
# * * * *
# * * * * *


n = 5
for i in range(n):
    for k in range(i):
        print(' ', end=" ")
    for j in range(k+1):
        print("*", end=' ')
    print()
