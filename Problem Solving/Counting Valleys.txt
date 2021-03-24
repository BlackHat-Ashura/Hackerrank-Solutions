def countingValleys(steps, path):
    u = 0
    d = 0
    valley = 0
    sea_level = []
    for i in range(steps):
        if path[i] == 'U':
            u += 1
        if path[i] == 'D':
            d += 1
        if d-u == 0:
            sea_level.append(i)
    for i in sea_level:
        if path[i] == 'U':
            valley += 1
    return valley