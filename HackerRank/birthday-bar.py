def birthday(s, d, m):
    total = 0
    count = 0
    while (len(s) >= m):
        for x in range(m):
            total += s[x]
        if (total == d):
            count += 1
        total = 0
        s.pop(0)
    return count
