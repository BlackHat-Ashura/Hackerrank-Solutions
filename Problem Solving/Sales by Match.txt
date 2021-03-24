def sockMerchant(n, ar):
    d = {}
    count = 0
    for i in range(n):
        if ar[i] in d.keys():
            d[ar[i]] += 1
        else:
            d[ar[i]] = 1
    for i in d.keys():
        count += d[i]//2
    return count
