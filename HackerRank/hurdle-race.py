def hurdleRace(k, height):
    # Write your code here
    val = height[0]
    for i in height:
        if val < i:
            val = i

    if k >= val:
        return 0
    else:
        res = abs(k - val)
        return res
