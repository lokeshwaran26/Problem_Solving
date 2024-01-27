def climbingLeaderboard(ranked, player):
    # Write your code here
    res = []
    for i in ranked:
        if i not in res:
            res.append(i)
    final = []
    left = res[i]
    right = res[i+1]
    for i in range(0, (len(res)-1)):
        for j in player:
            if left >= player <= right:
                final.append(i+1)
                break
            if 
