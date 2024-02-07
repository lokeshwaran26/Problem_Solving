def permutationEquation(p):
    c = p.copy()
    c.sort()
    b = []
    for x in c:

        k = p.index(x)+1
        b.append((p.index(k)+1))
    return b
