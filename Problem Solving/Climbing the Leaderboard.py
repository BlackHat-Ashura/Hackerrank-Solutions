def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    n = len(ranked)
    i = 0
    ranked.sort()
    lis = []
    
    for score in player:
        while i<n and ranked[i] <= score:
            i += 1
        lis.append(n-(i-1))
    
    return lis