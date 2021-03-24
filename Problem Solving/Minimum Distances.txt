def minimumDistances(a):
    n = len(a)
    min_dis = n    
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                dist = j - i
                if dist < min_dis:
                    min_dis = dist
    if min_dis != n:
        return min_dis
    else:
        return -1