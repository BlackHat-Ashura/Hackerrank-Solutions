def flatlandSpaceStations(n, c):
    max_dist = 0
    c.sort()
    for i in range(len(c)-1):
        max_dist = max(max_dist, (c[i+1] - c[i])//2)
    
    max_dist = max(max_dist, c[0], n-1 - c[-1])
    return max_dist