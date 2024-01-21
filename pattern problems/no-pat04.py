n = 5
for i in range(n):
    for j in range(i, n):
        print(" ",  end=' ')
    for k in range(i+1):
        if (i % 2 == 0):
            print('#', end=' ')
        else:
            print('$', end=' ')
    for l in range(i):
        if (i % 2 == 0):
            print('#', end=' ')
        else:
            print('$', end=' ')

    print()
