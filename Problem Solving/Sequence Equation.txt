def permutationEquation(p):
    n = len(p)
    y = []
    for i in range(1, n+1):
        tmp = p.index(i)
        new = p.index(tmp+1)
        y.append(new+1)
    return y