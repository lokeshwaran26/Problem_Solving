def utopianTree(n):
    h=0
    dic={}
    for i in range(n+1):
        if(i%2==0):
            h+=1
            dic[i]=h
        else:
            h*=2
            dic[i]=h
    return dic[n]