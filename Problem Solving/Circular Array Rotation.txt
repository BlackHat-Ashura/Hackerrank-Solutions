def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k%n
    b = [0]*n
    for i in range(k):
        b[i] = a[n-k+i]
    for i in range(n-k):
        b[i+k] = a[i]
    output = []
    for query in queries:
        output.append(b[query])
    return output