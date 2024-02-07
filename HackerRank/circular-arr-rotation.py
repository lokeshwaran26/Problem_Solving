def circularArrayRotation(a, k, queries):
    ans = []
    l = len(a)
    k = k % l
    newQ = a[l-k:] + a[:l-k]
    for q in queries:
        ans.append(newQ[q])
    return ans
