def countingValleys(n, s):
    valleycount = level = 0
    d = {'U': 1, 'D': -1}
    for step in s:
        level += d[step]
        if level == 0 and step == 'U':
            valleycount += 1
    return valleycount
