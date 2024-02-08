def findDigits(n):
    # Write your code here
    count = 0
    num = str(n)
    for i in num:
        if int(i) != 0:
            if n % int(i) == 0:
                count += 1
    return count


def findDigits(n):
    # Write your code here
    val = 0
    q = n
    while (n != 0):
        mod = n % 10
        if mod != 0 and q % mod == 0:
            val += 1
        n = n//10
    return val
