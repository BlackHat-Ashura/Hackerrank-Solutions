def birthday(s, d, m):
    n = len(s)
    count = 0
    for i in range(n-m+1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count