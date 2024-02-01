def reverse(i):
    mod = 0
    rev = 0
    while (i != 0):
        mod = i % 10
        rev = rev*10 + mod
        i = i//10
    return rev


def beautifulDays(i, j, k):
    # Write your code here
    day = 0
    for l in range(i, j+1):
        m = (l - reverse(l)) / k
        if m.is_integer():
            day += 1

    return day
