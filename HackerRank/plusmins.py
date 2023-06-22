
import math
import os
import random
import re
import sys
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

#


def plusMinus(arr):
    # Write your code here
    pos = neg = zero = 0

    for i in range(n):
        if (arr[i] > 0):
            pos += 1
        elif (arr[i] < 0):
            neg += 1
        else:
            zero += 1
    x = pos/n
    y = neg/n
    z = zero/n
    print(round(x, 6))
    print(round(y, 6))
    print(round(z, 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
