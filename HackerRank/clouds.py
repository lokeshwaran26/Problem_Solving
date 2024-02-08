def jumpingOnClouds(c, k):
    energy = 100
    index = 0
    while True:
        index = (index + k) % len(c)
        if c[index] == 1:
            energy -= 3
        else:
            energy -= 1
        if index == 0:
            break
    return energy
