# 1 
# 2 2
# 1 1 1
# 2 2 2 2
# 1 1 1 1 1

n = 5
count = 1

for i in range(n):
    if(i == 2 or i == 4):
        count = 1
    for j in range(i+1):
        print(count,  end=' ')
    count += 1
    print()

for i in range(n):
    for j in range(i+1):
        if( i%2 == 0):
            print('1', end=' ')
        else:
            print('2', end=' ')
    print()
