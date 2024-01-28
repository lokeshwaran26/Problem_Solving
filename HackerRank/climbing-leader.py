
def climbingLeaderboard(ranked, player):
    # Write your code here
    rnk = list(set(ranked))
    rnk.sort()
    n = len(rnk)
    final = []
    i = 0
    for scr in player:
        while i < n and rnk[i] <= scr:
            i += 1
        final.append(n-i + 1)
    return final



        
        
r = [ 100, 100, 50, 40, 40, 20, 10]
p = [ 5, 25, 50, 120]
result = climbingLeaderboard(r,p)
print(result)