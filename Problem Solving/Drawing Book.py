def pageCount(n, p):
    if p <= n//2:
        return p//2
    else:
        if n%2 == 0 and n==p+1:
            return (n-p)//2 + 1
        else:
            return (n-p)//2