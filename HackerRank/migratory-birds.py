def migratoryBirds(arr):
    dct = dict.fromkeys(arr, 0)
    for i in arr:
        dct[i]+=1

    maxFreq=max(dct.values())
    lst1=sorted(list(dct.keys()))
    for i in lst1:
        if dct.get(i)==maxFreq:
            return i