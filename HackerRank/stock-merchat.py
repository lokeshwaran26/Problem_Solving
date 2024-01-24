#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    # Write your code here
    arr = sorted(ar)
    left = 0
    right = 1
    count = 0
    while (right < n):
        if (arr[left] == arr[right]):
            count += 1
            left += 2
            right += 2
        else:
            left += 1
            right += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
