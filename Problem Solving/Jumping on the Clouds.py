def jumpingOnClouds(c):
    n = len(c)
    count = 0
    i = 0
    while i < n-3:
        if c[i+2] == 0:
            i += 2
        else:
            i += 1
        count += 1
    count += 1
    return count