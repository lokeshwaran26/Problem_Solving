def catAndMouse(x, y, z):
    cat1 = abs(z - x)
    cat2 = abs(z - y)
    if cat1 < cat2:
        return 'Cat A'
    elif cat2 < cat1:
        return 'Cat B'
    else:
        return 'Mouse C'
