def saveThePrisoner(n, m, s):
    total = m + s - 1
    total %= n
    if total == 0:
        return n
    return total