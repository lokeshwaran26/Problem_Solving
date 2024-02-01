def angryProfessor(k, a):
    # Write your code here
    at = 0
    late = 0
    for i in range(len(a)-1):
        if a[i] <= 0:
            at += 1
        else:
            late += 1
    if at >= k:
        return "NO"
    else:
        return "YES"
