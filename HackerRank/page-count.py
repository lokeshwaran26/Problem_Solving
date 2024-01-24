def pageCount(n, p):
    # Write your code here
    front = p//2

    if n % 2 == 1:
        back = (n-p)//2
    else:
        back = (n-p+1)//2
    return min(front, back)
