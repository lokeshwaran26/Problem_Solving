# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(i, n):
#         print("*", end=" ")

#     print()


#  * * * * *   if j loop print statement is empty space ---> print("")
#   * * * *
#    * * *
#     * *
#      *


n = 6
for i in range(1,n):
    for j in range(i,n-1):
        print(' ', end=' ')
    for k in range(i):
        print("*", end=' ')
    for l in range(i-1):
        print("*", end=' ')
    # for j in range(i, n-1):
    #     print(' ', end=' ')
    # for j in range(i, n-1):
    #     print(' ', end=' ')
    # for k in range(i):
    #     print("*", end=' ')
    # for l in range(i-1):
    #     print("*", end=' ')
    print()
s = 5
for i in range(1, s):
    for j in range(i):
        print(' ', end=' ')
    for k in range(i,n-1):
        print("*", end=' ')
    for l in range(i,s-1):
        print("*", end=' ')
    print()

