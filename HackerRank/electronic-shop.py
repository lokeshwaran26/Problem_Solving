#
def getMoneySpent(keyboards, drives, b):
    items = []
    
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            pls = keyboards[i] + drives[j]
            if ( pls <= b):
                items.append(pls)
    if (len(items) == 0):
        return -1
    else:
        bud = items[0]
        for i in items:
            if i > bud:
                bud = i
        return bud
    