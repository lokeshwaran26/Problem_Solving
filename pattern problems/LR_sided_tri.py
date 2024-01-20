# * * * * *
#   * * * *
#     * * *
#       * *
#         *

n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i, n):
        print("*", end=" ")

    print()


#  * * * * *   if j loop print statement is empty space ---> print("")
#   * * * *
#    * * *
#     * *
#      *
