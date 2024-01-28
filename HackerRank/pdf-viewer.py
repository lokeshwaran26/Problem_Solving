def designerPdfViewer(h, word):
    # Write your code here
    res = []
    n = len(word)

    for i in range(n-1):
        idx = ord(word[i]) - 97
        res.append(h[idx])
        idx = 0

    val = 0
    for i in res:
        if val < i:
            val = i
    final = val*n
    return final
